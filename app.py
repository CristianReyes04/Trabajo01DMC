import streamlit as st
import numpy as np
import datetime

st.sidebar.image("Abnaks.png")
st.sidebar.title("Módulos")

modulo = st.sidebar.selectbox("Elija un módulo", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulo == "Home":
  st.title("Proyecto Abanks - Ladonware")
  st.image("ladon.jpg")

  st.write("Módulo Home Datos Personales")
  estudiante = "Cristian Valentin Reyes Reyes"
  nom_modulo    = "Módulo 01"
  informacion = "Soy de profesión Ingeniero, de nacionalidad Peruana, actualmente vivo en Piura."
  anio = datetime.date.today().year
  descripcion = "El Proyecto de una plaforma que puedan gestionar operaciones Bancarias"
  tecnologias = "Python, Streamlit, NumPy"
  
  st.markdown(f""" **Nombre del estudiante:** {estudiante}""")
  st.markdown(f""" **Módulo:** {nom_modulo}""")
  st.markdown(f""" **Información del estudiante:** {informacion}""")
  st.markdown(f""" **Año:** {anio}""")
  st.markdown(f""" **Descripción del proyecto:** {descripcion}""")
  st.markdown(f""" **Tecnologías utilizadas:** {tecnologias}""")
  
elif modulo == "Ejercicio 1":
  st.write("Estas en el Ejercicio 1")
elif modulo == "Ejercicio 2":
  st.write("Estas en el Ejercicio 2")
elif modulo == "Ejercicio 3":
  st.write("Estas en el Ejercicio 3")
elif modulo == "Ejercicio 4":
  st.write("Estas en el Ejercicio 4")
else:
  st.write("Elija una Opción")

