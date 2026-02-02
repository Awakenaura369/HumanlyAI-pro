import streamlit as st
from groq import Groq

# 1. إعدادات الصفحة
st.set_page_config(page_title="Humanly AI Pro", layout="centered")

# 2. حل مشكلة الألوان (CSS) - فرض اللون الأسود
st.markdown("""
    <style>
    /* فرض اللون الأسود على كل شيء */
    .stApp, p, div, span, h1, h2, h3, h4, label {
        color: #000000 !important;
    }
    /* تحسين شكل خانة الكتابة */
    .stTextArea textarea {
        color: #000000 !important;
        background-color: #ffffff !important;
        border: 2px solid #6c5ce7 !important;
    }
    /* تحسين شكل البطاقة البيضاء */
    .seo-card {
        background-color: #f8f9fa !important;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ddd;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. جلب الـ API Key مع تنظيفه من أي سطر زايد
try:
    raw_key = st.secrets["GROQ_API_KEY"]
    api_key = raw_key.replace("\n", "").replace(" ", "").strip()
    client = Groq(api_key=api_key)
except Exception as e:
    st.error("Check your Secrets configuration!")
    st.stop()

st.title("✍️ Humanly AI Pro")
st.write("Convert AI text to human writing instantly.")

# خانة إدخال النص
user_input = st.text_area("Paste your AI content here:", height=200)

if st.button("Humanize Now ✨"):
    if user_input:
        with st.spinner('Transforming your text...'):
            try:
                # استبدال الموديل بـ 8b مؤقتاً للتأكد من السرعة والـ Quota
                completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a professional human editor. Rewrite the text to be natural and pass AI detection."},
                        {"role": "user", "content": user_input}
                    ],
                    model="llama3-8b-8192", 
                )
                
                result = completion.choices[0].message.content
                st.subheader("✅ Humanized Result:")
                st.info(result)
                
            except Exception as e:
                st.error(f"API Error: {str(e)}")
    else:
        st.warning("Please paste some text first!")

# SEO Section
st.markdown("""
<div class="seo-card">
    <h3 style="color: #000 !important;">Why use Humanly AI?</h3>
    <p style="color: #333 !important;">Our tool helps you bypass AI detectors like GPTZero by injecting natural human variance into your writing.</p>
</div>
""", unsafe_allow_html=True)
