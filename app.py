import streamlit as st
from groq import Groq
import streamlit.components.v1 as components

# 1. إعدادات محركات البحث (SEO Meta Tags)
# هاد الجزء ضروري باش جوجل يعرف الموقع علاش كيهضر
st.set_page_config(
    page_title="HumanAI Pro - Free Undetectable AI Bypass Tool (2026)",
    page_icon="✍️",
    layout="centered"
)

# حقن الـ Meta Tags في الـ Head ديال الصفحة
st.markdown(f"""
    <head>
        <meta name="description" content="HumanAI Pro is the #1 free undetectable AI humanizer. Convert ChatGPT, Gemini, and Claude text to human-like content and bypass AI detectors like GPTZero and Turnitin instantly.">
        <meta name="keywords" content="AI Humanizer, Undetectable AI, Bypass AI Detection, ChatGPT Humanizer, Free AI Text Converter, Groq LPU, Llama 3">
        <meta name="author" content="HumanAI Pro Team">
        <meta property="og:title" content="HumanAI Pro - Undetectable AI Bypass Tool">
        <meta property="og:description" content="Convert AI text to human writing in milliseconds using Groq LPU technology.">
        <meta property="og:type" content="website">
    </head>
""", unsafe_allow_html=True)

# 2. حقن إعلانات Adsterra
st.markdown("""
    <script src="https://rungbeacon.com/92/97/aa/9297aacea9c7c8e8d0d9acb6693e5029.js"></script>
    <script src="https://rungbeacon.com/58/3a/7e/583a7e58b9c89a27975b78aca70edfa3.js"></script>
""", unsafe_allow_html=True)

# 3. CSS للديزاين
st.markdown("""
    <style>
    .main { background-color: #f9fafb; }
    .stTextArea textarea { border-radius: 12px; border: 2px solid #e5e7eb; }
    .stButton>button { background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: white; border-radius: 10px; font-weight: 700; }
    .seo-card { background: white; padding: 2rem; border-radius: 1rem; border: 1px solid #e5e7eb; margin-top: 2rem; line-height: 1.8; }
    h1 { font-weight: 800; color: #1e293b; }
    </style>
    """, unsafe_allow_html=True)

# 4. الربط مع Groq
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("API Key Missing!")
    st.stop()

# --- القائمة الجانبية ---
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to", ["Home", "Privacy Policy", "Terms", "Contact"])
    st.markdown("---")
    st.write("🔥 **Speed:** Ultra Fast")
    st.write("🤖 **Model:** Llama-3 70B")

if page == "Home":
    # --- العناوين (H1 و H2 ضروريين لـ SEO) ---
    st.markdown("<h1>Humanize AI Text & Bypass Detection</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Transform ChatGPT content into 100% human-grade writing.</h2>", unsafe_allow_html=True)
    
    user_text = st.text_area("Paste your AI content here:", height=200)
    
    if st.button("Humanize Now ✨"):
        if user_text:
            with st.spinner('Processing...'):
                completion = client.chat.completions.create(
                    messages=[{"role": "system", "content": "Rewrite this to be human-like, natural, and pass AI detection."},
                              {"role": "user", "content": user_text}],
                    model="llama3-70b-8192",
                )
                res = completion.choices[0].message.content
                st.markdown("### ✅ Undetectable Result:")
                st.info(res)
        else:
            st.warning("Please input text.")

    # --- مقالة SEO مدعومة بـ Keywords ---
    st.markdown("""
    <div class="seo-card">
        <h3>The Ultimate Free AI Humanizer Tool</h3>
        <p>Are you struggling with <b>AI detectors</b>? Our <b>Undetectable AI</b> tool is specifically designed to bypass 
        platforms like <b>GPTZero</b>, <b>Originality.ai</b>, and <b>Turnitin</b>. By using the advanced <b>Llama 3 70B</b> 
        model hosted on <b>Groq LPU</b>, we ensure the highest quality of human-like flow.</p>
        
        <h4>Why Humanize Your Content?</h4>
        <p>Google's 2026 algorithms prioritize <i>helpful content</i>. Mass-produced AI text often lacks the nuance required to rank. 
        Our tool adds the 'human touch' by varying sentence structure and vocabulary, making your SEO strategy safer and more effective.</p>
    </div>
    """, unsafe_allow_html=True)

# ... (باقي الصفحات القانونية كتبقى كما هي)
