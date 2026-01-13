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
    /* Estilos generales */
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
    .credencial-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        padding: 25px;
        border-radius: 15px;
        color: white;
        border: 2px solid #fbbf24;
        box-shadow: 0 10px 15px rgba(0,0,0,0.3);
    }
    
    /* Botón flotante de WhatsApp */
    .whatsapp-float {
        position: fixed;
        width: 60px;
        height: 60px;
        bottom: 25px;
        right: 25px;
        background-color: #25d366;
        color: white;
        border-radius: 50px;
        text-align: center;
        font-size: 30px;
        box-shadow: 2px 5px 15px rgba(0,0,0,0.3);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .whatsapp-float:hover {
        background-color: #128c7e;
        transform: scale(1.1);
        color: white;
    }
    @media screen and (max-width: 768px) {
        .whatsapp-float { width: 50px; height: 50px; bottom: 20px; right: 20px; }
    }
    </style>
    
    <a href="https://wa.me/5491152628936?text=Hola%20STVP!%20Necesito%20realizar%20una%20consulta." 
       class="whatsapp-float" target="_blank">
        <svg width="30" height="30" fill="currentColor" viewBox="0 0 16 16">
          <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
        </svg>
    </a>
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
URL_SHEET = "https://docs.google.com/spreadsheets/d/1mmMbsH6BNfrcmtq3T7xDizBVxjd--sWUIUdBZtSPuFM/edit?gid=6508803#gid=6508803"
conn = st.connection("gsheets", type=GSheetsConnection)

@st.cache_data(ttl=600)
def get_data(worksheet_name):
    return conn.read(spreadsheet=URL_SHEET, worksheet=worksheet_name)

# --- SECCIÓN: INICIO ---
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
col_ini1, col_ini2 = st.columns([1, 2])
with col_ini1: 
    st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=200)
with col_ini2:
    st.title("Sindicato de Trabajadores de Vigilancia Privada")
    st.subheader("Portal de Autogestión Oficial")
    st.write("Gestioná tu afiliación, consultá deudas y accedé a beneficios exclusivos.")

st.markdown("---")

# --- SECCIÓN: BENEFICIOS (CON DATOS DEL FOLLETO) ---
st.markdown('<div id="beneficios" class="section-title">🎁 Beneficios y Convenios</div>', unsafe_allow_html=True)

# Tarjetas Rápidas
b1, b2, b3 = st.columns(3)
with b1:
    st.markdown('<div class="card"><h3>🚌 Turismo RolSol</h3><p>Viajes grupales con promociones.</p><a href="https://whatsapp.com/channel/0029VbAua9BJENy8oScpAH2B" target="_blank"><button style="width:100%; background:#25d366; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer;">WhatsApp</button></a></div>', unsafe_allow_html=True)
with b2:
    st.markdown('<div class="card"><h3>🏍️ Ciudad Moto</h3><p>Descuentos exclusivos en unidades y repuestos.</p></div>', unsafe_allow_html=True)
