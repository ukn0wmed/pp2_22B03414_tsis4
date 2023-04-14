import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    shape = 'circle'
    points = []

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'erase'
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_s:
                    shape = 'rectangle'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    start_pos = event.pos
                    end_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    end_pos = event.pos
                    if shape == 'circle':
                        draw_circle(screen, start_pos, end_pos, mode)
                    elif shape == 'rectangle':
                        draw_rectangle(screen, start_pos, end_pos, mode)

        pygame.display.flip()

        clock.tick(60)

def draw_circle(screen, start_pos, end_pos, color_mode):
    x1, y1 = start_pos
    x2, y2 = end_pos
    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    elif color_mode == 'erase':
        color = (0, 0, 0)

    pygame.draw.circle(screen, color, start_pos, radius, 0)

def draw_rectangle(screen, start_pos, end_pos, color_mode):
    x1, y1 = start_pos
    x2, y2 = end_pos

    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    elif color_mode == 'erase':
        color = (0, 0, 0)

    pygame.draw.rect(screen, color, pygame.Rect(x1, y1, x2 - x1, y2 - y1), 0)

main()