#base_datos_Jason
import json
try:
    with open ("base_de_datos.jason", r) as archivo_db:
        print("Leyendo base de datos.....")
        lista_estudiantes=jason.load(archivo_db)
        print("Base de datos cargada exitosamente")
except:
    print("Creando nueva base de datos...")
    lista_estudiantes=[]

#calcular promedio
def calcular_promedio(lista_notas_estudiantes):
    total_suma=0
    for nota in lista_notas_estudiantes:
        total_suma = total_suma + nota
    cantidad_notas = len(lista_notas_estudiantes)
    promedio = total_suma / cantidad_notas
    prom=(("{:.2f}".format(promedio)))
    return prom

#ingresar usuario
def ingresar_alumno():
    #ingresar nombre
    nombre= str(input("Ingrese su nombre: "))
    #ingresar numero de carnet
    a=0
    while True:
        carnet=str(input("Ingrese numero de carnet: "))
        for i in lista_estudiantes:
            if carnet==i:
                print("Error de carnet")
                a=i
        if carnet!=a:
            break
    #ingresar nota
    lista_notas=[]
    opcion_notas=input("Desea ingresar una  nota? (y / n): ")
    while opcion_notas =='y' or opcion_notas== 'Y':
        nueva_nota=int(input("Ingrese la nota: "))
        lista_notas.append(nueva_nota)
        opcion_notas = input("Desea ingresar otra nota? (y / n): ")
    #Año de ingreso
    dig_carnet=str(input("Ingrese los primeros dos digitos de su numero de carnet "))
    dig_año="20"
    año=dig_año+dig_carnet
    #promedio del estudiante
    promedio_estudiante = calcular_promedio (lista_notas)
    #cantidad de cursos asignados
    cantidad_asignados = len(lista_notas)
    #cantidad de cursos aprobados
    mayores=0
    for i in lista_notas:
        if i>=61:
            mayores=mayores+1
    #porcentaje de cursos aprobados
    porcentaje=100*(mayores/cantidad_asignados)
    porc=(("{:.0f}".format(porcentaje)))
    #crear estudiante
    estudiante={  
        "nombre":nombre,
        "carnet":carnet,
        "notas":lista_notas,
        "año de ingreso": año,
        "promedio":promedio_estudiante,
        "cantidad_asignados":cantidad_asignados,
        "cantidad_aprobados": mayores,
        "porcentaje_aprobados":porc
    }
    lista_estudiantes.append(estudiante)
    return 

#Buscar usuario
def buscar_usuario(carnet):
    buscar = input('Ingrese el número de carnet del alumno: ')
    for estudiante in lista_estudiantes:
        if carnet == buscar:
            print(estudiante)
    print(estudiante)
    return

#listado de estudiantes
def listado_estudiantes():
    for i in (lista_estudiantes):
        print("Nombre: ", i['nombre'])
        print("Carnet: ", i['carnet'])
        print("Notas: ",i['notas'])
        print("Promedio: ",i['promedio'])
        print("Año de ingreso: ",i['año de ingreso'])
        print("Cantidad de cursos asignados: ", i['cantidad_asignados'])
        print("Cantidad de cursos aprobados: ", i['cantidad_aprobados'])
        print("Porcentajes de cursos aprobados: ", i['porcentaje_aprobados'],"%")
        print ("=================")    
    return 

#salir sin gradar
def salir_sin_guardar():
    salir_guardar = input('¿Desea salir y guardar?: (y/n)')
    if salir_guardar == 'y' or salir_guardar == 'Y':
        with open('base_datos.json', 'w') as archivo_db:
            print('Guardando en la base de datos')
            print('Guardado')
            print('¡Gracias por utilizar este programa!')
            json.dump(lista_estudiantes, archivo_db)
            exit()
    if salir_guardar == 'n' or salir_guardar == 'N':
        print('¡Gracias por utilizar este programa!')
        exit()
    salir_sin_guardar()

#menu navegacion 
def mostrar_menu () :
    mensaje_menu = """Ingrese la opcion deseada\n
    1.Ingresar usuario\n
    2.Buscar usuario\n 
    3.Mostrar listado de usuarios\n
    0.salir\n 
    >
    """
    opcion = input(mensaje_menu)
    opcion = int(opcion)
    if opcion==1:
        ingresar_alumno()
    if opcion==2:
        buscar_usuario(ingresar_alumno)
    if opcion==3:
        listado_estudiantes()
    if opcion==0:
        salir_sin_guardar()
    mostrar_menu()
    return
mostrar_menu()


