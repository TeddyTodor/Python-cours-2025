import pygame
import os


width = 900
height = 500

spaceship_width = 80
spaceship_height = 60

white = (255, 255, 255)
black = (0, 0, 0)

window = pygame.display.set_mode((width, height)) #Fenetre de jeuµ
pygame.display.set_caption("Space Game")

Y_image = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png")) # image
Y_spaceship = pygame.transform.rotate(pygame.transform.scale( # acteur
    Y_image,(spaceship_width, spaceship_height)), -90
    )

R_image = pygame.image.load(os.path.join("Assets", "spaceship_red.png")) # image
R_spaceship = pygame.transform.rotate(pygame.transform.scale( # acteur
    R_image,(spaceship_width, spaceship_height)), 90
    )

def R_control (key, rect) :
    if key[pygame.K_UP] :
        rect.y -= 5
    if key[pygame.K_DOWN] :
        rect.y += 5
    if key[pygame.K_LEFT] :
        rect.x -= 5
    if key[pygame.K_RIGHT] :
        rect.x += 5

def Y_control (key, rect) :
    if key[pygame.K_z] :
        rect.y -= 5
    if key[pygame.K_s] :
        rect.y += 5
    if key[pygame.K_q] :
        rect.x -= 5
    if key[pygame.K_d] :
        rect.x += 5

def main () :

    Y_rect = pygame.Rect(100, 300, spaceship_width, spaceship_height) # hitbox
    R_rect = pygame.Rect(700, 300, spaceship_width, spaceship_height) # hitbox

    run = True
    clock = pygame.time.Clock() 

    while run :
        clock.tick(60) #Frame par seconde 

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        key_pressed = pygame.key.get_pressed()
        Y_control (key_pressed, Y_rect)
        R_control (key_pressed, R_rect)

        window.fill(black) # Remplis la fentre
                
        window.blit(R_spaceship, R_rect) # Affiche le spaceship + hitbox (pas afficher)
        window.blit(Y_spaceship, Y_rect) # Affiche le spaceship + hitbox (pas afficher)
        pygame.display.update()     # Mets a jour

    pygame.quit() #Ferme la fenetre 

main ()