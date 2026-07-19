import streamlit as st
import numpy as np
import datetime

st.sidebar.image("Abnaks.png")
st.sidebar.title("Módulos")

modulo = st.sidebar.selectbox("Elija un módulo", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulo == "Home":
  st.title("Proyecto Bancario Abanks - Ladonware")
  st.image("ladon.jpg")

  lv_estudiante = "Cristian Valentin Reyes Reyes"
  lv_modulo    = "Modulo 01"
  lv_informacion = "Soy de profesión Ingeniero, de nacionalidad Peruana, actualmente vivo en Piura."
  lv_anio = datetime.date.today().year
  lv_descripcion = "El Proyecto conciste en una plaforma que puedan gestionar operaciones Bancarias"
  lv_tecnologias = "Python, Streamlit, NumPy"

  st.write("Nombre del estudiante:",lv_estudiante)
  st.write("Nombre del Módulo:",lv_modulo)
  st.write("Información general del estudiante:",lv_informacion)
  st.write("Año:",lv_anio)
  st.write("Descripción del Proyecto:",lv_descripcion)
  st.write("Tecnologías utilizadas:",lv_tecnologias)
  
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

