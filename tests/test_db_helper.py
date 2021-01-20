from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class TestDbHelper(TestCase):
    def setUp(self):
        self.db = DbHelper()

    @patch('src.db_helper.DbHelper')
    def test_salary_with_mocking(self, Mockdbhelper):
        dbhelper = Mockdbhelper()  
        dbhelper.get_maximum_salary.return_value =20000
        Max = dbhelper.get_maximum_salary()   
        dbhelper.get_minimum_salary.return_value =10000
        Min = dbhelper.get_minimum_salary()
        self.assertGreater(Max, Min)

