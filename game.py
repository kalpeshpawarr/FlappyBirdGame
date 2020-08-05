import pygame, sys

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,900))
    screen.blit(floor_surface,(floor_x_pos + 576,900))

pygame.init()
screen = pygame.display.set_mode((576,1024))

bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('assets/omkya.jpg').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface,(0,0))
    screen.blit(bird_surface,bird_rect)
    floor_x_pos -= 0.5
    screen.blit(floor_surface,(floor_x_pos,900))
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0






    pygame.display.update()
    

 
