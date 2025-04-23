import streamlit as st

def main():
    st.set_page_config(layout="wide")
    st.title('Awareness Community')
    st.markdown('---')
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('community.jpeg', width=350)
    with col2:
        st.markdown(
                "<h1 style='font-size: 70px;margin-top:15px;margin-top;15px;' >CyberSnitch</h1 >",
                unsafe_allow_html=True)
        st.markdown(
                "<h1 style='font-size: 70px;margin-top:15px;margin-top;15px;' >Community</h1 >",
                unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("This is a community where you interact with Ethical Hackers to improve on your security systems and get updates on new Cyberattack techniques.")

    st.markdown("---")

    option = st.selectbox("Choose a section:",
                          ["Join As either a Hacker or a Member...", "Ethical Hacker's Log", "Members Log (Users)", "Cybersecurity Updates"])

    if option == "Ethical Hacker's Log":
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('ethicalhackerlog.jpeg', width=400)
        with col2:
            st.markdown(
                "<h1 style='font-size: 70px;margin-top:15px;margin-top;15px;' >Ethical</h1 >",
                unsafe_allow_html=True)
            st.markdown(
                "<h1 style='font-size: 70px;margin-top:15px;margin-top;15px;' >Hacker's</h1 >",
                unsafe_allow_html=True)
            st.markdown(
                "<h1 style='font-size: 70px;margin-top:15px;margin-top;15px;' >Page</h1 >",
                unsafe_allow_html=True)
        st.write("### Why register as an Ethical Hacker in Cybersnitch Community?")
        st.write("- Gain access to advanced cybersecurity tools")
        st.write("- Collaborate with other ethical hackers")
        st.write("- Receive recognition for your contributions")
        st.write("- Get job from Clients for Vulnerability analysis")
        st.write("- Sharpen Your skills by taking challenges posted in the ")

        st.write("#### Register or Login:")
        if st.button("Register"):
            st.success("Redirecting to registration page...")
            st.write("### Welcome to CyberSnitch Hackers World ")
        if st.button("Login"):
            st.success("Redirecting to login page...")
            st.write("### Hey Hacker Lets Pick it up from where you left it")

    elif option == "Members Log (Users)":
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('member.jpeg', width=400)
        with col2:
            st.markdown(
                "<h1 style='font-size: 70px;margin-top:15px;margin-top;15px;' >Members</h1 >",
                unsafe_allow_html=True)
            st.markdown(
                "<h1 style='font-size: 70px;margin-top:15px;margin-top;15px;' >Page</h1 >",
                unsafe_allow_html=True)
        st.write(" ### Why you should become a member of Cybersnitch Community?")

        st.write('''
                1.Learn cybersecurity skills first hand

                2.Connect with like-minded people

                3.Get career opportunities and mentorship from ethical hackers

                4.Be part of a trusted ethical hacking network
        ''')
        st.write("### Register or Login:")
        if st.button("Register"):
            st.success("Redirecting to workshop registration page...")
            st.write("### Welcome and start connecting with skilled Ethical Hackers!")
        if st.button("Login"):
            st.success("Redirecting to workshop login page...")
            st.write("### Welcome Back!")

    elif option == "Cybersecurity Updates":
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('updates.jpeg', width=500)
        with col2:
                st.markdown(
                    "<h1 style='font-size: 70px;margin-top:15px;margin-top;15px;' >CyberSecurity</h1 >",
                    unsafe_allow_html=True)
                st.markdown(
                    "<h1 style='font-size: 70px;margin-top:15px;margin-top;15px;' >Updates</h1 >",
                    unsafe_allow_html=True)
        st.write("### Stay informed with the latest security trends to stay safe online")
        st.markdown('---')
        st.write("This section contains new phishing techniques and updates posted by Ethical Hackers.")
        st.info("""
        Example Update:

                1.⚠️Watch out for spear-phishing emails using fake security alerts!

            2.⚠️ New phishing scam targeting PayPal users

            3.🛡️ Critical Windows vulnerability discovered (patch available)

            4.📱 Android malware disguised as a battery saver app

            5.🌐 DNS hijacking attack on a major hosting provider

            6.🧑💻 GitHub repositories leaking API tokens

            7.🕵️ Rise in Ransomware-as-a-Service platforms

            8.🔍 Deepfake audio used in CEO impersonation scams
        """)
if __name__ == '__main__':
    main()
