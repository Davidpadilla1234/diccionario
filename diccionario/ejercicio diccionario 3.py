usuarios usuarios= {
    "iperurena" : {
            "nombre" : "Iñaki" ,
               "apellido" : "Perurena" ,
               "contraseña" : "123123"
          },
    "fmuguruza" : {
            "nombre" : "Fermin" ,
                "apellido" : "Muguruza" ,
                "contraseña" : "654321"
          },
    "aolaizola" : {
            "nombre" : "Aimar" ,
                "apellido" : "Olaizola" ,
                "contraseña" : "123456"
          }
     }
p = 0
lista = []
para  clave  en  usuarios . artículos ():
    usuario = str ( input ( "Ingrese su usuario: " ))
    contraseñ a = int ( input ( " Ingrese contraseña: " ))
    lista _ agregar ( clave )
    si  usuario  en  lista  y  contrase ñ a  en  lista :
        pag = pag + 1
        imprimir ( "incorrecto" )
    más :
        imprimir ( usuarios [ usuario ][ "nombre" ])
        imprimir ( usuarios [ usuario ][ "apellido" ])
        descanso
    si ( p == 3 ):
        print ( "Cuenta bloqueada" )
        descanso