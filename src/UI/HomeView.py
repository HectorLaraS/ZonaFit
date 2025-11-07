import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from src.Controller.login_controller import *
from src.Controller.login_controller import *
from src.UI.AppView import *
from PIL import Image, ImageTk
from pathlib import Path
from src.UI.ClientView import *

BASE_DIR = Path(__file__).resolve().parent.parent
image_user = BASE_DIR / "images" / "circle-user.png"
image_payment = BASE_DIR / "images" / "payroll-check.png"
image_worker = BASE_DIR / "images" / "user-plumber.png"

class HomeView:
    APP_NAME = "ZonaFit - Home"
    def __init__(self, username: str):
        self._username = username

    def home_view(self):
        root = App()
        root.title(HomeView.APP_NAME)
        controller = LoginController()

        for x in range(3):
            root.columnconfigure(x, weight=1)
            root.rowconfigure(x, weight=1)
        root.rowconfigure(3,weight=0)

        image_icon_user = tk.PhotoImage(file=image_user)
        image_icon_worker = tk.PhotoImage(file=image_worker)
        image_icon_payment = tk.PhotoImage(file=image_payment)

        client_frame = ttk.Frame(root,style="App.TFrame")
        client_frame.grid(row=0, column=0,sticky=tk.NSEW, padx=5, pady=5)
        client_frame.rowconfigure(0,weight=1)
        client_frame.rowconfigure(1,weight=0)

        ###CLIENTES
        btn_clients = ttk.Button(
            client_frame,
            image=image_icon_user,  # imagen
            compound="top",  # texto debajo de la imagen
            command=lambda: print("Abrir módulo Clientes"),  # acción
            style="Icon.TButton"  # estilo (puedes usar el tuyo)
        )
        btn_clients.grid(row=0, column=0, sticky="nsew")

        lbl_clients = ttk.Label(client_frame,style="Button.TLabel",text="Clientes", anchor="center", justify="center", width=24 )
        lbl_clients.grid(row=1, column=0, sticky=tk.NSEW)

        ###TRABAJADORES

        worker_frame = ttk.Frame(root, style="App.TFrame")
        worker_frame.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)
        worker_frame.rowconfigure(0, weight=1)
        worker_frame.rowconfigure(1, weight=0)

        btn_workers = ttk.Button(
            worker_frame,
            image=image_icon_worker,  # imagen
            compound="top",  # texto debajo de la imagen
            command=lambda: print("Abrir módulo Clientes"),  # acción
            style="Icon.TButton"  # estilo (puedes usar el tuyo)
        )
        btn_workers.grid(row=0, column=0, sticky="nsew")

        lbl_workers = ttk.Label(worker_frame, style="Button.TLabel", text="Trabajadores", anchor="center", justify="center",
                                width=24)
        lbl_workers.grid(row=1, column=0, sticky=tk.NSEW)


        lbl_user = ttk.Label(root,text=f"Usuario: {self._username}", style="Brand.TLabel")
        lbl_user.grid(row=3,column=0, sticky=tk.NSEW)

        ###PAGOS

        payment_frame = ttk.Frame(root, style="Icon.TFrame")
        payment_frame.grid(row=0, column=2, sticky=tk.NSEW, padx=5, pady=5)
        payment_frame.rowconfigure(0, weight=1)
        payment_frame.rowconfigure(1, weight=0)

        btn_payment = ttk.Button(
            payment_frame,
            image=image_icon_payment,  # imagen
            compound="top",  # texto debajo de la imagen
            command=lambda: print("Abrir módulo Clientes"),  # acción
            style="Icon.TButton"  # estilo (puedes usar el tuyo)
        )
        btn_payment.grid(row=0, column=0, sticky="nsew")

        lbl_payment = ttk.Label(payment_frame, style="Button.TLabel", text="Pagos", anchor="center",
                                justify="center",
                                width=24)
        lbl_payment.grid(row=1, column=0, sticky=tk.NSEW)

        lbl_user = ttk.Label(root, text=f"Usuario: {self._username}", style="Brand.TLabel")
        lbl_user.grid(row=3, column=0, sticky=tk.NSEW)


        def abrir_modulo_clientes(event):
            root.withdraw()
            root.destroy()
            mod_clients = ClientView(username=self._username)
            mod_clients.client_view()


        # EVENTOS
        btn_clients.bind("<Return>", abrir_modulo_clientes)
        btn_clients.bind("<Button-1>", abrir_modulo_clientes)


        root.mainloop()


if __name__ == "__main__":
    home = HomeView("hlaras")
    home.home_view()