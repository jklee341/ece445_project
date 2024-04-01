import os
import time
from PIL import Image
import supervision as sv
from torch.utils.data import DataLoader
import cv2
import threading
import queue

from PytorchWildlife.models import detection as pw_detection
from PytorchWildlife.models import classification as pw_classification
from PytorchWildlife.data import transforms as pw_trans
from PytorchWildlife.data import datasets as pw_data
from PytorchWildlife import utils as pw_utils

DEVICE = "cpu"

detection_model = None
classification_model = None

trans_det = None
trans_clf = None

def load_models(det, clf):
    global detection_model, classification_model, trans_det, trans_clf

    detection_model = pw_detection.__dict__[det](device=DEVICE, pretrained=True)
    if clf != "None":
        classification_model = pw_classification.__dict__[clf](device=DEVICE, pretrained=True)

    trans_det = pw_trans.MegaDetector_v5_Transform(target_size=detection_model.IMAGE_SIZE,
                                                   stride=detection_model.STRIDE)
    trans_clf = pw_trans.Classification_Inference_Transform(target_size=224)

    return "Loaded Detector: {}. Loaded Classifier: {}".format(det, clf)

def single_image_detection(input_img, det_conf_thres, clf_conf_thres, img_index=None):
    # Resize the input frame
    resized_frame = cv2.resize(input_img, (640, 480))

    results_det = detection_model.single_image_detection(trans_det(resized_frame),
                                                         resized_frame.shape,
                                                         img_path=img_index,
                                                         conf_thres=det_conf_thres)
    if classification_model is not None:
        labels = []
        for xyxy, det_id in zip(results_det["detections"].xyxy, results_det["detections"].class_id):
            if det_id == 0:
                cropped_image = sv.crop_image(image=resized_frame, xyxy=xyxy)
                results_clf = classification_model.single_image_classification(trans_clf(Image.fromarray(cropped_image)))
                labels.append("{} {:.2f}".format(results_clf["prediction"] if results_clf["confidence"] > clf_conf_thres else "Unknown",
                                                 results_clf["confidence"]))
            else:
                labels = results_det["labels"]
    else:
        labels = results_det["labels"]

    return labels

def detection_thread(frame_queue, result_queue, det_conf_thres, clf_conf_thres):
    while True:
        frame = frame_queue.get()
        if frame is None:
            break
        labels = single_image_detection(frame, det_conf_thres=det_conf_thres, clf_conf_thres=clf_conf_thres)
        result_queue.put(labels)

def video_detection(det_conf_thres, clf_conf_thres):
    cap = cv2.VideoCapture(0)
    frame_queue = queue.Queue(maxsize=1)
    result_queue = queue.Queue(maxsize=1)

    det_thread = threading.Thread(target=detection_thread, args=(frame_queue, result_queue, det_conf_thres, clf_conf_thres))
    det_thread.start()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_queue.empty():
            frame_queue.put(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if not result_queue.empty():
            labels = result_queue.get()
            print("Detected animals:", labels)

        cv2.imshow("Live Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    frame_queue.put(None)
    det_thread.join()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    det_model = "MegaDetectorV5"
    clf_model = "None"
    det_conf_thres = 0.2
    clf_conf_thres = 0.7

    load_models(det_model, clf_model)
    video_detection(det_conf_thres, clf_conf_thres)