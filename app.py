import streamlit as st
import numpy as np
import datetime
import pandas as pd

st.sidebar.image("Abnaks.png")
st.sidebar.title("Módulos")

modulo = st.sidebar.selectbox("Elija un módulo", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulo == "Home":
  st.title("Proyecto Abanks - Ladonware")
  st.image("ladon.jpg")

  st.write("Módulo Home Datos Personales")
  estudiante = "Cristian Valentin Reyes Reyes"
  nom_modulo    = "Módulo 01"
  informacion = "Soy de nacionalidad Peruana, actualmente vivo en Piura."
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
  st.title("Verificado Simple")
  presupuesto = st.number_input("Ingrese Presupuesto", value=0)
  gasto = st.number_input("Ingrese Gasto", value=0)
  if st.button("Verificar"):
        if gasto <= presupuesto:
            saldo = presupuesto - gasto
            st.success(f"✅ El gasto está dentro del presupuesto.")
            st.write(f"Saldo disponible: S/ {saldo:.2f}")
        else:
            exceso = gasto - presupuesto
            st.error(f"❌ El presupuesto fue excedido.")
            st.write(f"Excedido por: S/ {exceso:.2f}")
  
elif modulo == "Ejercicio 2":
  st.title("Registro Actividades Financieras")
  if "actividades" not in st.session_state:
    st.session_state.actividades = []
    
  nombre = st.text_input("Nombre de la actividad")
  tipo = st.selectbox(
    "Tipo de actividad",
    ["Capacitación", "Viaje", "Compra", "Evento", "Otro"])
    
  presupuesto = st.number_input(
    "Presupuesto",
    min_value=0.0,
    value=0.0)
  
  gasto_real = st.number_input(
    "Gasto real",
    min_value=0.0,
    value=0.0
  )
  if st.button("Agregar actividad"):
    actividad = {
      "Nombre": nombre,
      "Tipo": tipo,
      "Presupuesto": presupuesto,
      "Gasto Real": gasto_real
    }
    for actividad in st.session_state.actividades:
      if actividad["Gasto Real"] <= actividad["Presupuesto"]:
        st.write(f"✅ {actividad['Nombre']}: Dentro del presupuesto")
      else:
        st.write(f"❌ {actividad['Nombre']}: Excedió el presupuesto")
        
elif modulo == "Ejercicio 3":
  st.write("Estas en el Ejercicio 3")
elif modulo == "Ejercicio 4":
  st.write("Estas en el Ejercicio 4")
else:
  st.write("Elija una Opción")

