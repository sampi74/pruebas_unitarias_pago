# Archivo: models.py

from datetime import datetime


class EstadoPago:
    def __init__(self, id_estado_pago, nombre_estado_pago, fecha_baja_estado_pago=None):
        self.id_estado_pago = id_estado_pago
        self.nombre_estado_pago = nombre_estado_pago
        self.fecha_baja_estado_pago = fecha_baja_estado_pago

    def __repr__(self):
        return (f"EstadoPago(id_estado_pago={self.id_estado_pago}, "
                f"nombre_estado_pago={self.nombre_estado_pago}, "
                f"fecha_baja_estado_pago={self.fecha_baja_estado_pago})")


class EstadoConflicto:
    def __init__(self, id_estado_conflicto, nombre_estado_conflicto, fecha_baja_estado_conflicto=None):
        self.id_estado_conflicto = id_estado_conflicto
        self.nombre_estado_conflicto = nombre_estado_conflicto
        self.fecha_baja_estado_conflicto = fecha_baja_estado_conflicto

    def __repr__(self):
        return (f"EstadoConflicto(id_estado_conflicto={self.id_estado_conflicto}, "
                f"nombre_estado_conflicto={self.nombre_estado_conflicto}, "
                f"fecha_baja_estado_conflicto={self.fecha_baja_estado_conflicto})")


class Conflicto:
    def __init__(self, id_conflicto, fecha, nombre, estado_conflicto):
        self.id_conflicto = id_conflicto
        self.fecha = fecha
        self.nombre = nombre
        self.estado_conflicto = estado_conflicto

    def __repr__(self):
        return (f"Conflicto(id_conflicto={self.id_conflicto}, fecha={self.fecha}, "
                f"nombre={self.nombre}, estado_conflicto={self.estado_conflicto})")

    def cambiar_estado_conflicto(self,estado_conflicto):
        self.estado_conflicto=estado_conflicto


class Pago:
    def __init__(self, id_pago, estado_pago, fecha_pago, conflicto=None):
        self.id_pago = id_pago
        self.estado_pago = estado_pago
        self.fecha_pago = fecha_pago
        self.conflicto = conflicto

    def __repr__(self):
        return (f"Pago(id_pago={self.id_pago}, estado_pago={self.estado_pago}, "
                f"fecha_pago={self.fecha_pago}, conflicto={self.conflicto})")

    def ver_estado_pago(self):
        nombre_estado = self.estado_pago.nombre_estado_pago
        return nombre_estado
    
    def agregar_conflicto_a_pago(self,conflicto):
        self.conflicto=conflicto

    def cambiar_estado_pago(self,estado_pago):
        self.estado_pago=estado_pago


class DetallePago:
    def __init__(self, id_detalle_pago, titular_tarjeta, cant_cuotas, monto, factura):
        self.id_detalle_pago = id_detalle_pago
        self.titular_tarjeta = titular_tarjeta
        self.cant_cuotas = cant_cuotas
        self.monto = monto
        self.factura = factura

    def __repr__(self):
        return (f"DetallePago(id_detalle_pago={self.id_detalle_pago}, "
                f"titular_tarjeta={self.titular_tarjeta}, cant_cuotas={self.cant_cuotas}, "
                f"monto={self.monto}, factura={self.factura})")
