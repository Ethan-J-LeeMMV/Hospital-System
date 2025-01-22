from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException

from clinic.patient import Patient
from clinic.note import Note
from clinic.dao.patient_dao import PatientDAO
from clinic.dao.patient_dao_json import PatientDAOJSON

import hashlib

""" class Controller uses functions from patient_dao_json and note_dao_pickle for its CRUD/Search methods
"""
class Controller:
    def __init__(self, autosave):
        self.autosave = autosave
        if self.autosave == False:
            self.users = {"user": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92", "ali": "6394ffec21517605c1b426d43e6fa7eb0cff606ded9c2956821c2c36bfee2810", "kala": "e5268ad137eec951a48a5e5da52558c7727aaa537c8b308b5e403e6b434e036e"}
        else:
            self.users = self.load_user()
        self.logged_in = False
        self.current_patient = None
        self.patient_dao = PatientDAOJSON(autosave)

    def load_user(self):
        users = {}
        with open("clinic/users.txt") as file:
            for line in file:
                line = line.strip("\n")
                (username, password) = line.split(",")
                users[str(username)] = password
            return users

    def get_password_hash(self, password):
        encoded_password = password.encode('utf-8')
        hash_object = hashlib.sha256(encoded_password)
        hex_dig = hash_object.hexdigest()
        return hex_dig

    def is_logged(self):
        return self.logged_in

    def login(self, username, password):

        if self.is_logged() == False:
            password_hash = self.get_password_hash(password)
            if username in self.users:
                if self.users[username] == password_hash:
                    self.logged_in = True
                    return True

    def logout(self):
        if self.is_logged() == True:
            self.logged_in = False
            return True


    def create_patient(self, phn: int, name: str, dob: str, phone: str, email: str, address: str):

        p = Patient(phn, name, dob, phone, email, address)
        return self.patient_dao.create_patient(p)

    def search_patient(self, phn: int):
        if self.is_logged() == True:
            return self.patient_dao.search_patient(phn)
        else:
            raise IllegalAccessException

    def retrieve_patients(self, name: str):
        if self.is_logged():
            return self.patient_dao.retrieve_patients(name)

        else:
            raise IllegalAccessException

    def update_patient(self, phn: int, new_phn: int, new_name: str, new_birth_date: str, new_phone: str, new_email: str, new_address: str):

        if not self.is_logged():
            raise IllegalAccessException
        if self.current_patient is not None and self.current_patient.phn == phn:
           raise IllegalOperationException


        current_patient = self.patient_dao.search_patient(phn)
        new_patient = Patient(new_phn, new_name, new_birth_date, new_phone, new_email, new_address, self.autosave)

        if current_patient is None:
            raise IllegalOperationException


        if phn == new_phn:
            if current_patient == new_patient:
                return False
            self.patient_dao.update_patient(phn, new_patient)

            return True


        if self.patient_dao.search_patient(new_phn) is not None:
            raise IllegalOperationException


        self.patient_dao.delete_patient(phn)
        self.patient_dao.create_patient(new_patient)

        return True

    def delete_patient(self, phn: int):

        if not self.is_logged():
            raise IllegalAccessException

        if self.current_patient is not None and phn == self.current_patient.phn:
            raise IllegalOperationException

        result = self.patient_dao.delete_patient(phn)

        if result == True:
            return True
        else:
            raise IllegalOperationException

    def list_patients(self):
        return self.patient_dao.list_patients()



    def get_current_patient(self):
        if self.is_logged():
            if self.current_patient is not None:
                return self.current_patient
        else:
            raise IllegalAccessException

    def set_current_patient(self, phn):
        if self.current_patient is None:
            if self.is_logged():
                if self.search_patient(phn) is not None:
                    self.current_patient = self.search_patient(phn)
                else:
                    raise IllegalOperationException
            else:
                raise IllegalAccessException
    def unset_current_patient(self):
        if self.is_logged():
            if self.current_patient is not None:
                self.current_patient = None
        else:
            raise IllegalAccessException

    def create_note(self, text: str) -> Note:
        """creates a new Note and returns a Note by calling the create_note method from PatientRecord class

        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged():
            if self.current_patient is not None:
                note = self.current_patient.record.create_note(text)
                return note
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException

    def search_note(self, code: int) -> Note:
        """searches for a Note and returns a Note by calling the search_note_using_code method from PatientRecord class

        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged():
            if self.current_patient is not None:
                return self.current_patient.record.search_note_using_code(code)
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException


    def retrieve_notes(self, text) -> list[Note]:
        """retrieves Notes as a list of Notes by calling the retrieve_notes method in PatientRecord

        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged():
            if self.current_patient is not None:
                return self.current_patient.record.retrieve_notes(text)
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException

    def update_note(self, code: int, new_text: str) -> bool:
        """updates Note by calling update_note method in PatientRecord, returns True if successfully updated, False otherwise

        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged():
            if self.current_patient is not None:
                return self.current_patient.record.update_note(code, new_text)
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException

    def delete_note(self, code: int) -> bool:
        """deletes note by using delete_existing_note method in PatientRecord, and returns True if successfully deleted, False otherwise

        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged():
            if self.current_patient is not None:
                return self.current_patient.record.delete_existing_note(code)
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException

    def list_notes(self) -> list[Note]:
        """lists the notes in a sorted order, from last created note to first created note
        by calling the list_patient_record method from PatientRecord

        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged():
            if self.current_patient is not None:
                return self.current_patient.record.list_patient_record()
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException
