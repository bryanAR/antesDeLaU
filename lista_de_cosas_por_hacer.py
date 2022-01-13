"""
Usando las estructuras de condicion agregar los siguientes casos:

- Si hoy es lunes (1) ir a cobrar; sumar a la billetera el sueldo
- Si es martes(2) ir a comprar pizza y restar el costo de la pizza de la billetera
- Si es miercoles(3) o jueves(4) ir a pasear; si me roban perder la mitad de la plata
de mi billtera
- Si es viernes(5) ir a trabajar y restar los 10 del transporte
- Si es sabado(6) ir al poker y apostar todo, si gano duplico mi plata si pierda quedo con 2
- Si es domingo(7), no hacer nada

NOTA:
Antes del 15 de enero ganas 50.000$
"""





if "cobrar= dinero" :
    print("hoy es lunes(1),fue a cobrar")
    print("cobro la suma de 10500")
elif 10500:

    print("el martes(2) fue a comprar pizza y costo 1000")
    print("resta de la compra de la pizza",10500-1000)

elif ("el miercoles") or ("el jueves, va a un viaje "):
    print("tuve un viaje y me robaron la mitad de la plata", 10500//2)
elif 5250:

    print("fue a trabajar","resta el tranporte", 5250-10)
elif 5240:

    print(" fue y aposto todo")
    print("tiene la posibilidad que pierda todo o duplique su dinero, si saca 1 gana o si saca 0 pierde")


saca_1_gana=int(input( "que numero sacaria? "))
saca_0_pierde=0

if  saca_1_gana > saca_0_pierde:
    print("duplique wiiiiiiiiiiiiiiiiii")
else:
    print("noooooo solo quede con 2 ")

print ("el domingo(7) no hace nada en todo el dia")