with b3:
    st.markdown('<div class="card"><h3>🏢 Otros</h3><p>Asesoría legal y descuentos en farmacias.</p></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🏖️ Detalle Convenio Luz y Fuerza - Temporada 25/26")
st.warning("⚠️ Tarifas válidas hasta diciembre de 2025. Menores de 3 a 12 años abonan el 50%.")

tab_sb, tab_mdq, tab_vg, tab_brc, tab_rec = st.tabs(["🌊 San Bernardo", "🏖️ Mar del Plata", "🌲 Villa Giardino", "🏔️ Bariloche", "⛲ Recreos"])

with tab_sb:
    st.markdown("#### Hotel 'Por la Liberación Nacional' (Todo Incluido)")
    st.write("📍 Chiozza 2455, San Bernardo. Piscina climatizada.")
    st.table({"Habitación": ["Doble", "Triple", "Cuádruple"], "Adulto": ["$100.000", "$95.000", "$90.000"], "Menor": ["$50.000", "$47.500", "$45.000"]})
    with st.expander("📅 Ver Contingentes (3 y 4 días)"):
        st.write("**Dic:** 01-12 al 05-12 | 05-12 al 08-12 | 12-12 al 15-12 | 19-12 al 22-12")
        st.write("**Ene:** 02-01 al 05-01 | 05-01 al 09-01 | 12-01 al 16-01 | 19-01 al 23-01")

with tab_mdq:
    st.markdown("#### Hotel 'Oscar Lescano' - Punta Mogotes")
    st.write("📍 Av. De Los Trabajadores 3971. Todo Incluido.")
    st.write("**Tarifas:** Doble: $100.000 | Triple: $95.000")
    st.caption("🎁 Beneficio: Descuento en Balneario 1.")

with tab_vg:
    st.markdown("#### Hotel 'Por los Derechos del Trabajador' (Córdoba)")
    st.write("📍 Villa Giardino. Estadías de 7 días.")
    st.table({"Habitación": ["Doble", "Triple", "Cuádruple"], "Precio": ["$83.000", "$78.850", "$74.700"]})
    with st.expander("📅 Ver Fechas (7 días)"):
        st.write("- 06-12 al 13-12 | 20-12 al 27-12 | 03-01 al 10-01 | 31-01 al 07-02")

with tab_brc:
    st.markdown("#### Hotel 'Alún Nehuén' (Bariloche)")
    st.write("📍 Av. Bustillo km 32. Vista al Lago Nahuel Huapi. Media Pensión.")
    st.write("**Tarifas:** Individual: $176.000 | Doble: $88.000 | Triple: $83.600")

with tab_rec:
    st.markdown("#### Campos de Recreo")
    st.write("- **Villa del Parque:** Evita 666, CABA.\n- **Tiger (Delta):** Río Luján.\n- **Ezeiza:** Autopista Riccheri km 23.5.")

st.markdown("---")

# --- SECCIÓN: CREDENCIALES ---
st.markdown('<div id="credenciales" class="section-title">🪪 Credencial Digital</div>', unsafe_allow_html=True)
col_c1, col_c2 = st.columns(2)
with col_c1:
    st.write("### Tu carnet siempre con vos")
    url_cred = "https://stvp-credencial.streamlit.app/#stvp-digital"
    st.markdown(f'<a href="{url_cred}" target="_blank"><button style="width:100%; background:#1e3a8a; color:white; padding:15px; border-radius:10px; font-weight:bold; cursor:pointer; border:none; font-size:1.2rem;">MOSTRAR CREDENCIAL</button></a>', unsafe_allow_html=True)
with col_c2:
    st.markdown('<div class="credencial-box"><p style="font-size: 0.7rem; letter-spacing: 2px;">SINDICATO TRABAJADORES VIGILANCIA PRIVADA</p><h2 style="color: #fbbf24;">STVP DIGITAL</h2><p>AFILIADO: NOMBRE Y APELLIDO</p><p>DNI: XX.XXX.XXX</p></div>', unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN: AFILIACIÓN ---
st.markdown('<div id="afiliacion" class="section-title">📝 Solicitud de Afiliación</div>', unsafe_allow_html=True)
with st.form("form_afiliacion"):
    f1, f2 = st.columns(2)
    nombre = f1.text_input("Nombre Completo")
    dni = f2.text_input("DNI")
    empresa = f1.text_input("Empresa")
    cel = f2.text_input("Celular")
    if st.form_submit_button("Enviar Solicitud"):
        if nombre and dni and cel:
            try:
                df_afi = get_data("Afiliaciones")
                nueva = pd.DataFrame([{"Nombre": nombre, "DNI": dni, "Empresa": empresa, "Celular": cel, "Fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}])
                conn.update(spreadsheet=URL_SHEET, worksheet="Afiliaciones", data=pd.concat([df_afi, nueva]))
                st.success("¡Datos registrados con éxito!")
            except: st.error("Error al guardar.")
        else: st.warning("Completá los campos obligatorios.")

st.markdown("---")

# --- SECCIÓN: CONSULTA ---
st.markdown('<div id="consulta" class="section-title">🔍 Consulta de Deuda</div>', unsafe_allow_html=True)
dni_s = st.text_input("Ingresá tu DNI para consultar deuda:")
if st.button("Consultar"):
    try:
        df_d = get_data("Cuota")
        res = df_d[df_d['DNI'].astype(str) == dni_s]
        if not res.empty:
            st.info(f"Afiliado: {res.iloc[0]['NOMBRE']}")
            st.warning(f"Deuda: {res.iloc[0]['TOTAL ADEUDADO']}")
        else: st.error("DNI no encontrado.")
    except: st.error("Error de conexión.")

st.markdown("---")

# --- SECCIÓN: CONTACTO ---
st.markdown('<div id="contacto" class="section-title">📞 Contacto</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown("### Sede Central STVP\n- 🏛️ Piedras 1065, CABA.\n- 📧 stvp.sindicatodeseguridad@gmail.com\n- ⏰ Lun a Vie 09:00 - 17:00 hs")
with c2:
    st.markdown('<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3283.472935270114!2d-58.382006!3d-34.617462!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccad6334f669b%3A0x6e267151e222956c!2sPiedras%201065%2C%20C1070AAU%20CABA!5e0!3m2!1ses-419!2sar!4v1715634567890!5m2!1ses-419!2sar" width="100%" height="250" style="border:0; border-radius:15px;"></iframe>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:grey; margin-top:50px;'>© 2024 STVP - Sindicato de Trabajadores de Vigilancia Privada.</p>", unsafe_allow_html=True)
