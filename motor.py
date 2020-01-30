class Motor:
    def __init__(self,numero_de_serie,cilindrado):
        self.numero_de_serie=numero_de_serie
        self.cilindrado=cilindrado
        self.encendido=False

    def encender(self):
        if self.encendido==False:
            self.encendido=True
        else:
            print("el motor ya esta encendido")
    def apagar(self):
        self.encendido=False
    def esta_encendido(self):
        # if self.encendido==False:
        #     print("no")
        # else:
        #     print("si")
        return self.encendido

    def obtener_cilindrado(self):
        return self.cilindrado    
        