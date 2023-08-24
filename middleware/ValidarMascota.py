def validarDatosMascota(nombre,edad,cedulaDelpropietario,especie,raza,peso):
    #validacion del nombre
    if nombre == None or nombre == "":
        print("nombre no valido")
        raise Exception("nombre no valido")
    
    #validacion de la edad 
    if edad == "" or edad == None:
        print("Edad no valida")
        raise Exception("Edad no valida")
    try:
        edad = int(edad)
    except:
        print("Edad no valida")
        raise Exception("edad debe ser entero")
    
    #validacion cedula
    if cedulaDelpropietario == "" or cedulaDelpropietario == None:
        print("Cedula no valido")
        raise Exception("cedula no valido")        
    try:
        cedulaDelpropietario = int(cedulaDelpropietario)
    except:
        print("Cedula debe ser entero")
        raise Exception("cedula debe ser entero")
    #
    if especie == None or especie == "":
        print("Especie no valido")
        raise Exception("Especie no valido")
    
    if raza == None or raza == "":
        print("Raza no valido")
        raise Exception("Raza no valido")
    
    #validacion Peso
    if peso == "" or peso == None:
        print("peso no valido")
        raise Exception("cedula no valido")        
    try:
        peso = float(peso)
    except:
        print("Cedula debe ser entero")
        raise Exception("cedula debe ser entero")
    

def buscarMascota(veterinaria,id):
    for mascota in veterinaria.mascotas:
        if mascota.id==id:
            return mascota
    raise Exception("no se entrego mascota")
    #Nota: no se deberia validar tambien en el ID pensando en el momento que se va a buscar una mascota 