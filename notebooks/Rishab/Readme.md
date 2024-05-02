# February 26th

## **Goals**
Discuss what we need in our PCB and create our initial design and begin testing the software side

## **What was completed:** 

We were able to figure out everything that was necessary on our PCB. However we were not able to start designing the PCB and will complete an initial design by the first PCB round. 
I on my end began research into how to develop the software since this didn't need any reliance on the hardware.

______________________________________________________________________________________________________________________________


# March 4th

## **Goals**: 
Finish the initial PCB design

## **What was completed**: 

We finished designing our initial PCB design, this was mainly done by Mankeerat and Jungki. 
I on my end am still continuing research to see if there has been any existing implementation. Attached is some research of using this public repo provided from Microsoft called MegaDetector. 
This, however, doesn't seem like its viable as the model has too many parameters.

![image](https://github.com/jklee341/ece445_project/assets/72641482/6a2a8eaf-85a6-439b-83e6-1faa71cb8643)
![image](https://github.com/jklee341/ece445_project/assets/72641482/ca9823a8-a5ee-4950-bbc3-ce178cb01a71)

Detection research:

https://www.sciencedirect.com/science/article/pii/S2351989422001068
https://towardsdatascience.com/detecting-animals-in-the-backyard-practical-application-of-deep-learning-c030d3263ba8

______________________________________________________________________________________________________________________________


# March 25th

## **Goals:** 

Testing sensors and begin sodering the our PCB. Have initial code for detection for humans

## **What was completed:** 

Jungki and Mankeerat began the sodering of the PCB. They ran into difficulties in the sodering due to the fact that we didn't get a stencil with the PCB, making some aspects to be extremely difficult to soder. 
I have began experimeting with object detection, first starting with just human face detection. Furthermore, we didn't begin testing or coding any of the sensors we picked up from the shop or the cupboard. 
We need to also begin coding the ESP to test the sensors, which we haven't done with the devboard. This will be the plan for the following meeting. We didn't meet the prior week due to committments in other classes for the members. 

![image](https://github.com/jklee341/ece445_project/assets/72641482/1a51ee7a-1ea8-439b-b7ec-7af0f4cf58d0)


______________________________________________________________________________________________________________________________


# April 8th

## **Goals:** 

Finish sodering, test connections on PCB, finish coding PIR and Ultrasonic sensor and stepper motors. 

## **What was completed:** 

We were able to finish sodering the PCB, and began testing the connections. So far it looks to be fine and working and we are able to see the connection with the ESP when connected with the USB-C port. 
I started coding the PIR sensors and it works on the IDE sketch. The Ultrasonic and stepper motors also work. However, we noticed as a team that the stepper motors do not deliver the precision we want. That is, when spinning the motors, there is cooldown time to when it stops. 
We are going to buy servos instead. We have to figure out how to get 360 degree though as servo only provide 180. We might have to mount 2 on top of each other. All in all, we were pretty successful as we kept our goals more realistic, but we need to start making more progress!!! 




______________________________________________________________________________________________________________________________


# April 11th

## **Goals:** 

Connect object detection code with ESP32, test multiple sensors and iron down order of logic for system

## **What was completed:** 
I was able to connect my object detection code (which runs locally on my laptop) with the ESP32 dev board serially. The object detection code correctly sends info to the dev board.
I coded it to turn the light on detection and also coded it to turn stepper motor when the bounding box of the animal appears past set bounds in the frame. Although this is sucessful we were unable to do the following.
Firstly, we are unable to load the model on the ESP32S. Moreover, we are finding difficulty with working with the IoT system on Espressif and are unable to send info wirelessly to the ESP. 
Our team discussed and decided to instead most of the software work on the Rpi4, which we havent got to yet. 




______________________________________________________________________________________________________________________________


# April 15th

## **Goals:** 

Finish 3D printing our tower and code object detection on Rpi4

## **What was completed:** 
Today was a long working day for 445. With the mock demo coming up we need to start working longer hours to finish. We started the 3D printing process. This should be finished before our mock demo. Setting up the Rpi4 took some time, especially after we realized that some of the object detection code needs to be in 64bit envrionment. 
However, we have no ported it over. We haven't got our Rpi camera module yet so we can't test how viable the object detection code is on this device with less compute. On the good note is that the object detection is pretty reliable, at least running on the Mac
and we just have to port it over to Python code and using RPi GPIOs. We also ordered some more servos as we need 2 for the deterrence tower. We also managed to figure out how we were going to strobe the LEDs and play noise from the transducer and, like the sensors,
we coded this using the Arduino IDE sketch. Need to port this over later as well! I also, behind the scenes did some analysis on the accuracy of my object detection which can be seen below. Right now I am seeing a lot of hit on accuracy when running the model and comparing to human detection.

![image](https://github.com/jklee341/ece445_project/assets/72641482/bfbac36a-95c6-4764-818f-f50c1fbbe5fb)
![image](https://github.com/jklee341/ece445_project/assets/72641482/18c8cabc-fe98-4c20-953f-d122100b8c57)





______________________________________________________________________________________________________________________________

# April 19th

## **Goals:** 

Attach tower to servos, code the servo movement using RPi GPIOs, test each individual sensor, LED and transducer with RPi as well

## **What was completed:** 
Another long working day. We didn't finish writing the code on the RPi for the transducer and ultrasonic sensors since these require a wave signal as the power and I was unsure how to code this. While I was coding everything for the RPi,
Jungki and Mankeerat began assembling the 3D parts that we build and sent for printing last meeting. The RPi camera module has yet to come and has been delayed again. The servos I ordered came however which is nice so Jungki and Mankeerat devised a way to attach the towers to the base. 
We tested out most of the assembly using double sided tape first before sealing them properly with super glue. The towers were successfully attached to the base, there is a little instability, but it should still be stable once attaching everything to it. 
I was able to code some basic servo movement for the tower, which just allowed it to turn 0-180 degrees and back. We have 1 more servo that Mankeerat had and this we will use for the camera module since we want the camera to be able to cover 360 degree field of view. 
We are holding off on attaching this until we get the camera module that we ordered! The sensors were easily coded using the RPi GPIOs and the same logic that I used in the Arduino IDE sketches and I was able to complete them by today's meeting!

______________________________________________________________________________________________________________________________

# April 22nd

## **Goals:** 

Attach sensors to the sensing tower and test all of the sensing towers functionality

## **What was completed:** 
With the final demo coming soon we plan on working every day to complete this. We attached the 3 PIR sensors using double sided tape to the tower such that it covers the 360 field of view. We also attached the ultrasonic sensor to one of the sides. 
Today was mainly testing the functionality of the sensing tower. Since this is the activation mechanism of the tower we wanted to make sure it performed to the level that we expected. The wiring of all the sensors to the RPi4 and PCB is looking bad. 
We currently just wired for functionality purpose, but might need to redo it since it is getting out of hand and will be difficult to debug in the future if a wire slips out. We tested out each individual sensor by running each program for each sensor individually.
These function properly. I then coded them in order of how they should function and it worked!


![image](https://github.com/jklee341/ece445_project/assets/72641482/2c8cce62-5a61-4636-b2af-d7c5b34c21b6)

______________________________________________________________________________________________________________________________

# April 23rd

## **Goals:** 

Attach camera module and test object detection

## **What was completed:** 
The RPi camera module finally came in! We were able test the camera and attach it to the extra servo and test that we are getting 360 degree rotation. I adjusted the object detection code to cover the 360 degree view and did some simple modulo arithmetic such that it knew which 
servo to move given the current angle the camera is looking at. One thing we noticed is that, the RPi4 isn't as strong and this may be a concern for the demo. Since the algorithm uses a lot of compute the frames of the video feed are dropping, causing the object detection to, at times,
miss the detection, since the frame quality is blurred and bad. However, the object detection still works when detecting the object and sends a messasge in terminal once detected! Due to the project nearing its end its hard to fix the issue of frame drops as this was unexpected so
we will continue on and for the demo hopefully be able to show that it still works if we have a good frame. 
______________________________________________________________________________________________________________________________

# April 24th

## **Goals:** 

Adjust object detection code to stop once detected and track object in view, attach the deterrence to the tower (LEDs and transducer)

## **What was completed:** 
I was able to adjust the code to stop once it has detected the object of choice. I also was able to get some working mechanism of it being to follow the object, however, the frames are INCREDIBLY slow that it sometimes can't keep up with the movement of the object. Another issue that 
we ran into is that the code fails to know which direction to go when there are multiple objects in view. This is a concern, but again, something we can't fix within the current period in time. Looking back our team discussed that some of these concerns should've been addressed earlier.
Mankeerat and Jungki were able to attacah the LEDs to the RPi and tower. We tested the LEDs and it worked perfectly with the RPi. I was also able to integrate it with the code such that, when it detected an object, it blinked. The transducer is proving to be more difficult since it 
requires a wave signal as its input and we need to figure out how much voltage it needs. We also may need to change how the LED is attached to the system as it may collide with the other tower should the tower start turning wiht the servo.



![image](https://github.com/jklee341/ece445_project/assets/72641482/c241a741-2e95-4ea0-a693-c5f7f62d5e97)


______________________________________________________________________________________________________________________________

# April 25th

## **Goals:** 

Attach and finish everything, combine the code to run everything at once, test feasability outside

## **What was completed:** 
We worked long hours today. We collected a lot of data on the components and finally tested out the whole system at once. We reattached the LEDs to be shorter length and also managed to figure out how to activate the transducer before the meeting. We attached everything together
and tested out the whole deterrence tower first. It seemed to work fine, but again, the object detection program still seemed to be pretty heavy for the RPi compute! We then connected everything together. I combined the sensing tower code with the deterrence tower code.
The system should follow the steps:
1. Detect motion with PIR
2. Activate ultrasonic and map environment
3. Activate camera
4. Find object and follow
5. If found deterrence on

This mechanism worked perfectly when combining, but again at times, failed due to the object detection not seeing the frame properly! Alas, we cannot do anything about this, but we are happy that, in practice it works. We also tested this outside and it seemed to work better in open space.
I adapted the code to identify squirrels and it worked if it was able to detect the squirrel in image. The deterrence seemed to work as well as the squirrel ran away!!!. All in all we are hoping that we can show the concept of this project working. For the demo, the team discussed to use
a battery pack as the "portable battery" making the system autonomous, but in reality we are still using a wall connector. Overall, quite proud considering the barriers we had to overcome and the fact that we switched to using RPi extensively rather than relying too heavily on the ESP on our PCB.




![image](https://github.com/jklee341/ece445_project/assets/72641482/205ca8ae-8f59-46ba-9b4f-c9a308e32cde)



