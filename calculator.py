import customtkinter as ctk
import darkdetect
from buttons import Button, Numbers, Signs
import tkinter as tk

from settings import *

try:
    from ctypes import windll, byref, c_int, sizeof
except:
    pass


class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        # set up
        super(Calculator, self).__init__(fg_color=(white, black))
        ctk.set_appearance_mode('dark' if is_dark else 'light')
        self.geometry(f'{app_size[0]}x{app_size[1]}+1150+100')
        self.resizable(False, False)
        self.title('')
        self.iconbitmap()

        # attributes
        self.mode = is_dark
        self.formula = tk.StringVar(value='')
        self.answer = tk.StringVar(value='0')
        self.answer_list = []
        self.formula_list = []

        # methods
        self.color_bar()

        # grid layout on the window level
        self.rowconfigure(list(range(main_rows)), weight=1, uniform='a')
        self.columnconfigure(list(range(main_columns)), weight=1, uniform='a')

        # widgets
        self.create_widgets()
        # run
        self.mainloop()

    def create_widgets(self):
        main_font = ctk.CTkFont(family=family, size=normal_font)
        result_font = ctk.CTkFont(family=family, size=output_font)
        Results(self, 0, main_font, 'se', self.formula)  # formula
        Results(self, 1, result_font, 'e', self.answer)  # answer

        # clear button
        Button(self, self.clear, operators['clear']['text'], main_font, operators['clear']['col'],
               operators['clear']['row'])
        # percent button
        Button(self, self.percent, operators['percent']['text'], main_font, operators['percent']['col'],
               operators['percent']['row'])
        # invert button
        Button(self, self.invert, operators['invert']['text'], main_font, operators['invert']['col'],
               operators['invert']['row'])

        for value, key in number_positions.items():
            Numbers(self, self.number_press, value, main_font, key['col'], key['row'], key['span'])

        for value, key in math_signs.items():
            Signs(self, self.sign_press, key['character'], main_font, key['col'], key['row'], key['operator'])

    def number_press(self, value):
        self.answer_list.append(str(value))
        current_number = ''.join(self.answer_list)
        self.answer.set(current_number)

    def sign_press(self, sign):
        current_number = ''.join(self.answer_list)

        if current_number:
            if sign != '=':
                self.formula_list.append(current_number)
                self.formula_list.append(sign)
                self.answer_list.clear()
                self.formula.set(' '.join(self.formula_list))
                self.answer.set(' ')
            else:
                if self.answer:
                    current_number = ''.join(self.answer_list)
                    self.formula_list.append(current_number)
                    self.answer_list.clear()
                    self.formula.set(''.join(self.formula_list))
                    evaluate = eval(''.join(self.formula_list))
                    self.answer.set(round(evaluate, 5))
                    self.formula_list.clear()
                else:
                    pass

    def clear(self):
        self.answer.set(" ")
        self.formula.set(" ")
        self.formula_list.clear()
        self.answer_list.clear()

    def percent(self):
        current = self.answer.get()
        percentage = current + '/ 100'
        self.answer_list.clear()
        self.answer_list.append(str(eval(percentage)))
        self.answer.set(eval(percentage))

    def invert(self):
        current = self.answer.get()
        invert = "-"+current if eval(current) > 0 else eval(current + '* -1')
        self.answer_list.clear()
        self.answer_list.append(invert)
        self.answer.set(invert)

    def color_bar(self):
        try:
            window_id = windll.user32.GetParent(self.winfo_id())
            target_attribute = 35
            color = title_bar_color['dark'] if self.mode else title_bar_color['light']
            windll.dwmapi.DwmSetWindowAttribute(window_id, target_attribute, byref(c_int(color)), sizeof(c_int))
        except:
            pass


class Results(ctk.CTkLabel):
    def __init__(self, parent, row, font, anchor, text_string):
        super(Results, self).__init__(master=parent, font=font, textvariable=text_string)
        self.grid(column=0, columnspan=4, row=row, sticky=anchor, padx=10)


if __name__ == '__main__':
    Calculator(darkdetect.isDark())

