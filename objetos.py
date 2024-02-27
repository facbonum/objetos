""" class Usuario: # convention: uppercase all classnames
    nombre = "Felipe"
    apellido = "Feliz"

usuario = Usuario()

print(usuario) # 

print(usuario.nombre, usuario.apellido) """

""" class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def saludo(self):
        print('Hola!, mi nombre es', self.nombre, self.apellido)



class Admin(Usuario):
    def superSaludo(self):
        print('Hola!, me llamo', self.nombre, ' y soy administrador')

usuario = Usuario('Felipe', 'Feliz')
# usuario2 = Usuario('Chanchito', 'Feliz')

usuario.saludo()
# usuario2.saludo()
usuario.nombre = 'Chanchito'
usuario.saludo()
# del usuario.nombre
# del usuario
# print(usuario)

# instancia de administrador
admin = Admin('Super', 'Feliz')
admin.saludo()
admin.superSaludo()

usuario.superSaludo() """
'''AttributeError: 'Usuario' object has no attribute 'superSaludo
Como pueden ver acá, superSaludo no se encuentra 
definido dentro de la instancia de la clase usuario.'''

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

""" Resumiendo, nuestras clases son el plano de lo que nosotros vamos a querer crear.

En el caso de una casa va a ser el plano de una casa.

En el caso de los usuarios va a ser el plano de cómo se forman o cómo se crean los usuarios.

Y los objetos son instancias de estos planos, como por ejemplo la casa ya construida o el usuario que

de verdad ya existe en una base de datos o en este caso en nuestro código. """

""" 'self' No es necesario que nosotros se lo pasemos como un parámetro a nuestra clase cuando estemos instancias.

Si vamos a necesitar pasar los otros valores.

Que va a necesitar nuestra clase para generar una instancia. """



class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'


class Perro(Animal):
    tipo = 'perro'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()