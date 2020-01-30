class Calculadora:
    def __init__(self,numero1,numero2):
        self.numero1=numero1
        self.numero2=numero2
    
    def sumar(self):
        try:
            r=self.numero1+self.numero2
            print("la suma del numero {} y el numero {} es {} ".format(self.numero1, self.numero2, r))
        except TypeError:
            print("tipo de dato debe ser numerico")
        except:
            print("error al dividir")

    def restar(self):
        try:
            resp=self.numero1-self.numero2
            print("la resta del numero {} y el numero {} es {} ".format(self.numero1, self.numero2, resp))
        except TypeError:
            print("tipo de dato debe ser numerico")
        except:
            print("error al dividir")

    def multiplicar(self):
        try:
            s=self.numero1*self.numero2
            print("la multiplicacion del numero {} y el numero {} es {} ".format(self.numero1, self.numero2, s))
        except TypeError:
            print("tipo de dato debe ser numerico")
        except:
            print("error al dividir")

    def dividir(self):
        try:
            solu=self.numero1/self.numero2
            print("la divicion del numero {} y el numero {} es {} ".format(self.numero1, self.numero2, solu))
        except ZeroDivisionError:
            print("no se puede dividir entre 0")
        except TypeError:
            print("tipo de dato debe ser numerico")
        except:
            print("error al dividir")

    def sacar_exponente(self):
        try:
            solucion=self.numero1**self.numero2
            print("el resultato de sacar exponente del numero {} y el numero {} es {} ".format(self.numero1, self.numero2, solucion))
        except TypeError:
            print("tipo de dato debe ser numerico")
        except:
            print("error al dividir")
