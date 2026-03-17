import base64
import streamlit as st
st.set_page_config(layout="wide")

# Function to encode the image
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Use your actual filename here
bin_str = get_base64('ap2.jpg') 

st.markdown(f"""
    <style>
    /* 1. Remove unnecessary padding at the top */
    .block-container {{
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
    }}

    /* 2. Adjust background to be fixed and center */
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)), 
                          url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 3. Scale down fonts for laptop screens */
    h1 {{ font-size: 2.8rem !important; margin-bottom: 0px !important; }}
    h3 {{ font-size: 1.8rem !important; margin-top: 10px !important; }}
    p, .stCaption {{ font-size: 1rem !important; line-height: 1.2 !important; }}

    /* 4. Optimize Cards for Desktop */
    div[data-testid="stVerticalBlockBorderControl"] {{
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(12px) !important;
        padding: 15px !important; /* Smaller padding */
        min-height: 180px; /* Ensures all cards are same height */
    }}
    </style>
    """, unsafe_allow_html=True)






# 2. Hero Section
st.title("🛡️ Vayu Rakshak")
st.subheader("The 'Proof-of-Fix' Protocol for Zero-Error Aviation Maintenance")
st.markdown("---")

# 3. Features Grid with "Sutra" Card Aesthetics
st.markdown("### 🚀 Core Capabilities")
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.write("### 🤖") # Big Emoji instead of broken link
        st.write("**Closed-Loop Verification**")
        st.caption("AI-driven gates that lock safety reports until visual confirmation is achieved.")

with col2:
    with st.container(border=True):
        st.write("### 📱")
        st.write("**Edge-Inference Ready**")
        st.caption("Mobile-first architecture designed for offline hangar environments.")

with col3:
    with st.container(border=True):
        st.write("### ⚙️")
        st.write("**Modular Protocols**")
        st.caption("Instant injection of Boeing/Airbus blueprints via JSON-template engine.")

# 4. The Workflow Preview (The "Proof-of-Fix" logic)
st.markdown("### 🛠️ The Safety Workflow")
st.info("Our proprietary 3-Phase verification process:")

# We use columns to create a visual "step" effect
s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("#### Phase A")
    st.warning("**Detection**")
    st.caption("AI identifies sub-millimeter configuration errors.")

with s2:
    st.markdown("#### Phase B")
    st.warning("**Intervention**")
    st.caption("Mechanic performs and logs the corrective action.")

with s3:
    st.markdown("#### Phase C")
    st.success("**Verification**")
    st.caption("Visual re-scan generates an Immutable Audit Trail.")
    st.success("Redirecting to verification engine... (Enabled for Offline Phase)")
