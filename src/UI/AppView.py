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
    ACCENT_HOVER = "#f2ce6b"  # un poco más claro
    TABLE_BG = "#e5edf5"
    HEADER_HOVER = "#84B7F0"  # azul neblina (hover)

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

        style.configure("Icon.TButton", background=App.BG,
                        borderwidth=0, relief="flat"
                        , focusthickness=0, padding=6)
        style.configure("App.TLabel", background=App.BG, foreground=App.TEXT,
                        borderwidth=0, relief="flat",
                        font=("Segoe UI", 11),
                        focusthickness=0,padding=6)
        style.configure("FormTitle.TLabel", background=App.PANEL, foreground=App.TEXT,
                        borderwidth=0, relief="flat",
                        font=("Segoe UI", 14,"bold"),
                        focusthickness=0, padding=6)
        style.configure("Form.TLabel", background=App.PANEL, foreground=App.TEXT,
                        borderwidth=0, relief="flat",
                        font=("Segoe UI", 10),
                        focusthickness=0, padding=6)
        style.configure("Brand.TLabel", background=App.BG, foreground=App.TEXT,
                        borderwidth=0, relief="flat",
                        font=("Segoe UI", 10)
                        , focusthickness=0, padding=6)
        style.configure("Button.TLabel", background=App.ACCENT, foreground=App.TEXT,
                        borderwidth=0, relief="flat",
                        font=("Segoe UI", 11),
                        focusthickness=0, padding=6)
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
        style.configure("App.TEntry", foreground="#000000",
                        relief="flat")

        style.configure(
            "InformationForm.TEntry",
            foreground=App.TEXT,  # color del texto
            fieldbackground=App.PANEL,  # color de fondo (para ttk.Entry)
            borderwidth=0,  # sin borde lateral o superior
            relief="flat",  # sin relieve, base plana
            highlightthickness=0,  # evita el borde brillante en algunos temas
            padding=(0, 0, 0, 2)  # espacio inferior visual
        )

        # 🔹 Simulación del borde inferior:
        style.map(
            "InformationForm.TEntry",
            bordercolor=[("focus", App.ACCENT), ("!focus", App.SUBTONE)],
            lightcolor=[("focus", App.ACCENT)],
            darkcolor=[("focus", App.ACCENT)]
        )

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

        style.map(
            "App.TButton",
            background=[
                ("active", App.ACCENT_HOVER),  # cuando el mouse pasa encima
                ("pressed", "#d97b4b"),  # cuando se presiona
            ],
            foreground=[
                ("disabled", "#999999")
            ]
        )

        style.map(
            "Icon.TButton",
            background=[
                ("active", App.PANEL),  # cuando el mouse pasa encima
                ("pressed", App.ACCENT_HOVER),  # cuando se presiona
            ],
            foreground=[
                ("disabled", "#999999")
            ]
        )

        # === Treeview general ===
        style.configure(
            "ZonaFit.Treeview",
            background=App.TABLE_BG,
            fieldbackground=App.TABLE_BG,
            foreground="#111111",
            rowheight=28,
            borderwidth=0
        )

        style.map(
            "ZonaFit.Treeview",
            background=[("selected", "#e09f3e")],
            foreground=[("selected", "#1d2d44")]
        )

        # === Encabezados planos y sin bordes ===
        style.configure(
            "Treeview.Heading",
            background=App.PANEL,  # mismo tono que la tabla
            foreground=App.TEXT,
            relief="flat",  # sin bordes
            borderwidth=0,
            font=("Segoe UI", 10, "bold")
        )

        # Hover de encabezado
        style.map(
            "Treeview.Heading",
            background=[("active", App.HEADER_HOVER)],
            relief=[("active", "flat"), ("pressed", "flat")]
        )

        style.configure(
            "InformationForm.TCombobox",
            foreground=App.TEXT,  # texto
            fieldbackground=App.PANEL,  # fondo del campo
            background=App.PANEL,  # fondo del widget (importante para el dropdown)
            arrowcolor=App.TEXT,  # color del ícono de flecha
            borderwidth=0,
            relief="flat",
            padding=(0, 0, 0, 2)
        )

        # 🔹 Simulación de borde inferior
        style.map(
            "InformationForm.TCombobox",
            fieldbackground=[
                ("readonly", App.PANEL),
                ("!disabled", App.PANEL)
            ],
            bordercolor=[("focus", App.ACCENT), ("!focus", App.SUBTONE)],
            lightcolor=[("focus", App.ACCENT)],
            darkcolor=[("focus", App.ACCENT)],
            arrowcolor=[("active", App.ACCENT_HOVER), ("!active", App.TEXT)]
        )

        # Agregar
        style.configure("Add.TButton", background=App.ACCENT_HOVER, foreground="black", borderwidth=0, relief="flat",
                        padding=6)
        style.map("Add.TButton", background=[("active", "#6fdc6f")])

        # Editar
        style.configure("Edit.TButton", background=App.ACCENT_HOVER, foreground="black", borderwidth=0, relief="flat",
                        padding=6)
        style.map("Edit.TButton", background=[("active", "#74d5ef")])

        # Eliminar
        style.configure("Delete.TButton", background=App.ACCENT_HOVER, foreground="black", borderwidth=0, relief="flat",
                        padding=6)
        style.map("Delete.TButton", background=[("active", "#e4746f")])

        # Guardar
        style.configure("Save.TButton", background=App.ACCENT_HOVER, foreground="black", borderwidth=0, relief="flat",
                        padding=6)
        style.map("Save.TButton", background=[("active", "#66bb6a")])

        #PANEL DE BOTONES


if __name__ == "__main__":
    app = App()
    app.mainloop()