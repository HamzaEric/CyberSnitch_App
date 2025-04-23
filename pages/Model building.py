import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
def main():
    st.title('Model Building Using Supervised Machine Learning And Deep Learning Algorithms')
    st.markdown('---')
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('TensorFlow.jpeg', width=500)
        st.image('sklearn.jpeg', width=600)
    with col2:

        st.markdown(
            "<h3 style='font-size: 50px;margin-top:15px;margin-top;15px;' >1.Deep Learning:Autoencoder Neural Network</h3 >",
            unsafe_allow_html=True)
        st.markdown(
            "<h3 style='font-size: 50px;margin-top:15px;margin-top;15px;' >NB:Keras Library was also used in ANN</h3 >",
            unsafe_allow_html=True)
        st.markdown('---')
        st.markdown('---')
        st.markdown(
            "<h3 style='font-size: 50px;margin-top:15px;margin-top;10px;' >1.Deep Learning:Multilayer Perceptron(MLP)</h3 >",
            unsafe_allow_html=True)
        st.markdown(
            "<h3 style='font-size: 50px;margin-top:15px;margin-top;10px;' >2.XGBoost Classifier</h3 >",
            unsafe_allow_html=True)
        st.markdown(
            "<h3 style='font-size: 50px;margin-top:15px;margin-top;10px;' >3.Random Forest Classifier</h3 >",
            unsafe_allow_html=True)
        st.markdown(
            "<h3 style='font-size: 50px;margin-top:15px;margin-top;10px;' >4.Decision Tree Classifier</h3 >",
            unsafe_allow_html=True)
        st.markdown(
            "<h3 style='font-size: 50px;margin-top:15px;margin-top;10px;'>5.Support Vector Machines(SVM)</h3 >",
            unsafe_allow_html=True)
    st.markdown('---')
    st.write('''
    MLP and XGBoost emerged as the top-performing models in our phishing website detection Model Building, delivering the highest accuracy and overall performance
    compared to other algorithms evaluated.
    ''')
    st.markdown('---')

    html_file = Path('Model_Building_in_Phising_Website_Detection.html')
    components.html(html_file.read_text(encoding='utf-8', errors='replace'), height=1000, scrolling=True)
if __name__ == '__main__':
    st.set_page_config(
        layout="wide",
    )
    main()
