import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Portal STVP - Sindicato de Vigilancia",
    page_icon="🛡️",
    layout="wide"
)

# --- 2. ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
    <style>
    .section-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e3a8a;
        margin-top: 3rem;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .nav-bar {
        position: fixed;
        top: 0; left: 0; width: 100%;
        background-color: white;
        z-index: 1000;
        padding: 10px;
        text-align: center;
        border-bottom: 2px solid #2563eb;
    }
    .nav-bar a { 
        margin: 0 15px; 
        text-decoration: none; 
        color: #2563eb; 
        font-weight: bold; 
    }
    .card {
        padding: 1.5rem;
        border-radius: 0.75rem;
        background-color: white;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        height: 100%;
    }
    /* Estilo para el carnet digital */
    .credencial-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        padding: 25px;
        border-radius: 15px;
        color: white;
        border: 2px solid #fbbf24;
        box-shadow: 0 10px 15px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. NAVEGACIÓN SUPERIOR ---
st.markdown("""
    <div class="nav-bar">
        <a href="#inicio">INICIO</a>
        <a href="#beneficios">BENEFICIOS</a>
        <a href="#credenciales">CREDENCIALES</a>
        <a href="#afiliacion">AFILIACIÓN</a>
        <a href="#consulta">CONSULTA Y PAGO</a>
        <a href="#contacto">CONTACTO</a>
    </div>
    <div style="margin-top: 80px;"></div>
    """, unsafe_allow_html=True)

# --- 4. CONEXIÓN A GOOGLE SHEETS ---
# Usamos el link de edición para que el conector pueda escribir
URL_SHEET = "https://docs.google.com/spreadsheets/d/1B6DkX8W6yE6mQpS_zS9z-D8oH9uT-vX-8_yD3XU-y-M/edit"
conn = st.connection("gsheets", type=GSheetsConnection)

# --- SECCIÓN: INICIO ---
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
col_ini1, col_ini2 = st.columns([1, 2])
with col_ini1: 
    st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=200)
with col_ini2:
    st.title("Sindicato de Trabajadores de Vigilancia Privada")
    st.subheader("Portal de Autogestión Oficial")
    st.write("""
    Bienvenido al portal centralizado del STVP. Aquí podrás gestionar tu afiliación, 
    consultar el estado de tu cuenta de cuotas, conocer convenios de turismo 
    y acceder a tu documentación digital de forma rápida y segura.
    """)

st.markdown("---")

# --- SECCIÓN: BENEFICIOS ---
st.markdown('<div id="beneficios" class="section-title">🎁 Beneficios y Convenios</div>', unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)
with b1:
    st.markdown("""
    <div class="card">
        <h3>🚌 Turismo RolSol</h3>
        <p>Viajes y salidas grupales con promociones para vigiladores.</p>
        <a href="https://whatsapp.com/channel/0029VbAua9BJENy8oScpAH2B" target="_blank">
            <button style="width:100%; background:#25d366; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer; font-weight:bold;">Canal WhatsApp</button>
        </a>
    </div>
    """, unsafe_allow_html=True)
with b2:
    st.markdown("""
    <div class="card">
        <h3>🏨 Luz y Fuerza</h3>
        <p>Acceso a hoteles y complejos de turismo social.</p>
        <a href="https://www.sind-luzyfuerza-cap.org.ar/slyf/secretarias/turismo/tarifas/" target="_blank">
            <button style="width:100%; background:#2563eb; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer; font-weight:bold;">Ver Tarifas</button>
        </a>
    </div>
    """, unsafe_allow_html=True)
with b3:
    st.markdown("""
    <div class="card">
        <h3>🏍️ Ciudad Moto</h3>
        <p>Descuentos exclusivos en unidades y repuestos presentando tu credencial digital.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN: CREDENCIALES ---
st.markdown('<div id="credenciales" class="section-title">🪪 Credencial Digital</div>', unsafe_allow_html=True)
col_c1, col_c2 = st.columns(2)
with col_c1:
    st.write("### Tu carnet siempre con vos")
    st.write("Hacé clic en el botón para abrir tu credencial oficial. Es tu identificación para trámites y beneficios.")
    url_cred = "https://stvp-credencial.streamlit.app/#stvp-digital"
    st.markdown(f'<a href="{url_cred}" target="_blank"><button style="width:100%; background:#1e3a8a; color:white; padding:15px; border-radius:10px; font-weight:bold; cursor:pointer; border:none; font-size:1.2rem;">MOSTRAR CREDENCIAL</button></a>', unsafe_allow_html=True)
with col_c2:
    st.markdown("""
    <div class="credencial-box">
        <p style="font-size: 0.7rem; letter-spacing: 2px; margin-bottom: 5px;">SINDICATO TRABAJADORES VIGILANCIA PRIVADA</p>
        <h2 style="color: #fbbf24; margin-top: 0;">STVP DIGITAL</h2>
        <div style="height: 1px; background: rgba(255,255,255,0.2); margin: 15px 0;"></div>
        <p style="margin-bottom: 5px; font-size: 0.9rem; color: #94a3b8;">AFILIADO</p>
        <p style="font-size: 1.2rem; font-weight: bold; margin-bottom: 10px;">NOMBRE Y APELLIDO</p>
        <p style="margin-bottom: 5px; font-size: 0.9rem; color: #94a3b8;">DNI / CUIL</p>
        <p style="font-size: 1.1rem; font-weight: bold;">XX.XXX.XXX</p>
        <div style="float: right; background: white; padding: 5px; border-radius: 4px; margin-top: -60px;">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=60x60&data=STVP" width="60">
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN: AFILIACIÓN (ESCRITURA EN SHEET) ---
st.markdown('<div id="afiliacion" class="section-title">📝 Solicitud de Afiliación</div>', unsafe_allow_html=True)
with st.form("form_afiliacion_final"):
    f_col1, f_col2 = st.columns(2)
    nombre_afi = f_col1.text_input("Nombre Completo")
    dni_afi = f_col2.text_input("DNI")
    empresa_afi = f_col1.text_input("Empresa donde trabajás")
    cel_afi = f_col2
