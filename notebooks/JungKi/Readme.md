# March 1st

During the PCB review, we talked with the TA about the revisions we made to our PCB. We initially were going to use a combination of Raspberry PI and some other microcontroller and had both the deterrent system and sensing system running simultaneously. This changed to a more power efficient design where we have the sensing system running first, then the deterrent system. Only an ESP32 chip would be needed since less computations are taking place. With the WiFi module already installed, this would communicate with a computer doing the detection separately. The TA approved this idea, even though it may be hard to deal with the ESP32 chip. We have yet to see how this will turn out. 
______________________________________________________________________________________________________________________________

# March 4th

The initial PCB design has been made. We have yet to solder this.

![image](https://github.com/jklee341/ece445_project/assets/100997714/d236987a-56a1-44e6-83cd-4d6e2d40ef5b)
![image](https://github.com/jklee341/ece445_project/assets/100997714/b84540bf-3e15-48e4-85cd-d1448fb8e0fa)
![image](https://github.com/jklee341/ece445_project/assets/100997714/cb2cd5e3-cf64-41df-b90b-1ab00d3b45ae)
_____________________________________________________________________________________________________________________________

# March 25th 

We have not worked on this project for a long time due to other commitments. I have ordered parts to start soldering our PCB. In the mean time, we have started playing around with the ESP32 Dev Board that we borrowed from the cabinet. I have never worked with one before so it is very hard to navigate through everything. 
______________________________________________________________________________________________________________________________

# April 8th

We have finished soldering the PCB and started testing the connections to see if they are reporting the proper voltages.

We have decided to make some changes to our design. We observed the stepper motors is not precise enough and also does not produce enough torque. We cannot control the acceleration of the stepper motor, so when we want the motors to spin the opposite direction, it takes some time to do so. Therefore, we will be using servo motors instead. Since servo motors only cover 180 degrees, our task is to figure out a method to cover all 360 degrees since that is one of our high level requirements. 

![rn_image_picker_lib_temp_63725f25-d365-464e-a281-e58a5ba136df](https://github.com/jklee341/ece445_project/assets/100997714/c9a81707-f8ba-4bd6-8520-c4e74ff26a1d)
______________________________________________________________________________________________________________________________

# April 11th

We have attempted multiple times to solder our PCB and the reported voltage does not turn out to be 3.3V. Instead, it returns about 1.3V which is nowhere close to what we want the voltage supplied to the ESP32 to be. The calculations that we made for the 5V to 3.3V voltage converter does not seem to be incorrect as the formula is $V_{OUT} = V_{FB} × (1 + R1 / R2)$. We used the right resistor values of R1 = 1MΩ, and R2 = 200kΩ, so our converter should theoretically work. Something may be wrong with the LDO chip that we are using. 

![image](https://github.com/jklee341/ece445_project/assets/100997714/8c61a900-0720-4f3e-bc7e-10f9f4b0eadd)

Additionally, as we were experiencing too many difficulties with the ESP32 chip, we have decided to switch to use a Raspberry Pi 4. The IOT system library code we found on the example codebase of ESP32 does not work with our chip due to version issues perhaps. This may be much easier if we switch to a Raspberry Pi 4 and let the chip do all the power delivery and the detection on its own.
______________________________________________________________________________________________________________________________

# April 15th

We started the 3D printing process and the parts should be finished before the mock demo. Shifting over to Raspberry Pi 4 was an arduous process. We had to boot an operating system onto the Raspberry Pi 4. After multiple failures and bootloops, we realized that we had to boot the 64-bit Raspbian environment.  
______________________________________________________________________________________________________________________________

# April 22nd

We picked up the 3D printed parts from SCD and MEB. We assembled the two towers to the base and the motors and tested the rotation of both towers. Though a little instable, the sensors (PIR sensor, ultrasonic sensor) were attached to the towers using double sided tape and later using glue. Today primarily involved testing the operational capacity of the sensing tower. The packaging of our device is horrible as wires are sticking out everywhere and this may become a safety hazard when this device is used in outdoor settings. Currently, everything is connected to a breadboard, which we may lodge inside the base or the sides. Unit tests were conducted to test each sensor. We have a GUI that shows how our ultrasonic sensor is mapping the environment and it seems legit. We may need to test it outside since right now it is detecting everything within 7 meter range.

![image](https://github.com/jklee341/ece445_project/assets/72641482/2c8cce62-5a61-4636-b2af-d7c5b34c21b6)
![image](https://github.com/jklee341/ece445_project/assets/100997714/2543746c-a84f-4b88-bf84-4e5ec551529e)
______________________________________________________________________________________________________________________________

# April 25th

We attached the deterrence system and the RPi camera to the deterrence tower. We had the problem of the lights interfering with the camera, so we added a slab of wood beneath the camera to place the LEDs and the ultrasonic transducer. For now, the ultrasonic transducers frequency was set to 200Hz so that we can hear it. When we set it outside, we will adjust this frequency to 20kHz which is the frequency known to deter rodents. With the logic that is sent by the RPi, we were able to run the deterrence mechanism fully. As said in an earlier post, we were certain that the ultrasonic sensor was working since there were more empty spaces. 

Lights: https://github.com/jklee341/ece445_project/assets/100997714/def22a45-abbf-441f-8bf3-3bd4c6349be7 \
Ultrasonic transducer: https://github.com/jklee341/ece445_project/assets/100997714/c76f73f7-d3aa-4201-bbb2-9eff4c495512


![image](https://github.com/jklee341/ece445_project/assets/72641482/205ca8ae-8f59-46ba-9b4f-c9a308e32cde)

The system should follow the steps:

Detect motion with PIR --> Activate ultrasonic and map environment --> Activate camera --> Find object and follow --> If found,deterrence on

We were able to test this on humans and it definitely worked. 
______________________________________________________________________________________________________________________________

# April 26th

We tested this on squirrels outside to see if this can be applied to rodents. The result was successful and we were able to take video footage of it actually identifying the squirrel and deterring with lights and sounds.

![image](https://github.com/jklee341/ece445_project/assets/100997714/829572c4-59a4-4c44-815b-002912369e51)

