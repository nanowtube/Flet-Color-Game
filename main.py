import flet as ft
import random
import time
def main(page: ft.page):
    page.title = "Colorify"
    page.window_width = 450
    page.window_height = 800
    page.theme_mode = "LIGHT"
    page.bgcolor = "#B5F1CC"
    page.padding = ft.padding.only(left=20, top=60, right=20)
    def start(e):
        introView.visible = False
        mainView.visible = True
        btnView.visible = True
        page.update()
    def btnColorChoices():
        colors = ["red", "orange", "blue", "yellow",
                  "white", "purple", "green", "pink"]
        color = colors[random.randint(0, len(colors) - 1)]
        firstColorChoice = colors[random.randint(0, len(colors)-1)]
        secondColorChoice = colors[random.randint(0, len(colors)-1)]
        if firstColorChoice == secondColorChoice:
            secondColorChoice = colors[random.randint(0, len(colors)-1)]
        if firstColorChoice == color:
            firstColorChoice = colors[random.randint(0, len(colors)-1)]
        if secondColorChoice == color:
            secondColorChoice = colors[random.randint(0, len(colors)-1)]
        else:
            pass
        choices = [firstColorChoice, secondColorChoice, color]
        random.shuffle(choices)
        choices.append(color)
        return choices
    def reset():
        btnColors = btnColorChoices()
        c.bgcolor = btnColors[3]
        c.update()
        btnOne.text = btnColors[0]
        btnTwo.text = btnColors[1]
        btnThree.text = btnColors[2]
        btnOne.bgcolor = btnTwo.bgcolor = btnThree.bgcolor = "#F3CA40"
    def colorCheck(e):
        if btnOne.text == c.bgcolor:
            btnOne.bgcolor = "green"
            btnTwo.bgcolor = btnThree.bgcolor = "red"
        elif btnTwo.text == c.bgcolor:
            btnTwo.bgcolor = "green"
            btnOne.bgcolor = btnThree.bgcolor = "red"
        elif btnThree.text == c.bgcolor:
            btnThree.bgcolor = "green"
            btnTwo.bgcolor = btnOne.bgcolor = "red"
        else:
            pass
        c.opacity = 1
        c.update()
        page.update()
        time.sleep(1)
        c.opacity = 0
        c.update()
        time.sleep(1)
        reset()
        page.update()
    btnColors = btnColorChoices()
    correct = btnColors[len(btnColors)-1]
    introText = ft.Text(
        value="Welcome to Colorify! \n Press Start to begin!",
        size=20
    )
    startBtn = ft.ElevatedButton(
        text="Start",
        on_click=start,
        width=200,
        bgcolor="#F3CA40",
        color="white"
    )
    c = ft.Container(
        width=300,
        height=300,
        bgcolor=correct,
        border_radius=10,
        animate_opacity=300,
        opacity=0,
    )
    btnOne = ft.ElevatedButton(
        text=btnColors[0],
        on_click=colorCheck,
        width=150,
        bgcolor="#F3CA40",
        color="white"
    )
    btnTwo = ft.ElevatedButton(
        text=btnColors[1],
        on_click=colorCheck,
        width=150,
        bgcolor="#F3CA40",
        color="white"
    )
    btnThree = ft.ElevatedButton(
        text=btnColors[2],
        on_click=colorCheck,
        width=150,
        bgcolor="#F3CA40",
        color="white"
    )
    introView = ft.Row(
        [ft.Column([introText, startBtn])],
        alignment=ft.MainAxisAlignment.CENTER
    )
    mainView = ft.Row(
        [c],
        alignment=ft.MainAxisAlignment.CENTER,
        visible=False
    )
    btnView = ft.Row(
        [ft.Column([btnOne, btnTwo, btnThree])],
        visible=False,
        alignment=ft.MainAxisAlignment.CENTER
    )
    page.add(introView, mainView, btnView)
ft.app(target=main)