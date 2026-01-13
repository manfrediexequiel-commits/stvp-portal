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

# --- 2. ESTILOS PERSONALIZADOS (ALTA VISIBILIDAD) ---
st.markdown("""
    <style>
    /* Fondo celeste para toda la aplicación */
    .stApp {
        background-color: #E3F2FD;
    }
    
    /* Títulos con máxima visibilidad */
    .section-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #0D47A1; /* Azul marino profundo */
        margin-top: 3rem;
        margin-bottom: 1.5rem;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }

    /* Barra de navegación blanca para contraste */
    .nav-bar {
        position: fixed;
        top: 0; left: 0; width: 100%;
        background-color: #ffffff;
        z-index: 1000;
        padding: 12px;
        text-align: center;
        border-bottom: 3px solid #0D47A1;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .nav-bar a { 
        margin: 0 15px; 
        text-decoration: none; 
        color: #0D47A1; 
        font-weight: bold;
        font-size: 1.1rem;
    }

    /* Tarjetas blancas con borde definido */
    .card {
        padding: 2rem;
        border-radius: 1rem;
        background-color: #ffffff;
        border: 2px solid #0D47A1;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        text-align: center;
        color: #1A237E;
        height: 100%;
    }

    /* Recuadro de Credencial */
    .credencial-box {
        background: linear-gradient(135deg, #1A237E 0%, #0D47A1 100%);
        padding: 30px;
        border-radius: 20px;
        color: white;
        border: 3px solid #FFC107;
        box-shadow: 0 15px 25px rgba(0,0,0,0.4);
    }

    /* Botón flotante de WhatsApp */
    .whatsapp-float {
        position: fixed;
        width: 65px;
        height: 65px;
        bottom: 30px;
        right: 30px;
        background-color: #25d366;
        color: white;
        border-radius: 50px;
        text-align: center;
        box-shadow: 2px 5px 20px rgba(0,0,0,0.4);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
    }
    
    /* Inputs y formularios con bordes oscuros para que se vean bien */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border: 2px solid #0D47A1 !important;
    }
    
    </style>
    
    <a href="https://wa.me/5491152628936?text=Hola%20STVP!%20Necesito%20una%20consulta." class="whatsapp-float" target="_blank">
        <svg width="35" height="35" fill="white" viewBox="0 0 16 16">
            <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
        </svg>
    </a>
    """, unsafe_allow_html=True)

# --- 3. NAVEGACIÓN ---
st.markdown("""<div class="nav-bar"><a href="#inicio">INICIO</a><a href="#beneficios">BENEFICIOS</a><a href="#credenciales">CREDENCIALES</a><a href="#afiliacion">AFILIACIÓN</a><a href="#consulta">CONSULTA</a><a href="#contacto">CONTACTO</a></div><div style="margin-top: 100px;"></div>""", unsafe_allow_html=True)

# --- 4. CONEXIÓN A GOOGLE SHEETS ---
URL_SHEET = "https://docs.google.com/spreadsheets/d/1mmMbsH6BNfrcmtq3T7xDizBVxjd--sWUIUdBZtSPuFM/edit#gid=6508803"
conn = st.connection("gsheets", type=GSheetsConnection)

def get_data(worksheet_name):
    return conn.read(spreadsheet=URL_SHEET, worksheet=worksheet_name)

# --- SECCIÓN: INICIO ---
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
col_ini1, col_ini2 = st.columns([1, 2])
with col_ini1: 
    st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=220)
with col_ini2:
    st.markdown("<h1 style='color: #0D47A1;'>Sindicato de Trabajadores de Vigilancia Privada</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1565C0;'>Portal de Autogestión Oficial - STVP</h3>", unsafe_allow_html=True)
    st.write("**Bienvenido.** Gestione sus beneficios y trámites de manera rápida y segura.")

st.markdown("---")

# --- SECCIÓN: BENEFICIOS ---
st.markdown('<div id="beneficios" class="section-title">🎁 Beneficios y Convenios</div>', unsafe_allow_html=True)

