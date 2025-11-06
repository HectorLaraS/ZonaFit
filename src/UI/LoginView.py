import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from src.Controller.login_controller import *
from AppView import *

root = App()
root.title("Login View")

#GRID Design
for x in range(3):
    root.columnconfigure(x,weight=1)
    root.rowconfigure(x,weight=1)

container = ttk.Frame(root,style="Brand.TFrame")
container.grid(row=1,column=1,sticky="nsew")

#GRID DE CONTAINER Rejilla interna del container: dos columnas (branding | formulario)
container.columnconfigure(0,weight=1)
container.columnconfigure(1,weight=1)
container.rowconfigure(0,weight=1)

#Branding // Marca
branding = ttk.Frame(container,style="Brand.TFrame")
branding.grid(row=0, column=0, sticky="nsew", padx=(10, 5), pady=10)
branding.columnconfigure(0, weight=1)
branding.rowconfigure(0, weight=1)
branding.rowconfigure(1, weight=0)
branding.rowconfigure(2, weight=1)

title = ttk.Label(
    branding,text="ZonaFit", style="Title.TLabel"
)
title.grid(row=0, column=0, sticky="s", pady=(0, 10))

subtitle = ttk.Label(branding,text="¡Supera tus limmites!",style="Subtitle.TLabel")
subtitle.grid(row=1, column=0, sticky="n")

form = ttk.Frame(container,style="App.TFrame")
form.grid(row=0, column=1, sticky="nsew", padx=(5, 10), pady=10)

for r in range(6):
    # Las filas con inputs y botón se pueden expandir un poco
    form.rowconfigure(r, weight=1 if r in (0, 1, 2, 4) else 0)
form.columnconfigure(0, weight=1)  # labels
form.columnconfigure(1, weight=2)  # entries (se expanden más)

header = ttk.Label(form, text="Inicia sesión", style="FORM.TLabel")
header.grid(row=0, column=0, columnspan=2, sticky="w", padx=18, pady=(18, 6))

# Usuario
lbl_user = ttk.Label(form, text="Usuario", style="App.TLabel")
lbl_user.grid(row=1, column=0, sticky="e", padx=(18, 8), pady=6)
ent_user = ttk.Entry(form,style="App.TEntry")
ent_user.grid(row=1, column=1, sticky="we", padx=(0, 18), pady=6, ipady=4)

# Password
lbl_password = ttk.Label(form, text="Usuario", style="App.TLabel")
lbl_password.grid(row=2, column=0, sticky="e", padx=(18, 8), pady=6)
ent_password = ttk.Entry(form,show="*",style="App.TEntry")
ent_password.grid(row=2, column=1, sticky="we", padx=(0, 18), pady=6, ipady=4)


# Separador visual
sep = tk.Frame(form, bg=App.SUBTONE, height=1)
sep.grid(row=3, column=0, columnspan=2, sticky="we", padx=18, pady=(6, 6))

# Botones
def on_login():
    print("Login:", ent_user.get())
    print("password", ent_password.get())

btn_login = tk.Button(form, text="Entrar", bg=App.ACCENT, fg="black", activebackground=App.ACCENT,
                      relief="flat", padx=14, pady=8, command=on_login)
btn_login.grid(row=4, column=0, columnspan=2, pady=14)

# Enlace de registro
def on_register():
    header.config(text="Crear cuenta")
    btn_login.config(text="Registrar")

link = tk.Label(form, text="¿No tienes cuenta? Crear una →", cursor="hand2",
                bg=App.PANEL, fg=App.SUBTONE, font=("Segoe UI", 10, "underline"))
link.grid(row=5, column=0, columnspan=2, sticky="e", padx=18, pady=(0, 14))
link.bind("<Button-1>", lambda e: on_register())

#METODOS
def validar(event):
    usuario = ent_user.get()
    password = ent_password.get()
    if usuario == "admin" and password == "admin":
        print("Auth Success")
        showinfo(title="Login", message="Datos Correctos")
    else:
        showerror(title="Login", message="Datos Correctos")

#EVENTOS
btn_login.bind("<Return>",validar)
btn_login.bind("<Button-1>",validar)







root.mainloop()