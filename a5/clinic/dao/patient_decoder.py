from json import JSONDecoder
from clinic.patient import Patient
""" PatientDecoder class that decodes and returns the patient in JSON format
"""
class PatientDecoder(JSONDecoder):

    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)
    
    def object_hook(self, patient_object):

        if "__type__" in patient_object and patient_object["__type__"] == "Patient":
            
            return Patient(
                patient_object["phn"],
                patient_object["name"],
                patient_object["birth_date"],
                patient_object["phone"], 
                patient_object["email"], 
                patient_object["address"],

                autosave = patient_object.get("autosave", False)

            )
        return patient_object