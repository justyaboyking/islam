import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Eid Mubarak",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ultra-minimal CSS
st.markdown("""
<style>
    .main {
        background-color: #0f1116;
    }
    
    h1 {
        color: white;
        text-align: center;
        font-size: 3rem;
        margin-top: 3rem;
        margin-bottom: 0.5rem;
    }
    
    p {
        color: white;
        text-align: center;
    }
    
    .countdown-box {
        border: 2px solid #ffc94b;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        background-color: #0f1116;
    }
    
    .countdown-value {
        color: #ffc94b;
        font-size: 2rem;
        font-weight: bold;
        margin: 0;
    }
    
    .countdown-label {
        color: white;
        font-size: 0.9rem;
    }
    
    .lantern {
        color: #ffc94b;
        font-size: 2rem;
        text-align: center;
    }
    
    .mosque {
        color: #ffc94b;
        font-size: 3rem;
        text-align: center;
        margin: 2rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Button styling */
    .stButton>button {
        background-color: #ffc94b !important;
        color: #0f1116 !important;
        font-weight: bold !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>Eid Mubarak</h1>", unsafe_allow_html=True)
st.markdown("<p>Het gezegende feest vieren met vreugde en dankbaarheid</p>", unsafe_allow_html=True)

# Lanterns using emoji
st.markdown("<div class='lantern'>🪔 🪔 🪔 🪔</div>", unsafe_allow_html=True)

# Mosque using emoji
st.markdown("<div class='mosque'>🕌</div>", unsafe_allow_html=True)

# Countdown Section
st.markdown("<h3 style='text-align: center; color: white;'>Resterende Tijd Tot Eid</h3>", unsafe_allow_html=True)
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

# Refresh button for updating the countdown
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Ververs Aftellen"):
        st.rerun()
