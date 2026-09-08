import tkinter as tk
import winsound
import os

# Datos de los elementos: [Número Atómico, Símbolo, Nombre, Masa, Categoría, Fila, Columna]
# Las filas 9 y 10 son para los Lantánidos y Actínidos respectivamente.
elementos = [
    [1,"H","Hidrógeno",1.008,"no metal",1,1],[2,"He","Helio",4.003,"gas noble",1,18],
    [3,"Li","Litio",6.941,"metal alcalino",2,1],[4,"Be","Berilio",9.012,"alcalinotérreo",2,2],[5,"B","Boro",10.81,"metaloide",2,13],[6,"C","Carbono",12.01,"no metal",2,14],[7,"N","Nitrógeno",14.01,"no metal",2,15],[8,"O","Oxígeno",16.00,"no metal",2,16],[9,"F","Flúor",19.00,"halógeno",2,17],[10,"Ne","Neón",20.18,"gas noble",2,18],
    [11,"Na","Sodio",22.99,"metal alcalino",3,1],[12,"Mg","Magnesio",24.31,"alcalinotérreo",3,2],[13,"Al","Aluminio",26.98,"post-transición",3,13],[14,"Si","Silicio",28.09,"metaloide",3,14],[15,"P","Fósforo",30.97,"no metal",3,15],[16,"S","Azufre",32.07,"no metal",3,16],[17,"Cl","Cloro",35.45,"halógeno",3,17],[18,"Ar","Argón",39.95,"gas noble",3,18],
    [19,"K","Potasio",39.10,"metal alcalino",4,1],[20,"Ca","Calcio",40.08,"alcalinotérreo",4,2],[21,"Sc","Escandio",44.96,"transición",4,3],[22,"Ti","Titanio",47.87,"transición",4,4],[23,"V","Vanadio",50.94,"transición",4,5],[24,"Cr","Cromo",52.00,"transición",4,6],[25,"Mn","Manganeso",54.94,"transición",4,7],[26,"Fe","Hierro",55.85,"transición",4,8],[27,"Co","Cobalto",58.93,"transición",4,9],[28,"Ni","Níquel",58.69,"transición",4,10],[29,"Cu","Cobre",63.55,"transición",4,11],[30,"Zn","Zinc",65.38,"transición",4,12],[31,"Ga","Galio",69.72,"post-transición",4,13],[32,"Ge","Germanio",72.63,"metaloide",4,14],[33,"As","Arsénico",74.92,"metaloide",4,15],[34,"Se","Selenio",78.97,"no metal",4,16],[35,"Br","Bromo",79.90,"halógeno",4,17],[36,"Kr","Kriptón",83.80,"gas noble",4,18],
    [37,"Rb","Rubidio",85.47,"metal alcalino",5,1],[38,"Sr","Estroncio",87.62,"alcalinotérreo",5,2],[39,"Y","Itrio",88.91,"transición",5,3],[40,"Zr","Circonio",91.22,"transición",5,4],[41,"Nb","Niobio",92.91,"transición",5,5],[42,"Mo","Molibdeno",95.95,"transición",5,6],[43,"Tc","Tecnecio",98.00,"transición",5,7],[44,"Ru","Rutenio",101.1,"transición",5,8],[45,"Rh","Rodio",102.9,"transición",5,9],[46,"Pd","Paladio",106.4,"transición",5,10],[47,"Ag","Plata",107.9,"transición",5,11],[48,"Cd","Cadmio",112.4,"transición",5,12],[49,"In","Indio",114.8,"post-transición",5,13],[50,"Sn","Estaño",118.7,"post-transición",5,14],[51,"Sb","Antimonio",121.8,"metaloide",5,15],[52,"Te","Telurio",127.6,"metaloide",5,16],[53,"I","Yodo",126.9,"halógeno",5,17],[54,"Xe","Xenón",131.3,"gas noble",5,18],
    [55,"Cs","Cesio",132.9,"metal alcalino",6,1],[56,"Ba","Bario",137.3,"alcalinotérreo",6,2],
    [72,"Hf","Hafnio",178.5,"transición",6,4],[73,"Ta","Tantalio",180.9,"transición",6,5],[74,"W","Wolframio",183.8,"transición",6,6],[75,"Re","Renio",186.2,"transición",6,7],[76,"Os","Osmio",190.2,"transición",6,8],[77,"Ir","Iridio",192.2,"transición",6,9],[78,"Pt","Platino",195.1,"transición",6,10],[79,"Au","Oro",197.0,"transición",6,11],[80,"Hg","Mercurio",200.6,"transición",6,12],[81,"Tl","Talio",204.4,"post-transición",6,13],[82,"Pb","Plomo",207.2,"post-transición",6,14],[83,"Bi","Bismuto",209.0,"post-transición",6,15],[84,"Po","Polonio",209.0,"post-transición",6,16],[85,"At","Astato",210.0,"halógeno",6,17],[86,"Rn","Radón",222.0,"gas noble",6,18],
    [87,"Fr","Francio",223.0,"metal alcalino",7,1],[88,"Ra","Radio",226.0,"alcalinotérreo",7,2],
    [104,"Rf","Rutherfordio",267.0,"transición",7,4],[105,"Db","Dubnio",268.0,"transición",7,5],[106,"Sg","Seaborgio",269.0,"transición",7,6],[107,"Bh","Bohrio",270.0,"transición",7,7],[108,"Hs","Hassio",277.0,"transición",7,8],[109,"Mt","Meitnerio",278.0,"desconocido",7,9],[110,"Ds","Darmstadtio",281.0,"desconocido",7,10],[111,"Rg","Roentgenio",282.0,"desconocido",7,11],[112,"Cn","Copernicio",285.0,"transición",7,12],[113,"Nh","Nihonio",286.0,"desconocido",7,13],[114,"Fl","Flerovio",289.0,"desconocido",7,14],[115,"Mc","Moscovio",290.0,"desconocido",7,15],[116,"Lv","Livermorio",293.0,"desconocido",7,16],[117,"Ts","Tenesino",294.0,"desconocido",7,17],[118,"Og","Oganesón",294.0,"desconocido",7,18],
    # Lantánidos (Fila 9)
    [57,"La","Lantano",138.9,"lantánido",9,3],[58,"Ce","Cerio",140.1,"lantánido",9,4],[59,"Pr","Praseodimio",140.9,"lantánido",9,5],[60,"Nd","Neodimio",144.2,"lantánido",9,6],[61,"Pm","Prometio",145.0,"lantánido",9,7],[62,"Sm","Samario",150.4,"lantánido",9,8],[63,"Eu","Europio",152.0,"lantánido",9,9],[64,"Gd","Gadolinio",157.3,"lantánido",9,10],[65,"Tb","Terbio",158.9,"lantánido",9,11],[66,"Dy","Disprosio",162.5,"lantánido",9,12],[67,"Ho","Holmio",164.9,"lantánido",9,13],[68,"Er","Erbio",167.3,"lantánido",9,14],[69,"Tm","Tulio",168.9,"lantánido",9,15],[70,"Yb","Iterbio",173.0,"lantánido",9,16],[71,"Lu","Lutecio",175.0,"lantánido",9,17],
    # Actínidos (Fila 10)
    [89,"Ac","Actinio",227.0,"actínido",10,3],[90,"Th","Torio",232.0,"actínido",10,4],[91,"Pa","Protactinio",231.0,"actínido",10,5],[92,"U","Uranio",238.0,"actínido",10,6],[93,"Np","Neptunio",237.0,"actínido",10,7],[94,"Pu","Plutonio",244.0,"actínido",10,8],[95,"Am","Americio",243.0,"actínido",10,9],[96,"Cm","Curio",247.0,"actínido",10,10],[97,"Bk","Berkelio",247.0,"actínido",10,11],[98,"Cf","Californio",251.0,"actínido",10,12],[99,"Es","Einstenio",252.0,"actínido",10,13],[100,"Fm","Fermio",257.0,"actínido",10,14],[101,"Md","Mendelevio",258.0,"actínido",10,15],[102,"No","Nobelio",259.0,"actínido",10,16],[103,"Lr","Lawrencio",266.0,"actínido",10,17]
]

