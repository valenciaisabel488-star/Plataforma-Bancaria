from controllers.cliente_controller import ClienteController


controller = ClienteController()


while True:

    print("\n===================================")
    print("       PLATAFORMA BANCARIA")
    print("===================================")
    print("1. Registrar cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente")
    print("4. Actualizar cliente")
    print("5. Eliminar cliente")
    print("6. Salir")


    opcion = input("\nSeleccione una opción: ")


    if opcion == "1":

        controller.registrar_cliente()


    elif opcion == "2":

        controller.listar_clientes()


    elif opcion == "3":

        controller.buscar_cliente()


    elif opcion == "4":

        controller.actualizar_cliente()


    elif opcion == "5":

        controller.eliminar_cliente()


    elif opcion == "6":

        print("\n¡Hasta luego!")
        break


    else:

        print("\n❌ Opción inválida.")