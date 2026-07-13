import words
import random
import pygame
import sys
pygame.init()
pygame.font.init()
screen_width = 800
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("greenle")
background_color = (40, 44, 52)  
screen.fill(background_color)
a=0
b=0
c=[0,0,0,0,0]
l=["     ","     ","     ","     ","     "]
input_word = []
font = pygame.font.SysFont("Arial", 45)
word = random.choice(words.five_letter_words)
print(word)
while a < 5:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    print("Enter a five-letter word: ")
    isdrawing = True
    while isdrawing == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(input_word) == 5:
                    l[a]=input_word
                    isdrawing = False
                elif event.key == pygame.K_BACKSPACE:
                    input_word = input_word[:-1]
                elif len(input_word) < 5:
                    input_word.append(event.unicode)
            b=0
            screen.fill((50,50,50))
            for x in input_word:
                pygame.draw.rect(screen, (100, 100, 100), (screen_width/10 * b+screen_width/4, screen_hight/5 * a, 45, 45), 2)
                blank = font.render(x, True, (0, 0, 0))
                screen.blit(blank, (screen_width/10 * b+screen_width/4, screen_hight/5 * a))
                b+=1
            pygame.display.flip()
    b=0
    if len(input_word) != 5:
        print("Please enter a five-letter word.")
        continue
    for y in l:
        b=0
        for x in y: 
            if x in word and not x == word[b]:
                c[b] = 1
                one = font.render(x, True, (255, 255, 0))
                screen.blit(one, (screen_width/10 * b+screen_width/4, screen_hight/5 * a))
            elif x in word and x == word[b]:
                c[b] = 2
                two = font.render(x, True, (0, 255, 0))
                screen.blit(two, (screen_width/10 * b+screen_width/4, screen_hight/5 * a))
            else:
                c[b] = 0
                three = font.render(x, True, (255, 0, 0))
                screen.blit(three, (screen_width/10 * b+screen_width/4, screen_hight/5 * a))
            b+=1
    a+=1
    input_word = []
    print(f"{c[0]}{c[1]}{c[2]}{c[3]}{c[4]}")
    if c == [2,2,2,2,2]:
        print("Congratulations! You guessed the word correctly.")
        break
    elif a == 5:
        print("Game over. The word was: " + word)
pygame.quit()
sys.exit()