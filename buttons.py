from customtkinter import CTkButton
from settings import *


class Button(CTkButton):
    def __init__(self, parent, function, text, font, col, row, corner=styling['corner-radius'], gap=styling['gap'],
                 color='dark-gray'):
        super(Button, self).__init__(master=parent,
                                     command=function,
                                     text=text,
                                     font=font,
                                     corner_radius=corner,
                                     fg_color=colors[color]['fg'],
                                     hover_color=colors[color]['hover'],
                                     text_color=colors[color]['text'])
        self.grid(column=col, row=row, sticky='news', padx=gap, pady=gap)


class Numbers(Button):
    def __init__(self, parent, function, text, font, col, row, span, corner=styling['corner-radius'],
                 gap=styling['gap'],
                 color='light-gray'):
        super(Numbers, self).__init__(parent=parent, function=lambda: function(text), text=text, font=font, col=col,
                                      row=row,
                                      color=color)
        self.grid(column=col, row=row, sticky='news', padx=gap, pady=gap, columnspan=span)


class Signs(Button):
    def __init__(self, parent, function, text, font, col, row, operator, corner=styling['corner-radius'],
                 gap=styling['gap'],
                 color='orange'):
        super(Signs, self).__init__(parent, lambda: function(operator), text, font, col, row, color=color)
