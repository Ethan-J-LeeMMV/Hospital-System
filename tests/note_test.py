from unittest import main, TestCase
from datetime import datetime
from clinic.note import Note

class TestNoteFeatures(TestCase):

    def test_note_fields(self):

        note = Note(1, "Test note")
        self.assertEqual(note.code, 1)
        self.assertEqual(note.text, "Test note")
    
    def test_note_equality(self):

        note1 = Note(1, "patient has a fever")
        note2 = Note(1, "patient has a fever")
        self.assertEqual(note1, note2)
    
    def test_note_inequality(self):
        
        note1 = Note(1, "patient has a fever")
        note2 = Note(1, "patient needs surgery")
        self.assertNotEqual(note1, note2)
    
    def test_note_str(self):

        timestamp = datetime(2024, 7, 21, 12, 0)
        note = Note(1, "patient has a cough", timestamp)
        self.assertEqual(str(note), f"Note 1: patient has a cough, timestamp: {timestamp}")


    def test_note_repr(self):

        timestamp = datetime(2024, 7, 21, 12, 0)
        note = Note(1, "patient has a cough", timestamp)
        expected_repr_note = f"Note(code = 1, text = patient has a cough, timestamp = {timestamp})"
        self.assertEqual(repr(note), expected_repr_note)

if __name__ == '__main__':
    unittest.main()