from tabnanny import check
from hospital_system.database_service.generic_database import basic_database as pdb
from hospital_system.database_service.patient import patient as pat

class meet(pdb):
    def check_meet(self, id):
        with open(self.database_name, "r") as datos:
            valores = []
            count = 0
            for linea in datos:
                valores.append([x for x in linea.strip().split(",")])
                if id == valores[count][0] and bool(valores[count][5]):
                    print(f'La persona tiene cita activa para el día {valores[count][1]} a las {valores[count][2]}')
                    datos.close()
                    return True
                count += 1
        datos.close()
        return False
    
    def create(self, data: list):
        patient = pat( 'hospital_system/database_service/base/patient.txt' )
        if patient.patient_exist(data[0]):
            if self.check_meet(data[0]):
                print('El paciente ya tiene cita activa')
            else:
                return super().create(data)
        else: 
            print('El paciente no existe, por favor creelo.')
    

    def read(self, id):
        if self.check_meet(id) != True:
            print('El paciente no tiene cita activa')
