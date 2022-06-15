import pandas as pd

df = pd.read_csv("../Datasets/covid.csv")

df.drop(df.columns.difference(["Carimbo de data/hora",
"Número do Registro/Prontuário RHP",
"Sexo Biológico do Paciente",
"Idade do Paciente (anos completos)",
"Temperatura do Paciente (__ . _ ºC) ",
"Frequência Cardíaca (bpm)",
"Frequência Respiratória (ciclos/min)",
"PAS ( mmHg) ",
"PAD ( mmHg) ",
"Saturação de Oxigênio (  __  %)",
"SINTOMAS [Antecedente de Febre]",
"SINTOMAS [Tosse]",
"SINTOMAS [Tosse com produção de expetoração]",
"SINTOMAS [Tosse com hemoptise]",
"SINTOMAS [Dor de garganta]",
"SINTOMAS [Pingo no nariz (rinorreia)]",
"SINTOMAS [Fadiga/Cansaço]",
"SINTOMAS [Dificuldades respiratórias]",
"SINTOMAS [Cefaleia]",
"SINTOMAS [Dor abdominal]",
"SINTOMAS [Vómitos/náuseas]",
"SINTOMAS [Diarréia]",
"SINTOMAS [Conjuntivite]",
"Comorbidades Prévias [Doenca Cardíaca Crônica]",
"Comorbidades Prévias [Hipertensão Arterial Sistêmica (HAS)]",
"Comorbidades Prévias [DM sem complicação]",
"Comorbidades Prévias [DM com complicação]",
"Comorbidades Prévias [IAM ]",
"Comorbidades Prévias [ICC]",
"Comorbidades Prévias [Doença Vascular Periférica]",
"Comorbidades Prévias [Doença Neurológica Crônica]",
"Comorbidades Prévias [Doença Pulmonar Crônica]",
"Comorbidades Prévias [Doença Hepática]",
"Comorbidades Prévias [Doença Renal moderada a severa]",
"Tabagismo",
"Testes Realizados [Coronavírus]",
]), 1, inplace=True)

df.dropna(inplace= True)

for i in df.columns:
  df = df[df[i] != "Sem informação"]

for i in df.columns:
  df = df[df[i] != "Não realizado"]

  df.to_csv('../DataWarehouse/filtred.csv')  