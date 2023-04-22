#Linking
from tkinter import *
import random
from PIL import ImageTk, Image
root=Tk()

#Configuring Window
root.title("Pokemon Game")
root.geometry("800x600")
root.configure(background = "yellow2")

#Images
abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))

#Names Label
player1label = Label(root, text="Player1",bg="yellow2")
player2label = Label(root,text="Player2",bg="yellow2")
player1label.place(relx=0.1,rely=0.3,anchor = CENTER)
player2label.place(relx=0.9,rely=0.3,anchor = CENTER)

#Score Label
player1label_score = Label(root, text="0",bg="#3333ff",fg="white")
player2label_score = Label(root,text="0",bg="#3333ff",fg="white")
player1label_score.place(relx=0.1,rely=0.4,anchor = CENTER)
player2label_score.place(relx=0.9,rely=0.4,anchor = CENTER)

#Main Label
randomselectedpokemon = Label(root, fg ="black",bg="yellow1")
randomselectedpokemon.place(relx=0.5,rely=0.5,anchor = CENTER)

#Score Variables
player1score = 0
player2score = 0

#Image and Score
PokemonPower=[30,60,50,100,70,70,60,90,40,70,200,40,50]
pokemonlist=[abra,bulbasour,charmender,iyvasour,jigglypuff,kadabra,meowth,nidoking,paras,persion,pikachu,ratata,squirtle]

#Functions
def player1():
    global player1score
    randomno = random.randint(0,13)
    randomselectedpokemon["text"] = ""
    player1score = player1score + PokemonPower[randomno]
    player1label_score["text"] = str(player1score)
    randomselectedpokemon["image"]=pokemonlist[randomno]
    
def player2():
    global player2score
    randomno2 = random.randint(0,13)
    randomselectedpokemon["text"] = ""
    player2score = player1score + PokemonPower[randomno2]
    player2label_score["text"] = str(player2score)
    randomselectedpokemon["image"]=pokemonlist[randomno2]

#Player Buttons
player1button = Button(root, image = button,command=player1)
player1button.place(relx=0.1,rely=0.6,anchor=CENTER)
player2button = Button(root, image = button,command=player2)
player2button.place(relx=0.9,rely=0.6,anchor=CENTER)

#To make app functional
root.mainloop()
