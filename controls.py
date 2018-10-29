#Created by: Alexander Freer
#Oct. 30, 2018

import pygame


pygame.init()

window = pygame.display.set_mode((225,225))
pygame.display.set_caption("Drive")
background = pygame.image.load("wheel2.jpg").convert()
#try to make image turn when driving the car!


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
            
            #print ("------------")
            #print ("Right:", rightSide)
            #print ("Left:", leftSide)

            if (leftSide == -50):
                #Right side forwards
                #left side backwards
                print("Turn Left")
            elif (rightSide == -50):
                #Right side backwards
                #left side forwards
                print("Turn Right")
            elif (rightSide == 100 and leftSide == 50 ):
                #Right side forwards
                #Left side off
                print("Turn half left")
            elif (rightSide == 50 and leftSide == 100 ):
                #Right side off
                #Left side forwards
                print("Turn half right")
            elif (rightSide == 100 and leftSide == 100 ):
                #Right side forwards
                #Left side forwards
                print("full steam ahead")
                
            elif (rightSide == -100 and leftSide == -100 ):
                #Right side backwards
                #Left side backwards
                print("full steam backwards")
            elif (rightSide == -150 and leftSide == -100 ):
                #Right side off
                #Left side Backwards
                print("Turn Half Right Backwards")
            elif (rightSide == -100 and leftSide == -150 ):
                #Right side backwards
                #Left side off
                print("Turn Half Left Backwards")
            else:
                #motors off
                print("stopped")
         
                
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
                #left side backwards
                print("Turn Left")
            elif (rightSide == -50):
                #Right side backwards
                #left side forwards
                print("Turn Right")
            elif (rightSide == 100 and leftSide == 50 ):
                #Right side forwards
                #Left side off
                print("Turn half left")
            elif (rightSide == 50 and leftSide == 100 ):
                #Right side off
                #Left side forwards
                print("Turn half right")
            elif (rightSide == 100 and leftSide == 100 ):
                #Right side forwards
                #Left side forwards
                print("full steam ahead")
                
            elif (rightSide == -100 and leftSide == -100 ):
                #Right side backwards
                #Left side backwards
                print("full steam backwards")
            elif (rightSide == -150 and leftSide == -100 ):
                #Right side off
                #Left side Backwards
                print("Turn Half Right Backwards")
            elif (rightSide == -100 and leftSide == -150 ):
                #Right side backwards
                #Left side off
                print("Turn Half Left Backwards")
            else:
                #motors off
                print("stopped")
        
            
   
    
pygame.quit()
