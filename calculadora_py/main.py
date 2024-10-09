import flet as ft
import numpy as np
from buttons import DigitButton, ActionButton, ExtraActionButton, ScientificButton

def main(page: ft.Page):
    page.title = "Scientific Calc App"
    expression = "0"
    result = ft.Text(value="0", 
                     color=ft.colors.WHITE, 
                     size=20)

    def update_result(new_value):
        result.value = new_value
        page.update()

    def on_digit_click(e):
        nonlocal expression
        if expression == "0":
            expression = e.control.text
        else:
            expression += e.control.text
        update_result(expression)

    def on_action_click(e):
        nonlocal expression
        match e.control.text:
            case "=":
                try:
                    expression = str(eval(expression))
                except:
                    expression = "Error"
            case "AC":
                expression = "0"
            case "C":
                if expression != "0":
                    expression = expression[:-1] 
                    if expression == "":
                        expression = "0"
            case "+/-":
                if expression and expression[0] == "-":
                    expression = expression[1:]
                else:
                    expression = "-" + expression
            case "%":
                try:
                    expression = str(float(expression) / 100)
                except:
                    expression = "Error"
            case _:
                expression += e.control.text
       
        update_result(expression)

    def on_scientific_click(e):
        nonlocal expression 
        try:
            match e.control.text:
                case 'sin':
                    expression = str(np.sin(np.radians(float(expression)))) 
                case 'cos':
                    expression = str(np.cos(np.radians(float(expression)))) 
                case 'tan':
                    expression = str(np.tan(np.radians(float(expression)))) 
                case 'asin':
                    if -1 <= float(expression) <= 1:
                        expression = str(np.degrees(np.arcsin(float(expression)))) 
                    else:
                        expression = str(np.nan)
                case 'acos':
                    if -1 <= float(expression) <= 1:
                        expression = str(np.degrees(np.arccos(float(expression)))) 
                    else:
                        expression = str(np.nan)
                case 'atan':
                    if -1 <= float(expression) <= 1:
                        expression = str(np.degrees(np.arccos(float(expression)))) 
                    else:
                        expression = str(np.nan)
                case 'ln':
                    expression = str(np.log(float(expression))) 
                case 'log':
                    expression = str(np.log10(float(expression))) 
                case 'eˣ':
                    expression = str(np.exp(float(expression))) 
                case '10ˣ':
                    expression = str(10**float(expression)) 
                case 'x²':
                    expression = str(float(expression)**2) 
                case 'x³':
                    expression = str(float(expression)**3)
                case '√':
                    expression = str(np.sqrt(float(expression))) 
                case 'x⁻¹':
                    expression = str(1/float(expression))
                case 'E':
                    expression += "E"
                case 'EXP':
                    expression += "**"
                case 'pi':
                    expression = str(np.pi)
                case 'e':
                    expression = str(np.e)
                case '∞':
                    expression = str(np.inf)
                case 'radians':
                    expression = str(np.radians(float(expression)))
                case 'degrees':
                    expression = str(np.degrees(float(expression)))
                case 'NaN':
                    expression = str(np.nan)
                case _:
                    expression += e.control.text
            update_result(expression)
        except:
            expression = "Error"

    page.add(
        ft.Container(
            width=450,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment="end"),
                    ft.Row(
                        controls=[
                            ExtraActionButton(text="AC", on_click=on_action_click),
                            ExtraActionButton(text="+/-", on_click=on_action_click),
                            ExtraActionButton(text="%", on_click=on_action_click),
                            ExtraActionButton(text="C", on_click=on_action_click)
                            ActionButton(text="/", on_click=on_action_click),
                            
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="7", on_click=on_digit_click),
                            DigitButton(text="8", on_click=on_digit_click),
                            DigitButton(text="9", on_click=on_digit_click),
                            ActionButton(text="*", on_click=on_action_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="4", on_click=on_digit_click),
                            DigitButton(text="5", on_click=on_digit_click),
                            DigitButton(text="6", on_click=on_digit_click),
                            ActionButton(text="-", on_click=on_action_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="1", on_click=on_digit_click),
                            DigitButton(text="2", on_click=on_digit_click),
                            DigitButton(text="3", on_click=on_digit_click),
                            ActionButton(text="+", on_click=on_action_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="0", expand=2, on_click=on_digit_click),
                            DigitButton(text=".", on_click=on_digit_click),
                            ActionButton(text="=", on_click=on_action_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ScientificButton(text="sin", on_click=on_scientific_click),
                            ScientificButton(text="cos", on_click=on_scientific_click),
                            ScientificButton(text="tan", on_click=on_scientific_click),
                            ScientificButton(text="ln", on_click=on_scientific_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ScientificButton(text="asin", on_click=on_scientific_click),
                            ScientificButton(text="acos", on_click=on_scientific_click),
                            ScientificButton(text="atan", on_click=on_scientific_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ScientificButton(text="log", on_click=on_scientific_click),
                            ScientificButton(text="eˣ", on_click=on_scientific_click),
                            ScientificButton(text="x²", on_click=on_scientific_click),
                            ScientificButton(text="√", on_click=on_scientific_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ScientificButton(text="x³", on_click=on_scientific_click),
                            ScientificButton(text="x⁻¹", on_click=on_scientific_click),
                            ScientificButton(text="10ˣ", on_click=on_scientific_click),
                            ScientificButton(text="pi", on_click=on_scientific_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ScientificButton(text="e", on_click=on_scientific_click),
                            ScientificButton(text="∞", on_click=on_scientific_click),
                            ScientificButton(text="E", on_click=on_scientific_click),
                            ScientificButton(text="EXP", on_click=on_scientific_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ScientificButton(text="radians", on_click=on_scientific_click),
                            ScientificButton(text="degrees", on_click=on_scientific_click),
                            ScientificButton(text="NaN", on_click=on_scientific_click),
                        ]
                    ),
                ]
            ),
        )
    )

ft.app(target=main)


