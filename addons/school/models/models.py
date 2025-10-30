# -*- coding: utf-8 -*-
from odoo import models, fields #Importación de paquetes (models y fields)

#Definicion de tabla
class Student(models.Model):   # Clase con nombre del modelo que en este caso se llamara "Student", y de variables models.Model la clase Model
    #Propiedades que quiero que tenga la clase "Student"
    _name = "school.student"                #Nombre del modelo, esto para un control interno
    _description = "Tabla de Estudiantes"   #Agregar una descripción al modelo 
    
    
    name = fields.Char(string="Nombre", required=True) #Campo en la interfaz va a tener un string que dira nombre y va a ser un campo requerido
    age = fields.Integer(string="Edad") #Campo en la interfaz que va a tener un string que dira edad


# Nota: estos modelos necesitan ser guardados a través de una interfaz y para eso tenemos la carpeta llamada views. En ella tenemos
# el archivo llamado templates y views, en nuestro caso el que nos importa es el llamado templates (que sera donde vamos a definir
# todo lo que se va a ver en pantalla) 


