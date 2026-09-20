import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# ==========================================================
# CONFIGURACIÓN DE RUTAS Y COLORES
# ==========================================================

RUTA_DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")

COLOR_FONDO = "#F5F6FA"
COLOR_PRINCIPAL = "#5B5FEF"
COLOR_PRINCIPAL_OSCURO = "#4548C8"
COLOR_BLANCO = "#FFFFFF"
COLOR_TEXTO = "#202124"
COLOR_GRIS = "#6B7280"


# ==========================================================
# GLOSARIO DE 20 TÉRMINOS
# ==========================================================

glosario = {
    "Machine Learning": "Método de IA que permite a las computadoras aprender de los datos y mejorar sus resultados sin ser programadas para cada situación.",
    "Deep Learning": "Tipo de aprendizaje automático que utiliza redes neuronales con múltiples capas para analizar información compleja.",
    "Red neuronal artificial": "Modelo de IA formado por unidades conectadas que procesan información y reconocen patrones.",
    "IA generativa": "Tecnología de IA capaz de crear contenido nuevo, como texto, imágenes, audio, video o código.",
    "Procesamiento del Lenguaje Natural (PLN)": "Área de la IA que permite a las computadoras comprender, interpretar y generar lenguaje humano.",
    "Visión por computadora": "Tecnología que permite a los sistemas de IA analizar e interpretar imágenes y videos.",
    "Aprendizaje supervisado": "Método en el que una IA aprende utilizando datos que ya tienen respuestas o categorías conocidas.",
    "Aprendizaje no supervisado": "Método en el que la IA analiza datos sin respuestas previamente establecidas para encontrar patrones o grupos.",
    "Aprendizaje por refuerzo": "Método en el que un sistema aprende mediante acciones y recibe recompensas o penalizaciones según sus resultados.",
    "Modelo de IA": "Sistema entrenado con datos que puede realizar tareas como clasificar información, hacer predicciones o generar contenido.",
    "Modelo fundacional": "Modelo de IA entrenado con grandes cantidades de datos que puede utilizarse como base para diferentes aplicaciones.",
    "LLM": "Modelo de lenguaje entrenado con grandes cantidades de texto que puede comprender y generar lenguaje humano.",
    "Transformer": "Arquitectura de IA utilizada para procesar información y que es fundamental en muchos modelos modernos de lenguaje.",
    "Prompt": "Instrucción o pregunta que una persona proporciona a una inteligencia artificial para indicarle qué debe hacer.",
    "Token": "Unidad de información que un modelo de lenguaje utiliza para procesar texto, como una palabra, parte de una palabra o símbolo.",
    "Inferencia": "Proceso mediante el cual un modelo de IA utiliza lo aprendido durante su entrenamiento para generar una respuesta o realizar una predicción.",
    "Datos de entrenamiento": "Información utilizada para enseñar a un modelo de IA a reconocer patrones y realizar determinadas tareas.",
    "Big Data": "Se refiere a grandes cantidades de datos que pueden utilizarse para entrenar modelos de IA y encontrar patrones o tendencias.",
    "Parámetros": "Valores internos de un modelo de IA que se ajustan durante el entrenamiento para ayudarlo a aprender patrones.",
    "Automatización inteligente": "Uso de inteligencia artificial para realizar tareas de forma automática, con poca intervención humana."
}


# ==========================================================
# LÍNEA DEL TIEMPO
# ==========================================================

linea_tiempo_dict = {
    "1943 - Primer modelo de neurona artificial": "McCulloch y Pitts propusieron un modelo matemático que imitaba el funcionamiento de una neurona humana. Fue un antecedente de las redes neuronales.",
    "1950 - Test de Turing": "Alan Turing planteó una prueba para determinar si una máquina podía mostrar un comportamiento similar al de una persona.",
    "1956 - Nace oficialmente la IA": "En la conferencia de Dartmouth se utilizó formalmente el término Inteligencia Artificial, iniciando la IA como área de investigación.",
    "1966 - ELIZA": "Se desarrolló ELIZA, uno de los primeros programas capaces de mantener conversaciones mediante respuestas programadas.",
    "1970 - Sistemas expertos": "Comenzaron a desarrollarse sistemas que utilizaban conocimientos y reglas para resolver problemas de áreas específicas.",
    "1997 - Deep Blue": "La computadora Deep Blue, de IBM, derrotó al campeón mundial de ajedrez Garry Kasparov, demostrando el avance de la IA.",
    "2012 - Avance del aprendizaje profundo": "La red neuronal AlexNet obtuvo excelentes resultados en reconocimiento de imágenes, impulsando el desarrollo del Deep Learning.",
    "2017 - Arquitectura Transformer": "Se presentó Transformer, una tecnología que permitió grandes avances en el procesamiento y comprensión del lenguaje.",
    "2022 - Popularización de la IA generativa": "ChatGPT se hizo público y aumentó el interés en herramientas capaces de generar textos y responder preguntas.",
    "2024 - Expansión de la IA": "La IA generativa comenzó a utilizarse cada vez más en educación, empresas, programación, creación de contenido y otras áreas."
}


