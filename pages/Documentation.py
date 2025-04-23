import streamlit as st
def main():
    st.title('🛠️📖 Documentation')
    st.markdown('---')
    st.subheader('The Purpose Of The Project')
    st.markdown('---')
    st.write('''
    The primary goal of this project is to detect phishing websites using supervised machine learning algorithms and deep learning algorithms. 
    Phishing is a major cyber threat that tricks users into revealing sensitive information through deceptive websites. 
    By automating the detection process with machine learning, this project aims to:
    
    1.Reduce the risk of phishing attacks
    
    2.Assist security systems in flagging malicious websites
    
    3.Provide a learning tool for understanding phishing detection techniques
    
    4.Explore and compare the performance of different ML models hence collaboration between the two field of computing(cybersecurity and data science)
    
    ''')
    st.markdown('---')
    st.subheader('''📊 Dataset ''')
    st.write('''
     
    Source: UC Irvine Machine Learning Repository
    
    Total samples: 5000 Legitimate domains and 5000 Phising domains
    
    Features:(e.g., Have_IP,Have_At,DNS Record, domain age,Mouse_over,Right_Click,URL_Length,URL_Depth, redirection)
    
    Each sample is labeled as:
    
    1 → Phishing
    
    0 → Legitimate
    
    
    
    ''')
    st.markdown('---')
    st.subheader('🏗️Tech Stack')
    st.markdown('---')
    st.write('''
    
    1.Language: Python
    
    2.ML Libraries: Scikit-learn,TensorFlow/Keras
    
    Data Handling: Pandas, NumPy
    
    Visualization: Matplotlib, Seaborn
    
    Notebook: Jupyter
    ''')


    st.subheader("Code for the Chatbot Streamlit Page:")

    st.code("""
    import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

def main():
    st.set_page_config(layout="wide")
    st.title("AI Assistant")
    st.markdown('---')

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('uploadlogo.png', width=400)
    with col2:
        st.markdown(
            "<h1 style='font-size: 70px;margin-top:15px;' >Your AI-powered assistant designed to answer your questions about online security</h1 >",
            unsafe_allow_html=True)
        st.markdown('---')

    # Load environment variables
    load_dotenv("")
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    # Configure Gemini
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')


    system_instruction = (
        "You are strictly a systems and security assistant chatbot. Your name is PhishGuard. "
        "If asked something which is not within your scope, answer with "
        "'I am just a systems and security assistant so I cannot help you with that.' "
        "You answer questions and give advice on how to secure systems and avoid exploitation. "
        "Keep your responses brief and limit them to 150 tokens. "
        "Answer respectfully when someone uses abusive language."
    )

    # Function to display roles correctly
    def translate_role(role):
        return "assistant" if role == "model" else role

    # Start session and inject system instruction
    if "chat_session" not in st.session_state:
        chat = model.start_chat(history=[])
        # Send system instruction as hidden first message
        _ = chat.send_message(system_instruction)
        st.session_state.chat_session = chat

    # Show conversation history 
    for message in st.session_state.chat_session.history[1:]:
        with st.chat_message(translate_role(message.role)):
            st.markdown(message.parts[0].text)

    # Get user input
    user_prompt = st.chat_input("🎣 Ask PhishGuard")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        response = st.session_state.chat_session.send_message(
            user_prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=200,
                temperature=0.3
            )
        )
        with st.chat_message("assistant"):
            st.markdown(response.text)
if __name__ == '__main__':
     main()
        
    
    
    
    
    """)
    st.markdown('---')
    st.subheader('✅ Conclusion')
    st.markdown('---')
    st.write('''
    
    This project demonstrates that machine learning is highly effective for phishing detection. It provides strong accuracy and interpretability, and can be further extended into:
    
    Future improvements/works:
    
    1.Real-time browser plugins
    
    2.Drift Detection:Track if model performance drops due to changes in phishing techniques over time.
    
    3.Dynamic feature extraction using live web scraping 
    ''')
    st.markdown('---')
    st.subheader('📚 References')
    st.markdown('---')

    st.markdown("""
    - [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets)
    - [XGBoost Documentation](https://machinelearningmastery.com/save-gradient-boosting-models-xgboost-python/)
    - [Autoencoders Neural Network](https://blog.keras.io/building-autoencoders-in-keras.html)
    - [Deep Learning](https://github.com/shreyagopal/t81_558_deep_learning/blob/master/t81_558_class_14_03_anomaly.ipynb)
    - [Multilayer Perceptron](https://www.datacamp.com/tutorial/multilayer-perceptrons-in-machine-learning)
    - [PhishTank](https://www.phishtank.com/)
""")
    st.markdown('---')

    st.subheader('👨‍💻 Developer Information')
    st.markdown('---')
    st.code('''
    st.write('Name:Eric Hamza Maina')
    ''')
    st.write('Access Me')
    st.markdown('''
    [instagram](https://www.instagram.com/hamza.aaah_k1/)
    
    [Github](https://github.com/HamzaEric)
    
    ''')
if __name__ == '__main__':
    st.set_page_config(
        layout="wide",
    )
    main()