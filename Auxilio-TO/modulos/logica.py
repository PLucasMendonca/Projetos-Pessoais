from modulos.informacoes import informacoes
from modulos.informacoes import categorias


def iniciar_faixa_etaria(anos):
    match anos:
        case _ if 0 < anos < 1:
            return '0 a 1 anos'
        case _ if 1 <= anos < 2:
            return '1 a 2 anos'
        case _ if 2 <= anos < 3:
            return '2 a 3 anos'
        case _ if 3 <= anos < 4:
            return '3 a 4 anos'
        case _ if 4 <= anos < 5:
            return '4 a 5 anos'
        case _ if 5 <= anos < 6:
            return '5 a 6 anos'
        case _:
            print("Idade fora do intervalo suportado.")
            exit()

def obter_informacoes(faixa_etaria):
    respostas_usuario = []
    for item in informacoes[faixa_etaria]:
        print(f"Pergunta: {item['id']}\nTexto: {item['texto']}\n")
        item['resposta_usuario'] = input("Digite sua resposta: sim/não: ").strip().lower()
        respostas_usuario.append((item['id'], item['resposta_usuario']))
    return respostas_usuario

def processar_perguntas_nao(faixa_etaria):
    perguntas = informacoes[faixa_etaria]
    ids_nao = sorted([item['id'] for item in perguntas if item['resposta_usuario'] == 'não'])
    print(f"IDs das perguntas respondidas com NÃO: {ids_nao}")

    resultado = {}
    for categoria, subcats in categorias.items():
        if isinstance(subcats, list):
            subcats = {"Principal": subcats}
        
        for subcat, id_list in subcats.items():
            ids_encontrados = [id_ for id_ in ids_nao if id_ in id_list]
            if ids_encontrados:
                if categoria not in resultado:
                    resultado[categoria] = {}
                if subcat not in resultado[categoria]:
                    resultado[categoria][subcat] = []

                for id_nao in ids_encontrados:
                    anteriores = [i for i in id_list if i < id_nao]
                    resultado[categoria][subcat].extend(anteriores)
                
                resultado[categoria][subcat] = sorted(set(resultado[categoria][subcat]))

    for categoria, subcats in resultado.items():
        print(f"\nCategoria: {categoria}")
        for subcat, ids in subcats.items():
            print(f"  Subcategoria: {subcat}")
            print(f"    IDs anteriores ou iguais ao 'não': {ids}")
    
    return resultado

def condicoes_fluxo(faixa_etaria):

    perguntas = informacoes[faixa_etaria]
    total = len(perguntas)
    sim_count = sum(1 for item in perguntas if item['resposta_usuario'] == 'sim')
    nao_count = sum(1 for item in perguntas if item['resposta_usuario'] == 'não')
    
    print(f"Total de perguntas: {total}")
    print(f"Sim: {sim_count}, Não: {nao_count}")
    
    if sim_count >= total / 2:
        print("Metade ou mais das respostas são SIM → ação 1")
    else:
        processar_perguntas_nao(faixa_etaria)
    