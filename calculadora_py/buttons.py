import flet as ft 

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, expand=1, on_click=None):
        super().__init__(text=text, 
                         expand=expand, 
                         on_click=on_click)

class DigitButton(CalcButton):
    def __init__(self, text, expand=1, on_click=None):
        CalcButton.__init__(self, text, expand, on_click=on_click)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text, on_click=None):
        CalcButton.__init__(self, text, on_click=on_click)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text, on_click=None):
        CalcButton.__init__(self, text, on_click=on_click)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

class ScientificButton(CalcButton):
    def __init__(self, text, on_click=None):
        CalcButton.__init__(self, text, on_click=on_click)
        self.bgcolor = ft.colors.LIGHT_BLUE_500
        self.color = ft.colors.WHITE








