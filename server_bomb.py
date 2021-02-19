import socket
import threading
import pygame
import sys

ADD_CONNECT_SUCCESS = pygame.USEREVENT + 1
ADD_CONNECT_FAILED = pygame.USEREVENT + 2
ADD_SEND = pygame.USEREVENT + 3

pygame.init()
pygame.mixer.set_num_channels(128)
#screen = pygame.display.set_mode((1200, 500))
screen = pygame.display.set_mode((1400, 700))
font = pygame.font.SysFont(pygame.font.get_default_font(), 64)
break_sound = pygame.mixer.Sound(r"C:\Users\xcdyj\Desktop\break.ogg")
socket.setdefaulttimeout(100)
clock = pygame.time.Clock()

WIDTH = 20
HEIGHT = 20
THREAD_NUM = WIDTH * HEIGHT
BLOCK_WIDTH = 25
BLOCK_SPACK = 0
CLOSE = False

#send_times = int(input("Send times:"))
send_times = 0

send_cnt = 0
cs_cnt = 0
cf_cnt = 0
thread_state = list([[0, 0] for i in range(THREAD_NUM)])
fade_out_speed = 1

def wait_animation():
    pygame.time.wait(100)
    thread = int(threading.current_thread().name)
    while True:
        if thread_state[thread][1] <= 0:
            return
        pygame.time.wait(50)

def connect():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('lixiaoyishawn.com', 80))
            wait_animation()
            pygame.event.post(pygame.event.Event(ADD_CONNECT_SUCCESS, thread=int(threading.current_thread().name)))
            return client
        except (TimeoutError, ConnectionRefusedError):
            wait_animation()
            pygame.event.post(pygame.event.Event(ADD_CONNECT_FAILED, thread=int(threading.current_thread().name)))

def run():
    client = connect()
    i = 0
    while True:
        try:
            i += 1
            client.sendall(("robot." + "a"*1).encode())
            wait_animation()
            pygame.event.post(pygame.event.Event(ADD_SEND, thread=int(threading.current_thread().name)))
            break_sound.play()
            if i > send_times:
                if client is not None and CLOSE:
                    client.close()
                client = connect()
                i = 0
        except ConnectionAbortedError:
            i = 0
            if client is not None and CLOSE:
                client.close()
            client = connect()

def set_state(event):
    global thread_state
    thread_state[event.thread] = [event.type, BLOCK_WIDTH // 2]

def fade_out():
    for x in thread_state:
        x[1] -= fade_out_speed
        if x[1] < 0:
            x[0] = 0
            x[1] = 0

def get_draw_pos(x, y):
    return (
        BLOCK_WIDTH * x + BLOCK_SPACK * x + BLOCK_WIDTH // 2,
        BLOCK_WIDTH * y + BLOCK_SPACK * y + BLOCK_WIDTH // 2
    )

def draw_thread_state():
    surface = pygame.surface.Surface((
        BLOCK_WIDTH * WIDTH + BLOCK_SPACK * (WIDTH - 1),
        BLOCK_WIDTH * HEIGHT + BLOCK_SPACK * (HEIGHT - 1)
    ))
    for x in range(WIDTH):
        for y in range(HEIGHT):
            state = thread_state[x * WIDTH + y]
            if state[0] == ADD_SEND:
                pygame.draw.circle(surface, (0, 255, 0), get_draw_pos(x, y), state[1])
            elif state[0] == ADD_CONNECT_SUCCESS:
                pygame.draw.circle(surface, (0, 100, 255), get_draw_pos(x, y), state[1])
            elif state[0] == ADD_CONNECT_FAILED:
                pygame.draw.circle(surface, (255, 0, 0), get_draw_pos(x, y), state[1])
            else:
                pygame.draw.circle(surface, (255, 255, 255), get_draw_pos(x, y), 1)
    return surface

if __name__ == '__main__':
    for i in range(THREAD_NUM):
        t = threading.Thread(target=run, name=str(i))
        t.start()

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == ADD_SEND:
                send_cnt += 1
                set_state(event)
            elif event.type == ADD_CONNECT_SUCCESS:
                cs_cnt += 1
                set_state(event)
            elif event.type == ADD_CONNECT_FAILED:
                cf_cnt += 1
                set_state(event)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(font.render("Send count: " + str(send_cnt), False, (0, 255, 0)), (0, 0))
        screen.blit(font.render("Connect Success count: " + str(cs_cnt), False, (0, 100, 255)), (0, 100))
        screen.blit(font.render("Connect Failed count: " + str(cf_cnt), False, (255, 0, 0)), (0, 200))
        fade_out()
        screen.blit(draw_thread_state(), (700, 50))
        pygame.display.flip()
        clock.tick_busy_loop(30)
