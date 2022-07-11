from tkinter import W
import pygame

GREEN = (0,102,0)
BROWN = (102,102,0)
WHITE = (255,255,255)
RED = (155,0,0)

def run_camera(fname):
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 12)

    screen = pygame.display.set_mode((1420,720))
    pygame.display.set_caption("PD_Kacper_Achramowicz_xD")
    run = True
    

    # pygame.draw.rect(screen, GREEN, (700, 500, 120, 100))
    # pygame.draw.rect(screen, BROWN, (400, 60, 120, 100))
    # pygame.draw.rect(screen, (255,255,255), (450, 100, 120, 100))
    
    data = {}
    with open(fname, "r") as f:
        for line in f.readlines():
           frmt = line.strip('\n').split(":")
           tuples = list(map(lambda x: x[1:-1].split(","), frmt[1].split(";")))
           data[frmt[0]] = tuples[:-1]

    #OUTER
    pygame.draw.rect(screen, GREEN, (110, 10, 100, 100), 10)
    screen.blit(myfont.render(f"{data['OUTER'][0][0]}", True, WHITE), (130, 50))
    screen.blit(myfont.render(f"cards: {data['OUTER'][0][1]}", True, WHITE), (130, 70))
    
    without_corners = data['OUTER'][4:]
    for i in range(5):
        x = 10 + ((i%7)+1)*200
        y = 10
        pygame.draw.rect(screen, GREEN, (x, y, 200, 100), 10)
        screen.blit(myfont.render(f"{without_corners[i][0]}", True, WHITE), (x+20, y+40))
        screen.blit(myfont.render(f"cards: {without_corners[i][1]}", True, WHITE), (x+20, y+60))
    pygame.draw.rect(screen, GREEN, (x+200, 10, 100, 100), 10)
    screen.blit(myfont.render(f"{data['OUTER'][1][0]}", True, WHITE), (x +230, 50))
    screen.blit(myfont.render(f"cards: {data['OUTER'][0][1]}", True, WHITE), (x +230, 70))
    for i in range(7,13):
        x = 110
        y = 10 +((i%7)+1)*100
        if i == 12:
            screen.blit(myfont.render(f"{data['OUTER'][2][0]}", True, WHITE), (130, y+40))
            screen.blit(myfont.render(f"cards: {data['OUTER'][0][1]}", True, WHITE), (130, y+60))
        else:
            screen.blit(myfont.render(f"{without_corners[i][0]}", True, WHITE), (x+20, y+40))
            screen.blit(myfont.render(f"cards: {without_corners[i][1]}", True, WHITE), (x+20, y+60))
        pygame.draw.rect(screen, GREEN, (x, y, 100, 100), 10)
    for i in range(14,19):
        x = 10 + ((i%7)+1)*200
        y = 610
        pygame.draw.rect(screen, GREEN, (x, y, 200, 100), 10)
    
        screen.blit(myfont.render(f"{without_corners[i][0]}", True, WHITE), (x+20, y+40))
        screen.blit(myfont.render(f"cards: {without_corners[i][1]}", True, WHITE), (x+20, y+60))
    pygame.draw.rect(screen, GREEN, (x+200, 10, 100, 100), 10)
    screen.blit(myfont.render(f"{data['OUTER'][3][0]}", True, WHITE), (x+220, y+40))
    screen.blit(myfont.render(f"cards: {data['OUTER'][3][1]}", True, WHITE), (x+220, y+60))
    for i in range(21,27):
        x = 1210
        y = 10 +((i%7)+1)*100
        pygame.draw.rect(screen, GREEN, (x, y, 100, 100), 10)
        if i == 26: 
            pass
        else:
            screen.blit(myfont.render(f"{without_corners[i-6][0]}", True, WHITE), (x+20, y+40))
            screen.blit(myfont.render(f"cards: {without_corners[i-6][1]}", True, WHITE), (x+20, y+60))

    #  INNER
    pygame.draw.rect(screen, BROWN, (210, 110, 200, 100), 10)
    screen.blit(myfont.render(f"{data['INNER'][0][0]}", True, WHITE), (230, 150))
    screen.blit(myfont.render(f"cards: {data['INNER'][0][1]}", True, WHITE), (230, 180))
    for i in range(3):
        x = 210 + ((i%7)+1)*200
        y = 110
        pygame.draw.rect(screen, BROWN, (x, y, 200, 100), 10)
        screen.blit(myfont.render(f"{data['INNER'][i+1][0]}", True, WHITE), (x+20, y+40))
        screen.blit(myfont.render(f"cards: {data['INNER'][i+1][1]}", True, WHITE), (x+20, y+60))
    pygame.draw.rect(screen, BROWN, (x+200, 110, 200, 100), 10)
    screen.blit(myfont.render(f"{data['INNER'][i+2][0]}", True, WHITE), (x+220, y+40))
    screen.blit(myfont.render(f"cards: {data['INNER'][i+2][1]}", True, WHITE), (x+220, y+60))
    for i in range(4):
        x = 210
        y = 110 +((i%7)+1)*100
        pygame.draw.rect(screen, BROWN, (x, y, 200, 100), 10)
        screen.blit(myfont.render(f"{data['INNER'][i+5][0]}", True, WHITE), (x+20, y+40))
        screen.blit(myfont.render(f"cards: {data['INNER'][i+5][1]}", True, WHITE), (x+20, y+60))
    for i in range(3):
        x = 210 + ((i%7)+1)*200
        y = 510
        pygame.draw.rect(screen, BROWN, (x, y, 200, 100), 10)
        screen.blit(myfont.render(f"{data['INNER'][i+9][0]}", True, WHITE), (x+20, y+40))
        screen.blit(myfont.render(f"cards: {data['INNER'][i+9][1]}", True, WHITE), (x+20, y+60))
    pygame.draw.rect(screen, BROWN, (x+200, 110, 200, 100), 10)
    screen.blit(myfont.render(f"{data['INNER'][i+9][0]}", True, WHITE), (x+20, y+40))
    screen.blit(myfont.render(f"cards: {data['INNER'][i+9][1]}", True, WHITE), (x+20, y+60))
    for i in range(4):
        x = 1010
        y = 110 +((i%7)+1)*100
        pygame.draw.rect(screen, BROWN, (x, y, 200, 100), 10)
        screen.blit(myfont.render(f"{data['INNER'][i+10][0]}", True, WHITE), (x+20, y+40))
        screen.blit(myfont.render(f"cards: {data['INNER'][i+10][1]}", True, WHITE), (x+20, y+60))

    #ENDGAME
    pygame.draw.rect(screen, RED, (410, 210, 200, 100), 10)
    screen.blit(myfont.render(f"{data['ENDGAME'][0][0]}", True, WHITE), (430, 250))
    screen.blit(myfont.render(f"cards: {data['ENDGAME'][0][1]}", True, WHITE), (430, 270))
    for i in range(2):
        x = 410 + ((i%7)+1)*200
        y = 210
        pygame.draw.rect(screen, RED, (x, y, 200, 100), 10)
        screen.blit(myfont.render(f"{data['ENDGAME'][i+1][0]}", True, WHITE), (x+20, y+40))
        screen.blit(myfont.render(f"cards: {data['ENDGAME'][i+1][1]}", True, WHITE), (x+20, y+60))
    pygame.draw.rect(screen, RED, (x, 310, 200, 100), 10)
    screen.blit(myfont.render(f"{data['ENDGAME'][i+4][0]}", True, WHITE), (x+20, 350))
    screen.blit(myfont.render(f"cards: {data['ENDGAME'][i+4][1]}", True, WHITE), (x+20, 370))
    for i in range(2):
        x = 410
        y = 210 +((i%7)+1)*100
        pygame.draw.rect(screen, RED, (x, y, 200, 100), 10)
        screen.blit(myfont.render(f"{data['ENDGAME'][i+3][0]}", True, WHITE), (x+20, y+40))
        screen.blit(myfont.render(f"cards: {data['ENDGAME'][i+3][1]}", True, WHITE), (x+20, y+60))
    pygame.draw.rect(screen,RED,(x+200, 410, 200, 100), 10 )
    screen.blit(myfont.render(f"{data['ENDGAME'][-2][0]}", True, WHITE), (x+220, 450))
    screen.blit(myfont.render(f"cards: {data['ENDGAME'][-2][1]}", True, WHITE), (x+220, 470))
    pygame.draw.rect(screen,(255,0,0),(x+400, 410, 200, 100), 10 )
    screen.blit(myfont.render(f"{data['ENDGAME'][-1][0]}", True, WHITE), (x+420, 450))
    screen.blit(myfont.render(f"cards: {data['ENDGAME'][-1][1]}", True, WHITE), (x+420, 470))
        
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False