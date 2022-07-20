from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
    'id':'0',
    'nome':'Roberto',
     'habilidades':['Python', 'Flask']
     },
    {'id':'1',
    'nome':'Sergio',
     'habilidades':['Javascript', 'Nodejs']}

]

# devolve um desenvolvedor pelo ID, alterando e deletando
@app.route('/dev/<int:id>/', methods=['GET', 'PUT'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'falha', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o admin da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído'})

# lista todos os desenvolvedores e adiciona um novo
@app.route('/dev', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.apped(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__=='__main__':
    app.run(debug=True)
