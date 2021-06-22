#from snake_final import *
#from snake_bfs import *
#from snake_ideal import *
#from snake_github import *
from snake_s import *

def draw_screen(surface):
    surface.fill(SURFACE_CLR)

def draw_grid(surface):
    x = 0
    y = 0
    for r in range(ROWS):
        x = x + SQUARE_SIZE
        y = y + SQUARE_SIZE
        if r == ROWS-1:
            #print('MAX')
            pygame.draw.line(surface, GRID_CLR, (x, 0), (x, HEIGHT))
            pygame.draw.line(surface, WHITE, (0, y), (WIDTH, y))
        else:
            pygame.draw.line(surface, GRID_CLR, (x, 0), (x, HEIGHT))
            pygame.draw.line(surface, GRID_CLR, (0, y), (WIDTH, y))

def draw_text(game_surface, text, color):
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)
    text_surface = BASICFONT.render(text, True, color)
    textRect = text_surface.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    game_surface.blit(text_surface, textRect)

    if text == 'You Died':
        text_surface_1 = BASICFONT.render('Press Enter To Restart', True, WHITE)
        textRect_1 = text_surface_1.get_rect()
        textRect_1.center = (WIDTH // 2, HEIGHT // 2 + 30)
        game_surface.blit(text_surface_1, textRect_1)

def draw_score(game_surface, CURRENT_TIME, score):
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)

    text_score = BASICFONT.render('Score: '+str(score), True, WHITE)
    text_time = BASICFONT.render('Time: '+str(CURRENT_TIME), True, WHITE)

    textRect_score = text_score.get_rect()
    textRect_time = text_time.get_rect()

    textRect_score.center = (WIDTH//2-50, HEIGHT + GAP_SIZE//2+3)
    textRect_time.center = (WIDTH//2+50, HEIGHT + GAP_SIZE//2+3)

    game_surface.blit(text_score, textRect_score)
    game_surface.blit(text_time, textRect_time)


def print_userguide():
    print('\nWelcome to Greedy Snake King AI (hand-version).')
    print('User Guide:\n You will be able to press key w, a, s, d or arrow keys to control the snake.\n Good Luck!')

def main():

    # print_userguide()
    pygame.init()

    pygame.display.set_caption("Snake Game")
    game_surface = pygame.display.set_mode((WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake(game_surface)

    mainloop = True
    START, GAMEOVER, START_TIME = False, False, 0
    bef_time = 0 ##

    # create txt file
    #path = 'output_bfs.txt'
    #path = 'output_final.txt'
    #path = 'output_ideal.txt'
    #path = 'output_github.txt'
    path = 'output_s.txt'
    f = open(path, 'w')

    while mainloop:

        draw_screen(game_surface)
        draw_grid(game_surface)
        clock.tick(FPS)

        if not START:
            draw_text(game_surface, 'Press Enter To Start', WHITE)
        elif START and not GAMEOVER:
            if START_TIME == 0:
                START_TIME = pygame.time.get_ticks()
            CURRENT_TIME = (pygame.time.get_ticks() - START_TIME) // 1000
            draw_score(game_surface, CURRENT_TIME, snake.score)
        elif START and GAMEOVER:
            draw_text(game_surface, 'You Died', RED)
            draw_score(game_surface, CURRENT_TIME, snake.score)

        COMMAND_KEY = snake.update(START, GAMEOVER)
        if COMMAND_KEY == 'finish':
            mainloop = False
        elif COMMAND_KEY == 'start':
            START = True
        elif COMMAND_KEY == 'dead':
            GAMEOVER = True
            f.close()
            break
        elif COMMAND_KEY == 'restart':
            GAMEOVER = False
            START_TIME = 0
            snake.reset()

        # calculate
        unit_time = 0
        if START_TIME != 0:
            unit_time = (pygame.time.get_ticks() - START_TIME) // 100
        if unit_time != bef_time and START:
            bef_time = unit_time
            f.write(str(unit_time)+' '+str(snake.score)+'\n')
        if snake.score > 570:
            f.close()
            break

        pygame.display.update()

    f.close()
    pygame.quit()

if __name__ == '__main__':
    main()