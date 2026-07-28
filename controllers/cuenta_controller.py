import json
import os

from models.cuenta import Cuenta


class CuentaController:


    def __init__(self):

        self.archivo = "data/cuentas.json"



    def cargar_cuentas(self):

        if not os.path.exists(self.archivo):
            return []

        with open(self.archivo, "r", encoding="utf-8") as archivo:

            try:
                return json.load(archivo)

            except json.JSONDecodeError:
                return []



    def guardar_cuentas(self, cuentas):

        with open(self.archivo, "w", encoding="utf-8") as archivo:

            json.dump(
                cuentas,
                archivo,
                indent=4,
                ensure_ascii=False
            )



    # ================= CREAR CUENTA =================

    def crear_cuenta(self):

        print("\n========== CREAR CUENTA ==========")


        cuentas = self.cargar_cuentas()


        numero = input("Número de cuenta: ")


        for cuenta in cuentas:

            if cuenta["numero_cuenta"] == numero:

                print("\n❌ La cuenta ya existe.")

                return



        documento = input("Documento del cliente: ")

        tipo = input(
            "Tipo de cuenta (Ahorros/Corriente): "
        )


        while True:

            try:

                saldo = float(
                    input("Saldo inicial: ")
                )

                if saldo < 0:
                    print("❌ El saldo no puede ser negativo.")
                    continue

                break


            except ValueError:

                print("❌ Ingrese un valor válido.")



        nueva_cuenta = Cuenta(
            numero,
            documento,
            tipo,
            saldo
        )


        cuentas.append(
            nueva_cuenta.to_dict()
        )


        self.guardar_cuentas(cuentas)


        print("\n✅ Cuenta creada correctamente.")



    # ================= LISTAR =================


    def listar_cuentas(self):

        cuentas = self.cargar_cuentas()


        print("\n========== LISTA DE CUENTAS ==========")


        if not cuentas:

            print("❌ No existen cuentas registradas.")

            return



        for cuenta in cuentas:

            print("\n----------------------------")

            print(
                "Número:",
                cuenta["numero_cuenta"]
            )

            print(
                "Cliente:",
                cuenta["documento_cliente"]
            )

            print(
                "Tipo:",
                cuenta["tipo_cuenta"]
            )

            print(
                "Saldo:",
                cuenta["saldo"]
            )

            print(
                "Estado:",
                cuenta["estado"]
            )



    # ================= BUSCAR =================


    def buscar_cuenta(self):

        numero = input(
            "\nNúmero de cuenta: "
        )


        cuentas = self.cargar_cuentas()


        for cuenta in cuentas:


            if cuenta["numero_cuenta"] == numero:


                print("\n✅ Cuenta encontrada")

                print("----------------------------")

                print(cuenta)

                return



        print("\n❌ Cuenta no encontrada.")



    # ================= ACTUALIZAR =================


    def actualizar_cuenta(self):

        numero = input(
            "\nNúmero de cuenta: "
        )


        cuentas = self.cargar_cuentas()


        for cuenta in cuentas:


            if cuenta["numero_cuenta"] == numero:


                cuenta["tipo_cuenta"] = input(
                    "Nuevo tipo de cuenta: "
                )


                cuenta["estado"] = input(
                    "Nuevo estado: "
                )


                self.guardar_cuentas(cuentas)


                print(
                    "\n✅ Cuenta actualizada."
                )

                return



        print("\n❌ Cuenta no encontrada.")



    # ================= ELIMINAR =================


    def eliminar_cuenta(self):

        numero = input(
            "\nNúmero de cuenta: "
        )


        cuentas = self.cargar_cuentas()


        for cuenta in cuentas:


            if cuenta["numero_cuenta"] == numero:


                cuentas.remove(cuenta)


                self.guardar_cuentas(cuentas)


                print(
                    "\n✅ Cuenta eliminada."
                )

                return



        print("\n❌ Cuenta no encontrada.")