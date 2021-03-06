from pico2d import *
import game_framework
import title_state
import game_class
import start_state
import game_world


name= 'MainState'
hero = None
map = None
image = None
monster = None
monster_max_hp = 10
turn = 0

def enter():
    if title_state.turn >= 1:
        return

    global image
    image = load_image('sprites\\map\\stage.png')

    global hero
    hero = game_class.Player()

    global map
    map = game_class.Background(0)

    global monster
    monster = game_class.Monster(monster_max_hp)

def exit():
    global image

def handle_events():
    global turn
    global monster, monster_max_hp
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if hero.My_Turn_is_Now() is False:
                break
            x, y = event.x, 600 - 1 - event.y
            for card in title_state.card_stack:
                if card.Click(x, y) is True and hero.now_animation is 0:
                    if hero.Use_Possible(card.number) is False or card.use is True:
                        return
                    hero.update_animation(card.number)
                    card.delete()

        else:
            if turn is 3 or monster.hp <= 0:
                for card in title_state.card_stack:
                    card.delete()
                for card in title_state.deck:
                    card.use = False
                if monster.hp <= 0:
                    monster_max_hp += 5
                    monster = game_class.Monster(monster_max_hp)
                    hero.Change_My_Turn()
                    title_state.kill_monster += 1
                turn = 0
                title_state.stack = 0
                game_framework.pop_state()
            elif hero.hp.hp <= 0:
                game_framework.change_state(start_state)

def draw():
    clear_canvas()
    map.draw()
    image.draw(400, 300)
    title_state.font.draw(620, 570, '(Kill Enermy: %d)' % title_state.kill_monster, (0, 0, 255))

    hero.draw()
    monster.draw()

    for card in title_state.card_stack:
        card.draw()
    update_canvas()
    delay(0.1)

def update():
    hero.update()
    monster.update()

def pause():
    pass

def resume():
    pass


def get_player():
    return hero


def get_monster():
    return monster

