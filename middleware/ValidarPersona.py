def validarDatosUsuario(nombre,edad,cedula,rol,usuario,password):
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
    if cedula == "" or cedula == None:
        print("Cedula no valido")
        raise Exception("cedula no valido")        
    try:
        cedula = int(cedula)
    except:
        print("Cedula debe ser entero")
        raise Exception("cedula debe ser entero")
    
    #validacion rol
    if rol != "medico" and rol != "vendedor":
        print("Rol no valido")
        raise Exception("El Rol solo puede ser medico o vendedor ")
    
    #validar usuario 
    if usuario == None or usuario == "":
        print("usuario no valido")
        raise Exception("usuario no valido")
    
    #Validar contraseña
    if password == None or password == "":
        print("Contraseña no valida")
        raise Exception("contraseña no valida")
    
# validar si el usuario ya existe
def validarPersonaUnica(veterinaria,nuevo):
    for persona in veterinaria.personas:
        if (persona.usuario==nuevo.usuario or persona.usuario != None) and persona.cedula==nuevo.cedula  :
            raise Exception("Los Datos estan duplicados")
        

# validar datos dueño mascota  creado Clase 19 agosto 

def validarDatosPropietarioMascota(nombre,cedula,edad):
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
    if cedula == "" or cedula == None:
        print("Cedula no valido")
        raise Exception("cedula no valido")        
    try:
        cedula = int(cedula)
    except:
        print("Cedula debe ser entero")
        raise Exception("cedula debe ser entero")
    
def buscarPersona(veterinaria,cedula):
    for persona in veterinaria.personas:
        if persona.cedula==cedula:
            return persona
    print ("persona no encontrada")
    raise Exception ("persona no encontrada")

def buscarPersonaPorUsuario (veterinaria,usuario):
    for persona in  veterinaria.personas:
        if persona.usuario == usuario:
            return persona
    raise Exception("no se encontro persona con el usuario ")