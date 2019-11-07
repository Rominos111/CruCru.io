if __name__ == "__main__":
    import sys
    sys.path.append("..")

import pygame

from util.vector import Vect2d

from game.button import *
from game.gamestate import GameState
from game.map import Map

from view.display import Display

class Menu:
    @classmethod
    def applyState(cls, state):
        cls.can_play = False
        cls.state = state
        cls.can_quit = False

        Display.execWhenResized(cls.createButtons)

        cls.createButtons(Display.size.x, Display.size.y)

    @classmethod
    def play(cls):
        Map.reset()
        cls.can_play = True

    @classmethod
    def createButtons(cls, width, height):
        cls.buttons = []

        if cls.state == GameState.MENU:
            cls.applyMenu(width, height)
        else:
            cls.applyEnd(width, height)

    @classmethod
    def quit(cls):
        cls.can_quit = True

    @classmethod
    def applyMenu(cls, width, height):
        cls.buttons.append(Button(pos=Vect2d(width/4, height/3),
                                  size=Vect2d(width/2, height/3),
                                  text="Jouer",
                                  on_click=cls.play,
                                  when_display=buttonStart_Display,
                                  when_init=buttonStart_Init))

    @classmethod
    def applyEnd(cls, width, height):
        cls.buttons.append(Button(pos=Vect2d(width/4, height/5),
                                  size=Vect2d(width/2, height/5),
                                  text="Perdu !",
                                  when_display=buttonEnd_Display))

        cls.buttons.append(Button(pos=Vect2d(width/5, 3*height/5),
                                  size=Vect2d(width/5, height/5),
                                  text="Rejouer",
                                  on_click=cls.play,
                                  when_display=buttonEndReplay_Display))

        cls.buttons.append(Button(pos=Vect2d(3*width/5, 3*height/5),
                                  size=Vect2d(width/5, height/5),
                                  text="Quitter",
                                  on_click=cls.quit,
                                  when_display=buttonEndReplay_Display))

    @classmethod
    def update(cls, mouse_pos, mouse_pressed):
        cls.mouse_pos = mouse_pos

        if mouse_pressed:
            for i in range(len(cls.buttons)):
                if cls.buttons[i].isMouseOver(cls.mouse_pos):
                    cls.buttons[i].on_click()

    @classmethod
    def display(cls):
        for i in range(len(cls.buttons)):
            cls.buttons[i].display(cls.mouse_pos)
