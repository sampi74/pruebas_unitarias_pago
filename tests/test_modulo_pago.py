import unittest
from datetime import datetime
from src.modulo_pago import Pago, DetallePago, EstadoPago, EstadoConflicto, Conflicto


class TestEstadoPago(unittest.TestCase):
    def setUp(self):
        self.estado_pago = EstadoPago(id_estado_pago=1, nombre_estado_pago='completado')

    def test_estado_pago_attributes(self):
        self.assertEqual(self.estado_pago.id_estado_pago, 1)
        self.assertEqual(self.estado_pago.nombre_estado_pago, 'completado')
        self.assertIsNone(self.estado_pago.fecha_baja_estado_pago)


class TestEstadoConflicto(unittest.TestCase):
    def setUp(self):
        self.estado_conflicto = EstadoConflicto(id_estado_conflicto=1, nombre_estado_conflicto='abierto')

    def test_estado_conflicto_attributes(self):
        self.assertEqual(self.estado_conflicto.id_estado_conflicto, 1)
        self.assertEqual(self.estado_conflicto.nombre_estado_conflicto, 'abierto')
        self.assertIsNone(self.estado_conflicto.fecha_baja_estado_conflicto)


class TestConflicto(unittest.TestCase):
    def setUp(self):
        estado_conflicto = EstadoConflicto(id_estado_conflicto=1, nombre_estado_conflicto='abierto')
        self.conflicto = Conflicto(id_conflicto=1, fecha=datetime(2023, 6, 10), nombre='Conflicto de prueba',
                                   estado_conflicto=estado_conflicto)

    def test_conflicto_attributes(self):
        self.assertEqual(self.conflicto.id_conflicto, 1)
        self.assertEqual(self.conflicto.fecha, datetime(2023, 6, 10))
        self.assertEqual(self.conflicto.nombre, 'Conflicto de prueba')
        self.assertEqual(self.conflicto.estado_conflicto.id_estado_conflicto, 1)
        self.assertEqual(self.conflicto.estado_conflicto.nombre_estado_conflicto, 'abierto')
        self.assertIsNone(self.conflicto.estado_conflicto.fecha_baja_estado_conflicto)


class TestPago(unittest.TestCase):
    def setUp(self):
        estado_pago = EstadoPago(id_estado_pago=1, nombre_estado_pago='completado')
        self.pago_sin_conflicto = Pago(id_pago=1, estado_pago=estado_pago, fecha_pago=datetime(2023, 6, 10))

        estado_conflicto = EstadoConflicto(id_estado_conflicto=1, nombre_estado_conflicto='Resuelto')
        conflicto = Conflicto(id_conflicto=1, fecha=datetime(2023, 6, 10), nombre='Conflicto de prueba',
                              estado_conflicto=estado_conflicto)
        self.pago_con_conflicto = Pago(id_pago=2, estado_pago=estado_pago, fecha_pago=datetime(2023, 6, 10),
                                       conflicto=conflicto)

    def test_pago_attributes_sin_conflicto(self):
        self.assertEqual(self.pago_sin_conflicto.id_pago, 1)
        self.assertEqual(self.pago_sin_conflicto.estado_pago.id_estado_pago, 1)
        self.assertEqual(self.pago_sin_conflicto.estado_pago.nombre_estado_pago, 'completado')
        self.assertIsNone(self.pago_sin_conflicto.estado_pago.fecha_baja_estado_pago)
        self.assertEqual(self.pago_sin_conflicto.fecha_pago, datetime(2023, 6, 10))
        self.assertIsNone(self.pago_sin_conflicto.conflicto)

    def test_pago_attributes_con_conflicto(self):
        self.assertEqual(self.pago_con_conflicto.id_pago, 2)
        self.assertEqual(self.pago_con_conflicto.estado_pago.id_estado_pago, 1)
        self.assertEqual(self.pago_con_conflicto.estado_pago.nombre_estado_pago, 'completado')
        self.assertIsNone(self.pago_con_conflicto.estado_pago.fecha_baja_estado_pago)
        self.assertEqual(self.pago_con_conflicto.fecha_pago, datetime(2023, 6, 10))
        self.assertIsNotNone(self.pago_con_conflicto.conflicto)
        self.assertEqual(self.pago_con_conflicto.conflicto.id_conflicto, 1)

    def test_pago_nombre_estado_pago(self):
        nombre_estado = Pago.ver_estado_pago(self.pago_sin_conflicto)
        self.assertEqual(nombre_estado, "completado")


class TestDetallePago(unittest.TestCase):
    def setUp(self):
        self.detalle_pago = DetallePago(id_detalle_pago=101, titular_tarjeta='John Doe', cant_cuotas=12, monto=100.0,
                                        factura='F001')

    def test_detalle_pago_attributes(self):
        self.assertEqual(self.detalle_pago.id_detalle_pago, 101)
        self.assertEqual(self.detalle_pago.titular_tarjeta, 'John Doe')
        self.assertEqual(self.detalle_pago.cant_cuotas, 12)
        self.assertEqual(self.detalle_pago.monto, 100.0)
        self.assertEqual(self.detalle_pago.factura, 'F001')


if __name__ == '__main__':
    unittest.main()
