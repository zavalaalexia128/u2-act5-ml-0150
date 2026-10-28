import numpy as np
import pandas as pd
# Zavala Medina | NC= 0150 |Fecha 28 de Octubre 2026
## dato
datos_alumno =[
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas
df=pd.DataFrame(datos_alumno,columns=["ci","marca","paquete"])
print(df)
# datos a partir de un diccionario
datos_alumno={
    "nombre":["Daniel","Nieves","Hernandez","Iris","diego","Jazmin"],
    "calif":[60,90,100,80,70,50],
    "edad":[64,15,16,16,18,14]
}
estudiantes = pd.DataFrame(datos_alumno)
print(estudiantes)

print("Programa Realizado por Zavala Medina Alexia | NC= 0150")
