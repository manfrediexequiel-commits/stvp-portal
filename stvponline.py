import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Portal STVP - Sindicato de Vigilancia",
    page_icon="🛡️",
    layout="wide"
)

# --- 2. ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    .section-title {
        font-size: 2.2rem; font-weight: 800; color: #1A237E;
        text-align: center; margin: 2rem 0; text-transform: uppercase;
        letter-spacing: 1px;
    }
    p, span, label, .stMarkdown { color: #2C3E50 !important; font-weight: 500; }
    .nav-bar {
        position: fixed; top: 0; left: 0; width: 100%;
        background-color: #ffffff; z-index: 1000; padding: 15px;
        text-align: center; border-bottom: 3px solid #1A237E;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .nav-bar a { margin: 0 15px; text-decoration: none; color: #1A237E; font-weight: 700; font-size: 0.85rem; }
    .nav-bar a:hover { color: #D32F2F; }
    .white-container {
        background-color: #ffffff; padding: 30px; border-radius: 16px;
        border: 1px solid #E2E8F0; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    .btn-whatsapp-rolsol {
        background-color: #2563EB; color: white !important;
        padding: 10px 20px; text-decoration: none; border-radius: 8px;
        font-weight: bold; display: inline-block; font-size: 0.8rem;
    }
    .download-btn {
        display: inline-block; padding: 12px 24px; background-color: #EF4444;
        color: white !important; text-decoration: none; border-radius: 8px;
        font-weight: bold; text-align: center; font-size: 0.9rem; width: 100%;
    }
    .btn-credencial {
        background-color: #1A237E; color: white !important;
        padding: 15px 25px; text-decoration: none; border-radius: 10px;
        font-weight: bold; display: inline-block; text-align: center;
        box-shadow: 0 4px 15px rgba(26, 35, 126, 0.4);
    }
    .card-sample {
        background: linear-gradient(135deg, #1A237E 0%, #0D47A1 100%);
        color: white !important; border-radius: 15px; padding: 25px;
        max-width: 350px; margin: auto; box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.2);
    }
    .whatsapp-float {
        position: fixed; width: 60px; height: 60px; bottom: 30px; right: 30px;
        background-color: #22C55E; color: white; border-radius: 50px;
        text-align: center; box-shadow: 0 10px 25px rgba(34, 197, 94, 0.4);
        z-index: 9999; display: flex; align-items: center; justify-content: center;
    }
    </style>
    
    <a href="https://wa.me/5491152628936" class="whatsapp-float" target="_blank">
        <svg width="30" height="30" fill="white" viewBox="0 0 16 16">
            <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
        </svg>
    </a>
    """, unsafe_allow_html=True)

# --- 3. NAVEGACIÓN ---
st.markdown("""
    <div class="nav-bar">
        <a href="#inicio">INICIO</a>
        <a href="#turismo">TURISMO</a>
        <a href="#camping">CAMPING</a>
        <a href="#hoteles">HOTELES</a>
        <a href="#credencial">CREDENCIAL</a>
        <a href="#afiliacion">AFILIACIÓN</a>
        <a href="#contacto">SEDE</a>
    </div>
    <div style="margin-top: 100px;"></div>
""", unsafe_allow_html=True)

# --- 4. CABECERA ---
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
c_logo, c_title = st.columns([1, 4])
with c_logo: 
    st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=140)
with c_title:
    st.markdown("<h1 style='color: #1A237E; margin-bottom:0;'>STVP - Sindicato Vigilancia</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #475569;'>Gestión, Turismo y Beneficios</h4>", unsafe_allow_html=True)

# --- 5. TURISMO ROLSOL ---
st.markdown('<div id="turismo" class="section-title">🚌 Turismo RolSol</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
ct1, ct2 = st.columns([3, 1])
with ct1: st.subheader("Temporada Verano 2026")
with ct2:
    canal_whatsapp = "https://whatsapp.com/channel/0029VbAua9BJENy8oScpAH2B"
    st.markdown(f'<a href="{canal_whatsapp}" target="_blank" class="btn-whatsapp-rolsol">📢 Canal de WhatsApp</a>', unsafe_allow_html=True)

r1c1, r1c2, r1c3, r1c4 = st.columns(4)
with r1c1: st.image("https://i.postimg.cc/g0cwqwtH/rolsol1.jpg", caption="Bariloche", use_container_width=True)
with r1c2: st.image("https://i.postimg.cc/8CkFBFXH/rolsol2.jpg", caption="Villa de Merlo", use_container_width=True)
with r1c3: st.image("https://i.postimg.cc/5t9HqHKp/rolsol.jpg", caption="Mar del Plata", use_container_width=True)
with r1c4: st.image("https://i.postimg.cc/7LPCMCtM/rolsol3.jpg", caption="Noroeste", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 6. CAMPING FATICA ---
st.markdown('<div id="camping" class="section-title">🌳 Camping Néstor Kirchner</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
col_camp1, col_camp2 = st.columns([1, 1.5])
with col_camp1:
    st.image("https://i.postimg.cc/HLWJ4JvB/centro-nestor-kirchner.jpg", caption="Tarifario 25/26", use_container_width=True)
with col_camp2:
    st.markdown("<h3 style='color: #1A237E;'>Tarifas Afiliados STVP</h3>", unsafe_allow_html=True)
    st.markdown("- **Entrada General:** $3.000")
    st.markdown("- **Alojamiento diario:** $10.000")
    st.markdown("- **Parcela carpa:** $8.000")
    st.info("📍 Ruta 8 km. 76, Exaltación de la Cruz")
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. HOTELES LUZ Y FUERZA ---
st.markdown('<div id="hoteles" class="section-title">🏖️ Hotelería Luz y Fuerza</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
col_lyf1, col_lyf2 = st.columns([3, 1])
with col_lyf1:
    st.markdown("##### Convenio de Turismo Social - Temporada de Verano")
    st.write("Contamos con plazas en San Bernardo, Mar del Plata y Villa Giardino.")
with col_lyf2:
    folleto_drive = "https://drive.google.com/file/d/1jhcYwAVWGr9ZSHIiAgaPyU_j4eJho_yx/view?usp=drive_link"
    st.markdown(f'<a href="{folleto_drive}" target="_blank" class="download-btn">📥 PDF COMPLETO</a>', unsafe_allow_html=True)

tabs_lyf = st.tabs(["San Bernardo", "Mar del Plata", "Villa Giardino"])
with tabs_lyf[0]:
    st.write("**Hotel Por la Liberación Nacional** - Calle Chiozza 2455")
    st.table({"Habitación": ["Doble", "Triple", "Cuádruple"], "Tarifa Afiliado": ["$100.000", "$95.000", "$90.000"]})
with tabs_lyf[1]:
    st.write("**Hotel Oscar Lescano** - Frente al Mar")
    st.write("Servicio de buffet completo y recreación para niños.")
with tabs_lyf[2]:
    st.write("**Villa Giardino (Córdoba)**")
    st.write("Entorno natural serrano con pileta y pensión completa.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. SECCIÓN CREDENCIAL DIGITAL ---
st.markdown('<div id="credencial" class="section-title">🪪 Credencial Digital</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
col_cre1, col_cre2 = st.columns([1, 1])
with col_cre1:
    st.markdown("<h3 style='color: #1A237E;'>Tu identidad sindical, siempre con vos</h3>", unsafe_allow_html=True)
    st.write("Accede de forma rápida y segura a tu credencial digital.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<a href="https://stvp-credencial.streamlit.app/#stvp-digital" target="_blank" class="btn-credencial">ACCEDER A MI CREDENCIAL</a>', unsafe_allow_html=True)
with col_cre2:
    st.markdown("""
    <div class="card-sample">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <b style="color:white;">STVP DIGITAL</b>
            <img src="https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png" width="40">
        </div>
        <hr style="border:0.5px solid rgba(255,255,255,0.3)">
        <div style="font-size: 0.8rem; margin-top:10px; color:#E3F2FD;">AFILIADO:</div>
        <div style="font-size: 1.2rem; font-weight: bold; color:white;">NOMBRE COMPLETO</div>
        <div style="font-size: 0.8rem; margin-top:10px; color:#E3F2FD;">DNI:</div>
        <div style="font-size: 1.1rem; color:white;">XX.XXX.XXX</div>
        <div style="text-align:right; font-size: 0.7rem; margin-top:15px; opacity:0.8; color:white;">ESTADO: ACTIVO 2026</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 9. AFILIACIÓN (VERSION WHATSAPP SIN ERRORES DE CLAVE) ---
st.markdown('<div id="afiliacion" class="section-title">📝 Solicitud de Afiliación</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
with st.form("afi_form", clear_on_submit=True):
    f1, f2 = st.columns(2)
    nombre = f1.text_input("Nombre y Apellido*")
    dni = f2.text_input("DNI*")
    empresa = f1.text_input("Empresa de Seguridad*")
    celular = f2.text_input("WhatsApp de Contacto*")
    intereses = st.multiselect("Me interesa info de:", ["Turismo RolSol", "Hoteles LyF", "Camping", "Credencial Digital"])
    
    submit = st.form_submit_button("PREPARAR SOLICITUD")
    
    if submit:
        if nombre and dni and celular:
            texto_wa = f"Hola STVP! Mi nombre es {nombre}, DNI {dni}. Trabajo en {empresa}. Me interesa: {', '.join(intereses)}. Quiero afiliarme."
            # Codificar el texto para URL
            import urllib.parse
            texto_url = urllib.parse.quote(texto_wa)
            wa_link = f"https://wa.me/5491152628936?text={texto_url}"
            
            st.success("✅ Datos validados.")
            st.markdown(f'<a href="{wa_link}" target="_blank" class="download-btn">🟢 ENVIAR SOLICITUD POR WHATSAPP</a>', unsafe_allow_html=True)
            st.info("Haga clic en el botón verde de arriba para finalizar el envío.")
        else:
            st.warning("Por favor complete los campos obligatorios.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 10. SEDE Y MAPA ---
st.markdown('<div id="contacto" class="section-title">📍 Sede Central</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container" style="text-align:center;">', unsafe_allow_html=True)
st.markdown("<h4 style='color: #1A237E;'>Piedras 1065, Constitución, CABA</h4>", unsafe_allow_html=True)
map_data = pd.DataFrame({'lat': [-34.6215322], 'lon': [-58.3814838]})
st.map(map_data, zoom=14)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#94A3B8; font-size: 0.8rem;'>© 2026 STVP - Sindicato de Trabajadores de Vigilancia Privada</p>", unsafe_allow_html=True)
