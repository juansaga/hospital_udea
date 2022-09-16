# hospital_udea
Modelo para el manejo de un sistema de citas e historia clinica de un hospital.

Los archivos de las bases de datos se encuentran en la carpeta hospital_system/base

Para interactuar con las bases de datos utilice el archivo main.py, en este archivo encontrará los siguientes comandos:

    patient.create()
    patient.read()
    patient.update()
    patient.delete()

    doctor.create()
    doctor.read()
    doctor.update()
    doctor.delete()

    meet.create()
    meet.read()
    meet.update()
    meet.delete()

    historia.create()
    historia.read()

Cada uno de estos tiene un argumento ejemplo que puede modificar, para ejecutarlos descomentelos, ingrese en el argumento la información, ejecute el archivo main.py y consulte la modificación en el archivo de texto correspondiente en la carpeta hospital_system/base.

Luego de instanciar cada objeto en el archivo se ecuentran comentarios en los cuales se especifica la forma en la que se debe ingresar la información en los argumentos de los métodos.

Las clases para las operaciones (citas e historias) se encuentran en la carpeta hospital_operation, las clases para los doctores, los pacientes y la clase padre se encuentran en la carpeta hospital_system/database_service.

Creación: Dynamic Script.

Comunicate con nosotros: jmanuel.sanchez@udea.edu.co

Creadores:
Alex Calderon

Mateo Martín 

Juan Sánchez
