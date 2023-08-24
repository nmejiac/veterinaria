# Importar archivos o funciones de otras carpetas
from models.modelo import Veterinaria, Persona, Mascota, Orden
from middleware import ValidarPersona
from middleware import ValidarMascota
from middleware import ValidarOrden
from datetime import datetime

#
veterinaria = Veterinaria()
administrador = Persona("Norbey", 123, 29, "Admin", "ncortes", "asdf123.")
veterinaria.personas.append(administrador)
print("agregamos al admin: "+str(veterinaria.personas[0].nombre))

# Clase 19 agosto
medico = Persona("medico", 1234, 123, "medico", "medico")
veterinaria.personas.append(medico)


def Medico(veterinaria):
    usuario = input("ingrese el usuario del Medico: ")
    password = input("Ingrese Password: ")
    
    sesion = inicioSession(veterinaria, usuario, password, "Admin") # Nota 22-08-2023 --> preguntar si esto debe cambiar por medico

    while sesion:
        print("ingrese 0 para cerrar sesion")
        print("ingrese 1 para agregar propietario de mascota")
        print("ingrese 2 para agregar  mascota")
        print("ingrese 3 para registrar Historia Clinica")
        opcionMed = input()
        #  Cerrar sesion
        if opcionMed == "0":
            print("cerrando sesion")
            sesion = False
        # Agregar Propietario
        elif opcionMed == "1":
            print("ingrese los datos del dueño")
            nombre = input("ingrese nombre de la persona")
            cedula = input("ingrese cedula de la persona")
            edad = input("ingrese edad de la persona")
            try:
                ValidarPersona.validarDatosPropietarioMascota(
                    nombre, cedula, edad)
                propietario = Persona(nombre, cedula, edad, None, None, None)
                ValidarPersona.validarPersonaUnica(veterinaria, propietario)
                veterinaria.personas.append(propietario)
                print("Se a registrado el dueño ")
            except:
                print("No se Registro el propietario  ")
                print(Exception)

        # Agregar Mascotas
        elif opcionMed == "2":
            print(" se registra mascota")
            nombre = input("ingrese nombre de la Mascota")
            cedulaDelpropietario = input("ingrese cedula del propietario")
            edad = input("ingrese la edad de la Mascota")
            idMascota = len(veterinaria.mascotas)
            especie = input("ingrese la especie de la Mascota")
            raza = input("ingrese la raza de la Mascota")
            caracteristicas = input("ingrese caracteristicas de la Mascota")
            peso = input("ingrese peso de la Mascota")
            try:
                ValidarMascota.validarDatosMascota(nombre,edad,cedulaDelpropietario,especie,raza,peso)
                ValidarPersona.buscarPersona(veterinaria,cedulaDelpropietario)
                mascota  = Mascota(nombre,cedulaDelpropietario,edad,idMascota,especie,raza,caracteristicas,peso)
                veterinaria.mascotas.append(mascota)
                veterinaria.historiaClinica[str(id)]={}
                print("se agrego la mascota")
            except:
                print("no se pudo registrar Mascota")
        #Historia Clinica
        elif opcionMed == "3":
            id = input("ingrese ID mascota ")
            if id not in veterinaria.historiaClinica:
                print("no existe una mascota con ese ID")
                continue
            historia = veterinaria.historiaClinica[id]
            fechaActual = datetime.now()
            mascota = ValidarMascota.buscarMascota(veterinaria,int(id))
            medico = ValidarPersona.buscarPersonaPorUsuario(veterinaria,usuario)
            historiaActual={
                "fecha":fechaActual,
                "medico":medico.usuario
            }
            sintomas= input("ingrese sintomas")
            historiaActual["sintomatologia"]=sintomas
            motivoConsulta= input("ingrese motivoConsulta")
            historiaActual["motivoConsulta"]=motivoConsulta
            diagnostico= input("ingrese diagnostico")
            historiaActual["sintomatologia"]=diagnostico

            ordenmed = input("Ingrese 1 si se genera orden de medicamento")
            if ordenmed=="1" :
                medicamento= input("ingrese nombre del medicamento ")
                dosis= input("ingrese dosis del medicamento ")
                orden = Orden(len(veterinaria.ordenes),mascota.id,mascota.cedulaPropietario,medico.cedula,medicamento + " "+ dosis,fechaActual)
                print("Orden creada")
                veterinaria.ordenes.append(orden)
                historiaActual["idOrden"] = orden.id
                historiaActual["Medicamento"] = medicamento
                historiaActual["dosis"] = dosis
                #
            prodnmed = input("Ingrese 1 si se Aplica Procedimiento")
            if prodnmed=="1" :
                historiaActual["procedimiento"] = input("Ingrese nombre del procedimiento")
                historiaActual["detalle procedimiento"] = input("Ingrese el detalle del procedimiento")
                historiaActual["anulacionOrden"] = False
                
                #
            historia[fechaActual]=historiaActual
            print("se a agregado la historia Clinica")
            #
        elif opcionMed == "4":
            id = input("ingrese ID mascota ")
            if id not in veterinaria.historiaClinica:
                print("no existe una mascota con ese ID")
                continue
            orden = input ("ingrese el id de la orden")
            orden = ValidarOrden.burcarOrden(veterinaria,str(orden))
            if orden == False:
                print("no existe una orden con ese ID")
                continue
            if orden.fecha in veterinaria.historiaClinica[id]:
                print("la orden no corresponde a la mascota")
                continue
            veterinaria.historiaClinica[id][orden.fecha]["anulacionOrden"] = True






