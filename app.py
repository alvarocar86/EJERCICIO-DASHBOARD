import pandas as pd
import streamlit as st


url = "https://github.com/alvarocar86/TABLERO-DE-CONTROL/raw/refs/heads/main/datos_generales_ficticios.csv"
df = pd.read_csv(url, sep=";", encoding="utf8")

st.dataframe(df)

seleccion_columnas = ["FECHA_HECHOS", "DELITO", "ETAPA", "FISCAL_ASIGNADO", "DEPARTAMENTO", "MUNICIPIO_HECHOS"]
df = df[seleccion_columnas].sort_values(by="FECHA_HECHOS", ascending=True).reset_index(drop=True)

st.dataframe(df)

df["FECHA_HECHOS"] = pd.to_datetime(df["FECHA_HECHOS"], errors="coerce")
st.dataframe(df)

df["FECHA_HECHOS"] = df["FECHA_HECHOS"].dt.date
st.dataframe(df)

max_municipio =df["MUNICIPIO_HECHOS"].value_counts()
st.dataframe(max_municipio)

max_municipio =df["MUNICIPIO_HECHOS"].value_counts().iloc[0]
st.write(max_municipio)


max_cantidad_municipio = df["MUNICIPIO_HECHOS"].value_counts().index[0].upper()
max_cantidad_municipio = df["MUNICIPIO_HECHOS"].value_counts().iloc[0]
st.write(max_cantidad_municipio)

st.set_page_config(page_title="Dashboard de Delitos-Fiscalía", layout="centered")
st.header("Dashboard de Delitos-Fiscalía")
st.dataframe(df)

st.write(f"### Municipio con mas delitos: {max_municipio} con {max_cantidad_municipio} reportes")
st.dataframe(df)












