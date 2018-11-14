from pico2d import *
import game_framework
import title_state
import game_class
import game_world


name= 'MainState'
hero = None
map = None
image = None
monster = None

turn = 0

def enter():
    global image
    image = load_image('sprites\\map\\stage.png')

    global hero
    hero = game_class.Player()

    global map
    map = game_class.Background(0)

    global monster
    monster = game_class.Monster(0)

def exit():
    global image
    del(image)

def handle_events():
    global turn
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 600 - 1 - event.y
            for card in title_state.card_stack:
                if card.Click(x, y) is True:
                    hero.update_animation(card.number)
                    card.delete()
                    turn += 1
        else:
            if turn is 3:

                for card in title_state.card_stack:
                    card.delete()
                turn = 0
                title_state.stack = 0
                game_framework.pop_state()

def draw():
    clear_canvas()
    map.draw()
    image.draw(400, 300)

    hero.draw()
    monster.draw()

    for card in title_state.card_stack:
        card.draw()
    update_canvas()
    delay(0.2)

def update():
    hero.update()

def pause():
    pass

def resume():
    pass