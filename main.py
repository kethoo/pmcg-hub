import streamlit as st

st.set_page_config(page_title="PMCG Tools Hub", layout="wide")

st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
        }
        .tool-card {
            background-color: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            transition: all 0.3s ease;
        }
        .tool-card:hover {
            background-color: rgba(255,255,255,0.2);
            transform: translateY(-5px);
        }
        a {
            text-decoration: none;
            color: #fff;
            font-weight: 600;
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🧭 PMCG Tools Hub</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Choose which AI tool to launch below</p>", unsafe_allow_html=True)
st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="tool-card">
            <h2>🧪 Testing Tool</h2>
            <p>Run experimental model or data tests</p>
            <a href="https://testing-sxbopsnuxoqdfjkgwfkpey.streamlit.app/" target="_blank">Launch →</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="tool-card">
            <h2>🔍 Job Search Generator</h2>
            <p>Generate optimized job search strings</p>
            <a href="https://search-generator.streamlit.app/" target="_blank">Launch →</a>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="tool-card">
            <h2>📄 CV Assessment Tool</h2>
            <p>Analyze and evaluate resumes automatically</p>
            <a href="https://assess-cvs-c7copw3tnxvtusnmujw8kg.streamlit.app/" target="_blank">Launch →</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Developed by PMCG • Powered by OpenAI & Streamlit 🚀</p>", unsafe_allow_html=True)
