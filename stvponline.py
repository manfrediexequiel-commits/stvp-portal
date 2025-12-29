import streamlit as st
import time
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Portal STVP - Sindicato de Vigilancia",
    page_icon="🛡️",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
    <style>
    /* Estilo para las secciones */
    .section-container {
        padding: 60px 0;
        border-bottom: 1px solid #e2e8f0;
    }
    .card {
        padding: 1.5rem;
        border-radius: 0.75rem;
        background-color: white;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .section-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e3a8a;
        margin-top: 2rem;
        margin-bottom: 2rem;
        text-align: center;
    }
    /* Estilo Menú Sticky */
    .nav-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
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
    </style>
    """, unsafe_allow_html=True)

# --- MOCK DATA PARA CONSULTA DE PAGO ---
mock_deudas = [
    {"dni": "12345678", "nombre": "Juan Pérez", "deuda": 1500, "mes": "Diciembre 2024"},
    {"dni": "23456789", "nombre": "Ana García", "deuda": 0, "mes": "Al día"},
    {"dni": "34567890", "nombre": "Carlos López", "deuda": 2500, "mes": "Noviembre/Diciembre 2024"}
]

# --- NAVEGACIÓN SUPERIOR ---
st.markdown("""
    <div class="nav-bar">
        <a href="#inicio">INICIO</a>
        <a href="#beneficios">BENEFICIOS</a>
        <a href="#credenciales">CREDENCIALES</a>
        <a href="#afiliacion">AFILIACIÓN</a>
        <a href="#consulta">CONSULTA Y PAGO</a>
        <a href="#contacto">CONTACTO</a>
    </div>
    <div style="margin-top: 60px;"></div>
    """, unsafe_allow_html=True)

# --- SECCIÓN 1: INICIO ---
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
col_logo, col_intro = st.columns([1, 2])
with col_logo:
    st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=200)
with col_intro:
    st.title("Sindicato de Trabajadores de Vigilancia Privada")
    st.subheader("Portal Oficial de Autogestión")
    st.write("Bienvenido al centro de servicios digitales del STVP. Aquí podrás gestionar tu afiliación, consultar beneficios de turismo y acceder a tu credencial digital.")

st.markdown("---")

# --- SECCIÓN 2: BENEFICIOS ---
st.markdown('<div id="beneficios" class="section-title">🎁 Beneficios y Convenios</div>', unsafe_allow_html=True)
b_col1, b_col2, b_col3 = st.columns(3)

with b_col1:
    st.markdown("""
    <div class="card">
        <h3>🚌 Turismo RolSol</h3>
        <p>Accede a los mejores paquetes de viaje y salidas grupales con RolSol.</p>
        <a href="https://whatsapp.com/channel/0029VbAua9BJENy8oScpAH2B" target="_blank" style="text-decoration:none;">
            <button style="width:100%; background-color:#25d366; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer;">Canal de WhatsApp</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with b_col2:
    st.markdown("""
    <div class="card">
        <h3>🏨 Luz y Fuerza</h3>
        <p>Tarifas exclusivas en hoteles y complejos turísticos de Luz y Fuerza.</p>
        <a href="https://www.sind-luzyfuerza-cap.org.ar/slyf/secretarias/turismo/tarifas/" target="_blank" style="text-decoration:none;">
            <button style="width:100%; background-color:#2563eb; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer;">Ver Tarifas</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with b_col3:
    st.markdown("""
    <div class="card">
        <h3>🏍️ Ciudad Moto</h3>
        <p><b>Descuentos Exclusivos</b> para afiliados en la compra de unidades y repuestos.</p>
        <p style="color: #2563eb; font-weight: bold; margin-top: 10px;">¡Presentá tu credencial digital!</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN 3: CREDENCIALES ---
st.markdown('<div id="credenciales" class="section-title">🪪 Credenciales Digitales</div>', unsafe_allow_html=True)
st.info("Para identificarte en los comercios adheridos o ante las autoridades, accede a tu credencial digital aquí:")
cred_url = "https://stvp-credencial.streamlit.app/#stvp-digital"
st.markdown(f"""
    <div style="text-align: center;">
        <a href="{cred_url}" target="_blank">
            <button style="padding: 20px 40px; font-size: 20px; background-color: #1e3a8a; color: white; border: none; border-radius: 10px; cursor: pointer; font-weight: bold;">
                ABRIR MI CREDENCIAL DIGITAL
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN 4: AFILIACIÓN ---
st.markdown('<div id="afiliacion" class="section-title">📝 Solicitud de Afiliación</div>', unsafe_allow_html=True)
with st.form("form_afiliacion"):
    f_col1, f_col2 = st.columns(2)
    nombre = f_col1.text_input("Nombre completo")
    dni_f = f_col2.text_input("DNI")
    empresa = f_col1.text_input("Empresa de Seguridad")
    cel = f_col2.text_input("Celular de contacto")
    msg = st.text_area("Comentarios adicionales")
    
    if st.form_submit_button("Enviar Datos para Afiliación"):
        if nombre and dni_f:
            st.success("Solicitud recibida correctamente. Nos pondremos en contacto a la brevedad.")
            st.balloons()
        else:
            st.error("Por favor completa los campos obligatorios.")

st.markdown("---")

# --- SECCIÓN 5: CONSULTA Y PAGO ---
st.markdown('<div id="consulta" class="section-title">🔍 Consulta de Pago</div>', unsafe_allow_html=True)
c_col1, c_col2, c_col3 = st.columns([1, 2, 1])
with c_col2:
    dni_q = st.text_input("Ingresa tu DNI para ver estado de cuenta:")
    if st.button("Buscar Estado"):
        res = next((d for d in mock_deudas if d["dni"] == dni_q), None)
        if res:
            if res["deuda"] > 0:
                st.warning(f"Afiliado: {res['nombre']} - Deuda: ${res['deuda']} (Mes: {res['mes']})")
                st.write("Para regularizar, contacta a Tesorería vía Email.")
            else:
                st.success(f"¡Felicidades {res['nombre']}! Tu cuenta está al día.")
        else:
            st.error("DNI no registrado.")

st.markdown("---")

# --- SECCIÓN 6: CONTACTO ---
st.markdown('<div id="contacto" class="section-title">📞 Información de Contacto</div>', unsafe_allow_html=True)
con1, con2 = st.columns(2)
with con1:
    st.markdown("""
    ### Datos Principales
    - **📧 Email:** stvp.sindicatodeseguridad@gmail.com
    - **🏛️ Inscripción Gremial:** Nº 2822
    - **⏰ Horario:** Lunes a Viernes 09:00 - 17:00 hs
    """)
with con2:
    st.write("### Ubicación")
    st.write("Atención presencial bajo cita previa gestionada vía correo electrónico.")

# --- FOOTER ---
st.markdown("""
    <div style="text-align: center; padding: 50px; color: grey;">
        © 2024 Sindicato de Trabajadores de Vigilancia Privada (STVP) - Unidos por el trabajador.
    </div>
    """, unsafe_allow_html=True)
