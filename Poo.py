class Personaje:

    def __init__(self, nombre, salud_max):
        self.nombre = nombre
        self._salud = salud_max
        self.salud_max = salud_max
        self.inventario = ['pan', 'cafe']
    
    @property
    def salud(self):
        return self._salud
    
    @salud.setter
    def salud(self, nueva_salud):
        if nueva_salud <= 0:
            self._salud=0
            print("muerto")

        elif nueva_salud > self.salud_max:
            self._salud=self.salud_max

        else:
            self._salud=nueva_salud
            print("actualizada")
    
    @salud.deleter
    def salud(self):
        print("alerta")
    
    def _efecto_sonido_curacion(self):
        print("efecto de sonido")
    
    def tomar_pocion(self, cantidad_curacion):
        print("curacion")
        self._efecto_sonido_curacion()
        self.salud = self.salud + cantidad_curacion
    
    #Métodos mágicos
    def __str__(self):
        '''Se activa cuando se usa print(objeto) o srt(objeto)'''
        return f"Personaje {self.nombre} | HP {self.salud} / {self.salud_max}"

    def __repr__(self):
        '''Este metodo es para debug y funciona al inspeccionar un objeto'''
        return f"Personaje('{self.nombre}', {self.salud_max})"
    
    def __gt__(self, otro_personaje):
        '''Se activa al usar el operador >'''
        return self.salud_max > otro_personaje.salud_max
    
    def __add__(self, otro_personaje):
        '''se aciva al usar el simbolo +'''
        print(f"fusión entre {self.nombre} y {otro_personaje.nombre}")

        nuevo_nombre = f"{self.nombre[:3]}{otro_personaje.nombre[3:]}"
        nueva_salud = self.salud_max+otro_personaje.salud_max

        return Personaje(nuevo_nombre, nueva_salud)
    
    def __len__(self):
        '''Se activa al usar la función len(objeto)'''
        return len(self.inventario)
    
    def __eq__(self, otro_personaje):
        '''se activa al usar el operador =='''
        return self.size == otro_personaje.size
    
    def __lt__(self, otro_personaje):
        '''se activa al usar el operador <='''
        return self.salud_max < otro_personaje.salud_max

    @classmethod # decorador para generico
    def crear_npc(cls):
        '''Crea un personaje'''
        print("creando npc")
        return cls(nombre='aldeano generico', salud_max=10)
    
    @staticmethod # decorador para método estatico
    def mostrar_manual_juego():
        '''funciona sin necesidad de crear un personaje (objeto) ni usar la clase'''
        print("Manual de juego...")

class Guerrero(Personaje):

    def __init__(self, nombre, salud_max, puntos_armadura):
        super().__init__(nombre, salud_max)
        self.puntos_armadura = puntos_armadura
    
    def recibir_daño(self, daño_enemigo):
        print(f"ocurrió un ataque")

        daño_real = daño_enemigo - self.puntos_armadura
        if daño_real < 0: daño_real = 0

        self.salud = self.salud - daño_real

    def __str__(self):
        base = super().__str__()
        return f"{base} | Armadura: {self.puntos_armadura}"
    
    @classmethod
    def crear_guerrero_generico(cls):
        print("crea un guerrero cualquiera")
        return cls(nombre="juan perez", salud_max=200, puntos_armadura=30)
    

#clase nueva que herede de personaje.
class Monstruo(Personaje):

    def __init__(self, nombre, salud_max, poder):
        super().__init__(nombre, salud_max)
        self.poder = poder

    def __str__(self):
        base = super().__str__()
        return f"{base} | Poder: {self.poder}"
    
    # def __repr__(self):
    #     '''nuevo método magico repr para Monstruo'''
    #     repr = super().__repr__()
    #     return repr

    # def __gt__(self, otro_personaje):
    #     greater = super().__gt__(otro_personaje)
    #     return greater
    
    # def __add__(self, otro_personaje):
    #     return super().__add__(otro_personaje)
    
if __name__=='__main__':
    ilze=Personaje('ilze',30)
    musta=Guerrero('musta',20,30)
    # dragon=Monstruo('dragon', 100, 'fuego')
    