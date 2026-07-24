import threading
import customtkinter as ctk
from tkinter import filedialog

from services.process_service import ProcessService


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Medicamentos MX")
        self.geometry("900x600")

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.archivo_excel = ""

        self.process_service = ProcessService()

        self.crear_componentes()

    def crear_componentes(self):

        titulo = ctk.CTkLabel(
            self,
            text="Medicamentos MX",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=20)

        self.lbl_archivo = ctk.CTkLabel(
            self,
            text="Ningún archivo seleccionado"
        )
        self.lbl_archivo.pack(pady=10)

        btn_excel = ctk.CTkButton(
            self,
            text="Seleccionar Excel",
            command=self.seleccionar_excel
        )
        btn_excel.pack(pady=10)

        self.btn_iniciar = ctk.CTkButton(
            self,
            text="Iniciar",
            command=self.iniciar_proceso
        )
        self.btn_iniciar.pack(pady=10)

        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack(fill="x", padx=30, pady=20)
        self.progress.set(0)

        self.estado = ctk.CTkTextbox(self, height=300)
        self.estado.pack(fill="both", expand=True, padx=30, pady=20)

    def seleccionar_excel(self):

        archivo = filedialog.askopenfilename(
            filetypes=[("Excel", "*.xlsx")]
        )

        if archivo:
            self.archivo_excel = archivo

            self.lbl_archivo.configure(text=archivo)

            self.estado.insert(
                "end",
                f"Archivo seleccionado:\n{archivo}\n\n"
            )

    def iniciar_proceso(self):

        if not self.archivo_excel:

            self.estado.insert(
                "end",
                "Seleccione un archivo Excel.\n"
            )

            return

        self.btn_iniciar.configure(state="disabled")

        hilo = threading.Thread(
            target=self.ejecutar_proceso,
            daemon=True
        )

        hilo.start()

    def ejecutar_proceso(self):

        self.process_service.ejecutar(
            self.archivo_excel,
            callback=self.actualizar_progreso
        )

        self.after(
            0,
            lambda: self.estado.insert(
                "end",
                "\nProceso terminado.\n"
            )
        )

        self.after(
            0,
            lambda: self.btn_iniciar.configure(state="normal")
        )

    def actualizar_progreso(
        self,
        actual,
        total,
        medicamento
    ):

        porcentaje = actual / total

        self.after(
            0,
            lambda: self.progress.set(porcentaje)
        )

        self.after(
            0,
            lambda: self.estado.insert(
                "end",
                f"{actual}/{total} - {medicamento.producto}\n"
            )
        )

        self.after(
            0,
            lambda: self.estado.see("end")
        )