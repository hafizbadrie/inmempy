import unittest
from inmempy.inmempy import InmempyDb


class InmempyDbTest(unittest.TestCase):
    def setUp(self):
        InmempyDb.cleanup()

    def tearDown(self):
        InmempyDb.cleanup()

    def test_table_exists(self):
        self.assertFalse(InmempyDb.table_exists('students'))

        schema = {'id': 'integer', 'name': 'string'}
        InmempyDb.create_table('students', schema, 'id')

        self.assertTrue(InmempyDb.table_exists('students'))

    def test_create_table(self):
        schema = {'id': 'integer', 'name': 'string'}
        InmempyDb.create_table('students', schema, 'id')

        self.assertTrue(InmempyDb.table_exists('students'))

    def test_create_table_when_exists(self):
        schema = {'id': 'integer', 'name': 'string'}
        InmempyDb.create_table('students', schema, 'id')

        self.assertRaises(Exception, InmempyDb.create_table, 'students', schema, 'id')

    def test_insert_table(self):
        schema = {'id': 'integer', 'name': 'string'}
        InmempyDb.create_table('students', schema, 'id')

        data = {'id': 1, 'name': 'Hafiz'}
        InmempyDb.insert_to('students', data)

        result = InmempyDb.select_from('students')
        self.assertEqual(result, [data])

    def test_insert_without_providing_primary_key(self):
        schema = {'id': 'integer', 'name': 'string'}
        InmempyDb.create_table('students', schema, 'id')

        data = {'age': 1, 'name': 'Hafiz'}
        self.assertRaises(Exception, InmempyDb.insert_to, 'students', data)

    def test_insert_multiple_values_to_table(self):
        schema = {'id': 'integer', 'name': 'string'}
        InmempyDb.create_table('students', schema, 'id')

        student_1 = {'id': 1, 'name': 'Hafiz'}
        student_2 = {'id': 2, 'name': 'Badrie'}
        InmempyDb.insert_to('students', student_1)
        InmempyDb.insert_to('students', student_2)

        result = InmempyDb.select_from('students')
        self.assertEqual(result, [student_1, student_2])

    def test_insert_multiple_values_with_mismatch_columns_value(self):
        schema = {'id': 'integer', 'name': 'string'}
        InmempyDb.create_table('students', schema, 'id')

        student_1 = {'id': 1, 'age': 20}
        student_2 = {'id': 2, 'name': 'Badrie'}
        InmempyDb.insert_to('students', student_1)
        InmempyDb.insert_to('students', student_2)

        result = InmempyDb.select_from('students')
        expected_student_1 = {'id': 1, 'name': None}
        self.assertEqual(result, [expected_student_1, student_2])

    def test_select_one(self):
        schema = {'id': 'integer', 'name': 'string'}
        InmempyDb.create_table('students', schema, 'id')

        student_1 = {'id': 1, 'name': 'Hafiz'}
        student_2 = {'id': 2, 'name': 'Badrie'}
        InmempyDb.insert_to('students', student_1)
        InmempyDb.insert_to('students', student_2)

        result = InmempyDb.select_one('students', 1)
        self.assertEqual(result, student_1)

    def test_select_one_when_datum_doesnt_exist(self):
        schema = {'id': 'integer', 'name': 'string'}
        InmempyDb.create_table('students', schema, 'id')

        student_1 = {'id': 1, 'name': 'Hafiz'}
        student_2 = {'id': 2, 'name': 'Badrie'}
        InmempyDb.insert_to('students', student_1)
        InmempyDb.insert_to('students', student_2)

        result = InmempyDb.select_one('students', 3)
        self.assertIsNone(result)
