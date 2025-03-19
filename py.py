import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Eid Mubarak",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS with more visual elements but avoiding JavaScript issues
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');
    
    body {
        background-color: #0a1931;
        color: white;
        font-family: 'Poppins', Arial, sans-serif;
    }
    
    .main {
        background-color: #0a1931;
        background-image: radial-gradient(circle, rgba(255,255,255,0.05) 1px, transparent 1px);
        background-size: 30px 30px;
    }
    
    .title {
        font-family: 'Great Vibes', cursive;
        color: #d4af37;
        text-align: center;
        font-size: 5rem;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 10px rgba(212, 175, 55, 0.3);
    }
    
    .subtitle {
        text-align: center;
        color: white;
        font-size: 1.5rem;
        margin-bottom: 2rem;
    }
    
    h2 {
        color: #d4af37;
        text-align: center;
        font-size: 1.8rem;
    }
    
    p {
        text-align: center;
    }
    
    .container {
        margin: 1rem auto;
        max-width: 1000px;
    }
    
    .countdown-box {
        border: 2px solid #d4af37;
        border-radius: 15px;
        padding: 1.5rem 1rem;
        text-align: center;
        background-color: rgba(10, 25, 49, 0.6);
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
    }
    
    .countdown-value {
        color: #d4af37;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
    }
    
    .countdown-label {
        color: white;
        text-transform: uppercase;
        font-size: 0.9rem;
        letter-spacing: 1px;
    }
    
    .message-box {
        border: 1px solid #d4af37;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        background-color: rgba(10, 25, 49, 0.4);
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.1);
    }
    
    .message-title {
        color: #d4af37;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .bismillah {
        font-family: 'Amiri', serif;
        font-size: 2.5rem;
        color: #d4af37;
        text-align: center;
        margin: 2rem 0;
        text-shadow: 0 0 10px rgba(212, 175, 55, 0.3);
    }
    
    .footer {
        text-align: center;
        margin-top: 2rem;
        opacity: 0.7;
        padding: 1rem;
    }
    
    /* Lantern styling with pure CSS */
    .lantern-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .lantern {
        position: relative;
        width: 40px;
        height: 60px;
        background-color: #d4af37;
        border-radius: 20px;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
    }
    
    .lantern::before {
        content: '';
        position: absolute;
        top: -10px;
        left: 15px;
        width: 10px;
        height: 10px;
        background-color: #d4af37;
        border-radius: 50%;
    }
    
    .lantern::after {
        content: '';
        position: absolute;
        top: -20px;
        left: 17px;
        width: 6px;
        height: 20px;
        background-color: #d4af37;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Button styling */
    .stButton>button {
        background-color: #d4af37 !important;
        color: #0a1931 !important;
        font-weight: bold !important;
        border: none !important;
        padding: 0.5rem 1.5rem !important;
        border-radius: 30px !important;
        box-shadow: 0 0 10px rgba(212, 175, 55, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>Eid Mubarak</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Het gezegende feest vieren met vreugde en dankbaarheid</p>", unsafe_allow_html=True)

# Lanterns with CSS
st.markdown("""
<div class="lantern-container">
    <div class="lantern" style="height: 50px;"></div>
    <div class="lantern" style="height: 70px;"></div>
    <div class="lantern" style="height: 55px;"></div>
    <div class="lantern" style="height: 65px;"></div>
</div>
""", unsafe_allow_html=True)

# Mosque with more detail
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
        <!-- Main dome -->
        <ellipse cx="200" cy="60" rx="60" ry="30" fill="#ffc94b"/>
        <!-- Mosque body -->
        <rect x="80" y="60" width="240" height="100" fill="#ffc94b"/>
        <!-- Main door -->
        <path d="M180 160 L180 100 Q200 80 220 100 L220 160" fill="#0a1931"/>
        <!-- Left minaret -->
        <rect x="50" y="60" width="15" height="120" fill="#ffc94b"/>
        <circle cx="57.5" cy="50" r="10" fill="#ffc94b"/>
        <!-- Right minaret -->
        <rect x="335" y="60" width="15" height="120" fill="#ffc94b"/>
        <circle cx="342.5" cy="50" r="10" fill="#ffc94b"/>
        <!-- Small domes -->
        <ellipse cx="130" cy="60" rx="20" ry="10" fill="#ffc94b"/>
        <ellipse cx="270" cy="60" rx="20" ry="10" fill="#ffc94b"/>
        <!-- Windows -->
        <rect x="100" y="100" width="15" height="25" rx="7" fill="#0a1931"/>
        <rect x="140" y="100" width="15" height="25" rx="7" fill="#0a1931"/>
        <rect x="245" y="100" width="15" height="25" rx="7" fill="#0a1931"/>
        <rect x="285" y="100" width="15" height="25" rx="7" fill="#0a1931"/>
        <!-- Moon -->
        <circle cx="350" cy="30" r="15" fill="#d4af37"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# Countdown Section
st.markdown("<h2>Resterende Tijd Tot Eid</h2>", unsafe_allow_html=True)
st.markdown("<p>Zondag 30 maart 2025</p>", unsafe_allow_html=True)

# Set countdown end date
end_date = datetime(2025, 3, 30)

# Get countdown values
def get_countdown():
    now = datetime.now()
    delta = end_date - now
    
    # If countdown is finished
    if delta.total_seconds() <= 0:
        return 0, 0, 0, 0
    
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes, seconds

# Create columns for countdown display
col1, col2, col3, col4 = st.columns(4)

# Display countdown
days, hours, minutes, seconds = get_countdown()

with col1:
    st.markdown(f"""
    <div class="countdown-box">
        <h3 class="countdown-value">{days:02d}</h3>
        <p class="countdown-label">Dagen</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="countdown-box">
        <h3 class="countdown-value">{hours:02d}</h3>
        <p class="countdown-label">Uren</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="countdown-box">
        <h3 class="countdown-value">{minutes:02d}</h3>
        <p class="countdown-label">Minuten</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="countdown-box">
        <h3 class="countdown-value">{seconds:02d}</h3>
        <p class="countdown-label">Seconden</p>
    </div>
    """, unsafe_allow_html=True)

# Add space
st.markdown("<br>", unsafe_allow_html=True)

# Eid message
st.markdown("""
<div class="message-box">
    <h2 class="message-title">Eid Mubarak</h2>
    <p>Moge deze Eid vreugde, geluk, vrede en voorspoed brengen voor jou en je familie. De gezegende maand Ramadan leert ons de waarde van mededogen, geduld en dankbaarheid. Terwijl we wachten op Eid al-Fitr, laten we deze lessen onthouden en meenemen in ons leven.</p>
</div>
""", unsafe_allow_html=True)

# Islamic decoration
st.markdown("""
<div class="bismillah">﷽</div>
""", unsafe_allow_html=True)

# Decorative pattern
st.markdown("""
<div style="display: flex; justify-content: center; margin: 2rem 0;">
    <svg width="300" height="50" xmlns="http://www.w3.org/2000/svg">
        <line x1="10" y1="25" x2="290" y2="25" stroke="#d4af37" stroke-width="1" stroke-dasharray="5,5" />
        <circle cx="50" cy="25" r="15" fill="none" stroke="#d4af37" stroke-width="2" />
        <circle cx="50" cy="25" r="5" fill="#d4af37" />
        
        <circle cx="150" cy="25" r="15" fill="none" stroke="#d4af37" stroke-width="2" />
        <circle cx="150" cy="25" r="5" fill="#d4af37" />
        
        <circle cx="250" cy="25" r="15" fill="none" stroke="#d4af37" stroke-width="2" />
        <circle cx="250" cy="25" r="5" fill="#d4af37" />
    </svg>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Gemaakt door Zakaria Akanni</p>
</div>
""", unsafe_allow_html=True)

# Refresh button for updating the countdown - using st.rerun() instead of st.experimental_rerun()
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Ververs Aftellen"):
        st.rerun()  # Using the updated function name
