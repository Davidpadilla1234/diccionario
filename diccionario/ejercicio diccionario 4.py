est = {}
est . actualizar ({
        "1" :{
            "nombre" : "Lorea" ,
            "nota" : 8
    },
        "2" : {
            "nombre" : "Markel" ,
            "nota" : 4.2
    },
        "3" : {
            "nombre" : "Julián" ,
            "nota" : 6.5
    }
})

listas = []
lista = []
medios = []
para  i  en el  rango ( 0 , 10 ):
    num = int ( input ( "Numero de estudiante: " ))
    prof = input ( "Nombre del estudiante: " )
    nota = float ( input ( "Nota del estudiante: " ))
    est . actualizar ({ num :{ "nombre" : prof , "nota" : nota }})
para  clave  en  est . teclas ():
    if ( est [ clave ][ "nota" ] <= 5 ):
        listas . agregar ( est [ clave ][ "nombre" ])
    más :
        listaa . agregar ( est [ clave ][ "nombre" ])
    medios _ agregar ( est [ clave ][ "nota" ])
    s = suma ( medios ) / ( len ( listas ) + len ( listaa ))
imprimir ( listas )
imprimir ( listaa )
imprimir ( "{:.1f}" . formato ( s ))