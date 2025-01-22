from datetime import datetime
from clinic.note import Note
from clinic.dao.note_dao_pickle import NoteDAOPickle

class PatientRecord:

    """
        a class for a PatientRecord, which takes a Patient and may contain notes for that Patient
    """
    def __init__(self, phn: int, autosave = False):
        self.autosave = autosave
        self.phn = str(phn)
        self.note_dao = NoteDAOPickle(self.phn, self.autosave)

    def create_note(self, text: str) -> Note:
        """
        Creates a new note and adds to notes list while also incrementing autocounter

        Parameters
        ----------
        text: str
            patient's medical conditions
        
        Returns 
        -------
        Note
            returns the created Note
        """
        return self.note_dao.create_note(text)
    
    def search_note_using_code(self, code: int) -> Note:
        """
        Searches for a note using the note's code (autocounter)

        Parameters 
        ----------
        code: int
            the code that specifices what Note it is 
        
        Returns 
        -------
        Note
            returns the searched Note
        """
        return self.note_dao.search_note(code)

    def retrieve_notes(self, text: str) -> list[Note]: 
        """
        Uses "text" to search for patient record and sees if the text matches that in the Note, adds to retrieved_list and returns retrieved_list

        Parameters
        ----------
        text: str
            patient's medical conditions

        -------
        list[Note]
            returns a retrieved list of Notes that have been created
        """
        return self.note_dao.retrieve_notes(text)
    
    def update_note(self, code: int, new_text: str) -> bool:
        """
        Updates Note by changing the patient's medical information. Done so
        by checking if the code given is equal to the code of the note they want to change.

        Parameters
        ----------
        code: int
            the code that is given so the user can search for a Note that matches the code
        new_text: str
            the text that replaces the patient's old medical information
        
        Returns
        -------
        bool
            returns True if updated successfully, False otherwise
        """
        return self.note_dao.update_note(code, new_text)
       
    
    def delete_existing_note(self, code: int) -> bool:
        """
        Deletes the existing note

        Parameters
        ----------
        code: int
            the code that is given so the user can search for a Note that matches the code
        
        Returns
        -------
        bool
            returns True if successfully deleted, False otherwise
        """
        return self.note_dao.delete_note(code)
    
    def list_patient_record(self) -> list[Note]:
        """
        Lists the full patient record, with its Notes being in sorted order from largest code (most recent Note) 
        to lowest code (earliest Note)

        Parameters
        ----------
        None

        Returns
        -------
        list[Note]
            returns a list of Notes in sorted order
        """
        # sort the notes by their codes in descending order
        return self.note_dao.list_notes()
        

    
    


    

        
