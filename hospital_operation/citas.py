from tabnanny import check
from hospital_system.database_service.generic_database import basic_database as pdb

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
        if self.check_meet(data[0]):
            print('El paciente ya tiene cita activa')
        else:
            return super().create(data)