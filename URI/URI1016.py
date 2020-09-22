v_x = 60
v_y = 90
v_relativa = abs(v_x - v_y)
dist = int(input())
tempo = int((dist/v_relativa)*60)
print(f"{tempo} minutos")
