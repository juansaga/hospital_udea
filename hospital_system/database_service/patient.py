from asyncio import format_helpers
from doctest import ELLIPSIS_MARKER
from hospital_system.database_service.generic_database import basic_database as pdb

class patient(pdb):
    def patient_exist(self, id):
        if self.read(id):
            print('El paciente existe')
            return True
        else:
            print('El paciente no existe')
            return False