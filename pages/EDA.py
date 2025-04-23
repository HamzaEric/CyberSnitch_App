import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path


def main():
    st.title('Exploratory Data Analysis(EDA)')
    st.markdown('---')
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('pandas.jpeg', width=500)
        st.image('datavisual.jpeg', width=500)
    with col2:
        st.markdown(
            "<h2 style='font-size: 70px;margin-top:15px;margin-top;15px;' >Data Analysis:Pandas Library</h2 >",
            unsafe_allow_html=True)
        st.markdown('---')
        st.markdown('---')
        st.markdown(
            "<h2 style='font-size: 70px;margin-top:15px;margin-top;15px;' >Data Visualization</h2 >",
            unsafe_allow_html=True)
        st.markdown(
            "<h2 style='font-size: 40px;margin-top:15px;margin-top;15px;' >1.Matplotlib</h2 >",
            unsafe_allow_html=True)
        st.markdown(
            "<h2 style='font-size: 40px;margin-top:15px;margin-top;15px;' >2.Seaborn</h2 >",
            unsafe_allow_html=True)
    st.markdown('---')
    st.write('''
    Welcome to the EDA section
    We dive into the dataset to uncover patterns, spot anomalies, and understand the key features that distinguish phishing websites from legitimate ones.
    Visualizations and descriptive statistics are used to guide our feature selection and modeling strategy, ensuring our
    machine learning models are built on solid insights.
    ''')
    st.markdown('---')

    html_file=Path(r'Phishing_website_Detection_EDA.html')
    components.html(html_file.read_text(), height=1000, scrolling=True)

if __name__ == '__main__':
    st.set_page_config(
        layout="wide",
    )
    main()
