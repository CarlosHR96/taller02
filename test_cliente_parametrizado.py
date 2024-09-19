import unittest
import HtmlTestRunner
from cliente import Mantenimiento_Cliente, Cliente
from parameterized import parameterized
import csv

def cargar_datos_desde_csv(archivo):
    datos = []
    with open(archivo, newline='', encoding="utf-8") as csvfile:
        lector = csv.reader(csvfile)
        next(lector)  # Saltar el encabezado
        
        for fila in lector:
            datos.append(tuple(fila))
    return datos

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.mantenimiento_cliente = Mantenimiento_Cliente()
      #  self.mantenimiento_cliente.registrar_cliente(Cliente("Test1", "Pytest1", "correo1@testing.com", "Lima", 4))
       # self.mantenimiento_cliente.registrar_cliente(Cliente("Test2", "Pytest2", "correo2@testing.com", "Ica", 5))

    def tearDown(self):
        del self.mantenimiento_cliente
   
   
    @parameterized.expand(cargar_datos_desde_csv("cliente.csv"))
    def test_registrar_cliente_OK(self, apellidos, nombres, correoelectronico, direccion, id_cliente):
        cliente = Cliente(apellidos, nombres, correoelectronico, direccion, id_cliente)
        self.mantenimiento_cliente.registrar_cliente(cliente)
        clientes = self.mantenimiento_cliente.obtener_clientes()
        self.assertIn(cliente, clientes)
    
    @parameterized.expand(cargar_datos_desde_csv("cliente_duplicado.csv"))
    def test_registrar_cliente_NOK(self, apellidos, nombres, correoelectronico, direccion, id_cliente):
        cliente = Cliente(apellidos, nombres, correoelectronico, direccion, id_cliente)
        self.mantenimiento_cliente.registrar_cliente(cliente)
        self.mantenimiento_cliente.registrar_cliente(cliente)
        clientes = self.mantenimiento_cliente.obtener_clientes()
        self.assertEqual(clientes.count(cliente), 1)

    @parameterized.expand(cargar_datos_desde_csv("cliente.csv"))
    def test_busqueda_cliente_OK(self, apellidos, nombres, correoelectronico, direccion, id_cliente):
        cliente = Cliente(apellidos, nombres, correoelectronico, direccion, id_cliente)
        self.mantenimiento_cliente.registrar_cliente(cliente)
        clientes = self.mantenimiento_cliente.buscar_cliente_por_id(id_cliente)
        self.assertEqual(cliente, clientes)

    @parameterized.expand(cargar_datos_desde_csv("cliente.csv"))
    def test_busqueda_cliente_No_existe(self, apellidos, nombres, correoelectronico, direccion, id_cliente):
        cliente = Cliente(apellidos, nombres, correoelectronico, direccion, id_cliente)
        self.mantenimiento_cliente.registrar_cliente(cliente)
        cliente_no_existe = self.mantenimiento_cliente.buscar_cliente_por_id('007')# id inexistente
        self.assertIsNone(cliente_no_existe)

    @parameterized.expand([(4,)])
    def test_eliminar_cliente(self, id_cliente):
        mantenimiento_cliente = Mantenimiento_Cliente()
        cliente=Cliente("Test1", "Pytest1", "correo1@testing.com", "Lima", id_cliente)
        mantenimiento_cliente.registrar_cliente(cliente)
        cliente_existe = mantenimiento_cliente.buscar_cliente_por_id(id_cliente)
        self.assertEqual(cliente, cliente_existe)
        cliente_eliminado = self.mantenimiento_cliente.eliminar_cliente(id_cliente)
        cliente_busqueda = self.mantenimiento_cliente.buscar_cliente_por_id(id_cliente)
        self.assertIsNone(cliente_busqueda)
        self.assertFalse(cliente_eliminado)
    """
    @parameterized.expand(cargar_datos_desde_csv("cliente.csv"))
    def test_registrar_cliente(self, apellidos, nombres, correoelectronico, direccion, id_cliente):
       cliente = Cliente(apellidos, nombres, correoelectronico, direccion, id_cliente)
       self.mantenimiento_cliente.registrar_cliente(cliente)
    @parameterized.expand(cargar_datos_desde_csv("cliente_actualizar.csv"))
    def test_actualizar_cliente(self, id_cliente, nuevos_apellidos, nuevo_correoelectronico, nueva_direccion):
        self.mantenimiento_cliente.actualizar_cliente(
        id_cliente, 
        nuevos_apellidos=nuevos_apellidos, 
        nuevo_correoelectronico=nuevo_correoelectronico, 
        nueva_direccion=nueva_direccion
         )
        cliente_actualizado = self.mantenimiento_cliente.buscar_cliente_por_id(id_cliente)
        self.assertIsNotNone(cliente_actualizado, f"El cliente con ID {id_cliente} no fue encontrado.")
        self.assertEqual(cliente_actualizado.apellidos, nuevos_apellidos)
        self.assertEqual(cliente_actualizado.correoelectronico, nuevo_correoelectronico)
        self.assertEqual(cliente_actualizado.direccion, nueva_direccion)
    """
#python -m unittest test_cliente_parametrizado

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestCliente))
    return suite

if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(
        output="reportes",
        report_name="Reporte de Pruebas",
        report_title="Informe de Pruebas",
        combine_reports=True,
        add_timestamp=True
    )
    runner.run(suite())

