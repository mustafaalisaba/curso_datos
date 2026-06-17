from Poo import Personaje, Guerrero, Monstruo

def encapsulamiento():
    arturo = Personaje('arturo', 80)
    arturo._salud=40
    # print(arturo)

    # dragon = Monstruo('dragon', 79, 'fuego')
    
    # print(dragon.__repr__())

    # print(dragon.__gt__(arturo))

    # print(dragon.__add__(arturo))

#herencia
def herencia():
    ilse=Personaje('ilze', 100)
    kratos= Guerrero('kratos',100,80)

    kratos.recibir_daño(25)
    kratos.tomar_pocion(900)
    
    print(f"kratos tiene {kratos.puntos_armadura} de armadura")

    print(kratos)

def metodos_magicos():
    ilse=Personaje('ilze', 100)
    kratos= Guerrero('kratos',100,80)

    # print(ilse) # convoca al llamado del método mágico __str__
    # print(repr(ilse)) # __repr__

    # # __gt__
    # if kratos>ilse:
    #     print()
    # else:
    #     print("es menor")
    
    # combinacion = ilse+kratos
    # print(combinacion)

    # kratos.inventario.append("Espada")
    # print(len(kratos))

    # metodos magicos para Monstruo
    dragon = Monstruo('dragon', 79, 'fuego')
    
    print(dragon)
    print(ilse)

    print(repr(dragon))
    print(repr(ilse))
    
    if ilse > dragon:
        print(f"{ilse} es mayor")
    elif ilse < dragon:
        print(f"{ilse} es menor")
    else:
        print("son iguales")
    
    mezcla = dragon+ilse
    print(mezcla)

    dragon.inventario.append("Garras")
    print(len(dragon))

def decoradores():
    Personaje.mostrar_manual_juego()
    Monstruo.mostrar_manual_juego()

    #crear personajes genéricos
    npc = Personaje.crear_npc()
    monstruo_npc = Monstruo.crear_npc()
    
    extra = Guerrero.crear_npc()

    Guerrero.mostrar_manual_juego()

    try:
        del npc.salud
    except AttributeError:
        pass

    # decoradores para Monstruo

if __name__=='__main__':
    print("-----ENCAPSULAMIENTO-----")
    encapsulamiento()
    print("-----HERENCIA-----")
    herencia()
    print("-----MÉTODOS MÁGICOS-----")
    metodos_magicos()