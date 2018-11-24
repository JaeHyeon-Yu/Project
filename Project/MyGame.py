from pico2d import *
import game_framework
import start_state

open_canvas()

bgm = load_music('music\\title.mp3')
bgm.set_volume(64)
bgm.repeat_play()

game_framework.run(start_state)
close_canvas()