import streamlit as st

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="PMCG Tools Hub",
    page_icon="💼",
    layout="wide"
)

# ----------------- CUSTOM STYLING -----------------
st.markdown("""
    <style>
        body {
            background-color: #4B2E83;
            color: white;
        }
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #4B2E83 0%, #5E3EA1 100%);
            color: white;
        }
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }
        [data-testid="stToolbar"] {
            right: 2rem;
        }
        h1, h2, h3 {
            text-align: center;
            color: white !important;
        }
        .card {
            background: rgba(255,255,255,0.1);
            border-radius: 18px;
            padding: 30px 20px;
            text-align: center;
            transition: all 0.3s ease;
            height: 220px;
        }
        .card:hover {
            background: rgba(255,255,255,0.2);
            transform: translateY(-8px);
        }
        .card a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1rem;
        }
        .footer {
            text-align: center;
            margin-top: 60px;
            color: #E0E0E0;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)


# ----------------- PAGE TITLE -----------------
st.markdown("<h1>💼 PMCG AI Tools Hub</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:1.1rem;'>Select a tool to begin — powered by OpenAI and Streamlit</p>", unsafe_allow_html=True)
st.write("")

# ----------------- TOOL CARDS -----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="card">
            <h2>🧪 Testing Tool</h2>
            <p>Run and evaluate new model prompts and configurations.</p>
            <a href="https://testing-sxbopsnuxoqdfjkgwfkpey.streamlit.app/" target="_blank">Launch →</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card">
            <h2>🔍 Job Search Generator</h2>
            <p>Create optimized search strings for LinkedIn & DevelopmentAid.</p>
            <a href="https://search-generator.streamlit.app/" target="_blank">Launch →</a>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="card">
            <h2>📄 CV Assessment Tool</h2>
            <p>Analyze and assess resumes using AI-driven insights.</p>
            <a href="https://assess-cvs-c7copw3tnxvtusnmujw8kg.streamlit.app/" target="_blank">Launch →</a>
        </div>
    """, unsafe_allow_html=True)


# ----------------- FOOTER -----------------
st.markdown("""
    <div class="footer">
        <p>© 2025 PMCG • Delivering Progress</p>
    </div>
""", unsafe_allow_html=True)
