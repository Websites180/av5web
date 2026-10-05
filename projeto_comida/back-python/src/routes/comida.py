from config import *
from models.comida import Comida
import services.comida as comida_service


'''
--------------
LISTAR COMIDAS
--------------
'''

'''
TESTE DE ROTA - Comida - GET

curl localhost:5000/comidas
{
  "detalhes": [
    {
      "id": 1,
      "nome": "Macarrão ao molho branco",
      "pais_origem": "Itália",
      "porcao": 4,
      "receita": "cozinhe o macarrão, prepare o molho branco e misture tudo",
      "tempo_preparo": 35
    }
  ],
  "resultado": "ok"
}

'''

# rota para listar comidas
# rota liberada para listagem pública :-) não requer JWT
@app.route('/comidas', methods=['GET'])
def retornar_comidas():

    # buscar as pessoas
    comidas = comida_service.retornar_comidas()
    
    # retornar a lista de pessoas em JSON
    return jsonify({
        "resultado":"ok",
        "detalhes":[comida.json() for comida in comidas]
    })

'''
--------------
INCLUIR COMIDA
--------------
'''

'''
TESTE DE ROTA - Comida - POST

curl http://localhost:5000/pessoa -X POST -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NDU4NDIwNCwianRpIjoiNDE0NWNhOTUtYzA0NS00Mjk2LThjZjctNjUxNzliZTA5ZTMzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODQ1ODQyMDQsImNzcmYiOiJhMmMxNTU4Yy1lNjI0LTQ2OTYtOWRlZi0wZGY5YTg4Mjc0MzMiLCJleHAiOjE3ODQ1ODUxMDR9.C2ZOz5K7Dm90QCXsiGC7BslmHn-DGYsVYRUtmmaPWsI" -H "Content-Type:application/json" -d '{"nome":"Tiago Matos", "email":"tima@gmail.com","telefone":"47 9 8899 7766", "login":"tima","senha":"tima123"}'
{"detalhes":{"email":"tima@gmail.com","id":2,"login":"tima","nome":"Tiago Matos","senha":"$2b$12$x6rPCQgWQWNfYAOzHv5s5ua/mIe9jKI77lZQ9GLi/9oDAEZlpvCVe","telefone":"47 9 8899 7766"},"resultado":"ok"}

'''

# rota para inserir uma pessoa
@app.route('/comida', methods=['POST'])
@jwt_required()  # exige que o usuário esteja autenticado para acessar esta rota
def criar_comida():
    # ler os dados em json
    dados = request.json
    
    # se faltou algum dado obrigatório...
    if not dados or not dados.get('nome') or not dados.get('pais_origem') or not dados.get('porcao') or not dados.get('receita') or not dados.get('tempo_preparo'):
        # retorna erro
        return jsonify({"resultado":"erro", "detalhes":"Nome, país de origem, porção, receita e tempo de preparo são obrigatórios"}), 400
    
    # chama o serviço de criação de pessoa
    comida = comida_service.criar_comida(dados)    
    
    # retornar mensagem de sucesso :-)
    return jsonify({
        "resultado":"ok", 
        "detalhes":comida.json()
    }), 201

