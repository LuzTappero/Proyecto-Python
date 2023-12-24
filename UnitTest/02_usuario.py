class Usuario:

    def __init__(self, usuario, email):
        self.usuario = usuario
        self.email = email

    def obtener_usuario(self):
        return self.usuario

    def obtener_email(self):
        return self.email
    
usuario = Usuario("Luz01", "luz@a.com")
usuario = usuario.obtener_usuario()

if usuario == "Luz01":
    print("Prueba exitosa")
else:
    print("Prueba fallida")
#---------------------------------------------------#
usuario = Usuario("Luz01", "luz@a.com")
email = usuario.obtener_email()

if email == "luz@a.com":
    print("Prueba exitosa")
else:
    print("Prueba fallida")