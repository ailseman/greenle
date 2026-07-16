import words
import random
import pygame
import sys
from images import imageworker
startbutton = imageworker.startbutton
backgroundimg = imageworker.backgroundimg
shuflemodebutton = imageworker.shuflemodebutton
clasicmodebutton = imageworker.clasicmodebutton
titletext = imageworker.titletext
pygame.init()
pygame.font.init()
screen= pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen_width = screen.get_width()
screen_hight = screen.get_height()
pygame.display.set_caption("greengle")
background_color = (50, 80, 50)  
screen.fill(background_color)
a=0
won=False
mode=0
a1=0
clock = pygame.time.Clock()
b=0
c=[0,0,0,0,0]
l=["     ","     ","     ","     ","     ","     "]
input_word = []
font = pygame.font.SysFont("Arial", int((screen_hight+screen_width)/30))
font1 = pygame.font.SysFont("Arial", int((screen_hight+screen_width)/5))
word = random.choice(words.five_letter_words)
mousex,mousey=pygame.mouse.get_pos()
running=True


def button(buttonx,buttony,buttonscalex,buttonscaley,buttonimage,isdraw,hasevent = pygame.MOUSEBUTTONUP):
    if isdraw == True:
            screen.blit(pygame.transform.scale(buttonimage, (buttonscalex, buttonscaley)),(buttonx,buttony)) 
    if hasevent == pygame.MOUSEBUTTONDOWN and mousex>buttonx and mousex<buttonx+buttonscalex and mousey>buttony and mousey<buttony+buttonscaley:
        return(True)


while running:

    screen.fill(background_color)
    screen_width = screen.get_width()
    screen_hight = screen.get_height()

    mousex,mousey=pygame.mouse.get_pos()
    screen.blit(pygame.transform.scale(backgroundimg, (screen_width*2, screen_hight*2)),(-100,-100))
    screen.blit(pygame.transform.scale(titletext, (screen_width,screen_hight*1.75)),(0,0-screen_hight/1.5))
    button(screen_width/2-125,screen_hight/2,250,100,startbutton,True)
    for event in pygame.event.get():
        if  button(screen_width/2-125,screen_hight/2,250,100,startbutton,False,event.type):
            running=False
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    clock.tick(60)
    pygame.display.flip()    
    




running = True
while running:
    screen.fill(background_color)
    screen_hight = screen.get_height()
    screen_width = screen.get_width()
    screen.blit(pygame.transform.scale(backgroundimg, (screen_width*2, screen_hight*2)),(-100,-100))
    button(screen_width-screen_width/8-250,screen_hight/2,250,100,clasicmodebutton,True)
    button(screen_width/8,screen_hight/2,250,100,shuflemodebutton,True)
    for event in pygame.event.get():
        if button(screen_width/8,screen_hight/2,250,100,shuflemodebutton,False,event.type):
                mode=2
                running=False
        elif button(screen_width-screen_width/8-250,screen_hight/2,250,100,clasicmodebutton,False,event.type):
                mode=1
                running=False
        elif event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    pygame.display.flip()   
    clock.tick(60)
    mousex,mousey=pygame.mouse.get_pos()
    pygame.display.flip()
running = True
while running:
    print(word)
    while a < 6:
        screen_width = screen.get_width()
        screen_hight = screen.get_height()
        pygame.display.flip()
        screen.fill((50,80,50))
        screen.blit(pygame.transform.scale(backgroundimg,(screen_width*2,screen_hight*2)),(-100,-100))
        a1=0
        for y in l:
            b=0
            for x in y:
                pygame.draw.rect(screen, (100, 100, 100), (screen_width/10 * b+screen_width/4, screen_hight/6 * a1, 45, 45), 2)
                if x in word and not x == word[b]:
                    c[b] = 1
                    one = font.render(x, True, (150, 150, 150))
                    screen.blit(one, (screen_width/10 * b+screen_width/4, screen_hight/6 * a1))
                elif x in word and x == word[b]:
                    c[b] = 2
                    two = font.render(x, True, (255, 255, 255))
                    screen.blit(two, (screen_width/10 * b+screen_width/4, screen_hight/6 * a1))
                else:
                    c[b] = 0
                    three = font.render(x, True, (50, 50, 50))
                    screen.blit(three, (screen_width/10 * b+screen_width/4, screen_hight/6 * a1))
                b+=1
            a1+=1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(input_word) == 5 and "".join(input_word) in words.five_letter_words:
                    l[a]=input_word
                    if "".join(input_word) == word:
                        print("Congratulations! You guessed the word correctly.")
                        won = True
                        a = 10
                    else:
                        input_word = []
                        a+=1
                        if mode == 2:
                            word = random.choice(words.five_letter_words)
                            print(word)
                elif event.key == pygame.K_BACKSPACE:
                    input_word = input_word[:-1]
                elif len(input_word) < 5:
                    input_word.append(event.unicode)
            elif event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        b=0
        for x in input_word:
            pygame.draw.rect(screen, (100, 100, 100), (screen_width/10 * b+screen_width/4, screen_hight/6 * a, 45, 45), 2)
            blank = font.render(x, True, (0, 0, 0))
            screen.blit(blank, (screen_width/10 * b+screen_width/4, screen_hight/6 * a))
            b+=1
        b=0
        if c == [2,2,2,2,2]:
            a = 10
        clock.tick(60)
    runningwinloose = True
    while runningwinloose == True:
        screen_width = screen.get_width()
        screen_hight = screen.get_height()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    runningwinloose = False
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if won:
                screen.fill((0,255,0))
                wintext = font1.render("you won", True, (0,0,0))
                screen.blit(wintext, wintext.get_rect(center=(screen_width/2, screen_hight/2)))
                loosetext = font.render(f"the word was {word}", True, (0, 0, 0))
                screen.blit(loosetext, loosetext.get_rect(center=(screen_width/2, screen_hight/8)))
                pygame.display.flip()
            else:
                screen.fill((255,0,0))
                loosetext = font1.render("you lost", True, (0, 0, 0))
                screen.blit(loosetext, loosetext.get_rect(center=(screen_width/2, screen_hight/2)))
                loosetext = font.render(f"the word was {word}", True, (0, 0, 0))
                screen.blit(loosetext, loosetext.get_rect(center=(screen_width/2, screen_hight/8)))
                pygame.display.flip()
        clock.tick(60)
    a=0
    mode=0
    a1=0
    clock = pygame.time.Clock()
    b=0
    c=[0,0,0,0,0]
    l=["     ","     ","     ","     ","     ","     "]
    won=False
pygame.quit()
sys.exit()