class Crianca:
    def __init__(self, nome, idade, patologia):
        self._nome = nome
        self._idade = idade
        self.patologia = patologia
        self._respostas = {}

    def responder(self, pergunta_id, resposta):
        self._respostas[pergunta_id] = resposta

    def __str__(self):
        return f"{self._nome} ({self._idade} anos) - {self.patologia}"
