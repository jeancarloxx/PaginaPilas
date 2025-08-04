class Navegador:
    def __init__(self):
        self.pagina_actual= None
        self.pila_atras = [] #creacion de pila 
        self.pila_siguiente = [] #creacion de pila

    def carga(self, url):
        if self.pagina_actual:
          self.pila_atras.append(self.pagina_actual)
        self.pagina_actual= url
        self.pila_siguiente.clear()
        print(f"Página cargada: {self.pagina_actual}")

    def regresar(self):
        if not self.pila_atras:
            print("No hay páginas anteriores.")
            return
        self.pila_siguiente.append(self.pagina_actual)
        self.pagina_actual = self.pila_atras.pop()
        print(f"Retrocediste a: {self.pagina_actual}")

    def adelante(self):
        if not self.pila_siguiente:
            print("No hay páginas siguientes.")
            return
        self.pila_atras.append(self.pagina_actual)
        self.pagina_actual = self.pila_siguiente.pop()
        print(f"Avanzaste a: {self.pagina_actual}")
        
navegador = Navegador()

# Paso 1: Cargas página1
navegador.carga("pagina1")

# Paso 2: Cargas página2
navegador.carga("pagina2")

# Paso 3: Cargas página3
navegador.carga("pagina3")

# Paso 4: Retrocedes a página2
navegador.regresar()

# Paso 5: Retrocedes a página1
navegador.regresar()

# Paso 6: Avanzas a página2
navegador.adelante()

# Paso 7
navegador.carga("pagina4")

# Paso 8: Retrocedes a página2
navegador.regresar()