from hospital_system.database_service.patient import patient as pat
from hospital_system.database_service.doctor import doctor as doc
from hospital_operation.citas import meet as mt
from hospital_operation.historia_clinica import historia as ht

def main():
    patient = pat( 'hospital_system/database_service/base/patient.txt' )
    #patient.create(['1666666666', 'Alexander Calderon', '14/08/1993', 'alexander.calderon@udea.edu.co', '313500036'])
    #patient.read('1017208590')
    #patient.update('1231234',['1016548590','Santiago Echeverry','23/11/1989','el.mejor@udea.edu.co','3236253747'])
    #patient.delete('10348277737')

    doctor = doc('hospital_system/database_service/base/doctor.txt')
    #doctor.create(['102994666', 'Damian de Jesus', '01/01/1971', 'damian.hell@udea.edu.co', '3127463299', 'Pediatra', '7500000'])
    #doctor.read('52738494')
    #doctor.update('234566', ['Elkin Patarroyo','03/3/96','elkin.patarroyo@udea.edu.co','3154326746','Cirujano plastico','13000000'])
    #doctor.delete('52738494')

    meet = mt('hospital_system/database_service/base/cita.txt')
    #(id paciente, fecha cita, hora, id doctor, tipo de cita, estado cita 1 activa 0 para inactiva)
    #meet.create(['1666666666','9/09/2022','6:00 pm','234566','Aumento de busto','1'])
    #meet.check_meet('1216718055')
    #meet.read('1216718055')
    #meet.create(['1216718055','11/04/2023','4:00 pm','234566','Revision de rodilla','1'])
    #meet.update('1216718055',['1216718055','11/09/2022','8:00 am','52738494','Oscultacion','1'])

    historia = ht('hospital_system/database_service/base/historia.txt')
    #historia.create(['1666666666', 'Se hizo cirugia de busto con exito, tomar acetaminofen'])
    historia.read('1216718055')


if __name__ == "__main__":
    main()