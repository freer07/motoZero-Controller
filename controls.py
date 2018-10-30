#Created by: Alexander Freer

#3 GPIO pins are associated to each motor – 1 acts like a master on/off swith (enable), 
#and the other 2 pins go HIGH/LOW or LOW/HIGH to go forwards or backwards.

import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pygame.init()

window = pygame.display.set_mode((225,225))
pygame.display.set_caption("Drive")
background = pygame.image.load("wheel2.jpg").convert()
#try to make image turn when driving the car!

Motor1A = 27 
Motor1B = 24 
Motor1Enable = 5
Motor2A = 22 
Motor2B = 6 
Motor2Enable = 17
Motor3A = 16 
Motor3B = 23 
Motor3Enable = 12
Motor4A = 18 
Motor4B = 13 
Motor4Enable = 25

#Right side
GPIO.setup(Motor1A,GPIO.OUT)  
GPIO.setup(Motor1B,GPIO.OUT)  
GPIO.setup(Motor1Enable,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)  
GPIO.setup(Motor2B,GPIO.OUT)  
GPIO.setup(Motor2Enable,GPIO.OUT)

#Left side
GPIO.setup(Motor3A,GPIO.OUT)  
GPIO.setup(Motor3B,GPIO.OUT)  
GPIO.setup(Motor3Enable,GPIO.OUT)
GPIO.setup(Motor4A,GPIO.OUT)  
GPIO.setup(Motor4B,GPIO.OUT)  
GPIO.setup(Motor4Enable,GPIO.OUT)

#For forwards A = High and B = LOW
#For backwards A = LOW and B = HIGH
#Must enable motor 


driveLoop = True

#used to determine the speed of the car
rightSide = 0
leftSide = 0

