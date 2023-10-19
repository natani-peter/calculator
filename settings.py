# size
app_size = (400, 700)
main_rows = 7
main_columns = 4

# text
family = 'Helvetica'
output_font = 70
normal_font = 32

styling = {
    'gap': 0.5,
    'corner-radius': 0
}

number_positions = {
    '.': {'col': 2, 'row': 6, 'span': 1},
    0: {'col': 0, 'row': 6, 'span': 2},
    1: {'col': 0, 'row': 5, 'span': 1},
    2: {'col': 1, 'row': 5, 'span': 1},
    3: {'col': 2, 'row': 5, 'span': 1},
    4: {'col': 0, 'row': 4, 'span': 1},
    5: {'col': 1, 'row': 4, 'span': 1},
    6: {'col': 2, 'row': 4, 'span': 1},
    7: {'col': 0, 'row': 3, 'span': 1},
    8: {'col': 1, 'row': 3, 'span': 1},
    9: {'col': 2, 'row': 3, 'span': 1},
}

math_signs = {
    '/': {'col': 3, 'row': 2, 'character': '/', 'operator': '/', 'image_path': None},
    '*': {'col': 3, 'row': 3, 'character': 'x', 'operator': '*', 'image_path': None},
    '-': {'col': 3, 'row': 4, 'character': '-', 'operator': '-', 'image_path': None},
    '=': {'col': 3, 'row': 6, 'character': '=', 'operator': '=', 'image_path': None},
    '+': {'col': 3, 'row': 5, 'character': '+', 'operator': '+', 'image_path': None},
}

operators = {
    'clear': {'col': 0, 'row': 2, 'text': 'AC', 'image_path': None},
    'invert': {'col': 1, 'row': 2, 'text': '-/+', 'image_path': None},
    'percent': {'col': 2, 'row': 2, 'text': '%', 'image_path': None},
}

colors = {
    'light-gray': {'fg': ('#505050', "#d4d4d2"), 'hover': ('#686868', "#efefed"), 'text': ('white', 'black')},
    'dark-gray': {'fg': ("#d4d4d2", '#505050'), 'hover': ("#efefed", '#686868'), 'text': ('black', 'white')},
    'orange': {'fg': '#ff9500', 'hover': '#ffb143', 'text': ('black', 'white')},
    'orange-highlight': {'fg': 'white', 'hover': 'white', 'text': ('black', "#ff9500")}
}

title_bar_color = {
    'dark': 0x00000000,
    'light': 0x00eeeeee
}

black = '#000000'
white = '#eeeeee'

# import customtkinter as ctk
# from PIL import Image
#
# image_import = Image.open("path")
# kinder = ctk.CTkImage(light_image=image_import)
# ctk.CTkButton(ctk.CTk,image=kinder).pack(fill='both',expand= True)
