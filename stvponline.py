import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURACIÓN DE CONEXIÓN ---
# Nota: La URL debe ser la de edición (la que obtienes al abrir el archivo)
URL_AFILIACIONES = "https://docs.google.com/spreadsheets/d/1B6DkX8W6yE6mQpS_zS9z-D8oH9uT-vX-8_yD3XU-y-M/edit" # REEMPLAZA CON TU LINK DE EDICIÓN

# --- SECCIÓN 4: AFILIACIÓN ---
st.markdown('<div id="afiliacion" class="section-title">📝 Afiliación Online</div>', unsafe_allow_html=True)

# Establecemos la conexión con Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

with st.form("form_afi"):
    f1, f2 = st.columns(2)
    nombre_afi = f1.text_input("Nombre Completo")
    dni_afi = f2.text_input("DNI")
    empresa_afi = f1.text_input("Empresa de Seguridad")
    cel_afi = f2.text_input("Celular")
    
    submit_button = st.form_submit_button("Enviar Solicitud")

    if submit_button:
        if nombre_afi and dni_afi and cel_afi:
            try:
                # 1. Intentar leer los datos existentes de la hoja "Afiliaciones"
                # Si la hoja está vacía, creamos un DataFrame con las columnas
                try:
                    df_actual = conn.read(spreadsheet=URL_AFILIACIONES, worksheet="Afiliaciones")
                except:
                    df_actual = pd.DataFrame(columns=["Nombre", "DNI", "Empresa", "Celular", "Fecha"])

                # 2. Crear la nueva fila
                nuevo_dato = pd.DataFrame([{
                    "Nombre": nombre_afi,
                    "DNI": dni_afi,
                    "Empresa": empresa_afi,
                    "Celular": cel_afi,
                    "Fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }])

                # 3. Concatenar y actualizar la hoja
                df_final = pd.concat([df_actual, nuevo_dato], ignore_index=True)
                
                conn.update(
                    spreadsheet=URL_AFILIACIONES,
                    worksheet="Afiliaciones",
                    data=df_final
                )
                
                st.success(f"¡Gracias {nombre_afi}! Tus datos se guardaron en la hoja Afiliaciones.")
                st.balloons()
            except Exception as e:
                st.error("Error de permisos: Asegúrate de que el Google Sheet esté compartido como 'Editor' con 'Cualquier persona con el enlace'.")
                st.info(f"Detalle técnico: {e}")
        else:
            st.warning("Por favor, completa los campos obligatorios (Nombre, DNI y Celular).")
