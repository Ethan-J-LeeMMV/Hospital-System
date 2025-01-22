from clinic.dao.patient_dao import PatientDAO

from clinic.exception.illegal_operation_exception import IllegalOperationException

from clinic.patient import Patient

from clinic.dao.patient_encoder import PatientEncoder 
from clinic.dao.patient_decoder import PatientDecoder

import json

class PatientDAOJSON(PatientDAO):
    def __init__(self, autosave):
        self.autosave = autosave
        self.filepath = "clinic/patients.json"
        self.patients = {}

        if self.autosave == True:
            self.patients = self.load_patients()


    def load_patients(self) -> dict[int, Patient]:

        patients = {}
        try: 
            with open(self.filepath, "r") as file:
                data = json.load(file, cls=PatientDecoder)
                for phn, patient in data.items():
                    patients[int(phn)] = patient
        
        except FileNotFoundError or EOFError or JSONDecodeError:
            patients = {}
        
        return patients
    
    """
    helper method to save patients 
    """
    def save_patients(self): 

        with open(self.filepath, "w") as file:
            json.dump(self.patients, file, cls=PatientEncoder)        

    def search_patient(self, key):
        if key in self.patients:
            return self.patients[key]
        else: 
            return None



    def create_patient(self, patient: Patient) -> Patient:
        phn = patient.phn
        self.patients[phn] = patient
        if self.autosave == True:
            self.save_patients()

        return patient


    def retrieve_patients(self, search_string: str):
        retrieved_list = []
        for phn in self.patients: 
            patient = self.patients[phn]
            patient_name = patient.get_name().lower()
            search_string = search_string.lower()

            if search_string in patient_name:
                retrieved_list.append(patient)
        
        return retrieved_list

    def update_patient(self, key, patient):
        
        if key not in self.patients:
            return False
        
        existing_patient = self.patients[key]
        existing_patient.name = patient.name
        existing_patient.birth_date = patient.birth_date
        existing_patient.phone = patient.phone
        existing_patient.email = patient.email
        existing_patient.address = patient.address

        return True

    def delete_patient(self, phn):
        if phn in self.patients:

            del self.patients[phn]
            if self.autosave == True:
                self.save_patients()
            
            return True

        return False

    def list_patients(self) -> list[Patient]:
        return list(self.patients.values())

