from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.gameofthronesquotes.xyz/v1/random")
    data = response.json()
    quote = data["sentence"]
    person = data["character"]["name"]
    canvas.itemconfig(quote_text,text=quote,font=("Luminari", 20))
    window.title(f"{person} says")


window = Tk()
window.title("Presented by HBO")
window.geometry("450x600")

canvas = Canvas(width=445, height=595)
background_img = PhotoImage(file="scroll.png")
background_img1 = PhotoImage(file="bg2.png")
background_img2 = PhotoImage(file="logo.png")
canvas.create_image(150, 207, image=background_img1)
canvas.create_image(220, 50, image=background_img2)
canvas.create_image(220, 300, image=background_img)
quote_text = canvas.create_text(220, 300, text="Unveil the words that echo through realms.", width=250, font=("Game of Thrones", 22, "bold"),fill="black",justify="center")
canvas.place(x=0,y=0)
# canvas.grid(row=0, column=0)
#
got_img = PhotoImage(file="logo2.png")
got_button = Button(image=got_img, highlightthickness=0, command=get_quote)
got_button.place(x=162,y=520)

window.mainloop()
