from clinic.patient_record import PatientRecord
class Patient:

    def __init__(self, phn, name, birth_date, phone, email, address, autosave=True):
        self.phn = phn
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self. email = email
        self.address = address
        self.autosave = autosave
        self.record = PatientRecord(phn, self.autosave)


    def __eq__(self, other):
        return ((self.phn == other.phn) and (self.name == other.name) and (self.birth_date == other.birth_date) and (self.phone == other.phone) and (self.email == other.email) and (self.address == other.address))

    """a helper method that simply returns the name of the patient"""
    def get_name(self):
        return self.name