casos = int(input())
repetindo = 0
while casos != 0:
    soma_litros = 0
    soma_pessoas = 0
    repetindo += 1
    resumo = {}

    for i in range(casos):
        pessoas, consumo_imovel = map(int, input().split())
        soma_pessoas += pessoas
        soma_litros += consumo_imovel
        consumo_medio_imovel = float(consumo_imovel/pessoas)

        if str(int(consumo_medio_imovel)) in resumo.keys():
            resumo[str(int(consumo_medio_imovel))] += pessoas
        
        else:
            resumo[str(int(consumo_medio_imovel))] = pessoas

    lista_key = resumo.keys()
    print(lista_key)
    ordenado = sorted(lista_key)
    print(ordenado)
    for key in ordenado:
        print(f"{key}-{resumo[key]}", end = " ")

    # print(f"Cidade# {repetindo}:")
    # for v in resumo_ascendente:
        # print(f"{v[1]}-{int(v[0])}", end = " ")

    consumo_medio_total = soma_litros / soma_pessoas
    print()
    print(f"Consumo médio: {consumo_medio_total - 0.004:.2f} m3.")
    casos = int(input())
    if casos == 0:
        break
    else:
        print()
