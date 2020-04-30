import set_test_path
import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout
from datetime import datetime
from app import AppointmentsManagementSystem as Ams

class test_add_customer_to_memory(unittest.TestCase):

    customer_register_day = datetime.now().strftime("%Y-%m-%d")
    customer_register_time = datetime.now().strftime("%H:%M")

    RIGHT_INPUTS_CUSTOMER_ID_0 = ["João", "da Silva", "23-05-1978",
                                  "297.586.890-10", "Rua Bom Sucesso, 487",
                                  "Casa", "São Paulo", "SP"]

    RIGHT_RETURN_CUSTOMER_ID_0 = ["João", "da Silva", "23-05-1978",
                                  "297.586.890-10", "Rua Bom Sucesso, 487",
                                  "Casa", "São Paulo", "SP",
                                  customer_register_day, customer_register_time, "Active"]

    RIGHT_INPUTS_CUSTOMER_ID_1 = ["Joana", "Silveira", "17-02-1972",
                                  "434.763.780-20", "Felicidade, 14", "Ap. 201",
                                 "Rio de Janeiro", "RJ"]


    RIGHT_RETURN_CUSTOMER_ID_1 = ["Joana", "Silveira", "17-02-1972",
                                  "434.763.780-20", "Felicidade, 14", "Ap. 201",
                                 "Rio de Janeiro", "RJ",
                                  customer_register_day, customer_register_time, "Active"]

    def setUp(self):
        self.ams_instance = Ams()
        self.assertEqual(len(self.ams_instance.customers_registry), 0)

    def test_add_1_customer_passes(self):
        with mock.patch('builtins.input', side_effect=self.RIGHT_INPUTS_CUSTOMER_ID_0):
            self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[0])

    def test_add_2_customers_registry_passes(self):
        with mock.patch('builtins.input', side_effect=self.RIGHT_INPUTS_CUSTOMER_ID_0):
            self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[0])
        self.assertEqual(len(self.ams_instance.customers_registry), 1)
        with mock.patch('builtins.input', side_effect=self.RIGHT_INPUTS_CUSTOMER_ID_1):
            self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_1, self.ams_instance.customers_registry[1])
        self.assertEqual([self.RIGHT_RETURN_CUSTOMER_ID_0, self.RIGHT_RETURN_CUSTOMER_ID_1],
                         self.ams_instance.customers_registry)

    def test_add_1_customer_fails_forename_value_error(self):
        wrong_forename_input = "João2"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(0, wrong_forename_input)
        expected_exception = "Invalid input. The forename may only contain letter or spaces.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_surname_value_error(self):
        wrong_surname_input = "da Silva2"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(1, wrong_surname_input)
        expected_exception = "Invalid input. The surname may only contain letter or spaces.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_birthdate(self):
        wrong_birthdate_input = "24011978"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(2, wrong_birthdate_input)
        expected_exception = "Invalid input. The birthdate muss comply to the required format\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_customer_id(self):
        wrong_customer_id_input = "24011978"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(3, wrong_customer_id_input)
        expected_exception = "Invalid input. The customer id muss have 11 digits and " \
                             "comply to the required format\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)


    def test_add_1_customer_fails_customer_id2(self):
        wrong_customer_id_input = "1234567891!"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(3, wrong_customer_id_input)
        expected_exception = "Invalid input. The id number may only have numbers, points and dashes\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_address_street_and_number(self):
        wrong_address_street_and_number_input = "XX Street !"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(4, wrong_address_street_and_number_input)
        expected_exception = "Invalid input. The address may not contain special caracters.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_address_street_and_number2(self):
        wrong_address_street_and_number_input = "testing too long adress lalalalala"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(4, wrong_address_street_and_number_input)
        expected_exception = "Invalid input. The address may not be longer than 25 characters.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_address_others(self):
        wrong_address_others_input = "Apartment 101!"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(5, wrong_address_others_input)
        expected_exception = "Invalid input. The address may not contain special caracters.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_address_others2(self):
        wrong_address_others_input = "testing too long adress lalalalala"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(5, wrong_address_others_input)
        expected_exception = "Invalid input. The address may not be longer than 25 characters.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_address_city(self):
        wrong_address_city_input = "New York 101"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(6, wrong_address_city_input)
        expected_exception = "Invalid input. The city name may only contain letter or spaces.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_address_city2(self):
        wrong_address_city_input = "testing too long city lalalalalalala"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(6, wrong_address_city_input)
        expected_exception = "Invalid input. The city name may not be longer than 25 characters.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_address_state(self):
        wrong_address_state_input = "Florida 101"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(7, wrong_address_state_input)
        expected_exception = "Invalid input. The state name may only contain letter or spaces.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_address_state2(self):
        wrong_address_state_input = "testing too long state lalalalalalala"
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(7, wrong_address_state_input)
        expected_exception = "Invalid input. The state name may not be longer than 25 characters.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_0, self.ams_instance.customers_registry[-1])
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_customer_fails_type_error(self):
        wrong_customer_name_input = 2
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(0, wrong_customer_name_input)
        with self.assertRaises(TypeError):
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()

    def test_add_1_customer_fails_type_error2(self):
        wrong_customer_id_input = 2
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(3, wrong_customer_id_input)
        with self.assertRaises(TypeError):
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()

    def test_add_1_customer_fails_type_error3(self):
        wrong_address_other_input = True
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(6, wrong_address_other_input)
        with self.assertRaises(TypeError):
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()

    def test_add_1_customer_fails_type_error4(self):
        wrong_address_street_and_number_input = 3
        inputed_inputs = self.RIGHT_INPUTS_CUSTOMER_ID_0[:]
        inputed_inputs.insert(4, wrong_address_street_and_number_input)
        with self.assertRaises(TypeError):
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.ams_instance.add_customer_to_registry()

    def tearDown(self):
        self.ams_instance = None

if __name__ == "__main__":
    unittest.main()