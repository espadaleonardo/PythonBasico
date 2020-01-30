from vehiculo import Vehiculo
from motor import Motor
from simulador import Simulador
from calculadora import Calculadora

motor1=Motor("R764",1000)
motor2=Motor("G76755",2000)

calcu=Calculadora(6,5)

yhe = Vehiculo("uhc456", "azul", "toyota", "2014", "gasoina", 1000, 78.5, True)
camion = Vehiculo("jfh323", "blanco", "suzuki", "2006", "diesel", 2000, 99.1, True)
carrera = Vehiculo("lol123", "rosa", "bugatti", "2004", "gas", 0, 45.5, False)

yhe.poner_motor(motor1)
camion.poner_motor(motor2)
carrera.poner_motor(motor2)


lista_vehiculos=[yhe, camion, carrera]
s=Simulador(lista_vehiculos)
#s.iniciar_simulacion(2)

calcu.sumar()
calcu.restar()
calcu.multiplicar()
calcu.dividir()
calcu.sacar_exponente()