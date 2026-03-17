import streamlit as st
from PIL import Image  # Capital PIL, even though the library is called Pillow
# 1. Page Configuration
st.set_page_config(page_title="Vayu Rakshak | AI Aviation Safety", page_icon="🛡️", layout="wide")

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
