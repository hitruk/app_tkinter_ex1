
import unittest
from main import AppForTest, DownFrame, UpFrame, ResultFrame



# СОЗДАЙ ТЕСТОВУЮ APP В ОСНОВНОМ ФАЙЛЕ!!

# Вот так можно указать количество знаков после запятой при выводе
# a = [1000, 2.4, 2.23456754323456, 2754.344]
#for i in a:
#    print('%.3f' % i)  # 3 знака после запятой


class TestView(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Running setUpClass')
        cls.app = AppForTest()
        cls.down_frame = DownFrame(cls.app)
        cls.up_frame = UpFrame(cls.app)
        cls.res_frame = ResultFrame(cls.app)

    @classmethod
    def tearDownClass(cls):
        print('Running tearDownClass')
        if cls.app:
            cls.app.destroy()

    # DownFrame
    def test_get_value_rb_return_type(self):
        #app = App()
        #self.l_frame = DownFrame(self.app)
        x = self.down_frame.get_value_rb()
        self.assertIsInstance(x, str)

    def test_get_value_rb_return_value(self):
        #app = App()
        #l_frame = DownFrame(self.app)
        value_rb_defoult = self.down_frame.values_rb[0]
        x = self.down_frame.get_value_rb()
        self.assertEqual(x, value_rb_defoult)

    def test_get_value_rb_return_value(self):
        # находится ли получаемое значение в списке
        pass

    # UpFrame
    def test_get_text_label_return_value(self):
        # значение радиокнопки из фрейма DownFrame
        value_rb = self.down_frame.get_value_rb()
        label_text = self.up_frame.get_text_label(value_rb)
        self.assertEqual(label_text, f'Convert {value_rb}:')
    
    # в работе
    def test_get_entry_return_value_type(self):
        l_values = ['aZ', -1, '1', '-1', 12.45345]
        for val in l_values:
            self.up_frame.entry.insert(0, val)
            x = self.up_frame.get_entry_value() 
            self.assertIsInstance(x, float)


    # ResultFrame
    def test_text_title_label_return_value(self):
        value_rb = self.down_frame.get_value_rb()
        text_title_label = self.res_frame.get_text_title_label(value_rb)
        self.assertEqual(text_title_label, f'Convert {value_rb}:')     



if __name__ == '__main__':
    unittest.main(verbosity=2)
