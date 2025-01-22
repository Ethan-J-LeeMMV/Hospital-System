from clinic.dao.note_dao import NoteDAO

from clinic.exception.no_current_patient_exception import NoCurrentPatientException

from clinic.note import Note

import pickle

"""A class that handles the CRUD operations that were previously in PatientRecord
"""
class NoteDAOPickle(NoteDAO):
    def __init__(self, phn: str, autosave=False):
        self.autosave = autosave
        self.phn = phn
        
        self.autocounter = 0
        self.notes = []

        self.filepath = f"./clinic/records/{self.phn}.dat"

        if autosave == True:
            self.load_notes()

    def load_notes(self) -> None:
        """Helper method that takes no arguments - loads the notes"""
        try: 
            with open(self.filepath, 'rb') as file: 
                self.notes = pickle.load(file)
                if self.notes:
                    self.autocounter = max(note.code for note in self.notes)
        except FileNotFoundError or EOFError:
            self.notes = []

    def save_notes(self) -> None:
        """Helper method that saves notes"""
        with open(self.filepath, 'wb') as file:
            pickle.dump(self.notes, file)

    def search_note(self, key):
        for note in self.notes:
            if note.code == key:
                return note


    def create_note(self, text):
        self.autocounter += 1
        code = self.autocounter
        text = text

        note = Note(code, text)

        self.notes.append(note)

        if self.autosave == True:
            self.save_notes()
        return note

    def retrieve_notes(self, search_string):
        retrieved_list = []
        for note in self.notes:
            if search_string.lower() in note.text.lower():
                retrieved_list.append(note)

        return retrieved_list

    def update_note(self, key, text):
        lst = []
        for note in self.notes:
            lst.append(note.code)

        if key in lst: # is the code in the list of codes?
            for note in self.notes:
                if key == note.code:
                        note.text = text
                        if self.autosave == True:
                            self.save_notes()
                        return True
        
        return False
                

    def delete_note(self, key):
        for note in self.notes:
            if key == note.code:
                self.notes.remove(note)
                if self.autosave == True:
                    self.save_notes()
                return True

        return False
    def list_notes(self):
        return sorted(self.notes, key=lambda note: note.code, reverse=True)
