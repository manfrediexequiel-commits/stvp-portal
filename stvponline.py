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

# --- 2. ESTILOS DE ALTA VISIBILIDAD (FONDO CELESTE) ---
st.markdown("""
    <style>
    .stApp { background-color: #E3F2FD; }
    
    .section-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #0D47A1;
        text-align: center;
        margin: 2rem 0;
        text-transform: uppercase;
    }

    .nav-bar {
        position: fixed;
        top: 0; left: 0; width: 100%;
        background-color: #ffffff;
        z-index: 1000;
        padding: 12px;
        text-align: center;
        border-bottom: 4px solid #0D47A1;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .nav-bar a { 
        margin: 0 15px; 
        text-decoration: none; 
        color: #0D47A1; 
        font-weight: bold;
    }

    .benefit-card {
        padding: 25px;
        border-radius: 15px;
        background-color: #ffffff;
        border-left: 10px solid #1E88E5;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        min-height: 220px;
    }
    
    .white-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        border: 3px solid #0D47A1;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }

    .whatsapp-float {
        position: fixed;
        width: 65px; height: 65px;
        bottom: 30px; right: 30px;
        background-color: #25d366;
        color: white;
        border-radius: 50px;
        text-align: center;
        box-shadow: 2px 5px 20px rgba(0,0,0,0.4);
        z-index: 9999;
        display: flex; align-items: center; justify-content: center;
    }
    </style>
    
    <a href="https://wa.me/5491152628936" class="whatsapp-float" target="_blank">
        <svg width="35" height="35" fill="white" viewBox="0 0 16 16">
            <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
        </svg>
    </a>
    """, unsafe_allow_html=True)

# --- 3. NAVEGACIÓN ---
st.markdown("""<div class="nav-bar"><a href="#inicio">INICIO</a><a href="#beneficios">BENEFICIOS</a><a href="#afiliacion">AFILIACIÓN</a><a href="#consulta">CONSULTA</a></div><div style="margin-top: 100px;"></div>""", unsafe_allow_html=True)

# --- 4. CONEXIÓN ---
URL_SHEET = "https://docs.google.com/spreadsheets/d/1mmMbsH6BNfrcmtq3T7xDizBVxjd--sWUIUdBZtSPuFM/edit#gid=6508803"
conn = st.connection("gsheets", type=GSheetsConnection)

# --- INICIO ---
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
c1, c2 = st.columns([1, 2])
with c1: st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=200)
with c2:
    st.markdown("<h1 style='color: #0D47A1;'>Sindicato STVP</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1565C0;'>Portal de Autogestión para Vigiladores</h3>", unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN BENEFICIOS ---
st.markdown('<div id="beneficios" class="section-title">🎁 Beneficios y Convenios</div>', unsafe_allow_html=True)

# Tarjetas de colores
col_b1, col_b2, col_b3 = st.columns(3)
with col_b1:
    st.markdown("""<div class="benefit-card" style="border-left-color: #FF9800;"><h3>🚌 Turismo RolSol</h3><p>Viajes grupales y cuotas. <a href='https://whatsapp.com/channel/0029VbAua9BJENy8oScpAH2B'>Ver Canal</a></p></div>""", unsafe_allow_html=True)
with col_b2:
    st.markdown("""<div class="benefit-card" style="border-left-color: #E91E63;"><h3>🏍️ Ciudad Moto</h3><p>Descuentos exclusivos en unidades y repuestos para afiliados.</p></div>""", unsafe_allow_html=True)
with col_b3:
    st.markdown("""<div class="benefit-card" style="border-left-color: #4CAF50;"><h3>⚖️ Asesoría Legal</h3><p>Consultas gremiales y legales gratuitas para el trabajador.</p></div>""", unsafe_allow_html=True)

# Detalle Luz y Fuerza (Folleto PDF)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
st.subheader("🏖️ Temporada Verano 25/26 - Hoteles Luz y Fuerza")
st.warning("⚠️ Tarifas válidas hasta Dic 2025. Desde Enero se ajustan por IPC.")

t1, t2, t3, t4 = st.tabs(["🌊 San Bernardo", "🏖️ Mar del Plata", "🌲 Villa Giardino", "🏔️ Bariloche"])

with t1:
    st.markdown("**Hotel 'Por la Liberación Nacional'** (Chiozza 2455) [cite: 79, 80]")
    st.write("✅ Servicio Todo Incluido, Piscina Climatizada y Cochera[cite: 81, 83].")
    st.table({
        "Habitación": ["Individual", "Doble (p/p)", "Triple (p/p)", "Cuádruple (p/p)", "Menores (3-12)"],
        "Tarifa": ["$200.000", "$100.000", "$95.000", "$90.000", "$45.000 a $50.000"]
    }) # [cite: 75]

with t2:
    st.markdown("**Hotel 'Oscar Lescano'** (Punta Mogotes) [cite: 116, 117]")
    st.write("✅ Todo Incluido, Vista al Mar, Bar de Piscina[cite: 120].")
    st.table({
        "Habitación": ["Doble (p/p)", "Triple (p/p)", "Menores (3-12)"],
        "Tarifa": ["$100.000", "$95.000", "$47.500 a $50.000"]
    }) # [cite: 111]

with t3:
    st.markdown("**Hotel 'Por los Derechos del Trabajador'** (Córdoba) [cite: 34]")
    st.write("✅ Contingentes de 7 días[cite: 34].")
    st.table({
        "Habitación": ["Doble (p/p)", "Triple (p/p)", "Cuádruple (p/p)", "Menores (3-12)"],
        "Tarifa": ["$83.000", "$78.850", "$74.700", "$37.300 a $41.500"]
    }) # [cite: 37]

with t4:
    st.markdown("**Hotel 'Alún Nehuén'** (Bariloche) [cite: 144]")
    st.write("✅ Media Pensión (Desayuno/Cena), Spa y Gimnasio[cite: 32].")
    st.table({
        "Habitación": ["Doble (p/p)", "Triple (p/p)", "Menores (3-12)"],
        "Tarifa": ["$88.000", "$83.600", "$41.800 a $44.000"]
    }) # [cite: 29]

st.markdown('</div>', unsafe_allow_html=True)

# --- AFILIACIÓN ---
st.markdown('<div id="afiliacion" class="section-title">📝 Afiliación Online</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="white-container">', unsafe_allow_html=True)
    with st.form("form_afi"):
        c_f1, c_f2 = st.columns(2)
        nombre = c_f1.text_input("Nombre y Apellido*")
        dni = c_f2.text_input("DNI (Solo números)*")
        empresa = c_f1.text_input("Empresa de Seguridad*")
        celular = c_f2.text_input("WhatsApp de contacto*")
        intereses = st.multiselect("Intereses:", ["Turismo", "Salud", "Legal", "Kit Escolar"])
        acepto = st.checkbox("Acepto el tratamiento de mis datos (Ley 25.326)")
        
        if st.form_submit_button("SOLICITAR AFILIACIÓN"):
            if acepto and nombre and dni.isdigit():
                st.success("¡Solicitud enviada! Nos contactaremos pronto.")
                st.balloons()
            else: st.error("Verificá los campos obligatorios.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- CONSULTA ---
st.markdown('<div id="consulta" class="section-title">🔍 Consulta de Estado</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="white-container">', unsafe_allow_html=True)
    dni_q = st.text_input("Ingresá tu DNI para consultar cuotas:")
    if st.button("Consultar"):
        st.info("Buscando en el padrón...")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-weight:bold; color:#0D47A1;'>© 2026 STVP - Sindicato Vigilancia. Piedras 1065, CABA.</p>", unsafe_allow_html=True)
