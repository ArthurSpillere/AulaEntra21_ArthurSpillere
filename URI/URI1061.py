minuto_d = 0
hora_d = 0
dia_d = 0

#Entrada
#Data Inicio (i)
quando_i = input().split()
dia_i = int(quando_i[1])

horario_i = input().split(' : ')
hora_i, minuto_i, segundo_i = int(horario_i[0]), int(horario_i[1]), int(horario_i[2])

#Data Término (f)
quando_f = input().split()
dia_f = int(quando_f[1])

horario_f = input().split(' : ')
hora_f, minuto_f, segundo_f = int(horario_f[0]), int(horario_f[1]), int(horario_f[2])

#Calcula duração do evento (d)
dif_seg = segundo_f - segundo_i
dif_min = minuto_f - minuto_i
dif_hora = hora_f - hora_i
dif_dia = dia_f - dia_i

#Segundos
if dif_seg >= 0:
    segundo_d = dif_seg    
else:
    segundo_d = 60 + dif_seg
    minuto_d -= 1

#Minutos
if dif_min >= 0:
    minuto_d += dif_min
else:
    minuto_d += 60 + dif_seg
    hora_d -= 1

#Horas e Dias
if dif_hora >= 0:
    hora_d += dif_hora
    dia_d += dif_dia
else:
    hora_d += 24 + dif_hora
    dia_d += dif_dia - 1    

print(f"""{dia_d} dia(s)
{hora_d} hora(s)
{minuto_d} minuto(s)
{segundo_d} segundo(s)""")
