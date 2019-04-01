# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:29:15 2019



next steps:
    convert words to array
        get letter start subarry ranges to shorten search time
    convert deffintions to array
    
    draw and populate tile bag
    
    animate special tile squares
    
    score calculator 
        with special effects
        
    placement and word checker mechanic
    
    highscore
    
    2nd player (hand and discreteness)


    future:
        ai
        max score ranking
        click for word deffinitiion
        


@author: gilld
"""

import pygame, random
''' colours are not deffined so to decect we need to store them as rgb values
note how i put them outside all the functions therefor they are gobal and can be accessed anywhre.. also note the are tuples'''

black=(0,0,0)#black is all colours at a min
white=(255,255,255)#white is all colours at a max
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
beige=(210,190,150)

display_width=650
display_hieght=650

#main does setup and calls the main loop
pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_hieght))  #top left is 0,0 ... soemthimes better to make these variables
gameDisplay.fill(beige)
#puts a label on the window to help the user know whats going on
pygame.display.set_caption('Scrabble??!')

def mouse_checker(x,y,rectangles):  #works!
    for row in range(0,15):
        for collumn in range (0,15):
            temp_rect=rectangles[row][collumn]
            temp_y=temp_rect.top
            temp_x=temp_rect.left
            
            if (temp_y<y and y<temp_y+40 ):
                if(temp_x<x and x<temp_x+40):
                    #normally would return center as position to place the 
                    pygame.draw.rect(gameDisplay,blue,temp_rect)
                    pygame.display.update()
    



def game_logic():
    text_display("Welcome to the world of Scrabble",(display_width/2, display_hieght/2))
    text_display("Created by David Gill",(display_width/2,display_hieght/2-40))
    pygame.display.update()
    pygame.time.delay(2000)
    ''' high_score_checker(score)'''
    #infomation gets hidden in highscore
    gameDisplay.fill(beige)
    pygame.draw.rect(gameDisplay,black,(50,2,display_width-50,display_hieght-50),5)  #width=597-100   height 600
    
        
    rectangles=[]
    for x in range (0,15):
        newrow=[]
        for y in range (0,15):
            temp_coords=pygame.Rect(50+y*40,3+x*40, 40, 40)#set a rectangle in each section
            pygame.draw.rect(gameDisplay,black,temp_coords,3)
            newrow.append(temp_coords)
        rectangles.append(newrow)
    
    pygame.display.update()
    done=0
    while ( not done):  # .. while not true loop

                        #this grabs any event that happens on the window, where is mouse click, key click.... the loop will basicallyl check this once per frame
        for event in pygame.event.get():

            #giving the user a manual way out
            if (event.type== pygame.QUIT): # pygame. quit looks for when they try to x out the window
                fill_colour=beige
                gameDisplay.fill(fill_colour)
                return 0,"manual"
            
            elif (event.type ==pygame.MOUSEBUTTONDOWN):
                x, y = event.pos
                mouse_checker(x,y,rectangles)


def text_display(text,location,colour=white,size=32):
    font =pygame.font.SysFont('arial',size)# type then size
    try:
       textSurface =font.render(text, True , colour )# makes a text retangle
    except TypeError:
        print("sorry we couldn't print that, make sure you are passing strings")
        return
    else:
        text_rectangle= textSurface.get_rect()
        text_rectangle.center=(location) #this centers it at location
        gameDisplay.blit(textSurface,text_rectangle)
        pygame.display.update()



def main():
    Exit=0

    while (not Exit):

        good_words,cauuse_of_death=game_logic()# game takes place here

        if cauuse_of_death=="manual":
            Exit=1
         
            
            
        else:
            gameDisplay.fill(beige)
            text_display("Hope you had fun",(display_width/2, display_hieght/2))
            pygame.display.update()
            
            
            screen_click=0
            while not screen_click:
                for event in pygame.event.get():
                    if (event.type== pygame.QUIT):
    
                        Exit=1
                        screen_click=1
    
    
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        screen_click=1
                        gameDisplay.fill(beige)
                        pygame.display.update()



    pygame.quit()
    quit()

if __name__=="__main__":
    main()