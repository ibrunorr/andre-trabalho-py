from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/questionario", methods=["POST"])
def questionario():
    data = request.json
    respostas_positivas = sum(1 for resposta in data.values() if resposta == 's')

    if respostas_positivas >= 7:
        nivel = "Alto"
        mensagem = "⚠️ Nível alto de estresse. Recomendamos procurar apoio psicológico."
    elif respostas_positivas >= 4:
        nivel = "Moderado"
        mensagem = "⚠️ Nível moderado de estresse. Considere melhorar sua rotina e autocuidado."
    elif respostas_positivas >= 1:
        nivel = "Baixo"
        mensagem = "✅ Nível leve de estresse. Mantenha hábitos saudáveis!"
    else:
        nivel = "Nenhum"
        mensagem = "✅ Sem sinais aparentes de estresse. Continue se cuidando!"

    return jsonify({"resposta": f"{mensagem} (Estresse: {nivel})"})


if __name__ == "__main__":
    app.run(debug=True)
