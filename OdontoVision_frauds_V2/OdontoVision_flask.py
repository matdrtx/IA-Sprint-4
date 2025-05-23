
from flask import Flask, request, render_template
import joblib
import pandas as pd
import json

app = Flask(__name__, template_folder="templates", static_folder="static")
model = joblib.load("fraude_model_v2.joblib")

# Dicionário com frequências para JS
df = pd.read_csv("odonto_fraude_enriquecida.csv")
pacientes = df['paciente_id'].value_counts().to_dict()
dentistas = df['dentista_id'].value_counts().to_dict()
stats_json = json.dumps({
    "pacientes": {str(k): int(v) for k, v in pacientes.items()},
    "dentistas": {str(k): int(v) for k, v in dentistas.items()}
})

@app.route("/")
def home():
    return render_template("index.html", stats_json=stats_json)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form
    try:
        input_data = pd.DataFrame([{
            "num_consultas": int(data['num_consultas'] or 0),
            "procedimento_custo": float(data['procedimento_custo'] or 0),
            "idade_paciente": int(data['idade_paciente'] or 0),
            "media_custo_por_consulta": float(data['media_custo_por_consulta'] or 0),
            "freq_dentista": int(data['freq_dentista'] or 0),
            "freq_paciente": int(data['freq_paciente'] or 0),
            "categoria_idade": data['categoria_idade'] or "adulto"
        }])
        prediction = model.predict(input_data)[0]
    except Exception as e:
        prediction = f"Erro: {str(e)}"
    return render_template("index.html", prediction=prediction, stats_json=stats_json)

if __name__ == "__main__":
    app.run(debug=True)
