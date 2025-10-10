import streamlit as st

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="PMCG Tools Hub",
    page_icon="pmcg-logo.png",  # Optional favicon if supported
    layout="wide"
)

# ----------------- CUSTOM STYLING -----------------
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #4B2E83 0%, #5E3EA1 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        [data-testid="stHeader"], [data-testid="stToolbar"] {
            background: rgba(0,0,0,0);
        }
        h1, h2, h3, p {
            color: white !important;
        }

        /* Title section */
        .title-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            margin-top: 2rem;
        }
        .title-container img {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            object-fit: cover;
        }
        .title-container h1 {
            font-size: 2rem;
            font-weight: 700;
            margin: 0;
        }

        /* Card grid layout */
        .card-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 2rem;
            padding: 2rem 0;
        }
        .card {
            flex: 1 1 280px;
            max-width: 350px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 18px;
            padding: 30px 20px;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        .card:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-6px);
        }
        .card h2 {
            font-size: 1.4rem;
            margin-bottom: 10px;
        }
        .card p {
            color: #EAEAEA;
            font-size: 0.95rem;
            margin-bottom: 15px;
        }
        .card a {
            display: inline-block;
            color: white;
            text-decoration: none;
            font-weight: 600;
            border: 1px solid white;
            border-radius: 8px;
            padding: 6px 12px;
            transition: all 0.3s ease;
        }
        .card a:hover {
            background: white;
            color: #4B2E83;
        }

        /* Footer placement */
        .footer {
            text-align: center;
            color: #E0E0E0;
            font-size: 0.9rem;
            margin-top: auto;
            padding: 1.5rem 0 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------- TITLE SECTION -----------------
st.markdown("""
    <div class="title-container">
        <img src="https://raw.githubusercontent.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>/main/pmcg-logo.png" alt="PMCG Logo">
        <h1>PMCG AI Tools Hub</h1>
    </div>
    <p style='text-align:center;font-size:1.1rem;'>Select a tool to begin — powered by OpenAI and Streamlit</p>
""", unsafe_allow_html=True)

# ----------------- TOOL CARDS -----------------
st.markdown("""
<div class="card-container">
    <div class="card">
        <h2>🧪 Testing Tool</h2>
        <p>Run and evaluate new model prompts and configurations.</p>
        <a href="https://testing-sxbopsnuxoqdfjkgwfkpey.streamlit.app/" target="_blank">Launch →</a>
    </div>
    <div class="card">
        <h2>🔍 Job Search Generator</h2>
        <p>Create optimized search strings for LinkedIn & DevelopmentAid.</p>
        <a href="https://search-generator.streamlit.app/" target="_blank">Launch →</a>
    </div>
    <div class="card">
        <h2>📄 CV Assessment Tool</h2>
        <p>Analyze and assess resumes using AI-driven insights.</p>
        <a href="https://assess-cvs-c7copw3tnxvtusnmujw8kg.streamlit.app/" target="_blank">Launch →</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- FOOTER -----------------
st.markdown("""
    <div class="footer">
        © 2025 PMCG • Delivering Progress
    </div>
""", unsafe_allow_html=True)