# ==========================================================
# CLASE PRINCIPAL
# ==========================================================

class AplicacionEscritorioIA:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Aplicación de Escritorio - Inteligencia Artificial")
        self.ventana.geometry("950x750")
        self.ventana.configure(bg=COLOR_FONDO)
        
        self.imagen_cargada = None
        self.menu_principal()

    def limpiar_ventana(self):
        self.ventana.unbind_all("<MouseWheel>")
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def agregar_barra_superior(self):
        marco_superior = tk.Frame(self.ventana, bg=COLOR_FONDO)
        marco_superior.pack(fill="x", padx=20, pady=(10, 0))

        boton_regresar = tk.Button(
            marco_superior,
            text="🏠 Volver al Menú Principal",
            command=self.menu_principal,
            font=("Arial", 10, "bold"),
            bg=COLOR_PRINCIPAL,
            fg=COLOR_BLANCO,
            activebackground=COLOR_PRINCIPAL_OSCURO,
            activeforeground=COLOR_BLANCO,
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=4
        )
        boton_regresar.pack(side="left")

    def crear_titulo(self, texto):
        titulo = tk.Label(
            self.ventana,
            text=texto,
            font=("Arial", 18, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO
        )
        titulo.pack(pady=(10, 5))

    def crear_boton_menu(self, texto, comando):
        boton = tk.Button(
            self.ventana,
            text=texto,
            command=comando,
            font=("Arial", 12, "bold"),
            width=32,
            height=2,
            bg=COLOR_PRINCIPAL,
            fg=COLOR_BLANCO,
            activebackground=COLOR_PRINCIPAL_OSCURO,
            activeforeground=COLOR_BLANCO,
            relief="flat",
            cursor="hand2"
        )
        boton.pack(pady=7)
        return boton

    # ======================================================
    # MENÚ PRINCIPAL
    # ======================================================

    def menu_principal(self):
        self.limpiar_ventana()

        titulo = tk.Label(
            self.ventana,
            text="INTELIGENCIA ARTIFICIAL",
            font=("Arial", 26, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_PRINCIPAL
        )
        titulo.pack(pady=(35, 5))

        subtitulo = tk.Label(
            self.ventana,
            text="Aplicación educativa de escritorio",
            font=("Arial", 12),
            bg=COLOR_FONDO,
            fg=COLOR_GRIS
        )
        subtitulo.pack(pady=(0, 20))

        self.crear_boton_menu("⏳  Línea del tiempo", self.mostrar_linea_tiempo)
        self.crear_boton_menu("📄  Infografía 1 - ChatGPT", lambda: self.mostrar_infografia(1))
        self.crear_boton_menu("🤖  Infografía 2 - Tesla Optimus", lambda: self.mostrar_infografia(2))
        self.crear_boton_menu("🧠  Infografía 3 - IA Superinteligente", lambda: self.mostrar_infografia(3))
        self.crear_boton_menu("📚  Glosario de IA", self.mostrar_glosario)

        boton_salir = tk.Button(
            self.ventana,
            text="Salir",
            command=self.salir,
            font=("Arial", 11, "bold"),
            width=20,
            bg="#E5E7EB",
            fg=COLOR_TEXTO,
            relief="flat",
            cursor="hand2"
        )
        boton_salir.pack(pady=15)

    # ======================================================
    # LÍNEA DEL TIEMPO
    # ======================================================

    def mostrar_linea_tiempo(self):
        self.limpiar_ventana()
        self.crear_titulo("LÍNEA DEL TIEMPO DE LA INTELIGENCIA ARTIFICIAL")

        subtitulo = tk.Label(
            self.ventana,
            text="Selecciona un acontecimiento histórico para ver los detalles",
            font=("Arial", 11),
            bg=COLOR_FONDO,
            fg=COLOR_GRIS
        )
        subtitulo.pack(pady=5)

        self.combo_eventos = ttk.Combobox(
            self.ventana,
            values=list(linea_tiempo_dict.keys()),
            state="readonly",
            font=("Arial", 11),
            width=55
        )
        self.combo_eventos.pack(pady=15)
        self.combo_eventos.bind("<<ComboboxSelected>>", self.mostrar_detalle_evento)

        etiqueta_desc = tk.Label(
            self.ventana,
            text="Acontecimiento:",
            font=("Arial", 12, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO
        )
        etiqueta_desc.pack(anchor="w", padx=100)

        self.texto_evento = tk.Text(
            self.ventana,
            height=8,
            width=75,
            font=("Arial", 12),
            wrap="word",
            relief="solid",
            bd=1
        )
        self.texto_evento.pack(pady=10)
        self.texto_evento.config(state="disabled")

        marco_botones = tk.Frame(self.ventana, bg=COLOR_FONDO)
        marco_botones.pack(pady=15)

        tk.Button(
            marco_botones, text="Limpiar", font=("Arial", 11, "bold"), width=15,
            command=self.limpiar_linea_tiempo, bg="#E5E7EB", fg=COLOR_TEXTO, relief="flat", cursor="hand2"
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            marco_botones, text="← Regresar al menú", font=("Arial", 11, "bold"), width=20,
            command=self.menu_principal, bg=COLOR_PRINCIPAL, fg=COLOR_BLANCO, relief="flat", cursor="hand2"
        ).grid(row=0, column=1, padx=8)

        tk.Button(
            marco_botones, text="Salir", font=("Arial", 11, "bold"), width=15,
            command=self.salir, bg="#E5E7EB", fg=COLOR_TEXTO, relief="flat", cursor="hand2"
        ).grid(row=0, column=2, padx=8)

    def mostrar_detalle_evento(self, event=None):
        evento = self.combo_eventos.get()
        if evento:
            self.texto_evento.config(state="normal")
            self.texto_evento.delete("1.0", tk.END)
            self.texto_evento.insert(tk.END, linea_tiempo_dict[evento])
            self.texto_evento.config(state="disabled")

    def limpiar_linea_tiempo(self):
        self.combo_eventos.set("")
        self.texto_evento.config(state="normal")
        self.texto_evento.delete("1.0", tk.END)
        self.texto_evento.config(state="disabled")

    # ======================================================
    # VISUALIZADOR DE INFOGRAFÍAS (CON OPCIÓN VOLVER AL MENÚ ARRIBA)
    # ======================================================

    def mostrar_infografia(self, num_infografia):
        self.limpiar_ventana()
        self.agregar_barra_superior()
        
        titulos = {
            1: "INFOGRAFÍA 1: CHATGPT",
            2: "INFOGRAFÍA 2: TESLA OPTIMUS",
            3: "INFOGRAFÍA 3: IA SUPERINTELIGENTE"
        }
        self.crear_titulo(titulos[num_infografia])

        nombres_posibles = [
            f"Infografia{num_infografia}.jpg.jpg",
            f"infografia{num_infografia}.jpg.jpg",
            f"Infografia{num_infografia}.jpg",
            f"infografia{num_infografia}.jpg"
        ]

        ruta_encontrada = None
        for nombre in nombres_posibles:
            ruta = os.path.join(RUTA_DOWNLOADS, nombre)
            if os.path.exists(ruta):
                ruta_encontrada = ruta
                break

        contenedor = tk.Frame(self.ventana, bg=COLOR_FONDO)
        contenedor.pack(fill="both", expand=True, padx=15, pady=5)

        canvas = tk.Canvas(contenedor, bg=COLOR_FONDO, highlightthickness=0)
        scrollbar = ttk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=COLOR_FONDO)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
        canvas.configure(yscrollcommand=scrollbar.set)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        self.ventana.bind_all("<MouseWheel>", _on_mousewheel)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        if ruta_encontrada:
            try:
                img_original = Image.open(ruta_encontrada)
                ancho_orig, alto_orig = img_original.size
                
                ancho_deseado = 620
                proporcion = ancho_deseado / float(ancho_orig)
                alto_deseado = int(float(alto_orig) * proporcion)

                img_resaltada = img_original.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)
                self.imagen_cargada = ImageTk.PhotoImage(img_resaltada)

                lbl_imagen = tk.Label(scrollable_frame, image=self.imagen_cargada, bg=COLOR_FONDO)
                lbl_imagen.pack(pady=5, anchor="center")

            except Exception as e:
                tk.Label(scrollable_frame, text=f"Error al cargar la imagen:\n{e}", fg="red", bg=COLOR_FONDO).pack(pady=50)
        else:
            tk.Label(scrollable_frame, text="No se encontró la imagen en Downloads.", fg=COLOR_GRIS, bg=COLOR_FONDO).pack(pady=50)

        boton_menu = tk.Button(
            self.ventana,
            text="← Regresar al menú",
            command=self.menu_principal,
            font=("Arial", 11, "bold"),
            width=25,
            bg=COLOR_PRINCIPAL,
            fg=COLOR_BLANCO,
            relief="flat",
            cursor="hand2"
        )
        boton_menu.pack(pady=10)

    # ======================================================
    # GLOSARIO
    # ======================================================

    def mostrar_glosario(self):
        self.limpiar_ventana()
        self.crear_titulo("GLOSARIO DE INTELIGENCIA ARTIFICIAL")

        subtitulo = tk.Label(
            self.ventana,
            text="Selecciona un término para consultar su definición",
            font=("Arial", 11),
            bg=COLOR_FONDO,
            fg=COLOR_GRIS
        )
        subtitulo.pack(pady=5)

        self.combo_terminos = ttk.Combobox(
            self.ventana,
            values=list(glosario.keys()),
            state="readonly",
            font=("Arial", 11),
            width=50
        )
        self.combo_terminos.pack(pady=15)
        self.combo_terminos.bind("<<ComboboxSelected>>", self.mostrar_definicion)

        etiqueta_def = tk.Label(
            self.ventana,
            text="Definición:",
            font=("Arial", 12, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO
        )
        etiqueta_def.pack(anchor="w", padx=100)

        self.texto_definicion = tk.Text(
            self.ventana,
            height=8,
            width=75,
            font=("Arial", 12),
            wrap="word",
            relief="solid",
            bd=1
        )
        self.texto_definicion.pack(pady=10)
        self.texto_definicion.config(state="disabled")

        marco_botones = tk.Frame(self.ventana, bg=COLOR_FONDO)
        marco_botones.pack(pady=15)

        tk.Button(
            marco_botones, text="Limpiar", font=("Arial", 11, "bold"), width=15,
            command=self.limpiar_glosario, bg="#E5E7EB", fg=COLOR_TEXTO, relief="flat", cursor="hand2"
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            marco_botones, text="← Regresar al menú", font=("Arial", 11, "bold"), width=20,
            command=self.menu_principal, bg=COLOR_PRINCIPAL, fg=COLOR_BLANCO, relief="flat", cursor="hand2"
        ).grid(row=0, column=1, padx=8)

        tk.Button(
            marco_botones, text="Salir", font=("Arial", 11, "bold"), width=15,
            command=self.salir, bg="#E5E7EB", fg=COLOR_TEXTO, relief="flat", cursor="hand2"
        ).grid(row=0, column=2, padx=8)

    def mostrar_definicion(self, event=None):
        termino = self.combo_terminos.get()
        if termino:
            self.texto_definicion.config(state="normal")
            self.texto_definicion.delete("1.0", tk.END)
            self.texto_definicion.insert(tk.END, glosario[termino])
            self.texto_definicion.config(state="disabled")

    def limpiar_glosario(self):
        self.combo_terminos.set("")
        self.texto_definicion.config(state="normal")
        self.texto_definicion.delete("1.0", tk.END)
        self.texto_definicion.config(state="disabled")

    # ======================================================
    # SALIR
    # ======================================================

    def salir(self):
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
            self.ventana.destroy()


# ==========================================================
# INICIAR APLICACIÓN
# ==========================================================

if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = AplicacionEscritorioIA(ventana)
    ventana.mainloop()