from turtle import update
from hospital_system.database_service.generic_database import basic_database as pdb
from hospital_operation.citas import meet as mt

class historia(pdb):
    """
    Crud para manejo de las historias clinicas
    """
    def create(self, data: list):
        meet = mt('hospital_system/database_service/base/cita.txt')
        if meet.check_meet(data[0]):
            with open(meet.database_name, "r") as datos:
                valores = []
                count = 0
                for linea in datos:
                    valores.append([x for x in linea.strip().split(",")])
                    if data[0] == valores[count][0] and valores[count][5] == '1':
                        cita = valores[count]
                        cita[5] = '0'
                        break
                    count += 1
            
            datos.close()

            meet.update(data[0],cita)
            data.append(cita[1])

            return super().create(data)
        else:
            print('No se puede ingresar historia sin una cita')

    def read(self, id):
        with open(self.database_name, "r") as datos:
            valores = []
            count = 0
            hist = []
            for linea in datos:
                valores.append([x for x in linea.strip().split(",")])
                if id == valores[count][0]:
                    hist.append(valores[count])
                count += 1
        datos.close()
        if hist == []:
            print('El paciente no existe o no tiene historia')
        else:
            print(hist)