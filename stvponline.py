import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Portal STVP - Sindicato de Vigilancia",
    page_icon="🛡️",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS (CSS) ---
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
    .nav-bar a { margin: 0 15px; text-decoration: none; color: #2563eb; font-weight: bold; }
    .card {
        padding: 1.5rem;
        border-radius: 0.75rem;
        background-color: white;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

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
    <div style="margin-top: 80px;"></div>
    """, unsafe_allow_html=True)

# --- CONEXIÓN A GOOGLE SHEETS ---
# URL de la hoja principal para deudas y para guardar afiliaciones
URL_SHEET = "https://docs.google.com/spreadsheets/d/1B6DkX8W6yE6mQpS_zS9z-D8oH9uT-vX-8_yD3XU-y-M/edit"
conn = st.connection("gsheets", type=GSheetsConnection)

# --- SECCIÓN 1: INICIO ---
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
col_ini1, col_ini2 = st.columns([1, 2])
with col_ini1: 
    st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=200)
with col_ini2:
    st.title("Sindicato de Trabajadores de Vigilancia Privada")
    st.subheader("Portal de Autogestión")
    st.write("Bienvenido. Desde aquí podrás gestionar tu afiliación, consultar beneficios de turismo y acceder a tu credencial digital.")

st.markdown("---")

# --- SECCIÓN 2: BENEFICIOS ---
st.markdown('<div id="beneficios" class="section-title">🎁 Beneficios y Convenios</div>', unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)
with b1:
    st.markdown("""
    <div class="card">
        <h3>🚌 Turismo RolSol</h3>
        <p>Viajes y salidas grupales exclusivas.</p>
        <a href="https://whatsapp.com/channel/0029VbAua9BJENy8oScpAH2B" target="_blank">
            <button style="width:100%; background:#25d366; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer;">Canal WhatsApp</button>
        </a>
    </div>
    """, unsafe_allow_html=True)
with b2:
    st.markdown("""
    <div class="card">
        <h3>🏨 Luz y Fuerza</h3>
        <p>Hotelería y turismo social.</p>
        <a href="https://www.sind-luzyfuerza-cap.org.ar/slyf/secretarias/turismo/tarifas/" target="_blank">
            <button style="width:100%; background:#2563eb; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer;">Ver Tarifas</button>
        </a>
    </div>
    """, unsafe_allow_html=True)
with b3:
    st.markdown("""
    <div class="card">
        <h3>🏍️ Ciudad Moto</h3>
        <p>Descuentos especiales en motos y repuestos presentando tu credencial.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN 3: CREDENCIALES ---
st.markdown('<div id="credenciales" class="section-title">🪪 Credencial Digital</div>', unsafe_allow_html=True)
col_c1, col_c2 = st.columns(2)
with col_c1:
    st.write("### Identificación Digital")
    st.write("Válida para todos los convenios y trámites gremiales.")
    url_cred = "https://stvp-credencial.streamlit.app/#stvp-digital"
    st.markdown(f'<a href="{url_cred}" target="_blank"><button style="width:100%; background:#1e3a8a; color:white; padding:15px; border-radius:10px; font-weight:bold; cursor:pointer; border:none; font-size:1.2rem;">MOSTRAR CREDENCIAL</button></a>', unsafe_allow_html=True)
with col_c2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); padding: 25px; border-radius: 15px; color: white; border: 2px solid #fbbf24;">
        <p style="font-size: 0.7rem; letter-spacing: 2px;">SINDICATO TRABAJADORES VIGILANCIA PRIVADA</p>
        <h2 style="color: #fbbf24;">STVP DIGITAL</h2>
        <p>NOMBRE Y APELLIDO: <b>JUAN PÉREZ</b></p>
        <p>DNI: <b>XX.XXX.XXX</b></p>
        <div style="float: right; background: white; padding: 5px; border-radius: 4px; margin-top: -40px;">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=60x60&data=STVP" width="60">
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN 4: AFILIACIÓN (GUARDAR EN GOOGLE SHEETS) ---
st.markdown('<div id="afiliacion" class="section-title">📝 Afiliación Online</div>', unsafe_allow_html=True)
with st.form("form_afi"):
    f1, f2 = st.columns(2)
    nombre_afi = f1.text_input("Nombre Completo")
    dni_afi = f2.text_input("DNI")
    empresa_afi = f1.text_input("Empresa de Seguridad")
    cel_afi = f2.text_input("Celular")
    
    if st.form_submit_button("Enviar Solicitud"):
        if nombre_afi and dni_afi and cel_afi:
            try:
                # Leer hoja "Afiliaciones"
                try:
                    df_actual = conn.read(spreadsheet=URL_SHEET, worksheet="Afiliaciones")
                except:
                    df_actual = pd.DataFrame(columns=["Nombre", "DNI", "Empresa", "Celular", "Fecha"])

                nuevo_dato = pd.DataFrame([{
                    "Nombre": nombre_afi, "DNI": dni_afi, 
                    "Empresa": empresa_afi, "Celular": cel_afi,
                    "Fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }])
                
                df_final = pd.concat([df_actual, nuevo_dato], ignore_index=True)
                conn.update(spreadsheet=URL_SHEET, worksheet="Afiliaciones", data=df_final)
                
                st.success(f"¡Gracias {nombre_afi}! Tu solicitud se guardó correctamente.")
                st.balloons()
            except Exception as e:
                st.error("Error al guardar. Verificá los permisos del Google Sheet.")
        else:
            st.warning("Completá Nombre, DNI y Celular.")

st.markdown("---")

# --- SECCIÓN 5: CONSULTA Y PAGO (LEER DEUDAS) ---
st.markdown('<div id="consulta" class="section-title">🔍 Consulta de Deuda</div>', unsafe_allow_html=True)
dni_search = st.text_input("Ingresá tu DNI para consultar total adeudado:")
if st.button("Consultar Total"):
    try:
        # Aquí se asume que las deudas están en la primera hoja por defecto
        df_deudas = conn.read(spreadsheet=URL_SHEET)
        df_deudas.columns = [c.strip() for c in df_deudas.columns]
        res = df_deudas[df_deudas['DNI'].astype(str) == dni_search]
        if not res.empty:
            st.info(f"Afiliado: **{res.iloc[0]['NOMBRE']}**")
            st.warning(f"Total Adeudado: **{res.iloc[0]['TOTAL ADEUDADO']}**")
        else:
            st.error("DNI no encontrado.")
    except Exception as e:
        st.error(f"Error al conectar con la base de datos de deudas: {e}")

st.markdown("---")

# --- SECCIÓN 6: CONTACTO Y UBICACIÓN ---
st.markdown('<div id="contacto" class="section-title">📞 Contacto y Ubicación</div>', unsafe_allow_html=True)
con1, con2 = st.columns(2)
with con1:
    st.markdown("""
    ### Sede Central STVP
    - **Dirección:** Piedras 1065, CABA, Argentina.
    - **Email:** stvp.sindicatodeseguridad@gmail.com
    - **Inscripción Gremial:** Nº 2822
    - **Horario:** Lunes a Viernes 09:00 - 17:00 hs
    """)
with con2:
    st.markdown("""
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3283.5668276410464!2d-58.3824424!3d-34.6151125!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccad617050589%3A0xc0c6d59518062973!2sPiedras%201065%2C%20C1070AAW%20CABA!5e0!3m2!1ses!2sar!4v1700000000000" 
    width="100%" height="300" style="border:0; border-radius:15px;" allowfullscreen="" loading="lazy"></iframe>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:grey;'>© 2024 STVP - Piedras 1065, CABA.</p>", unsafe_allow_html=True)
