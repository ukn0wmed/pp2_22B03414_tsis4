import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []

    drawing = False
    erasing = False
    shape = 'line'

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # Determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_l:
                    shape = 'line'
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_t:
                    shape = 'rectangle'
                elif event.key == pygame.K_e:
                    erasing = not erasing

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click
                    drawing = True
                    start_position = event.pos
                elif event.button == 3:  # right click
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # left click
                    drawing = False
                    end_position = event.pos
                    if shape == 'circle':
                        drawCircle(screen, start_position, end_position, mode)
                    elif shape == 'rectangle':
                        drawRectangle(screen, start_position, end_position, mode)

            if event.type == pygame.MOUSEMOTION and drawing and shape == 'line':
                # If mouse moved and left button is pressed, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]

        screen.fill((0, 0, 0))

        # Draw all points
        i = 0
        while i < len(points) - 1:
            if erasing:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, 'white', erase=True)
            else:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1

        pygame.display.flip()

        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode, erase=False):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    if erase:
        color = (255, 255, 255)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def drawCircle(screen, start, end, color_mode):
    center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)

    radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5 // 2)

    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)

    pygame.draw.circle(screen, color, center, radius, 1)


def drawRectangle(screen, start, end, color_mode):
    top_left = (min(start[0], end[0]), min(start[1], end[1]))

    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])

    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)

    pygame.draw.rect(screen, color, pygame.Rect(top_left, (width, height)), 1)


if __name__ == '__main__':
    main()
