import pandas as pd
import streamlit as st
import plotly.express as px



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

etapa_mas_frecuente = df["ETAPA"].value_counts().index[0]
cant_etapa_mas_frecuente = df["ETAPA"].value_counts().iloc[0]
st.dataframe(df)

st.set_page_config(page_title="Dashboard de Delitos - Fiscalia", layout="centered")
st.title("Dashboard de Delitos - Fiscalia")
st.dataframe(df)

st.write(f"## Municipio con más delitos: {max_municipio} con {max_cantidad_municipio} reportes")
st.write(f"{etapa_mas_frecuente} tiene {cant_etapa_mas_frecuente} registros")
st.dataframe(df)

st.subheader(f"## Municipio con más delitos: {max_municipio} con {max_cantidad_municipio} reportes")
st.subheader(f"{etapa_mas_frecuente} tiene {cant_etapa_mas_frecuente} registros")
st.dataframe(df)

delitos = df["DELITO"].value_counts()
st.write(delitos)

st.subheader("Comportamiento Delitos")
delitos = df["DELITO"].value_counts()
st.bar_chart(delitos)

st.subheader("Departamentos con mas casos")
departamento = df["DEPARTAMENTO"].value_counts()
st.bar_chart(departamento)


st.subheader("Distribucion por Departamentos")
fig =px.pie(
    names=departamento.index,
    values=departamento.values    
)
st.dataframe(df)


fig.update_traces(textposition="outside", textinfo="percent+label")
fig.update_layout(showlegend=False, height=400)
st.plotly_chart(fig)

df_delitos = df.groupby(['DEPARTAMENTO', 'DELITO']).size().reset_index(name='conteo')
fig = px.bar(df_delitos, x='DEPARTAMENTO', y='conteo', color='DELITO', barmode='stack')
st.plotly_chart(fig)
st.write(df_delitos)



