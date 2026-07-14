import words
import random
import pygame
import sys
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen_width = screen.get_width()
screen_hight = screen.get_height()
pygame.display.set_caption("greengle")
background_color = (50, 80, 50)  
screen.fill(background_color)
a=0
a1=0
b=0
backgroundimg = pygame.image.load("background.png")
startbutton = pygame.image.load("start_button.png")
titletext = pygame.image.load("titletext.png")
c=[0,0,0,0,0]
l=["     ","     ","     ","     ","     ","     "]
input_word = []
font = pygame.font.SysFont("Arial", 45)
word = random.choice(words.five_letter_words)
mousex,mousey=pygame.mouse.get_pos()
running=True
def button(buttonx,buttony,buttonscalex,buttonscaley,buttonimage,isdraw):
    if isdraw:
        screen.blit(pygame.transform.scale(buttonimage, (buttonscalex, buttonscaley)),(buttonx,buttony)) 
    if event.type == pygame.MOUSEBUTTONDOWN and buttonx<mousex and mousey<buttonx+buttonscalex and buttony<mousey and mousey<buttony+buttonscaley:
        return(True)


while running:

    screen_width = screen.get_width()
    screen_hight = screen.get_height()
    for event in pygame.event.get():
        if button(screen_width/2-125,screen_hight/2,250,100,startbutton,True):
            running = False
        elif event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    screen.fill(background_color)
    mousex,mousey=pygame.mouse.get_pos()
    screen.blit(pygame.transform.scale(backgroundimg, (screen_width*2, screen_hight*2)),(-100,-100)) 
    screen.blit(pygame.transform.scale(titletext, (800, 1000)),(screen_width/2-400,-350))
    pygame.display.flip()
print(word)
clock = pygame.time.Clock()
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
                input_word = []
                a+=1
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
        print("Congratulations! You guessed the word correctly.")
        break
    elif a == 6:
        print("Game over. The word was: " + word)   
    clock.tick(60)
pygame.quit()
sys.exit()