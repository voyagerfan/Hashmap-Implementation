import unittest
from hash_map_oa import HashMap
from a6_include import hash_function_1, hash_function_2

class TestCase(unittest.TestCase):
    """
    Tests the OA function put(self, key: str, value: object) w/ hash_function_1
    Return Value: None
    """
    def test1_put_OA(self):

        # position description
        descriptions = {0: "buckets", 1: "table_load", 2: "table_size", 3: "capacity"}

        # m.buckets(), m.table_load, m.get_size(), m.get_capacity()
        answer_key = ([28, 0.47, 25, 53],
                      [57, 0.47, 50, 107],
                      [148, 0.34, 75, 223],
                      [123, 0.45, 100, 223],
                      [324, 0.28, 125, 449],
                      [299, 0.33, 150, 449])
        
        m = HashMap(53, hash_function_1)
        answer_row = 0
        for i in range(150):
            m.put('str' + str(i), i * 100)
            if i % 25 == 24:
                round_tableload = round(m.table_load(), 2)
                output_arr = [m.empty_buckets(), round_tableload, m.get_size(), m.get_capacity()]

                for j in range(4):
                    subtest_tuple = (answer_row, descriptions[j])
                    with self.subTest(subtest_tuple):
                        self.assertEqual(output_arr[j], answer_key[answer_row][j],
                                         f'failed answer key row {answer_row} for {descriptions[j]}')

                answer_row += 1

    """
    Tests the OA function put(self, key: str, value: object) w/ hash_function_2
    Return Value: None
    """
    def test2_put_OA(self):
        # position description
        descriptions = {0: "buckets", 1: "table_load", 2: "table_size", 3: "capacity"}

        # m.buckets(), m.table_load, m.get_size(), m.get_capacity()
        answer_key = ([37, 0.1, 4, 41],
                      [34, 0.17, 7, 41],
                      [31, 0.24, 10, 41],
                      [27, 0.34, 14, 41],
                      [24, 0.41, 17, 41])

        m = HashMap(41, hash_function_2)
        answer_row = 0
        for i in range(50):
            m.put('str' + str(i // 3), i * 100)
            if i % 10 == 9:
                round_tableload = round(m.table_load(), 2)
                output_arr = [m.empty_buckets(), round_tableload, m.get_size(), m.get_capacity()]

                for j in range(4):
                    subtest_tuple = (answer_row, descriptions[j])
                    with self.subTest(subtest_tuple):
                        self.assertEqual(output_arr[j], answer_key[answer_row][j],
                                         f'failed answer key row {answer_row} for {descriptions[j]}')

                answer_row += 1

    """
    Tests the function table_load(self) w/ hash_function_1
    Return Value: float
    """
    def test1_table_load_OA(self):
        answer_key = [0.0, 0.01, 0.02, 0.02]

        output = []
        m = HashMap(101, hash_function_1)
        output.append(m.table_load())
        m.put('key1', 10)
        output.append(round(m.table_load(), 2))
        m.put('key2', 20)
        output.append(round(m.table_load(), 2))
        m.put('key1', 30)
        output.append(round(m.table_load(), 2))

        for i in range(4):
            with self.subTest(i+1):
                self.assertEqual(output[i], answer_key[i], f'failed subtest table_load subtest {i+1}')

if __name__ == '__main__':
    unittest.main()
