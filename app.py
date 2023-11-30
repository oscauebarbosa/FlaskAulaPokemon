from flask import Flask, render_template, request, redirect
app = Flask(__name__)

class cadpokemon:
    def __init__(self, numero, nome, tipo, altura, peso):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.altura = altura
        self.peso = peso

lista = []


@app.route('/pokemon')
def pokemon():
    return render_template('Pokemon.html', Titulo ="Pokémons Iniciais: ", ListaPokemons = lista)


@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = "Cadastro de Pokemon")


@app.route('/criar', methods= ['POST'])
def criar():
    numero = request.form['numero']
    nome = request.form['nome']
    tipo = request.form['tipo']
    altura = request.form['altura']
    peso = request.form['peso']
    obj = cadpokemon(numero,nome,tipo,altura,peso)
    lista.append(obj)
    return redirect('/pokemon')

@app.route('/excluir/<numeropkm>', methods=['GET','DELETE'])
def excluir(numeropkm) :
    for i, pkm in enumerate(lista):
        if pkm.numero == numeropkm:
            lista.pop(i)
            break
    return redirect('/pokemon')

@app.route('/editar/<numeropkm>', methods=['GET'])
def editar(numeropkm):
    for i, pkm in enumerate(lista):
        if pkm.numero == numeropkm:
            return render_template("Editar.html", pokemon=pkm, Titulo="Alterar Pokemon")

@app.route('/alterar', methods = ['POST','PUT'])
def alterar():
    numero = request.form['numero']
    for i, pkm in enumerate(lista):
        if pkm.numero == numero:
            pkm.nome = request.form['nome']
            pkm.tipo = request.form['tipo']
            pkm.altura = request.form['altura']
            pkm.peso = request.form['peso']
        return redirect('/pokemon')




if __name__ == '__main__':
    app.run()
