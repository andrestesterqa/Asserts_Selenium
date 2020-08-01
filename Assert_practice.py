import unittest

class Pruebas_de_standards(unittest.TestCase):

# IMPORTANTE! Al momento de crear un método es fundamental comenzar el nombre con "test", de lo contrario no corre la prueba

# Assert para validar que 2 elementos son iguales
    def test_suma(self):
        a = 2 + 2
        b = 3 + 1
        self.assertEqual(a, b)

# Assert para validar que 2 elementos NO son iguales
    def test_otra_suma(self):
        a = 5 + 1
        b = 8 + 20
        self.assertNotEqual(a, b)

# Assert para validar que 2 elementos son True
    def test_algo_verdadero(self):
        a = 2 + 2
        b = 3 + 1
        self.assertTrue(a==b)

# Assert para validar que 2 elementos son False
    def test_algo_falso(self):
        a = 3 + 1
        b = 5 + 1
        self.assertFalse(a==b)

# Assert para validar que un elemento es mayor que (>)
    def test_algo_es_mayor(self):
        a = 20
        b = 9
        self.assertTrue(a>b)

    def test_algo_es_mayor_II(self):
        a = 60
        b = 50
        self.assertGreater(a, b)

# Assert para validar que un elemento es menor

    def test_algo_es_menor(self):
        a = 20
        b = 30
        self.assertLess(a, b)

    def test_algo_es_menor_II(self):
        a = 20
        b = 20
        self.assertLessEqual(a, b)

# Assert para validar que dos listas son iguales

    def test_comparar_lista(self):
        a = [1, 2, "Fruta"]
        b = [1, 2, "Fruta"]
        self.assertListEqual(a, b)

# Assert para comparar Tuplas

    def test_comparar_tuplas(self):
        a = (1, 2, 3)
        b = (1, 2, 3)
        self.assertTupleEqual(a, b)

# Assert para comparar Diccionario

    def test_comparar_diccionarios(self):
        a = {"id":1, "Nombre":"Andres", "Apellido":"Hernández"}
        b = {"id":1, "Nombre":"Andres", "Apellido":"Hernández"}
        self.assertDictEqual(a, b)



if __name__ == "__main__":
    unittest.main()