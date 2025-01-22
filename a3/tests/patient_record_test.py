from unittest import main, TestCase
from clinic.patient_record import PatientRecord

class TestPatientRecord(TestCase):

    def setUp(self):
        """create a PatientRecord instance for testing"""

        self.patient_record = PatientRecord()

    def test_create_note(self):
        """test create_note method"""

        note = self.patient_record.create_note("patient has a cold.")
        self.assertEqual(note.code, 1)
        self.assertEqual(note.text, "patient has a cold.")
        self.assertEqual(len(self.patient_record.notes), 1)

    def test_search_note_using_code(self):
        """test searching for a note by code"""

        self.patient_record.create_note("patient has a cold.")
        note = self.patient_record.search_note_using_code(1)

        self.assertIsNotNone(note)
        self.assertEqual(note.text, "patient has a cold.")
        self.assertIsNone(self.patient_record.search_note_using_code(2)) # checking if an invalid note is None

    def test_retrieve_notes(self):
        """test retrieving notes that have specific medical info"""

        self.patient_record.create_note("patient has a cold.")
        self.patient_record.create_note("patient has a headache.")
        notes = self.patient_record.retrieve_notes("cold")

        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].text, "patient has a cold.")

    def test_update_note(self):
        """test updating an existing note"""

        self.patient_record.create_note("patient has a cold.")
        success = self.patient_record.update_note(1, "patient has the flu.")
        self.assertTrue(success)
        note = self.patient_record.search_note_using_code(1)
        self.assertEqual(note.text, "patient has the flu.")

        # testing updating a non-existent note
        success = self.patient_record.update_note(2, "this should not work.")
        self.assertFalse(success)

    def test_delete_existing_note(self):
        """test deleting a note"""

        self.patient_record.create_note("patient has a cold.")
        success = self.patient_record.delete_existing_note(1)
        self.assertTrue(success)
        self.assertEqual(len(self.patient_record.notes), 0)

        # testing deleting a non-existent note
        success = self.patient_record.delete_existing_note(2)
        self.assertFalse(success)

    def test_list_patient_record(self):
        """test listing notes in sorted order"""
        
        self.patient_record.create_note("Patient A.")
        self.patient_record.create_note("Patient B.")
        self.patient_record.create_note("Patient C.")
        
        # verify the order by checking the codes
        notes = self.patient_record.list_patient_record()
        self.assertEqual(len(notes), 3)
        self.assertEqual(notes[0].text, "Patient C.")  # most recent
        self.assertEqual(notes[1].text, "Patient B.")
        self.assertEqual(notes[2].text, "Patient A.")  # earliest

if __name__ == '__main__':
    unittest.main()
