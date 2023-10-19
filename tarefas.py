from flask import Flask, request, make_response, jsonify, abort

app = Flask(__name__)

lista_tarefas = []

@app.route("/tarefas", methods=['GET','POST'])
def tarefas():
    if request.method == "GET":
        return make_response(jsonify(lista_tarefas))
    elif request.method == "POST":
        pass


        #else:
         #   return make_response(jsonify("Tarefa já está na lista"),400)
    else:
        abort(404)

if __name__ == '__main__':
    app.run