import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from tkinter import messagebox
from src.Controller.login_controller import *
from src.Controller.client_controller import *
from src.UI.AppView import *
from PIL import Image, ImageTk
from pathlib import Path

from src.UI.HomeView import *
from src.utils.HelpFunctions import *
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent
image_user = BASE_DIR / "images" / "circle-user.png"
image_payment = BASE_DIR / "images" / "payroll-check.png"
image_worker = BASE_DIR / "images" / "user-plumber.png"

class ClientView:
    APP_NAME = "ZonaFit - Home"
    def __init__(self, username: str):
        self._username = username
        self._current_state = "WAITING"

    def client_view(self):

        #Funciones
        def cargar_datos():
            clients_information = controller.cargar_datos()
            return clients_information

        root = App()
        root.title(ClientView.APP_NAME)
        controller = ClientController()
        root.geometry("1050x500")

        for c in range(5):
            root.columnconfigure(c, weight=1)
        for r in range(5):
            root.rowconfigure(r, weight=1)
        root.rowconfigure(3,weight=0)

        #PANEL USUARIO
        panel_frame = ttk.Frame(root, style="App.TFrame")
        panel_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5, rowspan=2)

        # Usuario
        lbl_user_information = ttk.Label(panel_frame, text="Client Information", style="FormTitle.TLabel", )
        lbl_user_information.grid(row=0, column=0, sticky="e", padx=(18, 8), pady=6, columnspan=2,)

        lbl_name = ttk.Label(panel_frame, text="Nombre", style="Form.TLabel", justify="left", anchor="w")
        lbl_name.grid(row=1, column=0, sticky="we", padx=(18, 8), pady=6)
        ent_name = ttk.Entry(panel_frame, style="InformationForm.TEntry")
        ent_name.grid(row=1, column=1, sticky="we", padx=(0, 18), pady=6, ipady=4)

        lbl_last = ttk.Label(panel_frame, text="Apellido", style="Form.TLabel")
        lbl_last.grid(row=2, column=0, sticky="we", padx=(18, 8), pady=6)
        ent_last = ttk.Entry(panel_frame, style="InformationForm.TEntry")
        ent_last.grid(row=2, column=1, sticky="we", padx=(0, 18), pady=6, ipady=4)

        lbl_membresia = ttk.Label(panel_frame, text="Tipo de Membresia", style="Form.TLabel")
        lbl_membresia.grid(row=3, column=0, sticky="we", padx=(18, 8), pady=6)
        ent_membresia = ttk.Combobox(panel_frame, style="InformationForm.TCombobox",
                                     values=["Mensual", "Trimestral", "Anual", "VIP"],state="readonly")
        ent_membresia.grid(row=3, column=1, sticky="we", padx=(0, 18), pady=6, ipady=4)

        lbl_membresia_id = ttk.Label(panel_frame, text="Membresia ID", style="Form.TLabel")
        lbl_membresia_id.grid(row=4, column=0, sticky="we", padx=(18, 8), pady=6)
        ent_membresia_id = ttk.Entry(panel_frame, style="InformationForm.TEntry", state="readonly")
        ent_membresia_id.grid(row=4, column=1, sticky="we", padx=(0, 18), pady=6, ipady=4)

        lbl_payment_date = ttk.Label(panel_frame, text="Fecha de Corte", style="Form.TLabel")
        lbl_payment_date.grid(row=5, column=0, sticky="we", padx=(18, 8), pady=6)
        ent_payment_date = ttk.Entry(panel_frame, style="InformationForm.TEntry")
        ent_payment_date.grid(row=5, column=1, sticky="we", padx=(0, 18), pady=6, ipady=4)

        lbl_payment_pending = ttk.Label(panel_frame, text="Membresia Vencida", style="Form.TLabel")
        lbl_payment_pending.grid(row=6, column=0, sticky="we", padx=(18, 8), pady=6)
        ent_payment_pending = ttk.Combobox(panel_frame, style="InformationForm.TCombobox"
                                           ,values=["True", "False"],state="readonly")
        ent_payment_pending.grid(row=6, column=1, sticky="we", padx=(0, 18), pady=6, ipady=4)

        lbl_email = ttk.Label(panel_frame, text="Email", style="Form.TLabel")
        lbl_email.grid(row=7, column=0, sticky="we", padx=(18, 8), pady=6)
        ent_email = ttk.Entry(panel_frame, style="InformationForm.TEntry")
        ent_email.grid(row=7, column=1, sticky="we", padx=(0, 18), pady=6, ipady=4)

        lbl_phone = ttk.Label(panel_frame, text="Phone", style="Form.TLabel")
        lbl_phone.grid(row=8, column=0, sticky="we", padx=(18, 8), pady=6)
        ent_phone = ttk.Entry(panel_frame, style="InformationForm.TEntry")
        ent_phone.grid(row=8, column=1, sticky="we", padx=(0, 18), pady=6, ipady=4)

        # TABLA
        panel_frame.columnconfigure(0,weight=1)
        panel_frame.columnconfigure(1, weight=0)

        panel_frame = ttk.Frame(root, style="Brand.TFrame")
        panel_frame.grid(row=0, column=2,rowspan=3, sticky=tk.NSEW, padx=5, pady=5)

        columnas = ("Id", "Nombre", "Membresia", "MembresiaID", "Fecha Corte", "Membresia Vencida")
        tabla = ttk.Treeview(panel_frame, columns=columnas, show="headings", style="ZonaFit.Treeview")
        tabla.heading("Id", text=columnas[0], anchor=tk.CENTER)
        tabla.heading("Nombre", text=columnas[1], anchor=tk.W)
        tabla.heading("Membresia", text=columnas[2], anchor=tk.W)
        tabla.heading("MembresiaID", text=columnas[3], anchor=tk.W)
        tabla.heading("Fecha Corte", text=columnas[4], anchor=tk.W)
        tabla.heading("Membresia Vencida", text=columnas[5], anchor=tk.W)

        # Ajustar anchos (en píxeles)
        tabla.column("Id", width=60, anchor=tk.CENTER, stretch=False)
        tabla.column("Nombre", width=150, anchor=tk.W, stretch=False)
        tabla.column("Membresia", width=120, anchor=tk.W, stretch=False)
        tabla.column("MembresiaID", width=100, anchor=tk.CENTER, stretch=False)
        tabla.column("Fecha Corte", width=120, anchor=tk.CENTER, stretch=False)
        tabla.column("Membresia Vencida", width=150, anchor=tk.CENTER, stretch=False)


        # Cargar Datos a latabla
        datos = ((1, "Hector Lara", 32), (2, "Jazmin Banda", 32))
        datos_2 = datos + datos + datos

        #CODIGO A MODIFICAR

        datos = cargar_datos()
        for dato in datos:
            tabla.insert(parent="", index=tk.END, values=dato)
        """for dato in datos_2:
            tabla.insert(parent="", index=tk.END, values=dato)"""
        # CODIGO A MODIFICAR


        scrollbar = ttk.Scrollbar(panel_frame, orient=tk.VERTICAL, command=tabla.yview)
        tabla.configure(yscrollcommand=scrollbar.set)

        lbl_user = ttk.Label(root, text=f"Usuario: {self._username}", style="Brand.TLabel")
        lbl_user.grid(row=5, column=0, sticky=tk.NSEW)

        tabla.grid(row=0, column=0, sticky=tk.NSEW)
        scrollbar.grid(row=0, column=1, sticky=tk.NSEW)

        # PANEL DE BOTONES
        panel_buttons = ttk.Frame(root, style="App.TFrame")
        panel_buttons.grid(
            row=3, column=0, columnspan=5,
            sticky="ew", padx=10, pady=10, ipady=10
        )

        # 🧩 Distribuir espacio en columnas (no filas)
        for c in range(6):
            panel_buttons.columnconfigure(c, weight=1)
        panel_buttons.rowconfigure(0, weight=1)

        # 🎯 Crear botones centrados horizontalmente
        btn_regresar = ttk.Button(panel_buttons, text="Regresar", style="Add.TButton")
        btn_buscar = ttk.Button(panel_buttons, text="Buscar", style="Add.TButton")
        btn_agregar = ttk.Button(panel_buttons, text="Agregar", style="Add.TButton")
        btn_editar = ttk.Button(panel_buttons, text="Editar", style="Edit.TButton")
        btn_eliminar = ttk.Button(panel_buttons, text="Eliminar", style="Delete.TButton")
        btn_guardar = ttk.Button(panel_buttons, text="Guardar", style="Save.TButton")

        # 🧱 Acomodar en una sola fila (centrados)
        btn_regresar.grid(row=0, column=0, sticky="ew", padx=8, pady=8)
        btn_buscar.grid(row=0, column=1, sticky="ew", padx=8, pady=8)
        btn_agregar.grid(row=0, column=2, sticky="ew", padx=8, pady=8)
        btn_editar.grid(row=0, column=3, sticky="ew", padx=8, pady=8)
        btn_eliminar.grid(row=0, column=4, sticky="ew", padx=8, pady=8)
        btn_guardar.grid(row=0, column=5, sticky="ew", padx=8, pady=8)

        ##lbl_user = ttk.Label(root, text=f"Usuario: {self._username}", style="Brand.TLabel")
        ##lbl_user.grid(row=3, column=0, sticky=tk.NSEW)

        # FUNCIONES
        def mostrar_registro_seleccionado(event):
            if len(tabla.selection()) > 0:
                elemento_seleccionado = tabla.selection()[0]
                elemento = tabla.item(elemento_seleccionado)
                print(elemento.get("values"))
                ent_membresia_id.configure(state="normal")

                ent_name.delete(0,tk.END)
                ent_last.delete(0,tk.END)
                ent_membresia.delete(0,tk.END)
                ent_membresia_id.delete(0,tk.END)
                ent_payment_date.delete(0,tk.END)
                ent_payment_pending.delete(0,tk.END)
                ent_email.delete(0,tk.END)
                ent_phone.delete(0,tk.END)

                ent_name.focus_set()

                ent_name.insert(0,str(elemento.get("values")[1]).split(" ")[0])
                ent_last.insert(0,str(elemento.get("values")[1]).split(" ")[1])
                ent_membresia.set(str(elemento.get("values")[2]))
                ent_membresia_id.insert(0,str(elemento.get("values")[3]))
                ent_payment_date.insert(0,str(elemento.get("values")[4]))
                ent_payment_pending.set(str(elemento.get("values")[5]))
                ent_email.insert(0,str(elemento.get("values")[6]))
                ent_phone.insert(0, str(elemento.get("values")[7]))
                ent_membresia_id.configure(state="readonly")



        def agregar_usuario(event):
            ent_name.delete(0, tk.END)
            ent_last.delete(0, tk.END)
            ent_membresia.delete(0, tk.END)
            ent_membresia_id.delete(0, tk.END)
            ent_payment_pending.delete(0, tk.END)
            ent_payment_date.delete(0, tk.END)
            ent_email.delete(0, tk.END)
            ent_phone.delete(0, tk.END)

            ent_payment_pending.configure(state="normal")
            ent_payment_date.insert(0, datetime.now().strftime("%d/%m/%Y"))
            self._current_state = "ADD"

        def editar_usuario(event):
            if len(ent_membresia_id.get()) < 1:
                showerror(title="Error", message="Debe seleccionar un usuario primero")
            else:
                self._current_state = "EDIT"
                ent_membresia.configure(state="normal")
                ent_payment_pending.configure(state="normal")
                print(self._current_state)


        def eliminar_usuario(event):
            if len(ent_membresia_id.get()) < 1:
                showerror(title="Error", message="Debe seleccionar un usuario primero")
            else:
                self._current_state = "DELETE"
                print(self._current_state)

        def back_home(event):
            root.withdraw()
            root.destroy()
            home_view = HomeView(username=self._username)
            home_view.home_view()

        def buscar_usuario(event):
            pass


        def confirmar_usuario(event):
            if self._current_state == "ADD":
                tabla.selection_remove(tabla.selection())
                ent_payment_date.insert(0, datetime.now().strftime("%d/%m/%Y"))
                lst_elements = [ent_name.get(), ent_last.get(), ent_membresia.get(), ent_email.get(), ent_phone.get()]
                print(lst_elements)
                controller.agregar_usuario(lst_elements)
                tabla.selection_remove(tabla.selection())

                tabla.delete(*tabla.get_children())
                tabla.selection_remove(tabla.selection())
                tabla.focus("")  # quita el foco del ítem seleccionado
                ent_name.focus_set()


                datos = cargar_datos()


                for dato in datos:
                    tabla.insert(parent="", index=tk.END, values=dato)

                ent_name.delete(0, tk.END)
                ent_last.delete(0, tk.END)
                ent_membresia.delete(0, tk.END)
                ent_membresia_id.delete(0, tk.END)
                ent_payment_pending.delete(0, tk.END)
                ent_payment_date.delete(0, tk.END)
                ent_email.delete(0, tk.END)
                ent_phone.delete(0, tk.END)
                ent_payment_pending.configure(state="readonly")
                self._current_state = "WAITING"

            elif self._current_state == "EDIT":

                tabla.selection_remove(tabla.selection())
                if len(ent_name.get()) > 0:
                    if len(ent_last.get()) > 0:
                        if validar_fecha(ent_payment_date.get()):
                            if len(ent_email.get()) > 0:
                                if len(ent_phone.get()) > 0:
                                    lst_elements = [ent_name.get(), ent_last.get(), ent_membresia.get(), ent_email.get(), ent_phone.get(), ent_payment_date.get(), ent_payment_pending.get()]
                                    print(lst_elements)
                                    controller.editar_usuario(lst_elements)
                                    tabla.selection_remove(tabla.selection())

                                    tabla.delete(*tabla.get_children())
                                    tabla.selection_remove(tabla.selection())
                                    tabla.focus("")  # quita el foco del ítem seleccionado
                                    ent_name.focus_set()

                                    datos = cargar_datos()
                                    for dato in datos:
                                        tabla.insert(parent="", index=tk.END, values=dato)

                                    ent_name.delete(0, tk.END)
                                    ent_last.delete(0, tk.END)
                                    ent_membresia.delete(0, tk.END)
                                    ent_membresia_id.delete(0, tk.END)
                                    ent_payment_pending.delete(0, tk.END)
                                    ent_payment_date.delete(0, tk.END)
                                    ent_email.delete(0, tk.END)
                                    ent_phone.delete(0, tk.END)
                                    ent_membresia.configure(state="readonly")
                                    ent_payment_pending.configure(state="readonly")
                                    self._current_state = "WAITING"

                                else:
                                    showerror(title="Error", message="Numero de telefono del usuario no es correcto")
                            else:
                                showerror(title="Error", message="Correo del usuario no es correcto")
                        else:
                            showerror(title="Error", message="Formato de fecha no valido")
                    else:
                        showerror(title="Error", message="Apellido del usuario no es correcto")
                else:
                    showerror(title="Error", message="Nombre del usuario no es correcto")


                lst_elements = [ent_name.get(), ent_last.get(), ent_membresia.get(), ent_email.get(), ent_phone.get(), ent_payment_date.get()]
                print(lst_elements)
                self._current_state = "WAITING"

            elif self._current_state == "DELETE":
                lst_elements = [ent_name.get(), ent_last.get(), ent_membresia.get(), ent_email.get(), ent_phone.get(),
                                ent_payment_date.get()]
                respuesta = messagebox.askyesno(
                    title="Confirmar eliminación",
                    message="¿Estás seguro de que deseas eliminar este usuario?"
                )
                if respuesta:
                    controller.eliminar_usuario(lst_elements)
                    tabla.delete(*tabla.get_children())
                    tabla.selection_remove(tabla.selection())
                    tabla.focus("")  # quita el foco del ítem seleccionado
                    ent_name.focus_set()

                    datos = cargar_datos()
                    for dato in datos:
                        tabla.insert(parent="", index=tk.END, values=dato)

                    ent_name.delete(0, tk.END)
                    ent_last.delete(0, tk.END)
                    ent_membresia.delete(0, tk.END)
                    ent_membresia_id.delete(0, tk.END)
                    ent_payment_pending.delete(0, tk.END)
                    ent_payment_date.delete(0, tk.END)
                    ent_email.delete(0, tk.END)
                    ent_phone.delete(0, tk.END)
                    ent_membresia.configure(state="readonly")
                    self._current_state = "WAITING"
                else:
                    self._current_state = "WAITING"

            else:
                print("Waiting...")


        # EVENTOS
        tabla.bind("<<TreeviewSelect>>", mostrar_registro_seleccionado)
        btn_agregar.bind("<Return>", agregar_usuario)
        btn_agregar.bind("<Button-1>", agregar_usuario)
        btn_guardar.bind("<Return>", confirmar_usuario)
        btn_guardar.bind("<Button-1>", confirmar_usuario)
        btn_editar.bind("<Return>", editar_usuario)
        btn_editar.bind("<Button-1>", editar_usuario)
        btn_eliminar.bind("<Return>", eliminar_usuario)
        btn_eliminar.bind("<Button-1>", eliminar_usuario)
        btn_regresar.bind("<Return>", back_home)
        btn_regresar.bind("<Button-1>", back_home)
        btn_buscar.bind("<Return>", buscar_usuario)
        btn_buscar.bind("<Button-1>", buscar_usuario)




        root.mainloop()

if __name__ == "__main__":
    client = ClientView("hlaras")
    client.client_view()