from MasterMindGame.Serializers import JsonSerializer


import unittest



class JsonSerializer_Test(unittest.TestCase):

    string_control_serialize = "{\"var_test_a\": \"value_test_a\", \"var_test_c\": [\"value_1[0]\", \"value_2[1]\"], \"var_test_b\": \"value_test_b\"}"

    def test_When_Serialices_object(self):
        string_json_serialized = JsonSerializer.JsonSerializer.SerializeObject(TestClass())
        self.assertEqual(self.string_control_serialize, string_json_serialized)
        print string_json_serialized
        self.assertIn("[\"value_1[0]\", \"value_2[1]\"]", string_json_serialized)

    def test_When_Deserialices_json(self):
        test_class_obj = JsonSerializer.JsonSerializer.DeserializeJson(self.string_control_serialize,TestClass())
        self.assertEqual(test_class_obj.var_test_a, "value_test_a")
        self.assertEqual(test_class_obj.var_test_b, "value_test_b")
        self.assertEqual(test_class_obj.var_test_c[0], "value_1[0]")
        self.assertEqual(test_class_obj.var_test_c[1], "value_2[1]")




class TestClass(object):
    def __init__(self):
        self.var_test_a = "value_test_a"
        self.var_test_b = "value_test_b"
        self.var_test_c = ["value_1[0]", "value_2[1]"]




    if __name__ == '__main__':
        unittest.main()


