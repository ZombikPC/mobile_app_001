from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1280)
Config.set('graphics', 'height', 720)

class BugSklada(App):
    def build(self):
        bl = BoxLayout(orientation='vertical')
        gl = GridLayout(cols=2)
        bl.add_widget(Button(text="Операции с кассой",size_hint=[None,None], size=[1280,50]))

        gl.add_widget(Button(text="Взять с кассы",size_hint=[None,None], size=[300,50]))
        gl.add_widget(Button(text="Положить в кассу",size_hint=[None,None], size=[300,50]))
        gl.add_widget(Button(text="ok Списать",size_hint=[None,None], size=[300,50]))
        gl.add_widget(Button(text="ok Пополнить",size_hint=[None,None], size=[300,50]))



        al = AnchorLayout(anchor_x='center', anchor_y='top')
        # al.add_widget(Button(text="Операции с кассой!", size_hint=[None,None], size=[300,50]))
        bl.add_widget(gl)
        bl.add_widget(Button(text="Операции с Мой баланс",size_hint=[None,None], size=[600,50]))

        gl2 = GridLayout(cols=2)
        gl2.add_widget(Button(text="Взять с кассы",size_hint=[None,None], size=[300,50]))
        gl2.add_widget(Button(text="Положить в кассу",size_hint=[None,None], size=[300,50]))
        gl2.add_widget(Button(text="ok Списать",size_hint=[None,None], size=[300,50]))
        gl2.add_widget(Button(text="ok Пополнить",size_hint=[None,None], size=[300,50]))

        bl.add_widget(gl2)


        return bl


if __name__ == '__main__':
    BugSklada().run()