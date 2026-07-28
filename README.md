# 🏦 Plataforma Bancaria

![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-blue)
![Lenguaje](https://img.shields.io/badge/Lenguaje-Python-yellow)
![Almacenamiento](https://img.shields.io/badge/Almacenamiento-JSON-green)

---

# 📌 Información del Proyecto

## Plataforma Bancaria

Sistema desarrollado para la gestión básica de procesos bancarios, permitiendo administrar clientes y cuentas mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

El proyecto implementa una solución organizada utilizando programación orientada a objetos, separación por módulos y almacenamiento de información mediante archivos JSON.

---

# 👩‍💻 Integrantes del Proyecto

| Integrante | Rol |
|---|---|
| Michel | Desarrollo del sistema |
| Daniela | Desarrollo y documentación |
| Isabel Valencia | Desarrollo y gestión del proyecto |

---

# 🎓 Información Académica

**Programa:** Análisis y Desarrollo de Software (ADSO)  
**Ficha:** 3406451  
**Entidad:** Servicio Nacional de Aprendizaje - SENA  

---

# 📖 Descripción del Proyecto

La Plataforma Bancaria es una aplicación desarrollada en lenguaje Python orientada a la administración de información bancaria básica.

El sistema permite gestionar clientes y cuentas mediante módulos independientes, facilitando la organización del código, mantenimiento del sistema y futuras ampliaciones.

La aplicación implementa operaciones CRUD para administrar la información almacenada.

Actualmente permite:

- Registrar clientes.
- Listar clientes.
- Buscar clientes.
- Actualizar clientes.
- Eliminar clientes.
- Crear cuentas bancarias.
- Listar cuentas.
- Buscar cuentas.
- Actualizar cuentas.
- Eliminar cuentas.

---

# 🎯 Objetivo General

Desarrollar una plataforma bancaria básica que permita administrar clientes y cuentas mediante operaciones CRUD, aplicando principios de programación orientada a objetos, organización modular y buenas prácticas de desarrollo de software.

---

# 🎯 Objetivos Específicos

- Diseñar una estructura organizada del proyecto.
- Implementar clases utilizando programación orientada a objetos.
- Crear controladores para manejar la lógica del sistema.
- Gestionar información mediante archivos JSON.
- Implementar operaciones CRUD completas.
- Aplicar control de versiones utilizando Git y GitHub.
- Trabajar mediante ramas y procesos de integración.
- Documentar el desarrollo del proyecto.

---

# 🏗️ Arquitectura del Proyecto

El sistema está organizado mediante una arquitectura basada en modelos y controladores.
Plataforma-Bancaria

│
├── controllers
│ ├── cliente_controller.py
│ └── cuenta_controller.py
│
├── models
│ ├── cliente.py
│ └── cuenta.py
│
├── data
│ ├── clientes.json
│ └── cuentas.json
│
├── main.py
│
├── requirements.txt
│
└── README.md

---

# 📂 Estructura del Sistema

## 📁 controllers

Esta carpeta contiene la lógica principal del sistema.

### ClienteController

Permite administrar los procesos relacionados con clientes:

- Registrar clientes.
- Listar clientes.
- Buscar clientes.
- Actualizar clientes.
- Eliminar clientes.

---

### CuentaController

Permite administrar los procesos relacionados con cuentas:

- Crear cuentas.
- Listar cuentas.
- Buscar cuentas.
- Actualizar cuentas.
- Eliminar cuentas.

---

# 📦 Models

Contiene las clases principales utilizadas dentro del sistema.

---

## 👤 Clase Cliente

Representa la información de los clientes registrados.

### Atributos:

- Documento.
- Nombre.
- Apellido.
- Fecha de nacimiento.
- Correo.
- Teléfono.
- Dirección.

---

## 💳 Clase Cuenta

Representa la información de las cuentas bancarias.

### Atributos:

- Número de cuenta.
- Tipo de cuenta.
- Saldo.
- Cliente asociado.

---

# 💻 Tecnologías Utilizadas

## Lenguaje de programación

🐍 Python

---

## Herramientas utilizadas

- Visual Studio Code.
- Git.
- GitHub.
- PowerShell.

---

## Almacenamiento de información

El sistema utiliza archivos JSON:
data/

├── clientes.json
└── cuentas.json

Estos archivos permiten guardar y consultar la información registrada.

---

# 🔄 Funcionalidades del Sistema

# 👤 Módulo de Clientes

## Registrar Cliente

Permite ingresar nuevos clientes al sistema.

Validaciones:

- Verificación de documento existente.
- Almacenamiento de información personal.

---

## Listar Clientes

Permite visualizar todos los clientes registrados.

---

## Buscar Cliente

Permite encontrar un cliente mediante su documento.

---

## Actualizar Cliente

Permite modificar la información almacenada de un cliente.

---

## Eliminar Cliente

Permite eliminar registros existentes.

---

# 💳 Módulo de Cuentas

## Crear Cuenta

Permite crear una cuenta bancaria asociada a un cliente.

---

## Listar Cuentas

Permite visualizar las cuentas registradas.

---

## Buscar Cuenta

Permite consultar una cuenta específica.

---

## Actualizar Cuenta

Permite modificar información relacionada con una cuenta.

---

## Eliminar Cuenta

Permite eliminar una cuenta registrada.

---

# 🖥️ Instalación y Ejecución

## Requisitos

Tener instalado:

- Python 3.x
- Git
- Visual Studio Code

---

## Clonar el proyecto

Ejecutar:

```bash
git clone URL_DEL_REPOSITORIO
