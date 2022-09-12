from asyncio import format_helpers
from doctest import ELLIPSIS_MARKER
from hospital_system.database_service.generic_database import basic_database as pdb

class patient(pdb):
    """
    Crud para manejo de los pacientes
    """
    def patient_exist(self, id: str):
        """
        Args:
            id (str): identificacion del paciente       
        
        consulta si un paciente existe en la base de datos, retorna True si existe y False en caso contrario
        """
        if self.read(id):
            print('El paciente existe')
            return True
        else:
            print('El paciente no existe')
            return False