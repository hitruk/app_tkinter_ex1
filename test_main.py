import unittest
from main import Model


# test__имя_функции__что_тестируем


class TestModel(unittest.TestCase):
    # Тест ф-ций класса Model    
    # test function mi_to_km
    def test_mi_to_km_return_value(self):
        self.assertEqual(Model.mi_to_km(1), 1.609)
        self.assertEqual(Model.mi_to_km(1.2425), 2.0)
        self.assertEqual(Model.mi_to_km(10.5), 16.898)

    def test_mi_to_km_return_type(self):
        self.assertIsInstance(Model.mi_to_km(1), float)
     
    def test_mi_to_km_transmitted_value(self):
        
        for x in ('Az', '1', -1):
            self.assertEqual(Model.mi_to_km(x), 0)
            #self.assertEqual(Model.mi_to_km('Az'), 0)
            #self.assertEqual(Model.mi_to_km('1'), 0)
            #self.assertEqual(Model.mi_to_km(-1), 0)


    # test_func_km_to_mi
    def test_km_to_mi_return_result(self):
        self.assertEqual(Model.km_to_mi(1), 0.621) 
        self.assertEqual(Model.km_to_mi(4.82803), 3.0)

    # возвращаемое значение число с плавающей точкой
    # 4.82803 км = 3 милям
    def test_km_to_mi_return_type(self):
        self.assertIsInstance(Model.km_to_mi(4.82803), float)

    def test_km_to_mi_transmitted_value(self):
        for x in ('Az', '1', -1):
            self.assertEqual(Model.km_to_mi(x), 0)
#        self.assertEqual(Model.km_to_mi('Az'), 0)
#        self.assertEqual(Model.km_to_mi('1'), 0)
#        self.assertEqual(Model.km_to_mi(-1), 0)


if __name__ == '__main__':
    unittest.main()
