class Persona:
    def __init__(self,nombre,cedula,edad,rol, usuario,password):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad 
        self.rol = rol
        self.usuario = usuario 
        self.password = password


class Mascota:
    def __init__(self,nombre,cedulaDelpropietario, edad, id,especie,raza,caracteristicas,peso):
        self.nombre = nombre
        self.cedulaDelpropietario = cedulaDelpropietario
        self.edad = edad
        self.id = id
        self.especie = especie
        self.raza = raza
        self.caracteristicas = caracteristicas
        self.peso = peso

class Veterinaria:
    def __init__(self):
        self.personas=[]
        self.mascotas=[]
        self.ordenes=[]
        self.historiaCinica={}



class Orden:
    def __init__(self,id,idMascota,cedulaPropietario,cedulaMedico,nombreMedicamento,fecha):
        self.id = id
        self.idMascota = idMascota
        self.cedulaPropietario = cedulaPropietario
        self.cedulaMedico = cedulaMedico
        self.nombreMedicamento = nombreMedicamento
        self.fecha = fecha

