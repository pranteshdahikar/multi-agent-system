import sys
import os
import streamlit as st

# ✅ Ensure parent directory (project root) is in Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import run_workflow

# 🧠 Streamlit App UI
st.set_page_config(page_title="Multi-Agent Repository Analyzer", page_icon="🚀")

st.title("🚀 Multi-Agent Repository Analyzer")
st.markdown("Analyze and improve your GitHub repository using an intelligent multi-agent system.")

# 🔹 Input section
repo_path = st.text_input("Enter local repository path:")

if st.button("Analyze Repository"):
    if not repo_path.strip():
        st.error("❌ Please enter a valid repository path.")
    else:
        with st.spinner("🔍 Analyzing repository... please wait..."):
            try:
                result = run_workflow(repo_path)
                st.success("✅ Analysis complete!")
                st.json(result)
            except Exception as e:
                st.error(f"⚠️ Error during analysis: {str(e)}")
                st.stop()

# Optional footer
st.markdown("---")
st.caption("🧩 Powered by Multi-Agent System | Streamlit Interface")
