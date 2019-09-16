'''
Circle Example
==============

This example exercises circle (ellipse) drawing. You should see sliders at the
top of the screen with the Kivy logo below it. The sliders control the
angle start and stop and the height and width scales. There is a button
to reset the sliders. The logo used for the circle's background image is
from the kivy/data directory. The entire example is coded in the
kv language description.
'''

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class Cell(Widget):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(Cell, self).__init__(**kwargs)
        with self.canvas:
            touch = {'x':.3, 'y': .3}
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(200 - d / 2, 200 - d / 2), size=(d, d))
    
        


class PercolationGrid(GridLayout):
    def __init__(self, **kwargs):
        super(PercolationGrid, self).__init__(**kwargs)
        #self.cols = 3
        self.padding = (100,100,100,100)
        self.size_hint = (.6, .6)
        self.pos_hint={'x':.2, 'y':.37}
        
        for col in range(self.cols*self.cols):
            gridSite = Button(id=str(col))
            gridSite.bind(on_press=self.gridSiteCallback)
            self.add_widget(gridSite)

    def gridSiteCallback(self, value):
        value.background_color= (0,1,0,1)

class PercolationApp(App):
    def build(self):
        root = FloatLayout(size=(600, 600))
        title = Label(text="Percolation", font_size=70, pos_hint={'x':.0, 'y':.45})
        root.add_widget(title)
        root.add_widget(PercolationGrid(**{'cols':5}))
        root.add_widget(Cell())
        return root

PercolationApp().run()