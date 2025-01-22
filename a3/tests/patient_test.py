from unittest import main, TestCase
from clinic.patient import Patient

class TestPatientFeatures(TestCase):

    def test_patient_fields(self):
        """test the patient fields"""
        patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        self.assertEqual(patient.phn, 9790012000)
        self.assertEqual(patient.name, "John Doe")
        self.assertEqual(patient.birth_date, "2000-10-10")
        self.assertEqual(patient.phone, "250 203 1010")
        self.assertEqual(patient.email, "john.doe@gmail.com")
        self.assertEqual(patient.address, "300 Moss St, Victoria")



    def test_patient_equality(self):
        """test if two patients are equal"""
        p1 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        p2 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        self.assertEqual(p1, p2)
    
    def test_patient_inequality(self):
        """see if two patients are not equal"""
        p1 = Patient(9790012002, "Man Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        p2 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        
        p3 = Patient(9790012002, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        p4 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")

        
        self.assertNotEqual(p1, p2)
        self.assertNotEqual(p3, p4)
    
    def test_patient_str(self):
        """test the str method from Patient class"""

        patient = Patient(9790012002, "Man Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")

        expected_patient = ("Patient phn: 9790012002, name: Man Doe, birth_date: 2000-10-10, phone number: 250 203 1010, email: john.doe@gmail.com, address: 300 Moss St, Victoria")

        self.assertEqual(str(patient), expected_patient)

    def test_patient_repr(self):
        """test the repr method from Patient class"""

        patient = Patient(9790012002, "Man Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")


        expected_repr_patient = (
            "Patient(phn = 9790012002, name = Man Doe, birth_date = 2000-10-10, "
            "phone: 250 203 1010, email: john.doe@gmail.com, address: 300 Moss St, Victoria)"
        )
        self.assertEqual(repr(patient), expected_repr_patient)

if __name__ == '__main__':
    unittest.main()