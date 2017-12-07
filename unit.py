import unittest

import test
class Pruebas(unittest.TestCase):
    def test_concat(self):
        self.assertEqual(test.suma("hola","mundo"), "holamundo")
        self.fail("fallando :v")

if __name__=="__main__":
    unittest.main()
