from datetime import datetime
from clinic.note import Note

class PatientRecord:

    """
        a class for a PatientRecord, which takes a Patient and may contain notes for that Patient
    """
    def __init__(self):
        self.autocounter = 0
        self.notes = []
    
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
        self.autocounter += 1
        code = self.autocounter
        text = text

        note = Note(code, text)
        
        self.notes.append(note)

        return note
    
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
        for note in self.notes:
            if note.code == code:
                return note
        
        return None # return None if theres no notecode that is equal to code

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
        retrieved_list = []
        for note in self.notes: 
            if text in note.text:
                retrieved_list.append(note)

        return retrieved_list
    
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
        
        # populate a list to just have the note codes
        lst = []
        for note in self.notes: 
            lst.append(note.code)

        if code in lst: # is the code in the list of codes?
            for note in self.notes:
                if code == note.code:
                        note.text = new_text
                        return True
        return False
    
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

        for note in self.notes: 
            if code == note.code: 
                self.notes.remove(note)
                return True
        
        return False
    
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
        return sorted(self.notes, key=lambda note: note.code, reverse=True)

        

    
    


    

        
