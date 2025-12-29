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
URL_SHEET = "https://docs.google.com/spreadsheets/d/1mmMbsH6BNfrcmtq3T7xDizBVxjd--sWUIUdBZtSPuFM/edit?gid=6508803#gid=6508803"
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
    cel_afi = f_col2.text_input("Teléfono Celular")
    
    if st.form_submit_button("Enviar Datos"):
        if nombre_afi and dni_afi and cel_afi:
            try:
                # Intentamos leer la pestaña "Afiliaciones"
                try:
                    df_afi = conn.read(spreadsheet=URL_SHEET, worksheet="Afiliaciones")
                except:
                    df_afi = pd.DataFrame(columns=["Nombre", "DNI", "Empresa", "Celular", "Fecha"])

                nueva_fila = pd.DataFrame([{
                    "Nombre": nombre_afi, "DNI": dni_afi, 
                    "Empresa": empresa_afi, "Celular": cel_afi,
                    "Fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }])
                
                actualizado = pd.concat([df_afi, nueva_fila], ignore_index=True)
                conn.update(spreadsheet=URL_SHEET, worksheet="Afiliaciones", data=actualizado)
                
                st.success(f"¡Excelente {nombre_afi}! Tus datos se registraron con éxito.")
                st.balloons()
            except Exception as e:
                st.error("Error al guardar. Verificá que el Sheet tenga acceso de Editor.")
        else:
            st.warning("Por favor completá los campos obligatorios.")

st.markdown("---")

# --- SECCIÓN: CONSULTA Y PAGO (LECTURA DE DEUDA DESDE PESTAÑA 'CUOTA') ---
st.markdown('<div id="consulta" class="section-title">🔍 Consulta de Deuda</div>', unsafe_allow_html=True)
con_c1, con_c2, con_c3 = st.columns([1, 2, 1])
with con_c2:
    dni_search = st.text_input("Ingresá tu DNI para consultar total adeudado:", placeholder="Ej: 26688868")
    if st.button("Consultar Ahora"):
        try:
            # Leemos la pestaña 'Cuota'
            df_deudas = conn.read(spreadsheet=URL_SHEET, worksheet="Cuota")
            df_deudas.columns = [c.strip() for c in df_deudas.columns]
            
            res = df_deudas[df_deudas['DNI'].astype(str) == dni_search]
            
            if not res.empty:
                st.info(f"Afiliado registrado: **{res.iloc[0]['NOMBRE']}**")
                deuda_val = res.iloc[0]['TOTAL ADEUDADO']
                if "$ 0" in str(deuda_val) or "0.00" in str(deuda_val) or str(deuda_val).strip() == "":
                    st.success("✅ **¡Estás al día!** No registrás deuda.")
                else:
                    st.warning(f"⚠️ **Total Adeudado: {deuda_val}**")
            else:
                st.error("DNI no encontrado en el padrón de cuotas.")
        except Exception as e:
            st.error(f"Error al leer la base de datos: {e}")

st.markdown("---")

# --- SECCIÓN: CONTACTO Y UBICACIÓN ---
st.markdown('<div id="contacto" class="section-title">📞 Contacto y Ubicación</div>', unsafe_allow_html=True)
cont1, cont2 = st.columns(2)
with cont1:
    st.markdown("""
    ### Sede Central STVP
    - **🏛️ Dirección:** Piedras 1065, Ciudad Autónoma de Buenos Aires.
    - **📧 Email:** stvp.sindicatodeseguridad@gmail.com
    - **📜 Inscripción Gremial:** Nº 2822
    - **⏰ Horario:** Lunes a Viernes 09:00 - 17:00 hs
    """)
with cont2:
    # Mapa de Google Maps embebido (Piedras 1065, CABA)
    st.markdown("""
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3283.565780521404!2d-58.3822183!3d-34.615147!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccad06236353d%3A0x647e38356134b2f4!2sPiedras%201065%2C%20C1070AAW%20CABA!5e0!3m2!1ses!2sar!4v1700000000000!5m2!1ses!2sar" 
    width="100%" height="300" style="border:0; border-radius:15px;" allowfullscreen="" loading="lazy"></iframe>
    """, unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.markdown("<br><hr><p style='text-align:center; color:grey;'>© 2024 STVP - Sindicato de Trabajadores de Vigilancia Privada. Piedras 1065, CABA.</p>", unsafe_allow_html=True)
