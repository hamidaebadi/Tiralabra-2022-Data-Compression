import unittest
from logic.compress_data import CompressData

class TestCompressionData(unittest.TestCase):

    def setUp(self):
        self.huffman_encoding = CompressData()
        self.text = "test text"
        #ASCII character: 1 character = 8 bits
        self.original_text_size = len(self.text)* 8
        self.huffman_encoding.compress_huffman(self.text)
        self.encoded_text = self.huffman_encoding.get_encoded_content(self.text)
        self.encoded_size = len(self.huffman_encoding.get_encoded_content(self.text))

    def test_huffman_encoding_works(self):
        self.assertNotEqual(self.encoded_text, self.text)

    def test_huffman_reduced_size(self):
        self.assertLess(self.encoded_size, self.original_text_size)


    def test_reduced_size_is_sixty_precent_or_less_of_original_size(self):
        size_rate = self.encoded_size // len(self.encoded_text)
        self.assertLessEqual(size_rate, 60)

    def test_huffman_doesnt_work_on_empty_text(self):
        result = self.huffman_encoding.compress_huffman("")
        self.assertEqual(result, False)