from config import *
from models.comida import Comida

def criar_comida(data):
    comida = Comida(
        nome=data['nome'],
        pais_origem=data['pais_origem'],
        receita=data.get('receita'),
        tempo_preparo=data.get('tempo_preparo'),
        porcao=data.get('porcao')
    )
    
    db.session.add(comida)
    db.session.commit()
    
    return comida

def retornar_comida():

    comidas = Comida.query.all()
    
    return comidas

def gerar_token(login, senha):

    comida = Comida.query.filter_by(login=login).first()
    
    if comida:
        password_bytes = senha.encode('utf-8')
        stored_password_bytes = comida.senha.encode('utf-8')
        
        if bcrypt.checkpw(password_bytes, stored_password_bytes):
            token = create_access_token(identity=str(comida.id))
            return token
    
    return None