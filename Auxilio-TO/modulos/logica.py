from informacoes import informacoes, categorias

anos = float(input("Digite a idade em anos e meses: "))

def iniciar_faixa_etaria(anos):
    match anos:
        case _ if 0 < anos < 1:
            faixa_etaria = '0 a 1 anos'
        case _ if 1 <= anos < 2:
            faixa_etaria = '1 a 2 anos'
        case _ if 2 <= anos < 3:
            faixa_etaria = '2 a 3 anos'
        case _ if 3 <= anos < 4:
            faixa_etaria = '3 a 4 anos'
        case _ if 4 <= anos < 5:
            faixa_etaria = '4 a 5 anos'
        case _ if 5 <= anos < 6:
            faixa_etaria = '5 a 6 anos'
        case _:
            print("Idade fora do intervalo suportado.")
            exit()



def obter_infomacoes(faixa_etaria):
    respostas_usuario = []
    for item in informacoes[faixa_etaria]:
        print(f"Pergunta:{item['id']}\nTexto: {item['texto']}\n")
        item['resposta_usuario'] = input("Digite sua resposta:")
        respostas_usuario.append((item['id'], item['resposta_usuario']))

    print(respostas_usuario)