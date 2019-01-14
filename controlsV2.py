
import pygame
from gpiozero
import Motor, OutputDevice 


pygame.init()

window = pygame.display.set_mode((225,225))
pygame.display.set_caption("Drive")
background = pygame.image.load("wheel2.jpg").convert()
#try to make image turn when driving the car!

motor1 = Motor(24, 27)
motor1_enable = OutputDevice(5, initial_value=1)
motor2 = Motor(6, 22)
motor2_enable = OutputDevice(17, initial_value=1)
motor3 = Motor(23, 16)
motor3_enable = OutputDevice(12, initial_value=1)
motor4 = Motor(13, 18)
motor4_enable = OutputDevice(25, initial_value=1) 


driveLoop = True

#used to determine the direction of the car
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
                #Turn Left
                motor1.forwards()
                motor2.forwards()
                motor3.backwards()
                motor4.backwards()
                
            elif (rightSide == -50):
                #Turn Right
                motor3.forwards()
                motor4.forwards()
                motor1.backwards()
                motor2.backwards()
               
                
            elif (rightSide == 100 and leftSide == 50 ):
                #Turn half left
               
                motor3.stop()
                motor4.stop()
                motor1.forward(0.5)
                motor2.forward(0.5) 
                
            elif (rightSide == 50 and leftSide == 100 ):
                #Turn half right
                motor1.stop()
                motor2.stop()
                motor3.forward(0.5)
                motor4.forward(0.5) 
                
            elif (rightSide == 100 and leftSide == 100 ):
                #full steam ahead
                motor1.forwards()
                motor2.forwards()
                motor3.forwards()
                motor4.forwards()

            elif (rightSide == -100 and leftSide == -100 ):
                #full steam backwards
                motor1.backwards()
                motor2.backwards()
                motor3.backwards()
                motor4.backwards()
                
            elif (rightSide == -150 and leftSide == -100 ):
                #Turn Half Right Backwards
                motor1.stop()
                motor2.stop()
                motor3.reverse()
                motor4.reverse()
                
            elif (rightSide == -100 and leftSide == -150 ):
                #Turn Half Left Backwards
                motor1.stop()
                motor2.stop()
                motor3.reverse()
                motor4.reverse()
                
            else:
                #motors off
                motor1.stop()
                motor2.stop()
                motor3.stop()
                motor4.stop()
         
                
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
            
            if (leftSide == -50):
                #Turn Left
                motor1.forwards()
                motor2.forwards()
                motor3.backwards()
                motor4.backwards()
                
            elif (rightSide == -50):
                #Turn Right
                motor3.forwards()
                motor4.forwards()
                motor1.backwards()
                motor2.backwards()
               
                
            elif (rightSide == 100 and leftSide == 50 ):
                #Turn half left
               
                motor3.stop()
                motor4.stop()
                motor1.forward(0.5)
                motor2.forward(0.5) 
                
            elif (rightSide == 50 and leftSide == 100 ):
                #Turn half right
                motor1.stop()
                motor2.stop()
                motor3.forward(0.5)
                motor4.forward(0.5) 
                
            elif (rightSide == 100 and leftSide == 100 ):
                #full steam ahead
                motor1.forwards()
                motor2.forwards()
                motor3.forwards()
                motor4.forwards()

            elif (rightSide == -100 and leftSide == -100 ):
                #full steam backwards
                motor1.backwards()
                motor2.backwards()
                motor3.backwards()
                motor4.backwards()
                
            elif (rightSide == -150 and leftSide == -100 ):
                #Turn Half Right Backwards
                motor1.stop()
                motor2.stop()
                motor3.reverse()
                motor4.reverse()
                
            elif (rightSide == -100 and leftSide == -150 ):
                #Turn Half Left Backwards
                motor1.stop()
                motor2.stop()
                motor3.reverse()
                motor4.reverse()
                
            else:
                #motors off
                motor1.stop()
                motor2.stop()
                motor3.stop()
                motor4.stop()
        
            
   
    
pygame.quit()

