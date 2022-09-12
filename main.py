from pdb import Pdb
from hospital_system.database_service.patient import patient as pat
from hospital_system.database_service.doctor import doctor as doc
from hospital_operation.citas import meet as mt
from hospital_operation.historia_clinica import historia as ht

def main():

    #El objeto patient interactua con el archivo de texto en la ruta especificada
    patient = pat( 'hospital_system/database_service/base/patient.txt' )

    #La siguiente linea crea un paciente, la informacion se ingresa así: 
    #[identificacion, nombre, fecha de nacimiento, email, telefono]
    #patient.create(['123456789', 'Paciente Piloto', '25/03/1980', 'paciente.piloto@udea.edu.co', '3135784623'])
    

    #la siguiente linea lee si un paciente existe en el hospital ingresando su documento
    #patient.read('1017208590')

    #La siguiente linea actualiza un paciente, primero con la identificacion y luego 
    #con toda la informacion del paciente.
    #patient.update('1231234',['1016548590','Santiago Echeverry','23/11/1989','el.mejor@udea.edu.co','3236253747'])
    
    #La siguiente linea elimina un paciente.
    #patient.delete('10348277737')

    doctor = doc('hospital_system/database_service/base/doctor.txt')

    #Las sigiuentes lineas hacen lo mismo que las lineas anteriores pero con los doctores
    #la informacion se maneja así: [identificacion, nombre, fecha de nacimiento, email, telefono, especialidad, salario]

    #doctor.create(['102994666', 'Damian de Jesus', '01/01/1971', 'damian.hell@udea.edu.co', '3127463299', 'Pediatra', '7500000'])
    #doctor.read('52738494')
    #doctor.update('234566', ['Elkin Patarroyo','03/3/96','elkin.patarroyo@udea.edu.co','3154326746','Cirujano plastico','13000000'])
    #doctor.delete('52738494')

    meet = mt('hospital_system/database_service/base/cita.txt')

    #Para las citas se usa la siguiente forma:
    #[id paciente, fecha cita, hora, id doctor, tipo de cita, estado cita 1 activa 0 para inactiva]
    
    #meet.create(['1666666666','9/09/2022','6:00 pm','234566','Aumento de busto','1'])
    #meet.check_meet('1216718055')
    #meet.read('1216718055')
    #meet.create(['1216718055','11/04/2023','4:00 pm','234566','Revision de rodilla','1'])
    #meet.update('1216718055',['1216718055','11/09/2022','8:00 am','52738494','Oscultacion','1'])

    historia = ht('hospital_system/database_service/base/historia.txt')
    
    #Para las historias clinicas se usa la siguiente forma:
    #[identificacion del paciente, informacion de la cita]

    #historia.create(['1666666666', 'Se hizo cirugia de busto con exito tomar acetaminofen'])
    #historia.read('1216718055')

    #Las siguientes lineas brindan la informacion de cada objeto
    #help(Pdb)
    #help(doc)
    #help(pat)
    #help(mt)
    #help(ht)

if __name__ == "__main__":
    main()