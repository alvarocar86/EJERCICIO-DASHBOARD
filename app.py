import pandas as pd
import streamlit as st


url = "https://github.com/alvarocar86/TABLERO-DE-CONTROL/raw/refs/heads/main/datos_generales_ficticios.csv"
df = pd.read_csv(url, sep=";", encoding="utf8")

st.dataframe(df)

seleccion_columnas = ["FECHA_HECHOS", "DELITO", "ETAPA", "FISCAL_ASIGNADO", "DEPARTAMENTO", "MUNICIPIO_HECHOS"]
df = df[seleccion_columnas].sort_values(by="FECHA_HECHOS", ascending=True).reset_index(drop=True)

df["FECHA_HECHOS"] = pd.to_datetime(df["FECHA_HECHOS"], errors="coerce")

df_serie_tiempo = df.copy()
df_serie_tiempo["FECHA_HECHOS"] =df["FECHA_HECHOS"].dt.date


st.subheader("Tipo de Delito")
delitos = df["DELITO"].value_counts()
st.bar_chart(delitos)






