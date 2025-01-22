from clinic.patient_record import PatientRecord

class Patient:
    """
    a class for a Patient object, containing fields phn, name, their birth date,
    their phone number, email, address, and patient record
    """

    def __init__(self, phn, name, birth_date, phone, email, address):
        self.phn = phn
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self. email = email
        self.address = address
        self.record = PatientRecord()

    def __eq__(self, other):
        return ((self.phn == other.phn) and (self.name == other.name) and (self.birth_date == other.birth_date) and (self.phone == other.phone) and (self.email == other.email) and (self.address == other.address))
    
    def __str__(self):
        return (f"Patient phn: {self.phn}, "
        f"name: {self.name}, birth_date: {self.birth_date}, " 
        f"phone number: {self.phone}, email: {self.email}, "
        f"address: {self.address}")
    
    def __repr__(self):
        return f"Patient(phn = {self.phn}, name = {self.name}, birth_date = {self.birth_date}, phone: {self.phone}, email: {self.email}, address: {self.address})"
