class Cliente:
    def __init__(self, documento, nombre, apellido, fecha_nacimiento, correo, telefono, direccion):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion

    def to_dict(self):
        return {
            "documento": self.documento,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha_nacimiento": self.fecha_nacimiento,
            "correo": self.correo,
            "telefono": self.telefono,
            "direccion": self.direccion
        }