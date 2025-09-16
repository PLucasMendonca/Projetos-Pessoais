from modulos.logica import iniciar_faixa_etaria, obter_informacoes
from modulos.models import Crianca

def main():
    nome = input("Digite o nome da criança: ")
    idade = float(input("Digite a idade em anos e meses: "))
    patologia = input("Digite a patologia da criança: ")

    crianca = Crianca(nome, idade, patologia)
    faixa_etaria = iniciar_faixa_etaria(idade)
    respostas = obter_informacoes(faixa_etaria)

    for pergunta_id, resposta in respostas:
        crianca.responder(pergunta_id, resposta)

    print("\n📌 Respostas registradas:")
    for pid, resp in crianca._respostas.items():
        print(f"{pid}: {resp}")

if __name__ == "__main__":
    main()