while driveLoop:
    
    window.blit(background, [0,0])
    pygame.display.flip()
    for event in pygame.event.get():

        if (event.type == pygame.QUIT):
            driveLoop = False

        if (event.type == pygame.KEYDOWN):
            
            if (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                leftSide = leftSide - 50
                
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                rightSide = rightSide - 100
                leftSide = leftSide - 100
                
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                rightSide = rightSide - 50

            elif (event.key == pygame.K_w or event.key == pygame.K_UP):
                rightSide = rightSide + 100
                leftSide = leftSide + 100
            
            

            if (leftSide == -50):
                #Right side forwards
                GPIO.output(Motor1A,GPIO.HIGH) 
                GPIO.output(Motor1B,GPIO.LOW)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.HIGH) 
                GPIO.output(Motor2B,GPIO.LOW)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #left side backwards
                GPIO.output(Motor3A,GPIO.LOW) 
                GPIO.output(Motor3B,GPIO.HIGH)    
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.LOW) 
                GPIO.output(Motor4B,GPIO.HIGH)    
                GPIO.output(Motor4Enable,GPIO.HIGH)
                #print("Turn Left")
                
            elif (rightSide == -50):
                #Right side backwards
                GPIO.output(Motor1A,GPIO.LOW) 
                GPIO.output(Motor1B,GPIO.HIGH)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.LOW) 
                GPIO.output(Motor2B,GPIO.HIGH)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #left side forwards
                GPIO.output(Motor3A,GPIO.HIGH) 
                GPIO.output(Motor3B,GPIO.LOW)   
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.HIGH) 
                GPIO.output(Motor4B,GPIO.LOW)   
                GPIO.output(Motor4Enable,GPIO.HIGH)
                #print("Turn Right")
                
            elif (rightSide == 100 and leftSide == 50 ):
                #Right side forwards
                GPIO.output(Motor1A,GPIO.HIGH) 
                GPIO.output(Motor1B,GPIO.LOW)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.HIGH) 
                GPIO.output(Motor2B,GPIO.LOW)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #Left side off
                GPIO.output(Motor3Enable,GPIO.LOW)
                GPIO.output(Motor4Enable,GPIO.LOW)
                #print("Turn half left")
                
            elif (rightSide == 50 and leftSide == 100 ):
                #Right side off
                GPIO.output(Motor1Enable,GPIO.LOW)
                GPIO.output(Motor2Enable,GPIO.LOW)
                #Left side forwards
                GPIO.output(Motor3A,GPIO.HIGH) 
                GPIO.output(Motor3B,GPIO.LOW)    
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.HIGH) 
                GPIO.output(Motor4B,GPIO.LOW)    
                GPIO.output(Motor4Enable,GPIO.HIGH)
                #print("Turn half right")
                
            elif (rightSide == 100 and leftSide == 100 ):
                #print("full steam ahead")
                #Right side forwards
                GPIO.output(Motor1A,GPIO.HIGH) 
                GPIO.output(Motor1B,GPIO.LOW)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.HIGH) 
                GPIO.output(Motor2B,GPIO.LOW)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #Left side forwards
                GPIO.output(Motor3A,GPIO.HIGH) 
                GPIO.output(Motor3B,GPIO.LOW)    
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.HIGH) 
                GPIO.output(Motor4B,GPIO.LOW)    
                GPIO.output(Motor4Enable,GPIO.HIGH)

            elif (rightSide == -100 and leftSide == -100 ):
                #Right side backwards
                GPIO.output(Motor1A,GPIO.LOW) 
                GPIO.output(Motor1B,GPIO.HIGH)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.LOW) 
                GPIO.output(Motor2B,GPIO.HIGH)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #Left side backwards
                GPIO.output(Motor3A,GPIO.LOW) 
                GPIO.output(Motor3B,GPIO.HIGH)    
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.LOW) 
                GPIO.output(Motor4B,GPIO.HIGH)    
                GPIO.output(Motor4Enable,GPIO.HIGH)
                #print("full steam backwards")
                
            elif (rightSide == -150 and leftSide == -100 ):
                #Right side off
                GPIO.output(Motor1Enable,GPIO.LOW)
                GPIO.output(Motor2Enable,GPIO.LOW)
                #Left side Backwards
                GPIO.output(Motor3A,GPIO.LOW) 
                GPIO.output(Motor3B,GPIO.HIGH)    
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.LOW) 
                GPIO.output(Motor4B,GPIO.HIGH)    
                GPIO.output(Motor4Enable,GPIO.HIGH)
                #print("Turn Half Right Backwards")
                
            elif (rightSide == -100 and leftSide == -150 ):
                #Right side backwards
                GPIO.output(Motor1A,GPIO.LOW) 
                GPIO.output(Motor1B,GPIO.HIGH)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.LOW) 
                GPIO.output(Motor2B,GPIO.HIGH)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #Left side off
                GPIO.output(Motor3Enable,GPIO.LOW)
                GPIO.output(Motor4Enable,GPIO.LOW)
                #print("Turn Half Left Backwards")
                
            else:
                #motors off
                GPIO.output(Motor1Enable,GPIO.LOW)
                GPIO.output(Motor2Enable,GPIO.LOW)
                GPIO.output(Motor3Enable,GPIO.LOW)
                GPIO.output(Motor4Enable,GPIO.LOW)
                #print("stopped")
         
                
        if (event.type == pygame.KEYUP):
            
            if (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                #print('a or left = UP')
                #rightSide = rightSide - 100
                leftSide = leftSide + 50
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                #print('s or down = UP')
                rightSide = rightSide + 100
                leftSide = leftSide + 100
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                #print('d or right = UP')
                rightSide = rightSide + 50
                #leftSide = leftSide - 100

            elif (event.key == pygame.K_w or event.key == pygame.K_UP):
                #print('w or up = UP')
                rightSide = rightSide - 100
                leftSide = leftSide - 100
            
            #print ("------------")
            #print ("Right:", rightSide)
            #print ("Left:", leftSide)

            if (leftSide == -50):
                #Right side forwards
                GPIO.output(Motor1A,GPIO.HIGH) 
                GPIO.output(Motor1B,GPIO.LOW)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.HIGH) 
                GPIO.output(Motor2B,GPIO.LOW)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #left side backwards
                GPIO.output(Motor3A,GPIO.LOW) 
                GPIO.output(Motor3B,GPIO.HIGH)    
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.LOW) 
                GPIO.output(Motor4B,GPIO.HIGH)    
                GPIO.output(Motor4Enable,GPIO.HIGH)
                #print("Turn Left")
                
            elif (rightSide == -50):
                #Right side backwards
                GPIO.output(Motor1A,GPIO.LOW) 
                GPIO.output(Motor1B,GPIO.HIGH)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.LOW) 
                GPIO.output(Motor2B,GPIO.HIGH)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #left side forwards
                GPIO.output(Motor3A,GPIO.HIGH) 
                GPIO.output(Motor3B,GPIO.LOW)   
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.HIGH) 
                GPIO.output(Motor4B,GPIO.LOW)   
                GPIO.output(Motor4Enable,GPIO.HIGH)
                #print("Turn Right")
                
            elif (rightSide == 100 and leftSide == 50 ):
                #Right side forwards
                GPIO.output(Motor1A,GPIO.HIGH) 
                GPIO.output(Motor1B,GPIO.LOW)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.HIGH) 
                GPIO.output(Motor2B,GPIO.LOW)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #Left side off
                GPIO.output(Motor3Enable,GPIO.LOW)
                GPIO.output(Motor4Enable,GPIO.LOW)
                #print("Turn half left")
                
            elif (rightSide == 50 and leftSide == 100 ):
                #Right side off
                GPIO.output(Motor1Enable,GPIO.LOW)
                GPIO.output(Motor2Enable,GPIO.LOW)
                #Left side forwards
                GPIO.output(Motor3A,GPIO.HIGH) 
                GPIO.output(Motor3B,GPIO.LOW)    
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.HIGH) 
                GPIO.output(Motor4B,GPIO.LOW)    
                GPIO.output(Motor4Enable,GPIO.HIGH)
                #print("Turn half right")
                
            elif (rightSide == 100 and leftSide == 100 ):
                print("full steam ahead")
                #Right side forwards
                GPIO.output(Motor1A,GPIO.HIGH) 
                GPIO.output(Motor1B,GPIO.LOW)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.HIGH) 
                GPIO.output(Motor2B,GPIO.LOW)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #Left side forwards
                GPIO.output(Motor3A,GPIO.HIGH) 
                GPIO.output(Motor3B,GPIO.LOW)    
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.HIGH) 
                GPIO.output(Motor4B,GPIO.LOW)    
                GPIO.output(Motor4Enable,GPIO.HIGH)

            elif (rightSide == -100 and leftSide == -100 ):
                #Right side backwards
                GPIO.output(Motor1A,GPIO.LOW) 
                GPIO.output(Motor1B,GPIO.HIGH)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.LOW) 
                GPIO.output(Motor2B,GPIO.HIGH)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #Left side backwards
                GPIO.output(Motor3A,GPIO.LOW) 
                GPIO.output(Motor3B,GPIO.HIGH)    
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.LOW) 
                GPIO.output(Motor4B,GPIO.HIGH)    
                GPIO.output(Motor4Enable,GPIO.HIGH)
                #print("full steam backwards")
                
            elif (rightSide == -150 and leftSide == -100 ):
                #Right side off
                GPIO.output(Motor1Enable,GPIO.LOW)
                GPIO.output(Motor2Enable,GPIO.LOW)
                #Left side Backwards
                GPIO.output(Motor3A,GPIO.LOW) 
                GPIO.output(Motor3B,GPIO.HIGH)    
                GPIO.output(Motor3Enable,GPIO.HIGH)
                GPIO.output(Motor4A,GPIO.LOW) 
                GPIO.output(Motor4B,GPIO.HIGH)    
                GPIO.output(Motor4Enable,GPIO.HIGH)
                #print("Turn Half Right Backwards")
                
            elif (rightSide == -100 and leftSide == -150 ):
                #Right side backwards
                GPIO.output(Motor1A,GPIO.LOW) 
                GPIO.output(Motor1B,GPIO.HIGH)   
                GPIO.output(Motor1Enable,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.LOW) 
                GPIO.output(Motor2B,GPIO.HIGH)   
                GPIO.output(Motor2Enable,GPIO.HIGH)
                #Left side off
                GPIO.output(Motor3Enable,GPIO.LOW)
                GPIO.output(Motor4Enable,GPIO.LOW)
                #print("Turn Half Left Backwards")
                
            else:
                #motors off
                GPIO.output(Motor1Enable,GPIO.LOW)
                GPIO.output(Motor2Enable,GPIO.LOW)
                GPIO.output(Motor3Enable,GPIO.LOW)
                GPIO.output(Motor4Enable,GPIO.LOW)
                #print("stopped")
        
            
   
    
pygame.quit()
