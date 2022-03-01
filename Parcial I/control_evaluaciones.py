'''
El departamento de computación lo contrata a usted para que desarrolle un programa que, determine
los resultados del primer parcial de un grupo de estudiantes, al programa se le suministra la siguiente información: 

Nombre del estudiante, Hora y minutos de llegada a la prueba.

Y si logra entrar a la prueba, lea:
La Hora y los minutos de salida, así como también la calificación obtenida en la prueba.

Procese la información anterior y determine e imprima por consola:

Para cada estudiante:
1)Si pudo entrar o no a la prueba indicándolo con un mensaje, en caso de entrar en cuánto tiempo desarrolló la prueba en horas y minutos. 
2)Si llegó temprano a la prueba indíquelo con un mensaje y cuánto tiempo espero para entrar a la misma en minutos.

Para todos los estudiantes:
3)El Porcentaje de estudiantes que llegaron temprano con respecto al total que entraron a la prueba.
4)Cuántos estudiantes se procesaron antes de encontrar el primer estudiante que no entró la prueba.
5)El Promedio de las notas de los estudiantes que llegaron después de transcurridos 20 minutos de haber comenzado la prueba.

Consideraciones:
Una hora tiene 60 minutos.
La prueba comienza a las 8:00 AM (480 minutos de día) y termina a las 10:00 AM (600 minutos de día)
Todo estudiante que llegue a la 9:01 AM (541 minutos del día) o después no entra a la prueba.

VARIABLES DE ENTRADA
nombre = "" 'Nombre del estudiante
hh_lleg, mm_lleg ' Hora y minutos de llegada a la prueba
hh_sal, mm_sal 'Hora y minutos de salida
Calificación 'calificación obtenida en la prueba
resp

VARIABLES DE PROCESO
min_tot_ent, min_tot_sal
tot_est_temp, tot_est_ent
band
acum_notas e '5)
est_tar_20min  '5)

VARIABLES DE SALIDA
hor_presen, min_presen '1) Si pudo entrar o no a la prueba indicándolo con un mensaje, en caso de entrar en cuánto tiempo desarrolló la prueba en horas y minutos
min_esp  '2) Si llegó temprano a la prueba indíquelo con un mensaje y cuánto tiempo espero para entrar a la misma en minutos
porc_est_temp  '3) Porcentaje de estudiantes que llegaron temprano con respecto al total que entraron a la prueba.
prim_est_Ent  '4) Cuántos estudiantes se procesaron antes de encontrar el primer estudiante que no entró la prueba
prom_notas_20min  '5) Promedio de las notas de los estudiantes que llegaron después de transcurridos 20 minutos de haber comenzado la prueba
'''

# INICIALIZACIÓN DE VARIABLES
resp= 0
band = 0
tot_est_temp = 0
tot_est_ent = 0
acum_notas = 0
est_tar_20min = 0

while resp == 0:
    # Lectura de datos
    nombre = input("Nombre del Estudiante: ")
    hh_lleg = int(input("Hora de llegada: "))
    mm_lleg = int(input("Minutos de llegada: "))

    # Conversión a minutos de la hora y minutos de entrada
    min_tot_ent = hh_lleg * 60 + mm_lleg

    if min_tot_ent < 541: # El estudiante pudo entrar
        print("Ha llegado a tiempo, puede presentar")
        hh_sal = int(input("Hora de salida: "))
        mm_sal = int(input("Minuto de salida: "))
        calificación = int(input("Calificación: "))

        tot_est_ent += 1
        min_tot_sal = hh_sal * 60 + mm_sal

        if min_tot_ent >= 480:
            hor_presen = (min_tot_sal - min_tot_ent) // 60
            min_presen = (min_tot_sal - min_tot_ent) % 60

            if min_tot_ent > 500: # 5) 20 minutos después de comenzar la prueba
                acum_notas += calificación
                est_tar_20min += 1

        else:  # Llego temprano
            hor_presen = (min_tot_sal - 480) // 60
            min_presen = (min_tot_sal - 480) % 60

            print("Ha llegado temprano, y")
            min_esp = 480 - min_tot_ent
            print("2) Tardo " & min_esp & " en presentar")
            tot_est_temp += 1

        print("1) Realizó la prueba en " , hor_presen , " Horas y " , min_presen , " Minutos.")

    else:  # El estudiante no pudo entrar

        if band == 0:
            prim_est_ent = tot_est_ent  # 4) Guarda cuantos estudiantes se procesaron antes de encontrar el primer estudiante que no entró la prueba
            band = 1

        print("Ha llegado tarde, no puede presentar")

    resp = int(input("Desea ingresar otro estudiante (si=0,no=l): "))

if tot_est_ent != 0:
    porc_est_temp = tot_est_temp / tot_est_ent * 100
    print("3) Porcentaje de estudiantes que llegaron temprano con respecto al total que logro entrar= " , porc_est_temp , "%")
else:
    print("3) Ningún estudiante llegó temprano")

print("4) Estudiantes que entraron a la prueba antes del primero en llegar tarde= " , prim_est_ent)

if est_tar_20min != 0:
    prom_notas_20min = acum_notas / est_tar_20min
    print("5) Promedio de notas de los estudiantes que llegaron después de 20 min= " , prom_notas_20min)
else:
    print("5) Ningún estudiante llegó después de los 20 min")
