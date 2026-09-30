import tkinter
import time
import customtkinter as ctk
from PIL import Image

root = ctk.CTk()
root.geometry("600x600")
root.resizable(False, False)
root.title("OxyohanOS 1.0 'Yama'")
root.config(bg="gray5")

session = True
idiomas = [
    "Curta sua nova distro linux!",
    "Enjoy your new linux distro!",
    "¡Disfruta de tu nueva distro de Linux!",
    "Goditi la tua nuova distribuzione Linux!",
    "新しいLinuxディストリビューションをお楽しみください！",
    "祝您使用新的 Linux 发行版愉快！",
    "Наслаждайтесь своим новым диствибутивом Linux!"
]   # O google me ajudou nessa, eu nem lembrava que existia lista
atualInd = 0

Initframe = ctk.CTkFrame(root, bg_color="gray5", fg_color="gray10", width=575, height=575, corner_radius=15)
Initframe.place(x=15, y=15)

TitlePt = ctk.CTkLabel(Initframe, text="Bem vindo(a) ao OxyohanOS!", font=("Comic Sans MS", 35))
TitlePt.place(x=5, y=5)

TitleEn = ctk.CTkLabel(Initframe, text="Welcome to OxyohanOS!", font=("Comic Sans MS", 20))
TitleEn.place(x=5, y=55)

TitleEs = ctk.CTkLabel(Initframe, text="Bienvenido a OxyohanOS!", font=("Comic Sans MS", 20))
TitleEs.place(x=5, y=80)

TitleIta = ctk.CTkLabel(Initframe, text="Benvenuti al OxyohanOS!", font=("Comic Sans MS", 20))
TitleIta.place(x=5, y=105)

TitleJap = ctk.CTkLabel(Initframe, text="OxyohanOSへようこそ!", font=("Comic Sans MS", 20))
TitleJap.place(x=5, y=130)

TitleChi = ctk.CTkLabel(Initframe, text="欢迎使用 OxyohanOS！", font=("Comic Sans MS", 20))
TitleChi.place(x=5, y=155)

TitleRuss = ctk.CTkLabel(Initframe, text="Добро пожаловать в OxyohanOS!", font=("Comic Sans MS", 20))
TitleRuss.place(x=5, y=155)

logo = ctk.CTkImage(light_image=Image.open("oxyohan-logo.png"),
                                  dark_image=Image.open("oxyohan-logo.png"),
                                  size=(210, 210))

logoLabel = ctk.CTkLabel(Initframe, image=logo, text="")
logoLabel.place(x=340, y=50)

Enjframe = ctk.CTkFrame(Initframe, bg_color="gray10", fg_color="gray20", width=565, height=275, corner_radius=15)
Enjframe.place(x=5, y=295)

EnjoyLabel = ctk.CTkLabel(Enjframe, text=idiomas[0], font=("Comic Sans MS", 20))
EnjoyLabel.place(x=282, y=125, anchor="center")

def ChangeEnjoyPT():
    EnjoyLabel.configure(text=enjoyPT)

def ChangeEnjoyEN():
    EnjoyLabel.configure(text=enjoyEN)

def ChangeEnjoyES():
    EnjoyLabel.configure(text=enjoyES)

def ChangeEnjoyITA():
    EnjoyLabel.configure(text=enjoyIT)

def ChangeEnjoyJP():
    EnjoyLabel.configure(text=enjoyJP)

def ChangeEnjoyCH():
    EnjoyLabel.configure(text=enjoyCH)

def ChangeEnjoyRSS():
    EnjoyLabel.configure(text=enjoyRS)


# Google me ajudou nessa (Eu tava com dificuldade ;-;)
# FUNÇÃO QUE FAZ O "LOOP" CORRETO SEM TRAVAR A TELA
def rotacionar_idiomas():
    global atualInd
    
    # Avança para o próximo idioma da lista
    atualInd = (atualInd + 1) % len(idiomas)
    
    # Atualiza o texto da Label
    EnjoyLabel.configure(text=idiomas[atualInd])
    
    # Agenda a própria função para rodar novamente daqui a 2000 milissegundos (2 segundos)
    root.after(2000, rotacionar_idiomas)

root.after(2000, rotacionar_idiomas)

root.mainloop()
