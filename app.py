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
    /* 1. Background Image with Blur and Fit */
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                          url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    
    /* 2. Force Wide Layout and fix scrolling */
    .block-container {{
        padding-top: 1.4rem !important;
        max-width: 95% !important;
    }}



    /* 3. Enhanced Glassmorphism Cards */
    div[data-testid="stVerticalBlockBorderControl"] {{
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        border-radius: 20px !important;
        padding: 30px !important; /* Increased internal space */
        min-height: 250px !important; /* Forces cards to be larger and equal */
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}

    
   /* 3. Fixing Phase Labels (Phase A, B, C) visibility */
    h4 {{
        color: #ffffff !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin-bottom: 10px !important;
    }}


    /* 4. Font Sizes and Visibility */
    h1 {{ font-size: 4rem !important; color: white !important; font-weight: 800 !important; }}
    h3 {{ font-size: 2.5rem !important; color: #ffffff !important; }}
    p, .stCaption {{ font-size: 1.2rem !important; color: #f0f0f0 !important; }}
    
    /* Ensuring the sidebar stays professional */
    [data-testid="stSidebar"] {{
        background-color: rgba(15, 32, 39, 0.8) !important;
        backdrop-filter: blur(10px);
    }}
      /* 5. Boosting Feature Headings and Text */
    h3 {{ 
        font-size: 2.2rem !important; 
        color: white !important;
        margin-bottom: 15px !important;
    }}

    .stCaption {{
        font-size: 1.1rem !important;
        color: #e0e0e0 !important;
        line-height: 1.4 !important;
    }}

    /* 6. Making the 'Status' warnings more readable */
    .stAlert p {{
        font-size: 1.2rem !important;
        font-weight: 600 !important;
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
