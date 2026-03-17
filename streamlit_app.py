import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Vayu Rakshak | AI Aviation Safety", page_icon="🛡️", layout="wide")

# 2. Hero Section
st.title("🛡️ Vayu Rakshak")
st.subheader("The 'Proof-of-Fix' Protocol for Zero-Error Aviation Maintenance")
st.markdown("---")

# 3. Features Grid (The "Landing Page" feel)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png")
    st.write("**Closed-Loop Verification**")
    st.caption("AI-driven gates that lock safety reports until visual confirmation of mechanical integrity is achieved.")

with col2:
    st.image("https://img.icons8.com/fluency/96/smartphone-cpu.png")
    st.write("**Edge-Inference Ready**")
    st.caption("Mobile-first architecture designed for hangar environments with low connectivity.")

with col3:
    st.image("https://img.icons8.com/fluency/96/file-configuration.png")
    st.write("**Modular Protocols**")
    st.caption("Instant injection of Boeing/Airbus safety blueprints via our JSON-template engine.")

# 4. The Workflow Preview (The "Proof-of-Fix" logic)
st.markdown("### 🛠️ The Safety Workflow")
st.info("Our proprietary 3-Phase verification process:")
st.steps([
    "**Phase A: Detection** - AI identifies sub-millimeter configuration errors.",
    "**Phase B: Intervention** - Mechanic performs and logs the corrective action.",
    "**Phase C: Verification** - Visual re-scan generates an Immutable Audit Trail."
])

# 5. Call to Action for Judges
if st.button("Launch Prototype (Phase 1 Demo)"):
    st.success("Redirecting to verification engine... (Enabled for Offline Phase)")
