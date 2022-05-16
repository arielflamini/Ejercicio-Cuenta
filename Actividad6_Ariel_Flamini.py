#Link Colab: https://colab.research.google.com/drive/1vWn_ebnfmEg0YCyrI6FOCwr4XPPdl_PR?usp=sharing
class AnimalMarino():
    def __init__(self, cant_aletas, color):
        self.cant_aletas = cant_aletas
        self.color = color

    def habitat(self):
       return print("El mar")

class Mamifero():
    def __init__(self, cant_mamas, cant_patas):
        self.cant_mamas = cant_mamas
        self.cant_patas = cant_patas
    
    def vive_con_mama(self):
        return print("Verdad")

class Cetaceo(AnimalMarino, Mamifero):
    def __init__(self, cant_aletas, color, cant_mamas, cant_patas, peso, nombre):
        AnimalMarino.__init__(self, cant_aletas, color)
        Mamifero.__init__(self, cant_mamas, cant_patas)
        self.peso = peso
        self.nombre = nombre
    
    def vive_con_hermanos(self):
        return print("Verdad")
    
    def mostrar_datos(self):
        return print(f'El Cetáceo {self.nombre} tiene {self.cant_aletas} aletas, es de color {self.color}, tiene {self.cant_mamas} mamas, tiene {self.cant_patas} patas y pesa {self.peso} kg')
    
cetaceo1 = Cetaceo(2, "Marron", 4, 0, 800, "Miguel")
cetaceo1.mostrar_datos()

    
   



