from controllers.cliente_controller import ClienteController
from controllers.cuenta_controller import CuentaController


cliente_controller = ClienteController()
cuenta_controller = CuentaController()


while True:

    print("\n===================================")
    print("       PLATAFORMA BANCARIA")
    print("===================================")
    print("1. Registrar cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente")
    print("4. Actualizar cliente")
    print("5. Eliminar cliente")
    print("-----------------------------------")
    print("6. Crear cuenta")
    print("7. Listar cuentas")
    print("8. Buscar cuenta")
    print("9. Actualizar cuenta")
    print("10. Eliminar cuenta")
    print("-----------------------------------")
    print("11. Salir")


    opcion = input("\nSeleccione una opción: ")


    if opcion == "1":
        cliente_controller.registrar_cliente()

    elif opcion == "2":
        cliente_controller.listar_clientes()

    elif opcion == "3":
        cliente_controller.buscar_cliente()

    elif opcion == "4":
        cliente_controller.actualizar_cliente()

    elif opcion == "5":
        cliente_controller.eliminar_cliente()

    elif opcion == "6":
        cuenta_controller.crear_cuenta()

    elif opcion == "7":
        cuenta_controller.listar_cuentas()

    elif opcion == "8":
        cuenta_controller.buscar_cuenta()

    elif opcion == "9":
        cuenta_controller.actualizar_cuenta()

    elif opcion == "10":
        cuenta_controller.eliminar_cuenta()

    elif opcion == "11":
        print("\n¡Hasta luego!")
        break

    else:
        print("\n❌ Opción inválida.")