# Contenedor blanco para el folleto
with st.container():
    st.markdown("""<div style='background-color: white; padding: 25px; border-radius: 15px; border: 2px solid #0D47A1;'>""", unsafe_allow_html=True)
    st.subheader("🏖️ Convenio Especial Luz y Fuerza - Temporada 25/26")
    
    tabs = st.tabs(["🌊 San Bernardo", "🏖️ Mar del Plata", "🌲 Villa Giardino", "🏔️ Bariloche", "⛲ Recreos"])
    
    with tabs[0]:
        st.markdown("**Hotel 'Por la Liberación Nacional'** (Chiozza 2455)")
        st.table({"Habitación": ["Doble", "Triple", "Cuádruple"], "Tarifa Adulto": ["$100.000", "$95.000", "$90.000"]})
    
    with tabs[1]:
        st.markdown("**Hotel 'Oscar Lescano'** (Punta Mogotes)")
        st.write("Servicio Todo Incluido y beneficios en Balneario 1.")
        
    with tabs[2]:
        st.markdown("**Villa Giardino, Córdoba**")
        st.write("Estadías de 7 días. Tarifa base: $83.000 por adulto.")

    with tabs[3]:
        st.markdown("**Bariloche - Hotel Alún Nehuén**")
        st.write("Media pensión con vista al Nahuel Huapi.")

    with tabs[4]:
        st.markdown("**Predios y Recreos**")
        st.write("- Villa del Parque (CABA)\n- Recreo Tiger (Delta)\n- Predio Ezeiza")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN: AFILIACIÓN ---
st.markdown('<div id="afiliacion" class="section-title">📝 Solicitud de Afiliación</div>', unsafe_allow_html=True)
with st.container():
    st.markdown("<div style='background-color: white; padding: 30px; border-radius: 15px; border: 2px solid #0D47A1;'>", unsafe_allow_html=True)
    with st.form("form_afi"):
        c1, c2 = st.columns(2)
        nombre = c1.text_input("Nombre y Apellido*")
        dni = c2.text_input("DNI (Sin puntos)*")
        empresa = c1.text_input("Empresa Actual*")
        celular = c2.text_input("WhatsApp de contacto*")
        
        intereses = st.multiselect("Beneficios de su interés:", ["Turismo", "Salud", "Asesoría Gremial", "Kit Escolar"])
        
        st.markdown("**Aviso Legal:** Sus datos están protegidos por la Ley 25.326.")
        acepto = st.checkbox("Acepto los términos y el tratamiento de mis datos.")
        
        if st.form_submit_button("ENVIAR AFILIACIÓN"):
            if acepto and nombre and dni.isdigit():
                st.success("¡Solicitud enviada correctamente!")
                st.balloons()
            else:
                st.error("Por favor complete los campos obligatorios y acepte los términos.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- SECCIÓN: CONTACTO ---
st.markdown('<div id="contacto" class="section-title">📞 Contacto</div>', unsafe_allow_html=True)
c_con1, c_con2 = st.columns(2)
with c_con1:
    st.markdown("""
    <div class='card'>
        <h3>Sede Central</h3>
        <p><b>Dirección:</b> Piedras 1065, CABA</p>
        <p><b>Email:</b> stvp.sindicatodeseguridad@gmail.com</p>
        <p><b>Horario:</b> Lun a Vie 09:00 - 17:00 hs</p>
    </div>
    """, unsafe_allow_html=True)
with c_con2:
    st.markdown('<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3283.566874837583!2d-58.3837854!3d-34.6151247!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccad6111f1807%3A0x6a2977b2184f4f7!2sPiedras%201065%2C%20C1070AAW%20Cdad.%20Aut%C3%B3noma%20de%20Buenos%20Aires!5e0!3m2!1ses!2sar!4v1700000000000" width="100%" height="280" style="border:2px solid #0D47A1; border-radius:15px;"></iframe>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#0D47A1; font-weight: bold; margin-top:50px;'>© 2026 STVP - Sindicato de Trabajadores de Vigilancia Privada.</p>", unsafe_allow_html=True)
