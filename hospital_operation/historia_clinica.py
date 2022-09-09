from hospital_system.database_service.generic_database import basic_database as pdb
from hospital_operation.citas import meet as mt

class historia(pdb):
    def create(self, data: list):
        meet = mt('hospital_system/database_service/base/cita.txt')
        if meet.check_meet(data[0]):
            return super().create(data)
        else:
            print('No se puede ingresar historia sin una cita')