class AprovaExame:
    def __init__(self, tipo_exame: str) -> None:
        self.tipo_exame = tipo_exame

    def aprovar_solicitacao_exame(self):
        if self.verifica_condicoes_exame():
            print(f"Exame aprovado: {self.tipo_exame}")

    def verifica_condicoes_exame(self):
        pass


class Exame:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo


exame_sangue = Exame("sangue")
aprovar_sangue = AprovaExame(exame_sangue.tipo)
aprovar_sangue.aprovar_solicitacao_exame()

exame_raio_x = Exame("raio-x")
aprovar_raio_x = AprovaExame(exame_raio_x.tipo)
aprovar_raio_x.aprovar_solicitacao_exame()