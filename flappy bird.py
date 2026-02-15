from pygame import*
from random import randint
import sounddevice as sd
import numpy as np 
from time import sleep

sr=16000
block=256
mic_level=0.0

def audio_cd(indata, frames, time, status):
    global mic_level    
    if status:
        return
    rms=float(np.sqrt(np.mean(indata**2)))
    mic_level=0.85 * mic_level + 0.15*rms
init()
window_size = 800,600
window= display.set_mode(window_size)
clock = time.Clock()

player_rect= rect(50,500,100,100)
def generate_pipes( count,distance=650, pipe_width=140, gap=280  ,max_height=440 ,min_height=50 ):
    pipes=[]
    start_x= window_size[0]
    for  i in range(count):
        height = randint(min_height, max_height)
        top_pipe = Rect (start_x,0,pipe_width,height)
        bottom_pipe = Rect(start_x, height + gap,pipe_width, window_size[1]-(height +gap))
        pipes.extend([top_pipe, bottom_pipe])
        start_x += display
    return pipes
pies=generate_pipes(150)
with sd.InputStream(samplerate=sr, channels=1, blocksize=block, callback=audio_cd): 

    while True:
        for e in event.get():
            if e.type ==QUIT:
                quit()
        window.fill('sky blue')
        draw.rect(window,'red', player_rect)
        for pie in pies:
            if not lose:
                pie.x -= 10
            draw.rect(window, ' green', pie)
        if pie.x <= -100:
            pies
        if player_rect.colliderect(pie):
                lose=True
        if len(pies) < 8:
            pies += generate_pipes(150)
        keys =key.get_pressed()
        if keys[k_w] and not lose:
            player_rect.y-=15
        if keys[k_y] and not lose:
            player_rect.y-=15
        
        display.update()
        clock.tick(60)     