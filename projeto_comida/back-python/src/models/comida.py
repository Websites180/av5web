from config import *
class Comida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    pais_origem = db.Column(db.String(200), nullable=False)
    receita = db.Column(db.String(700), nullable=True)
    tempo_preparo = db.Column(db.String(200), nullable=True)
    porcao = db.Column(db.Integer, nullable=True)

    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "pais_origem":self.pais_origem,
            "receita":self.receita,
            "tempo_preparo":self.tempo_preparo,
            "porcao":self.porcao
            }
