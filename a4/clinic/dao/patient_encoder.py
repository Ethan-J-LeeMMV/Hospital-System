from json import JSONEncoder
from clinic.patient import Patient 

class PatientEncoder(JSONEncoder): 
    """encodes PatientDao into JSON file"""

    def default(self, patient_object):
        if isinstance(patient_object, Patient):
            return {"__type__": "Patient", "phn": patient_object.phn, 
                    "name": patient_object.name, 
                    "birth_date": patient_object.birth_date, 
                    "phone": patient_object.phone, 
                    "email": patient_object.email, 
                    "address": patient_object.address, 
                    "autosave": patient_object.autosave}
        
        return