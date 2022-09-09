from hospital_system.database_service.patient import patient as pat
from hospital_system.database_service.doctor import doctor as doc
from hospital_operation.citas import meet as mt

def main():
    #patient = pat( 'hospital_system/database_service/base/patient.txt' )
    #patient.create(['10348277737', 'Diego Gallego', '12/05/1992', 'diego.gallego@udea.edu.co', '3204617377'])
    #patient.read('1017208590')
    #patient.update('1231234',['1016548590','Santiago Echeverry','23/11/1989','el.mejor@udea.edu.co','3236253747'])
    #patient.delete('10348277737')

    #doctor = doc('hospital_system/database_service/base/doctor.txt')
    #doctor.create(['52738494', 'Doctor Amor', '13/7o/1990', 'amor.tequiero@udea.edu.co', '63537449', 'Ginecologia', '4000000'])
    #doctor.read('52738494')
    #doctor.update('234566', ['Elkin Patarroyo','03/3/96','elkin.patarroyo@udea.edu.co','3154326746','Cirujano plastico','13000000'])
    #doctor.delete('52738494')

    meet = mt('hospital_system/database_service/base/cita.txt')
    #(id paciente, fecha cita, hora, id doctor, tipo de cita, estado cita 1 activa 0 para inactiva)
    meet.create(['1017240816','15/09/2022','5:00 pm','52738494','General','1'])
    #meet.check_meet('1017240816')
if __name__ == "__main__":
    main()