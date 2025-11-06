import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror


class App(tk.Tk):
    # BRAND COLORES
    # 🎨 Paleta ZonaFit
    BG = "#1d2d44"  # fondo principal
    PANEL = "#3e5c76"  # panel/form
    TEXT = "#f0ebd8"  # texto claro
    ACCENT = "#e09f3e"  # botón/énfasis
    SUBTONE = "#748cab"  # detalles/bordes
    ACCENT_HOVER = "#f2956b"  # un poco más claro

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_estilos()

    def configurar_ventana(self):
        self.geometry("600x400")
        self.configure(background=App.BG)
        self.title("Manejo de Ventanas con POO")

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(self,background=App.BG,foreground=App.TEXT)
        style.configure("App.TFrame", background=App.PANEL)
        style.configure("App.TEntry",background="#000000")
        style.configure("Brand.TFrame", background=App.BG)
        style.configure("App.TButton", background=App.ACCENT,
                  borderwidth=0, relief="flat"
                  , focusthickness=0,padding=6)
        style.configure("App.TLabel", background=App.PANEL, foreground=App.TEXT,
                        borderwidth=0, relief="flat",
                        font=("Segoe UI", 11),
                        focusthickness=0,padding=6)
        style.configure("App.TLabel", background=App.PANEL, foreground=App.TEXT,
                        borderwidth=0, relief="flat"
                        , focusthickness=0, padding=6)
        style.configure(
            "Title.TLabel",
            background=App.BG,
            foreground=App.TEXT,
            font=("Segoe UI", 28, "bold"),
            padding=10
        )
        style.configure(
            "Subtitle.TLabel",
            background=App.BG,
            foreground=App.SUBTONE,
            font=("Segoe UI", 14, "bold"),
            padding=10
        )
        style.configure(
            "FORM.TLabel",
            background=App.PANEL,
            foreground=App.TEXT,
            font=("Segoe UI", 14, "bold"),
            padding=10
        )
        style.configure("App.TEntry", foreground="#000000")

        style.map(
            "Login.TButton",
            background=[
                ("active", App.ACCENT_HOVER),  # cuando el mouse pasa encima
                ("pressed", "#d97b4b"),  # cuando se presiona
            ],
            foreground=[
                ("disabled", "#999999")
            ]
        )

if __name__ == "__main__":
    app = App()
    app.mainloop()