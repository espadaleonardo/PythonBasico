class Vehiculo: 

    FACTOR_EMISION_GASOLINA=2.196
    FACTOR_EMISION_DIESEL=2.471    

    def __init__ (self,placa,color,marca,modelo,combustible,km,tanque,ac):
        self.placa = placa 
        self.color = color
        self.modelo = modelo
        self.marca=marca
        self.combustible = combustible 
        self.km = km
        self.tanque = tanque
        self.ac = ac
        self.encendido = False
        self.litros_consumidos=0

    # def encender(self):
    #     if self.encendido==False:
    #         self.encendido=True
    #     else:
    #         print("el vehiculo ya esta encendido")

    # def apagar (self):
    #     self.encendido = False

    def tocar_bocina (self):
        print("pii pii")

    def frenar (self):
        print("frenando...")

    def obtener_combustible (self):
        return self.tanque

    def mostrar_vehiculo(self):
        print("Lamarca es" + self.marca)
        print("km"+ str(self.km))

    def cargar_combustible(self,litros):
        self.tanque+=litros
        print("cargando combustible")
    
    def recorrer_distancia(self,distancia):
        if self.motor.esta_encendido():
            if distancia< (self.tanque*self.obtener_variante() ):
                self.km+=distancia
                total_litros=round(distancia/self.obtener_variante(),2)
                self.tanque-=total_litros
                self.litros_consumidos+=total_litros
                print("recorriendo {} kilometros".format(distancia))
            else:
                print("no tiene combustible")
            print("el vehiculo ya esta encendido") 
        else:
            print("el vehiculo esta apagado")

    def calcular_co2(self):
        if self.combustible=="gasolina":
            return self.litros_consumidos*self.FACTOR_EMISION_GASOLINA
        else:
            return self.litros_consumidos*self.FACTOR_EMISION_DIESEL
    
    def poner_motor(self,motor):
        self.motor=motor

    def obtener_variante(self):
        cilindrada=self.motor.obtener_cilindrado()
        if cilindrada==1000:
            return 12
        elif cilindrada==2000:
            return 10
        else:
            return 8
    
    def hay_combustible(self,distancia):
        variante=self.obtener_variante()
        if not distancia<(variante*self.tanque):
            return False
        return True
    
    def obtener_informe(self):
        informe="\n---------------------------------------------"
        informe+="\nINFORME FINAL-EMISION DE DIOXIDO DE CARBONO"
        informe+="\n------------------"
        informe+="\n Usted esta conduciendo un vehiculo marca  {}, modelo {}, color {} ".format(self.marca, self.modelo, self.color) 
        informe+="\n Ha recorrido un total de {} km de distancia".format(self.km)
        informe+="\n Ha consumido un total de {} litros de {}".format(self.litros_consumidos, self.combustible)
        informe+="\n En su tanque tiene {} litros de {}".format(self.tanque,self.combustible)
        informe+="\n Se emitio a la atmosfera un total de {} kh de co2".format(round(self.calcular_co2(),2))
        return informe