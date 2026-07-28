# 🏦 Plataforma Bancaria

![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-blue)
![Lenguaje](https://img.shields.io/badge/Python-3.x-yellow)
![Base de datos](https://img.shields.io/badge/Almacenamiento-JSON-green)

---

# 📌 Información del Proyecto

## Plataforma Bancaria

Sistema desarrollado para la gestión básica de procesos bancarios, permitiendo administrar clientes y cuentas mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

El proyecto busca implementar una solución organizada utilizando programación orientada a objetos, separación por capas y manejo de información mediante archivos JSON.

---

# 👩‍💻 Integrantes

| Nombre | Rol |
|---|---|
| Michel | Desarrollo del sistema |
| Daniela | Desarrollo y documentación |
| Isabel Valencia | Desarrollo y gestión del proyecto |

---

# 🎓 Formación

**Programa:** Análisis y Desarrollo de Software (ADSO)  
**Ficha:** 3406451  
**Entidad:** Servicio Nacional de Aprendizaje - SENA  

---

# 📖 Descripción del Proyecto

La Plataforma Bancaria es una aplicación desarrollada en Python que permite gestionar información relacionada con clientes y cuentas bancarias.

El sistema cuenta con módulos independientes que facilitan el mantenimiento del código y permiten ampliar nuevas funcionalidades en el futuro.

Actualmente permite:

- Registrar clientes.
- Consultar clientes.
- Actualizar información de clientes.
- Eliminar clientes.
- Crear cuentas bancarias.
- Consultar cuentas.
- Actualizar cuentas.
- Eliminar cuentas.

---

# 🎯 Objetivo General

Desarrollar una plataforma bancaria básica que permita administrar clientes y cuentas mediante operaciones CRUD, aplicando conceptos de programación orientada a objetos y buenas prácticas de desarrollo de software.

---

# 🎯 Objetivos Específicos

- Diseñar una estructura organizada del proyecto.
- Implementar clases utilizando programación orientada a objetos.
- Crear controladores para manejar la lógica del sistema.
- Implementar almacenamiento de información utilizando archivos JSON.
- Aplicar control de versiones mediante Git y GitHub.
- Integrar módulos mediante ramas de desarrollo.

---

# 🏗️ Arquitectura del Proyecto

El sistema está organizado utilizando una estructura basada en modelos y controladores.

```
Plataforma-Bancaria

│
├── controllers
│   ├── cliente_controller.py
│   └── cuenta_controller.py
│
├── models
│   ├── cliente.py
│   └── cuenta.py
│
├── data
│   ├── clientes.json
│   └── cuentas.json
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

# 📂 Descripción de Carpetas

## controllers

Contiene la lógica del sistema.

Incluye:

### ClienteController

Responsable de:

- Registrar clientes.
- Listar clientes.
- Buscar clientes.
- Actualizar clientes.
- Eliminar clientes.


### CuentaController

Responsable de:

- Crear cuentas.
- Listar cuentas.
- Buscar cuentas.
- Actualizar cuentas.
- Eliminar cuentas.

---

# 📦 Models

Contiene las clases principales del sistema.

## Clase Cliente

Representa la información de los usuarios registrados.

Atributos principales:

- Documento
- Nombre
- Apellido
- Fecha de nacimiento
- Correo
- Teléfono
- Dirección


## Clase Cuenta

Representa una cuenta bancaria.

Atributos principales:

- Número de cuenta
- Tipo de cuenta
- Saldo
- Cliente asociado

---

# 💻 Tecnologías Utilizadas

## Lenguaje

🐍 Python

## Herramientas

- Visual Studio Code
- Git
- GitHub
- PowerShell

## Almacenamiento

Archivos JSON:

- clientes.json
- cuentas.json

---

# 🔄 Funcionalidades del Sistema

# 👤 Módulo de Clientes

## Registrar cliente

Permite ingresar nuevos clientes validando que el documento no exista previamente.

## Listar clientes

Muestra todos los clientes registrados.

## Buscar cliente

Permite consultar un cliente mediante su documento.

## Actualizar cliente

Permite modificar información almacenada.

## Eliminar cliente

Permite eliminar registros existentes.

---

# 💳 Módulo de Cuentas

## Crear cuenta

Permite asociar una cuenta bancaria a un cliente.

## Listar cuentas

Muestra las cuentas registradas.

## Buscar cuenta

Permite consultar una cuenta específica.

## Actualizar cuenta

Permite modificar información de una cuenta.

## Eliminar cuenta

Permite eliminar una cuenta registrada.

---

# 🖥️ Ejecución del Proyecto

Para ejecutar el sistema:

1. Descargar el proyecto.

2. Abrir la terminal en la carpeta del proyecto.

3. Ejecutar:

```bash
python main.py
```

---

# 📋 Menú Principal

El sistema presenta las siguientes opciones:

```
1. Registrar cliente
2. Listar clientes
3. Buscar cliente
4. Actualizar cliente
5. Eliminar cliente

6. Crear cuenta
7. Listar cuentas
8. Buscar cuenta
9. Actualizar cuenta
10. Eliminar cuenta

11. Salir
```

---

# 🌳 Control de Versiones

El proyecto utiliza Git Flow para organizar el desarrollo.

Ramas utilizadas:

```
main
develop
feature/registro-clientes
feature/creacion-cuentas
```

Proceso utilizado:

```
Feature
   |
   ↓
Pull Request
   |
   ↓
Develop
   |
   ↓
Main
```

---

# 🧪 Pruebas Realizadas

Se realizaron pruebas de:

✅ Registro de clientes  
✅ Validación de documentos repetidos  
✅ Consulta de clientes  
✅ Actualización de información  
✅ Eliminación de registros  
✅ Creación de cuentas  
✅ Consulta de cuentas  

---

# 🚀 Mejoras Futuras

Algunas funcionalidades que pueden agregarse:

- Interfaz gráfica.
- Conexión con una base de datos real.
- Sistema de autenticación.
- Roles de usuario.
- Reportes bancarios.
- Seguridad avanzada.
- API web.

---

# 📌 Conclusiones

El desarrollo de la Plataforma Bancaria permitió aplicar conocimientos de programación orientada a objetos, manejo de archivos, estructuras de datos y control de versiones.

El proyecto demuestra la importancia de organizar correctamente un sistema mediante módulos independientes, facilitando su mantenimiento y futuras ampliaciones.

---

# 📄 Licencia

Proyecto académico desarrollado para fines educativos.

---

**SENA - Análisis y Desarrollo de Software**  
**Ficha: 3406451**