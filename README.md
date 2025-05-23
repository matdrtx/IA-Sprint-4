
# OdontoVision

**OdontoVision** é um sistema de detecção inteligente de fraudes em sinistros odontológicos, utilizando Machine Learning com modelo XGBoost treinado sobre uma base enriquecida com dados sintéticos e reais. O projeto conta com interface web em HTML/CSS e backend em Flask.

## Funcionalidades

- Classificação automática de sinistros como fraude ou não fraude
- Interface web leve, responsiva e em HTML puro
- Preenchimento automático de campos com base em IDs históricos
- Cálculo automático da média de custo por consulta
- Backend robusto com validações e tratamento de exceções
- Modelo compatível com scikit-learn >= 1.4

## Tecnologias Utilizadas

- Python 3.12
- Flask para o backend
- XGBoost como algoritmo de classificação
- Pandas / Scikit-learn para tratamento e modelagem de dados
- HTML5 e CSS3 para o frontend

## Arquitetura da IA

O modelo central é um XGBoostClassifier, inserido dentro de um pipeline scikit-learn que contém:

- Pré-processamento numérico com StandardScaler
- Codificação categórica com OneHotEncoder
- Pipeline completo com ColumnTransformer

A escolha do XGBoost foi baseada em sua capacidade de generalização, alta performance com dados tabulares, robustez com dados desbalanceados e facilidade de ajuste.

## Novas Features na Versão 2

- media_custo_por_consulta: cálculo derivado de custo / consultas
- freq_dentista: número de sinistros associados ao dentista
- freq_paciente: número de sinistros do paciente
- categoria_idade: categorização etária (jovem, adulto, meia-idade, idoso)

## Como Executar Localmente

1. Instale o Python 3.8 ou superior
2. Clone ou extraia o projeto
3. No terminal, navegue até a pasta do projeto:

```bash
cd OdontoVision_frauds_V2
```

4. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

5. Instale as dependências:

```bash
pip install flask xgboost pandas scikit-learn joblib
```

6. Execute o servidor:

```bash
python OdontoVision_flask.py
```

7. Acesse no navegador:

```
http://localhost:5000
```

## Resultados

- Acurácia: aproximadamente 95.7%
- F1-score (fraude): 0.92
- Recall (fraude): 0.91
- Precisão (fraude): 0.93

## Próximos Passos

- Implementação de dashboard com gráficos e estatísticas
- Deploy como API em ambiente cloud
- Aumento do recall via técnicas de oversampling
- Expansão para outros tipos de sinistros (médicos, hospitalares)

## Link do video:
-https://youtu.be/9edBmkYf7vM

