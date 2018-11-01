from pico2d import *
import game_framework
import title_state

name= "StartState"
image= None

def enter():
    global image
    image = load_image('sprites/title_beta.png')

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
                game_framework.quit()
            elif event.type==SDL_KEYDOWN and event.key==SDLK_SPACE:
                game_framework.change_state(title_state)

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass