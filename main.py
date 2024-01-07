import tkinter as tk

from tkinter.constants import * 
from tkinter import ttk


class Model:

    @staticmethod
    def check_value(x):
        if type(x) not in [int, float] or x < 0:
            x = 0
        return x

    @staticmethod
    def mi_to_km(x):
        mi = Model.check_value(x)
        #if type(mi) not in [int, float] or mi < 0:
        #    mi = 0
        print(x)
        return float(round(mi / 0.621371, 3))

    @staticmethod
    def km_to_mi(x):
        km = Model.check_value(x)
        #if type(x) not in [int, float] or km < 0:
        #    x = 0
        return float(round(km*0.621371, 3))

    @staticmethod
    def nmi_to_km(nmi):
        km = (nmi/1.852, 3)
        return km
    
    @staticmethod
    def km_to_nmi(km):
        nmi = round(km*1.852, 3)
        return nmi

# AppForTest использовать только для тестирования View
class AppForTest(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Converter')
        self.geometry('400x300')
        #self.resizable(False, False)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Converter')
        self.geometry('400x300')
        #self.resizable(False, False)
       
        # Model 
        model = Model()
        # View
        view_up = UpFrame(self)
        view_res = ResultFrame(self)
        view_down = DownFrame(self)
        # controller
        controller = Controller(model, view_up, view_res, view_down)

class Controller:
    def __init__(self, model, view_up, view_res, view_down):
        self.model = model
        self.view_up = view_up
        self.view_res = view_res
        self.view_down = view_down
    
        # RadioButton
        self.view_down.mi_km['command'] = self.create_label_text #self.print_value
        self.view_down.km_mi['command'] = self.create_label_text #self.print_value
        self.create_label_text()
        
        # Button
        self.view_up.button['command'] = self.convert_value

    def create_label_text(self):
        # взаимодействие между фреймами
        value_rb = self.view_down.get_value_rb()
        self.view_up.get_text_label(value_rb)
        self.view_res.get_text_title_label(value_rb)

    def convert_value(self):
        
        # 3)действия если значение неверное
        x = self.view_up.get_entry_value()
        print(f'get_entry: {x}')
        value_rb = self.view_down.get_value_rb()
        print(f'value rb: {value_rb}')
        if value_rb == self.view_down.values_rb[0]:
            res = self.model.mi_to_km(x)
        elif value_rb == self.view_down.values_rb[1]:
            res = self.model.km_to_mi(x)
        print(f'result: {res}')
        self.view_res.get_text_res_label(res)

class UpFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self['padding'] = 4
        self.pack(fill=BOTH, expand=True, padx=2, pady=2)

        # content
        options = {'padx':2, 'pady':2, 'anchor':W}
        self.label = ttk.Label(self, text='Convert')
        self.label.pack(**options)

        self.text = tk.StringVar() 
        self.entry = ttk.Entry(self, textvariable=self.text)
        self.entry.pack(**options)

        self.button = ttk.Button(self, text='click')
        self.button.pack(**options)
        
    def get_text_label(self, value_rb): # значение радиокнопки
        self.label['text'] = f'Convert {value_rb}:'
        return self.label['text']


    def check_entry_value(self, x):
        try:
            float(x)
        except ValueError:
            # !!!! Сделать оповещение
            x = 0
        return float(x)        
    
        #if type(x) not in [float, int] or x < 0:
        #    x = 0 
        #    return x
 
    def get_entry_value(self):
        x = self.entry.get()
        res_x = self.check_entry_value(x)
        return res_x

 
class ResultFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self['padding'] = 4
        self.pack(fill=BOTH, expand=True, padx=2, pady=2)

        # content
        options = {'padx':2, 'pady':2, 'anchor':CENTER}
        self.title_label = ttk.Label(self, text='Convert')
        self.title_label.pack(**options)
        self.result_label = ttk.Label(self, text='Result convert') 
        self.result_label.pack(**options)

    def get_text_title_label(self, value_rb): # протестировать
        #self.title_label['text'] = None
        self.title_label['text'] = f'Convert {value_rb}:'  
        return self.title_label['text']

    def get_text_res_label(self, x):
        self.result_label['text'] = f'Result: {x}'  
        return self.result_label['text']


class DownFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self['padding'] = 4
        self['text'] = 'Setting'
        self.pack(fill=BOTH, expand=True, padx=2, pady=2)

        # content
        options = {'anchor':W}
        # В Tkinter нельзя использовать любую переменную для хранения состояний виджетов.
        # Для этих целей предусмотрены специальные классы-переменные пакета tkinter – BooleanVar, IntVar, DoubleVar, StringVar.
        
        self.values_rb = ['miles to kilometers', 'kilometers to miles']
        self.widget_state = tk.StringVar(value=self.values_rb[0])#'miles_to_kilometers')
        
        self.mi_km = ttk.Radiobutton(
            self, 
            text = 'mi_to_km', 
            value = self.values_rb[0],
            #text= 'miles to kilometers', 
            #value = 'mi_to_km', 
            variable = self.widget_state,
            command = self.get_value_rb
        )
        self.mi_km.pack(**options)

        self.km_mi = ttk.Radiobutton(
            self, 
            text = 'km_to_mi',
            value = self.values_rb[1], #'kilometers to miles',
            variable = self.widget_state,
            command = self.get_value_rb
       )
        self.km_mi.pack(**options)
    
    def get_value_rb(self):
        a = self.widget_state.get()
        return a


if __name__ == '__main__':
    
    app = App()
    #app = AppForTest() # для теста
    #frame = UpFrame(app)
    #l_frame = DownFrame(app)
    app.mainloop()
