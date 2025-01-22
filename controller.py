from clinic.patient import Patient
from clinic.note import Note

class Controller:
    """A class used to represent controller

    ...
    Attributes
    ----------
    username: str
        a the username used to login to the system
    password: str
        the password used to login to the system
    logged_in: bool
        login status
    patients_list: list
        list of patients in the system
    current_patient: patient
        the current_patient the system is interacting with

    Methods
    -------
    is_logged()
        returns login status

    login()
        login to the system. check if credentials are right and change logged_in to true if they are

    logout()
        changes logged_in to false if it is true

    create_patient(phn, name dob, phone, email, address)
        creates patient instances with provided info and append to the list

    search_patient(phn)
        search for patient with the given phn in patients_list

    retrieve_patients(name)
        retrives and returns a list of patients with the given name

    update_patient(phn, new_phn, new_name, new_birth_datem, new_phone, new_email, new_address)
        searches a patient with given phn and update information of the patient with the given new info is different

    delete_patient(phn)
        deletes the patient with the given phn from patients_list

    list_patients()
        returns patients_list

    get_current_patient()
        returns current_patient

    set_current_patient(phn)
        set the patient with the given phn as current_patient

    unset_current_patient()
        set current_patient to none
    """

    def __init__(self):
        self.username = "user"
        self.password = "clinic2024"
        self.logged_in = False
        self.patients_list = []
        self.current_patient = None

    def is_logged(self):
        """checks login status
        returns true if logged in, false otherwise
        """
        return self.logged_in

    def login(self, username, password):
        """login to the system
        changes login status to true if initially false and given username and password match with the system.

        parameters
        ----------
        username: the username given that will be checked against the system
        password: the password given that will be checked against the system

        Returns
        -------
        boolean
            true if is_logged successfully changed from false to true, false otherwise
        """
        if self.is_logged() == False:
            if username == self.username:
                if password == self.password:
                    self.logged_in = True
                    return True
                else:
                    print("login in with incorrect password")
                    return False
            else:
                print("login in with incorrect username")
                return False

    def logout(self):
        """logout of the system
        changes login status to false if initially true

        Returns
        -------
            boolean
                true if is_logged successfully changed from true to false, false otherwise
        """
        if self.is_logged() == False:
            print("log out only after being logged in")
            return False
        else:
            self.logged_in = False;
            return True

    def create_patient(self, phn: int, name: str, dob: str, phone: str, email: str, address: str):
        """creates patient with given info and adds to patients_list

        the code checks if logged_in is true. Then, if logged_in is true, checks if a patient with the given phn is in patients_list. If not, the code creates an instance of the patient class and adds it to patients_list.

        Parameters
        ----------
            phn: int
                patient's personal health number
            name: str
                patient's name
            dob: str
                patient's date-of-birth
            phone: str
                patient's phone number
            email: str
                patient's email address
            address: str
                patient's physical address

        Returns
        -------
            patient
                an instance of the patient class that has just been added to the patients_list
        """
        if self.is_logged():
            if (not self.search_patient(phn)):
                p = Patient(phn, name, dob, phone, email, address)
                self.patients_list.append(p)
                return p
        else:
            print("cannot create patient without logging in")

    def search_patient(self, phn: int):
        """searches for the patient with the given phn on the system

        first check if list is empty. If not, loop throguh the list and returns the patient if found

        Parameter
        ---------
            phn: int
                the patient's personal health number

        Returns:
            patient:
                the full info of the patient with the given phn
        """
        if self.patients_list:
            for i in range(len(self.patients_list)):
                if self.patients_list[i].phn == phn:
                    return self.patients_list[i]

    def retrieve_patients(self, name: str):
        """retrieves patients matching the given name

        check if is_logged is true, proceed if it is. Then check if name can be split into two. If true, loops throgub patients_list, check and add patients to retrieved_list if names match. if name cannot be split into two, loop through patients_list. during each itteration, split patient name into two and check each against the name passed in to the function and add patient to retrieved_list if names match

        Parameter
        ---------
            name: string
                the name of patient wanted

        Retuns
            list
                a list of patients with matching name
        ------
        """
        retrieved_list = []
        if self.is_logged():
            if len(name.split()) == 2:
                for i in range(len(self.patients_list)):
                    if self.patients_list[i].name == name:
                        retrieved_list.append(self.patients_list[i]);

            else:
                for i in range(len(self.patients_list)):
                    split_name = self.patients_list[i].name.split()
                    if split_name[0] == name or split_name[1] == name:
                        retrieved_list.append(self.patients_list[i])
            return retrieved_list
        else:
            print("cannot retrieve patients without logging in")

    def update_patient(self, phn: int, new_phn: int, new_name: str, new_birth_date: str, new_phone: str, new_email: str, new_address: str):
        """ update patient with given phn with new info if they differ

        check if is_logged is true, terminates if not. loop through patients_list, first check if the patient at each iteration has matching phn and is not current_patient. The code then proceed to update phn, name, birthdate, phone number, email, address if the new one is differs from the old. before updating phn if it differs, the program checks if the new phn is associated with another patient

         Parameters
            phn: int
                used to search for the patient on the list
            new_phn: int
                the new phn of the patient
            new_name: str
                the new name of the patient
            new_birth_date: str
                the updated birth date of the patient
            new_phone: str
                the new phone number of the patient
            new_email: str
                the new email address of the patient
            new_address: str
                the new physical address of the patient

        Returns
            patient
                the patient instance containing updated info
         ---------
        """
        if self.is_logged():
            if self.patients_list is not None:
                for i in range(len(self.patients_list)):
                    if self.patients_list[i].phn == phn and self.patients_list[i] is not self.current_patient:
                        if (new_phn != self.patients_list[i].phn):
                            if self.search_patient(new_phn) is None:
                                self.patients_list[i].phn = new_phn
                            else:
                                return
                        if (new_name != self.patients_list[i].name):
                            self.patients_list[i].name = new_name
                        if (new_birth_date != self.patients_list[i].birth_date):
                            self.patients_list[i].birth_date = new_birth_date
                        if (new_phone != self.patients_list[i].phone):
                            self.patients_list[i].phone = new_phone
                        if (new_email != self.patients_list[i].email):
                            self.patients_list[i].email = new_email
                        if (new_address != self.patients_list[i].address):
                            self.patients_list[i].address = new_address

                        return self.patients_list[i]

    def delete_patient(self, phn: int):
        """deletes patient with the given phn from the system

        Parameter
        ---------
        phn: int
            the personal health number of the patient being deleted

        Returns
        -------
        boolean
            true if patient successfully deleted
        """
        if self.is_logged():
            if self.patients_list is not None:
                for i in range (len(self.patients_list)):
                    if self.patients_list[i].phn == phn and self.patients_list[i] is not self.current_patient:
                        del self.patients_list[i]
                        return True

    def list_patients(self):
        if self.is_logged():
            if self.patients_list is not None:
                return self.patients_list
    def get_current_patient(self):
        if self.is_logged():
            if self.current_patient is not None:
                return self.current_patient
    def set_current_patient(self, phn):
        if self.is_logged():
            self.current_patient = self.search_patient(phn) if self.search_patient(phn) is not None else None
    def unset_current_patient(self):
        if self.is_logged():
            if self.current_patient is not None:
                self.current_patient = None

    def create_note(self, text: str) -> Note:
        """creates a new Note and returns a Note by calling the create_note method from PatientRecord class
        
        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged() and self.current_patient is not None:
            note = self.current_patient.record.create_note(text)
            return note
        return None
    
    def search_note(self, code: int) -> Note:
        """searches for a Note and returns a Note by calling the search_note_using_code method from PatientRecord class

        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged() and self.current_patient is not None:
            return self.current_patient.record.search_note_using_code(code)
        return None
    
    def retrieve_notes(self, text) -> list[Note]:
        """retrieves Notes as a list of Notes by calling the retrieve_notes method in PatientRecord
        
        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged() and self.current_patient is not None:
            return self.current_patient.record.retrieve_notes(text)
        return None
    
    def update_note(self, code: int, new_text: str) -> bool:
        """updates Note by calling update_note method in PatientRecord, returns True if successfully updated, False otherwise

        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged() and self.current_patient is not None:
            return self.current_patient.record.update_note(code, new_text)
        
    def delete_note(self, code: int) -> bool:
        """deletes note by using delete_existing_note method in PatientRecord, and returns True if successfully deleted, False otherwise
            
        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged() and self.current_patient is not None:
            return self.current_patient.record.delete_existing_note(code)
    
    def list_notes(self) -> list[Note]:
        """lists the notes in a sorted order, from last created note to first created note 
        by calling the list_patient_record method from PatientRecord

        DETAILED DOCUMENTATION FOR SEARCH AND CRUD METHODS WILL BE FOUND IN PatientRecord
        """
        if self.is_logged() and self.current_patient is not None:
            return self.current_patient.record.list_patient_record()