def Administrador(veterinaria):
    usuario = input("ingrese el usuario del administrador: ")
    password = input("Ingrese Password: ")
    sesion = inicioSession(veterinaria, usuario, password, "Admin")
    while sesion:
        print("ingrese 1 para agregar medico")
        print("ingrese 2 para agregar vendedor")
        print("ingrese 3 cerrar session")
        opcionAdm = input()
        if opcionAdm == "1":
            print("se desea crear Medico")
            nombreMedico = input("Ingrese el nombre del medico: ")
            edadMedico = input("Ingrese la edad del medico: ")
            cedulaMedico = input("Ingrese la cedula del medico: ")
            usuarioMedico = input("Ingrese el Usaurio del medico: ")
            passwordMedico = input("Ingrese la contraseña del medico: ")
            try:
                ValidarPersona.validarDatosUsuario(
                    nombreMedico, edadMedico, cedulaMedico, "medico", usuarioMedico, passwordMedico)
                medico = Persona(nombreMedico, edadMedico, cedulaMedico,
                                 "medico", usuarioMedico, passwordMedico)
                ValidarPersona.validarPersonaUnica(veterinaria, medico)
                veterinaria.personas.append(medico)
                print("Se creo el Medico Correctamente\n")
                print(str(medico))

            except:
                print("No se creo el Medico ")
                print(Exception)

        elif opcionAdm == "2":
            print("se desea crear un nuevo vendedor")
            nombreVendedor = input("Ingrese el nombre del vendedor: ")
            edadVendedor = input("Ingrese la edad del vendedor: ")
            cedulaVendedor = input("Ingrese la cedula del vendedor: ")
            usuarioVendedor = input("Ingrese el Usaurio del vendedor: ")
            passwordVendedor = input("Ingrese la contraseña del vendedor: ")
            try:
                ValidarPersona.validarDatosUsuario(
                    nombreVendedor, edadVendedor, cedulaVendedor, "vendedor", usuarioVendedor, passwordVendedor)
                vendedor = Persona(nombreVendedor, edadVendedor, cedulaVendedor,
                                   "vendedor", usuarioVendedor, passwordVendedor)
                ValidarPersona.validarPersonaUnica(veterinaria, vendedor)
                veterinaria.personas.append(vendedor)
                print("Se creo el vendedor Correctamente")
            except Exception:
                print("No se creo el vendedor ")
                print(Exception)

        elif opcionAdm == "3":
            print("salir")
            sesion = False
        else:
            print("Opcion no valida")
    return


def inicioSession(veterinaria, usuario, password, rol):
    for persona in veterinaria.personas:
        if persona.usuario == usuario and persona.password == password and persona.rol == rol:
            print("ha iniciado sesion")
            return True
    print("")
    return False


while True:
    print("Menu Principal\n")
    print("Ingrese 1 para iniciar sesion como administrador")
    print("ingrese 4 para salir")
    opcion = input()
    if opcion == "1":
        Administrador(veterinaria)
    elif opcion == "4":
        break
    else:
        print("opcion no valida")
