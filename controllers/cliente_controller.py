import json
import os
from models.cliente import Cliente


class ClienteController:

    def __init__(self):
        self.archivo = "data/clientes.json"


    def cargar_clientes(self):
        if not os.path.exists(self.archivo):
            return []

        with open(self.archivo, "r", encoding="utf-8") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return []


    def guardar_clientes(self, clientes):
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            json.dump(clientes, archivo, indent=4, ensure_ascii=False)


    # ================= REGISTRAR =================

    def registrar_cliente(self):

        print("\n========== REGISTRAR CLIENTE ==========")

        documento = input("Documento: ")

        clientes = self.cargar_clientes()

        for cliente in clientes:
            if cliente["documento"] == documento:
                print("\n❌ Ya existe un cliente con ese documento.")
                return


        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        fecha_nacimiento = input("Fecha de nacimiento (AAAA-MM-DD): ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")


        nuevo_cliente = Cliente(
            documento,
            nombre,
            apellido,
            fecha_nacimiento,
            correo,
            telefono,
            direccion
        )


        clientes.append(nuevo_cliente.to_dict())

        self.guardar_clientes(clientes)

        print("\n✅ Cliente registrado correctamente.")



    # ================= LISTAR =================

    def listar_clientes(self):

        clientes = self.cargar_clientes()

        print("\n========== LISTA DE CLIENTES ==========")

        if not clientes:
            print("❌ No hay clientes registrados.")
            return


        for cliente in clientes:

            print("\n----------------------------")
            print("Documento:", cliente["documento"])
            print("Nombre:", cliente["nombre"])
            print("Apellido:", cliente["apellido"])
            print("Fecha nacimiento:", cliente["fecha_nacimiento"])
            print("Correo:", cliente["correo"])
            print("Teléfono:", cliente["telefono"])
            print("Dirección:", cliente["direccion"])



    # ================= BUSCAR =================

    def buscar_cliente(self):

        documento = input("\nIngrese documento del cliente: ")

        clientes = self.cargar_clientes()


        for cliente in clientes:

            if cliente["documento"] == documento:

                print("\n✅ Cliente encontrado")

                print("----------------------------")
                print("Nombre:", cliente["nombre"])
                print("Apellido:", cliente["apellido"])
                print("Correo:", cliente["correo"])
                print("Teléfono:", cliente["telefono"])
                print("Dirección:", cliente["direccion"])

                return


        print("\n❌ Cliente no encontrado.")



    # ================= ACTUALIZAR =================

    def actualizar_cliente(self):

        documento = input("\nDocumento del cliente a actualizar: ")

        clientes = self.cargar_clientes()


        for cliente in clientes:

            if cliente["documento"] == documento:


                print("\nActualizar datos")


                cliente["nombre"] = input(
                    "Nuevo nombre: "
                )

                cliente["apellido"] = input(
                    "Nuevo apellido: "
                )

                cliente["correo"] = input(
                    "Nuevo correo: "
                )

                cliente["telefono"] = input(
                    "Nuevo teléfono: "
                )

                cliente["direccion"] = input(
                    "Nueva dirección: "
                )


                self.guardar_clientes(clientes)


                print("\n✅ Cliente actualizado correctamente.")

                return


        print("\n❌ Cliente no encontrado.")



    # ================= ELIMINAR =================

    def eliminar_cliente(self):

        documento = input("\nDocumento del cliente a eliminar: ")

        clientes = self.cargar_clientes()


        for cliente in clientes:

            if cliente["documento"] == documento:

                clientes.remove(cliente)

                self.guardar_clientes(clientes)

                print("\n✅ Cliente eliminado correctamente.")

                return


        print("\n❌ Cliente no encontrado.")