# Colores para las categorías
colores = {
    "no metal": "#4CAF50",
    "gas noble": "#FF9800",
    "metal alcalino": "#F44336",
    "alcalinotérreo": "#FF5722",
    "transición": "#2196F3",
    "post-transición": "#0373F4",
    "metaloide": "#8BC34A",
    "halógeno": "#E91E63",
    "lantánido": "#9C27B0",
    "actínido": "#673AB7",
    "desconocido": "#607D8B"
}

class TablaPeriodicaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabla Periódica Interactiva")
        self.root.configure(bg="#263238")
        
        # Dimensiones de la celda
        self.cw = 62
        self.ch = 62
        self.fuente_texto = ("Segoe UI", 10)
        self.fuente_texto_negrita = ("Segoe UI Semibold", 10)
        self.fuente_boton = ("Segoe UI Semibold", 9)
        self.fuente_titulo = ("Segoe UI Semibold", 21)

        self.contenedor = tk.Frame(root, bg="#263238")
        self.contenedor.grid_columnconfigure(0, weight=1)
        self.contenedor.grid_rowconfigure(0, weight=1)
        self.contenedor.grid_rowconfigure(2, weight=1)
        self.panel_principal = tk.Frame(self.contenedor, bg="#263238")
        self.panel_principal.grid(row=1, column=0)
        
        # Crear lienzo (Canvas)
        self.canvas = tk.Canvas(self.panel_principal, width=18*self.cw + 20, height=11*self.ch + 100, bg="#263238", highlightthickness=0)
        self.canvas.pack(padx=10, pady=(22, 8))

        self.controls = tk.Frame(self.panel_principal, bg="#263238")
        self.controls.pack(pady=(2, 12))
        tk.Label(self.controls, text="Buscar", bg="#263238", fg="#CFD8DC", font=self.fuente_texto_negrita).pack(side="left", padx=(0, 7))
        self.busqueda = tk.StringVar()
        entrada = tk.Entry(self.controls, textvariable=self.busqueda, width=24, font=self.fuente_texto, bg="#FAFAFA", fg="#263238", relief="flat", highlightthickness=2, highlightbackground="#455A64", highlightcolor="#29B6F6")
        entrada.pack(side="left")
        entrada.bind("<Return>", self.buscar_elemento)
        self.crear_boton(self.controls, "Buscar", self.buscar_elemento, "#1976D2").pack(side="left", padx=(6, 3))
        self.crear_boton(self.controls, "Limpiar", self.limpiar_filtro, "#546E7A").pack(side="left", padx=3)
        self.texto_comparar = tk.StringVar(value="Comparar")
        self.crear_boton(self.controls, self.texto_comparar, self.alternar_comparacion, "#7E57C2").pack(side="left", padx=3)
        self.texto_favorito = tk.StringVar(value="☆ Favorito")
        self.crear_boton(self.controls, self.texto_favorito, self.alternar_favorito, "#F9A825", "#263238").pack(side="left", padx=3)
        self.texto_tema = tk.StringVar(value="Tema claro")
        self.crear_boton(self.controls, self.texto_tema, self.cambiar_tema, "#00897B").pack(side="left", padx=3)
        self.texto_sonido = tk.StringVar(value="🔊 Sonido")
        self.crear_boton(self.controls, self.texto_sonido, self.alternar_sonido, "#455A64").pack(side="left", padx=3)
        self.escala = tk.StringVar(value="Colores: categorías")
        opciones = tk.OptionMenu(self.controls, self.escala, "Colores: categorías", "Escala: masa", "Escala: número atómico", "Estado físico")
        opciones.configure(font=self.fuente_texto_negrita, bg="#37474F", fg="white", activebackground="#546E7A", activeforeground="white", relief="flat", bd=0, highlightthickness=0, padx=9, pady=4)
        opciones["menu"].configure(font=self.fuente_texto, bg="#FAFAFA", fg="#263238", activebackground="#CFD8DC")
        opciones.pack(side="left", padx=(5, 0))

        self.resultados = tk.Listbox(self.panel_principal, height=5, width=42, activestyle="none")
        self.resultados.bind("<<ListboxSelect>>", self.seleccionar_resultado)
        self.busqueda.trace_add("write", self.actualizar_resultados)

        self.info = tk.StringVar(value="Haz clic en un elemento para ver su información.")
        self.info_label = tk.Label(root, textvariable=self.info, bg="#37474F", fg="white", font=self.fuente_texto_negrita, padx=12, pady=9)
        self.info_label.pack(side="bottom", fill="x")
        self.contenedor.pack(expand=True, fill="both")
        
        # Título
        self.titulo_canvas = self.canvas.create_text((18*self.cw + 20)/2, 18, text="Tabla Periódica de los Elementos", fill="white", font=self.fuente_titulo)
        
        # Diccionario para guardar los IDs de los rectángulos y asociarlos a los elementos
        self.rectangulos = {}
        self.textos_elementos = {}
        self.leyenda_items = {}
        self.estrellas = {}
        self.textos_leyenda = []
        self.hovered_rect = None
        self.selected_rect = None
        self.filtro_categoria = None
        self.preview = None
        self.detalle_popup = None
        self.resultados_busqueda = []
        self.favoritos = set()
        self.comparacion = []
        self.tema_oscuro = True
        self.sonidos_activos = True
        self.ruta_sonido = os.path.join(os.path.dirname(__file__), "hover_sonido.wav")
        self.escala.trace_add("write", self.aplicar_escala)
        
        self.dibujar_tabla()
        self.dibujar_leyenda()
        
        # Eventos del ratón
        self.canvas.bind("<Motion>", self.on_hover)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Leave>", self.on_leave)
        self.root.bind("<Left>", lambda event: self.mover_seleccion("izquierda"))
        self.root.bind("<Right>", lambda event: self.mover_seleccion("derecha"))
        self.root.bind("<Up>", lambda event: self.mover_seleccion("arriba"))
        self.root.bind("<Down>", lambda event: self.mover_seleccion("abajo"))
        self.root.bind("<Return>", self.abrir_seleccion)

    def crear_boton(self, parent, texto, comando, color, texto_color="white"):
        opciones = {"command": comando, "font": self.fuente_boton, "bg": color, "fg": texto_color}
        if isinstance(texto, tk.StringVar):
            opciones["textvariable"] = texto
        else:
            opciones["text"] = texto
        return tk.Button(parent, **opciones, activebackground="#263238", activeforeground="white", relief="flat", bd=0, cursor="hand2", padx=10, pady=5, highlightthickness=0)

    def dibujar_tabla(self):
        offset_x = 10
        offset_y = 50
        
        for el in elementos:
            z, sym, nombre, masa, cat, fila, col = el
            x1 = offset_x + (col - 1) * self.cw
            y1 = offset_y + (fila - 1) * self.ch
            x2 = x1 + self.cw - 2
            y2 = y1 + self.ch - 2
            
            color = colores.get(cat, "#607D8B")
            
            # Dibujar rectángulo
            rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#37474F", width=2)
            
            # Dibujar textos (Número atómico y Símbolo)
            numero = self.canvas.create_text(x1 + 5, y1 + 3, text=str(z), anchor="nw", fill="white", font=("Segoe UI", 8))
            simbolo = self.canvas.create_text((x1+x2)/2, (y1+y2)/2 + 5, text=sym, fill="white", font=("Segoe UI Semibold", 16))
            estrella = self.canvas.create_text(x2 - 4, y1 + 4, text="", anchor="ne", fill="#FFEB3B", font=("Segoe UI Semibold", 10))
            
            # Guardar relación
            self.rectangulos[rect] = el
            self.textos_elementos[rect] = (numero, simbolo)
            self.estrellas[rect] = estrella

    def dibujar_leyenda(self):
        offset_x = 10
        offset_y = 50 + 10 * self.ch + 20  # Debajo de lantánidos y actínidos
        x = offset_x
        y = offset_y
        max_x = 18 * self.cw + 20
        
        titulo = self.canvas.create_text(x, y, text="Leyenda", anchor="nw", fill="white", font=self.fuente_texto_negrita)
        self.textos_leyenda.append(titulo)
        y += 20
        x += 10
        
        for cat, color in colores.items():
            if x + 120 > max_x:
                x = offset_x + 10
                y += 25

            rect = self.canvas.create_rectangle(x, y, x+15, y+15, fill=color, outline="white")
            texto = self.canvas.create_text(x+20, y+7, text=cat.capitalize(), anchor="w", fill="white", font=("Segoe UI", 9))
            self.textos_leyenda.append(texto)
            self.leyenda_items[rect] = cat
            self.leyenda_items[texto] = cat
            x += 120

    def reproducir_sonido(self, tipo):
        if not self.sonidos_activos:
            return
        try:
            winsound.PlaySound(self.ruta_sonido, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
        except RuntimeError:
            pass

    def alternar_sonido(self):
        self.sonidos_activos = not self.sonidos_activos
        self.texto_sonido.set("🔊 Sonido" if self.sonidos_activos else "🔇 Silencio")
        self.info.set("Sonidos activados." if self.sonidos_activos else "Sonidos desactivados.")

    def estado_fisico(self, sym):
        if sym in {"H", "He", "N", "O", "F", "Ne", "Cl", "Ar", "Kr", "Xe", "Rn", "Og"}:
            return "Gas"
        if sym in {"Br", "Hg"}:
            return "Líquido"
        if sym in {"At", "Ts"}:
            return "Desconocido"
        return "Sólido"

    def color_escala(self, valor, minimo, maximo):
        proporcion = 0 if maximo == minimo else (valor - minimo) / (maximo - minimo)
        rojo = int(52 + 200 * proporcion)
        azul = int(220 - 160 * proporcion)
        return f"#{rojo:02X}70{azul:02X}"

    def aplicar_escala(self, *args):
        modo = self.escala.get()
        self.filtro_categoria = None
        masas = [el[3] for el in elementos]
        numeros = [el[0] for el in elementos]
        colores_estado = {"Gas": "#90CAF9", "Líquido": "#4DD0E1", "Sólido": "#A5D6A7", "Desconocido": "#B0BEC5"}

        for rect, el in self.rectangulos.items():
            if modo == "Escala: masa":
                color = self.color_escala(el[3], min(masas), max(masas))
            elif modo == "Escala: número atómico":
                color = self.color_escala(el[0], min(numeros), max(numeros))
            elif modo == "Estado físico":
                color = colores_estado[self.estado_fisico(el[1])]
            else:
                color = colores.get(el[4], "#607D8B")
            self.canvas.itemconfig(rect, fill=color)
            for texto in self.textos_elementos[rect]:
                self.canvas.itemconfig(texto, fill="white")
            self.restaurar_rectangulo(rect)

    def actualizar_favorito(self):
        if not self.selected_rect:
            self.texto_favorito.set("☆ Favorito")
            return
        z = self.rectangulos[self.selected_rect][0]
        self.texto_favorito.set("★ Quitar favorito" if z in self.favoritos else "☆ Favorito")

    def alternar_favorito(self):
        if not self.selected_rect:
            self.info.set("Selecciona primero un elemento.")
            return
        z = self.rectangulos[self.selected_rect][0]
        if z in self.favoritos:
            self.favoritos.remove(z)
            self.canvas.itemconfig(self.estrellas[self.selected_rect], text="")
            self.info.set("Elemento eliminado de favoritos.")
        else:
            self.favoritos.add(z)
            self.canvas.itemconfig(self.estrellas[self.selected_rect], text="★")
            self.info.set("Elemento añadido a favoritos.")
        self.actualizar_favorito()
        self.reproducir_sonido("clic")

    def alternar_comparacion(self):
        self.comparacion = []
        activo = self.texto_comparar.get() == "Comparar"
        self.texto_comparar.set("Cancelar comparación" if activo else "Comparar")
        self.info.set("Selecciona dos elementos para compararlos." if activo else "Comparación cancelada.")

    def mostrar_comparacion(self):
        primero, segundo = self.comparacion
        a = self.rectangulos[primero]
        b = self.rectangulos[segundo]
        ventana = tk.Toplevel(self.root)
        ventana.title("Comparación de elementos")
        ventana.configure(bg="#37474F")
        ventana.resizable(False, False)
        encabezado = f"{a[1]} — {a[2]}".ljust(28) + f"{b[1]} — {b[2]}"
        texto = (
            f"{encabezado}\n\n"
            f"Número atómico: {a[0]:<12} {b[0]}\n"
            f"Masa atómica: {a[3]:<14} {b[3]}\n"
            f"Categoría: {a[4]:<17} {b[4]}\n"
            f"Estado físico: {self.estado_fisico(a[1]):<13} {self.estado_fisico(b[1])}\n"
            f"Período / grupo: {a[5]} / {a[6]:<12} {b[5]} / {b[6]}"
        )
        tk.Label(ventana, text=texto, bg="#37474F", fg="white", font=("Courier New", 11), justify="left", padx=20, pady=20).pack()
        tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=(0, 15))

    def cambiar_tema(self):
        self.tema_oscuro = not self.tema_oscuro
        fondo = "#263238" if self.tema_oscuro else "#ECEFF1"
        texto = "white" if self.tema_oscuro else "#263238"
        panel = "#37474F" if self.tema_oscuro else "#CFD8DC"
        self.root.configure(bg=fondo)
        self.contenedor.configure(bg=fondo)
        self.panel_principal.configure(bg=fondo)
        self.controls.configure(bg=fondo)
        self.info_label.configure(bg=panel, fg=texto)
        self.resultados.configure(bg="white", fg="#263238")
        self.canvas.configure(bg=fondo)
        self.canvas.itemconfig(self.titulo_canvas, fill=texto)
        for item in self.textos_leyenda:
            self.canvas.itemconfig(item, fill=texto)
        for widget in self.controls.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=fondo, fg=texto)
        self.texto_tema.set("Tema oscuro" if not self.tema_oscuro else "Tema claro")

    def mover_seleccion(self, direccion):
        if not self.selected_rect:
            self.seleccionar_elemento(next(iter(self.rectangulos)))
            return
        actual = self.rectangulos[self.selected_rect]
        fila, col = actual[5], actual[6]
        candidatos = []
        for rect, el in self.rectangulos.items():
            diferencia_fila = abs(el[5] - fila)
            diferencia_col = abs(el[6] - col)
            if direccion == "izquierda" and el[6] < col:
                candidatos.append((diferencia_col * 10 + diferencia_fila, rect))
            elif direccion == "derecha" and el[6] > col:
                candidatos.append((diferencia_col * 10 + diferencia_fila, rect))
            elif direccion == "arriba" and el[5] < fila:
                candidatos.append((diferencia_fila * 10 + diferencia_col, rect))
            elif direccion == "abajo" and el[5] > fila:
                candidatos.append((diferencia_fila * 10 + diferencia_col, rect))
        if candidatos:
            self.seleccionar_elemento(min(candidatos, key=lambda item: item[0])[1])

    def abrir_seleccion(self, event=None):
        if self.selected_rect:
            self.mostrar_detalles(self.rectangulos[self.selected_rect])

    def restaurar_rectangulo(self, rect):
        if rect == self.selected_rect:
            self.canvas.itemconfig(rect, outline="#FFFFFF", width=4)
        else:
            self.canvas.itemconfig(rect, outline="#37474F", width=2)

    def seleccionar_elemento(self, rect):
        anterior = self.selected_rect
        self.selected_rect = rect
        if anterior and anterior != rect:
            self.restaurar_rectangulo(anterior)
        self.restaurar_rectangulo(rect)
        self.actualizar_favorito()
        self.reproducir_sonido("clic")
        if self.texto_comparar.get() == "Cancelar comparación":
            if rect not in self.comparacion:
                self.comparacion.append(rect)
            if len(self.comparacion) == 2:
                self.mostrar_comparacion()
                self.comparacion = []
                self.texto_comparar.set("Comparar")
            else:
                self.info.set("Selecciona un segundo elemento para compararlo.")
        else:
            self.mostrar_detalles(self.rectangulos[rect])

    def buscar_elemento(self, event=None):
        termino = self.busqueda.get().strip().casefold()
        if not termino:
            self.info.set("Escribe un nombre, símbolo o número atómico.")
            return

        for rect, el in self.rectangulos.items():
            z, sym, nombre = el[:3]
            if termino in str(z) or termino in sym.casefold() or termino in nombre.casefold():
                self.seleccionar_elemento(rect)
                self.canvas.focus_set()
                return

        self.info.set("No se encontró ningún elemento con esa búsqueda.")

    def actualizar_resultados(self, *args):
        termino = self.busqueda.get().strip().casefold()
        self.resultados.delete(0, tk.END)
        self.resultados_busqueda = []

        if not termino:
            self.resultados.pack_forget()
            return

        for rect, el in self.rectangulos.items():
            z, sym, nombre = el[:3]
            if termino in str(z) or termino in sym.casefold() or termino in nombre.casefold():
                self.resultados_busqueda.append((rect, el))

        for _, el in self.resultados_busqueda[:6]:
            self.resultados.insert(tk.END, f"{el[1]} — {el[2]} ({el[0]})")

        if self.resultados_busqueda:
            self.resultados.pack(pady=(0, 8))
        else:
            self.resultados.pack_forget()

    def seleccionar_resultado(self, event=None):
        seleccion = self.resultados.curselection()
        if not seleccion:
            return

        rect, el = self.resultados_busqueda[seleccion[0]]
        self.busqueda.set(el[1])
        self.resultados.pack_forget()
        self.seleccionar_elemento(rect)
        self.canvas.focus_set()

    def limpiar_filtro(self):
        self.filtro_categoria = None
        self.busqueda.set("")
        self.aplicar_escala()
        self.info.set("Filtro eliminado. Haz clic en un elemento para ver su información.")

    def ocultar_preview(self):
        if self.preview:
            self.preview.destroy()
            self.preview = None

    def cerrar_detalle(self):
        if self.detalle_popup:
            self.detalle_popup.destroy()
            self.detalle_popup = None

    def mostrar_preview(self, rect, event):
        self.ocultar_preview()
        z, sym, nombre, masa, cat, fila, col = self.rectangulos[rect]
        color = colores.get(cat, "#607D8B")
        self.preview = tk.Toplevel(self.root)
        self.preview.overrideredirect(True)
        self.preview.configure(bg="#37474F")
        self.preview.attributes("-topmost", True)
        tk.Label(self.preview, text=sym, font=("Segoe UI Semibold", 28), bg="#37474F", fg=color).pack(padx=14, pady=(8, 0))
        tk.Label(self.preview, text=f"{nombre}\nN.º atómico: {z} | {masa} u", font=("Segoe UI", 10), bg="#37474F", fg="white", justify="center").pack(padx=14, pady=(0, 8))
        self.preview.geometry(f"+{event.x_root + 16}+{event.y_root + 16}")

    def mostrar_detalles(self, el):
        z, sym, nombre, masa, cat, fila, col = el
        color = colores.get(cat, "#607D8B")
        estado = self.estado_fisico(sym)
        caracteristica = {
            "metal alcalino": "Familia reactiva, frecuente en sales.",
            "alcalinotérreo": "Metal reactivo usado en aleaciones y minerales.",
            "transición": "Metal con aplicaciones industriales y tecnológicas.",
            "no metal": "Elemento esencial en numerosos compuestos.",
            "gas noble": "Gas muy poco reactivo, usado en iluminación y tecnología.",
            "halógeno": "Elemento reactivo, presente en sales y desinfectantes.",
        }.get(cat, "Elemento con propiedades características de su familia.")
        self.ocultar_preview()

        if self.detalle_popup:
            self.cerrar_detalle()

        self.detalle_popup = tk.Toplevel(self.root)
        self.detalle_popup.title(f"Información: {nombre}")
        self.detalle_popup.geometry("380x330")
        self.detalle_popup.configure(bg="#37474F")
        self.detalle_popup.resizable(False, False)
        self.detalle_popup.transient(self.root)
        self.detalle_popup.protocol("WM_DELETE_WINDOW", self.cerrar_detalle)

        tk.Label(self.detalle_popup, text=sym, font=("Segoe UI Semibold", 54), bg="#37474F", fg=color).pack(pady=(15, 0))
        tk.Label(self.detalle_popup, text=nombre, font=("Segoe UI Semibold", 20), bg="#37474F", fg="white").pack()
        detalles = (
            f"Número atómico: {z}\nMasa atómica: {masa} u\n"
            f"Categoría: {cat.capitalize()}\nPeríodo: {fila} | Grupo: {col}\n"
            f"Estado físico: {estado}\n\n{caracteristica}"
        )
        tk.Label(self.detalle_popup, text=detalles, font=("Segoe UI", 11), bg="#37474F", fg="#CFD8DC", justify="left", wraplength=330).pack(pady=15)
        tk.Button(self.detalle_popup, text="Cerrar", command=self.cerrar_detalle, bg=color, fg="white", font=self.fuente_boton, relief="flat", bd=0, cursor="hand2").pack(pady=5, ipadx=20, ipady=6)

    def filtrar_categoria(self, categoria):
        self.filtro_categoria = None if self.filtro_categoria == categoria else categoria
        for rect, el in self.rectangulos.items():
            activo = self.filtro_categoria is None or el[4] == self.filtro_categoria
            color = colores.get(el[4], "#607D8B") if activo else "#455A64"
            texto_color = "white" if activo else "#90A4AE"
            self.canvas.itemconfig(rect, fill=color)
            for texto in self.textos_elementos[rect]:
                self.canvas.itemconfig(texto, fill=texto_color)
            self.restaurar_rectangulo(rect)
        if self.filtro_categoria:
            self.info.set(f"Filtro activo: {categoria.capitalize()}. Pulsa otra vez la categoría para quitarlo.")
        else:
            self.info.set("Filtro eliminado.")

    def on_hover(self, event):
        items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        nuevo_rect = None
        for item in items:
            if item in self.rectangulos:
                nuevo_rect = item
                break

        if nuevo_rect == self.hovered_rect:
            return

        if self.hovered_rect:
            self.restaurar_rectangulo(self.hovered_rect)

        self.hovered_rect = nuevo_rect
        self.ocultar_preview()

        if nuevo_rect:
            self.canvas.itemconfig(nuevo_rect, outline="#FFEB3B", width=4)
            self.canvas.configure(cursor="hand2")
            self.mostrar_preview(nuevo_rect, event)
            self.reproducir_sonido("hover")
        else:
            self.canvas.configure(cursor="")

    def on_leave(self, event):
        if self.hovered_rect:
            self.restaurar_rectangulo(self.hovered_rect)
            self.hovered_rect = None
        self.ocultar_preview()
        self.canvas.configure(cursor="")

    def on_click(self, event):
        items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        for item in items:
            if item in self.leyenda_items:
                self.filtrar_categoria(self.leyenda_items[item])
                return
            if item in self.rectangulos:
                self.seleccionar_elemento(item)
                break


if __name__ == "__main__":
    root = tk.Tk()
    app = TablaPeriodicaApp(root)
    root.mainloop()
