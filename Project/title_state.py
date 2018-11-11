from pico2d import *
import game_framework
import main_state
import game_class

name= "TitleState"
image= None
card_stack = [game_class.Card() for i in range(5)]  # 턴 시작전 사용할 카드 선정!
stack = 0

deck = [game_class.Card() for card in range(10)]

def enter():
    global image
    global deck
    image = load_image('sprites\\map\\cardselect.png')
    
    deck[0].Initialize(1, load_image('sprites\\card\\001.png'), 170 + 114 * 0, 480)
    deck[1].Initialize(2, load_image('sprites\\card\\002.png'), 170 + 114 * 1, 480)
    deck[2].Initialize(3, load_image('sprites\\card\\003.png'), 170 + 114 * 2, 480)
    deck[3].Initialize(4, load_image('sprites\\card\\004.png'), 170 + 114 * 3, 480)
    deck[4].Initialize(5, load_image('sprites\\card\\005.png'), 170 + 114 * 4, 480)

    deck[5].Initialize(6, load_image('sprites\\card\\006.png'), 170 + 114 * 0, 320)
    deck[6].Initialize(7, load_image('sprites\\card\\007.png'), 170 + 114 * 1, 320)
    deck[7].Initialize(8, load_image('sprites\\card\\008.png'), 170 + 114 * 2, 320)
    deck[8].Initialize(9, load_image('sprites\\card\\009.png'), 170 + 114 * 3, 320)
    deck[9].Initialize(10,load_image('sprites\\card\\010.png'), 170 + 114 * 4, 320)
    # 이미지, 타이틀에서 좌표

def exit():
    global image
    del (image)

def handle_events():
    global stack
    global card_stack
    global deck

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()

            elif event.type ==SDL_KEYDOWN and event.key==SDLK_SPACE and stack==5:
                game_framework.push_state(main_state)

            elif event.type == SDL_MOUSEBUTTONDOWN:
                x, y = event.x, 600-1-event.y

                for card in deck:
                    if (card.Click(x, y) == True) and (stack < 5):
                        i = 0
                        for cs in card_stack:
                            if cs.Check() == True:
                                cs.Initialize(card.number, card.image, 170 + 114 * i, 100)
                                stack += 1
                                break
                            i += 1
                            # 앞부터 비어있는공간 찾는다

                for card in card_stack:
                    if (card.Click(x,y)== True):
                        card.delete()
                        stack -= 1


def draw():
    global image
    global stack
    global deck
    global select


    clear_canvas()
    image.draw(400, 300)

    for card in deck:
        card.draw()

    for card in card_stack:
        if card.image != None:
            card.draw()

    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass