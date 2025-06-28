# Python
import unittest
from Revision import (
    call_Parvathi,
    my_Func_args,
    my_MyFunc_KeyValue,
    Func_TwoList,
    func_Separate,
    MultiMerge_Lists,
    func_UnLimitedList,
    Main_func,
    key_list_names,
    is_prime
)

class TestRevisionFunctions(unittest.TestCase):

    def test_call_Parvathi(self):
        result = call_Parvathi("Devotee")
        self.assertIn("Devi Parvathi has blessed you:Devotee", result)

    def test_my_Func_args(self):
        result = my_Func_args(1, 2, 3, 4)
        self.assertEqual(result, 10)

    def test_my_MyFunc_KeyValue(self):
        result = my_MyFunc_KeyValue(Dev1="Value1", Devi3="Value3")
        self.assertEqual(result, "Value3")

    def test_Func_TwoList(self):
        result = Func_TwoList([1, 2], [3, 4])
        self.assertEqual(result, "[1, 2][3, 4]")

    def test_func_Separate(self):
        result = func_Separate("hello")
        self.assertEqual(result, ['h', 'e', 'l', 'l', 'o'])

    def test_MultiMerge_Lists(self):
        result = MultiMerge_Lists([1, 2], [3, 4])
        self.assertEqual(result, [3, 4])

    def test_func_UnLimitedList(self):
        result = func_UnLimitedList([1, 2], [3, 4], [5, 6])
        self.assertEqual(result, [5, 6])

    def test_key_list_names(self):
        result = key_list_names("key1", key1=[1, 2, 3, 4])
        self.assertEqual(result, 3)

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(1))

if __name__ == "__main__":
    unittest.main()