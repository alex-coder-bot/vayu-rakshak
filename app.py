import streamlit as st
from PIL import Image  # Capital PIL, even though the library is called Pillow
# 1. Page Configuration
st.set_page_config(page_title="Vayu Rakshak | AI Aviation Safety", page_icon="🛡️", layout="wide")

# Custom CSS for that "Popping" effect
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                          url("https://images.unsplash.com/photo-1559135197-8a45ea74d367?q=80&w=1920");
        background-size: cover;
        background-attachment: fixed;
    }
    </style>
    """, unsafe_allow_html=True)

# Add a professional banner in the sidebar
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&q=80&w=300", caption="Vayu Rakshak v1.0")
    st.divider()
    st.markdown("### 🛠️ Status: **Ready for Field Test**")


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
