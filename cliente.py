
class Cliente:
    def __init__(self, apellidos, nombres, correoelectronico, direccion, id_cliente):
        self.apellidos = apellidos
        self.nombres = nombres
        self.correoelectronico = correoelectronico
        self.direccion = direccion
        self.id_cliente = id_cliente

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.id_cliente == other.id_cliente
        return False

    def __hash__(self):
        return hash(self.id_cliente)

    def __repr__(self):
        return f"{self.nombres} {self.apellidos} ({self.id_cliente})"

class Mantenimiento_Cliente:

    def __init__(self):
        self._clientes = []

    def registrar_cliente(self, cliente):
        if cliente not in self._clientes:
            self._clientes.append(cliente)
            print(f"El cliente '{cliente.nombres} {cliente.apellidos}' ha sido registrado.")
        else:
            print(f"El cliente '{cliente.nombres} {cliente.apellidos}' ya está registrado.")
            
    def buscar_cliente_por_id(self, id_cliente):
        for cliente in self._clientes:
            if str(cliente.id_cliente) == str(id_cliente):
                
                print(f"El cliente {id_cliente}, si existe! ")
                return cliente
        print(f"No se encontró ningún cliente con id_cliente {id_cliente}.")
        return None
    
    def obtener_clientes(self):
        return self._clientes
    
    def actualizar_cliente(self, id_cliente, nuevos_apellidos=None, nuevos_nombres=None, nuevo_correoelectronico=None, nueva_direccion=None):
        cliente = self.buscar_cliente_por_id(id_cliente)
        if cliente:
            # Actualizar los campos solo si se proporciona un nuevo valor
            if nuevos_apellidos:
                cliente.apellidos = nuevos_apellidos
            if nuevos_nombres:
                cliente.nombres = nuevos_nombres
            if nuevo_correoelectronico:
                cliente.correoelectronico = nuevo_correoelectronico
            if nueva_direccion:
                cliente.direccion = nueva_direccion
            
            print(f"Cliente '{id_cliente}' ha sido actualizado.")
        else:
            print(f"Cliente con ID '{id_cliente}' no encontrado.")


    def eliminar_cliente(self, id_cliente):
        cliente = self.buscar_cliente_por_id(id_cliente)
        if cliente:
            self._clientes.remove(cliente)
            print(f"El cliente con ID {id_cliente} ha sido eliminado.")
            return True
        else:
            print(f"No se pudo eliminar: cliente con ID {id_cliente} no encontrado.")
            return False
  
    
