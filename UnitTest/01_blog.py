# Implementar una clase Usuario que tenga:
# Metodos: obtener_titulo(), obtener_autor()

class Blog:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def obtener_titulo(self):
        return self.titulo

    def obtener_autor(self):
        return self.autor
    
blog = Blog("Harry Potter", "JK Rowlling")
titulo = blog.obtener_titulo()

if titulo == "Harry Potter":
    print("Prueba exitosa")
else:
    print("Prueba fallida")
#---------------------------------------------------#
blog = Blog("Harry Potter", "JK Rowlling")
autor = blog.obtener_autor()

if autor == "JK Rowlling":
    print("Prueba exitosa")
else:
    print("Prueba fallida")