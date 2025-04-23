# import streamlit as st
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai
# from google.api_core import retry
# from google.api_core import exceptions as google_exceptions
# import time
#
#
# def main():
#     # Initialize app with wide layout
#     st.set_page_config(layout="wide")
#     st.title("AI Assistant")
#     st.markdown('---')
#
#     # Header section with logo and title
#     col1, col2 = st.columns([1, 2])
#     with col1:
#         st.image('uploadlogo.png', width=400)
#     with col2:
#         st.markdown(
#             "<h1 style='font-size: 70px;margin-top:15px;' >Your AI-powered assistant designed to answer your questions about online security</h1 >",
#             unsafe_allow_html=True)
#         st.markdown('---')
#
#
#     # Load environment variables with error handling
#     try:
#         load_dotenv(".Failed to load environment variables: 'st.secrets has no key "GEMINI_API_KEY". Did you forget to add it to secrets.toml, mount it to secret directory, or the app settings on Streamlit Cloud? More info: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management'")
#         gemini_api_key = os.getenv("GEMINI_API_KEY")
#         api_key=st.secrets["GEMINI_API_KEY"]
#         if not gemini_api_key:
#             st.error("GEMINI_API_KEY not found in environment variables")
#             st.stop()
#     except Exception as e:
#         st.error(f"Failed to load environment variables: {str(e)}")
#         st.stop()
#
#     # Configure Gemini with error handling
#     try:
#         with st.spinner("Connecting to PhishGuard AI..."):
#             genai.configure(api_key=gemini_api_key)
#             model = genai.GenerativeModel(
#                 'gemini-1.5-flash',
#                 generation_config=genai.types.GenerationConfig(
#                     max_output_tokens=200,
#                     temperature=0.3
#                 )
#             )
#     except Exception as e:
#         st.error(f"Failed to configure Gemini: {str(e)}")
#         st.stop()
#
#     system_instruction = (
#         "You are strictly a systems and security assistant chatbot. Your name is PhishGuard. "
#         "If asked something which is not within your scope, answer with "
#         "'I am just a systems and security assistant so I cannot help you with that.' "
#         "You answer questions and give advice on how to secure systems and avoid exploitation. "
#         "Keep your responses brief and limit them to 150 tokens. "
#         "Answer respectfully when someone uses abusive language."
#     )
#
#     # Custom retry configuration
#     custom_retry = retry.Retry(
#         initial=1.0,
#         maximum=10.0,
#         multiplier=2.0,
#         deadline=60.0,
#         predicate=retry.if_exception_type(
#             google_exceptions.DeadlineExceeded,
#             google_exceptions.ServiceUnavailable
#         )
#     )
#
#     # Function to display roles correctly
#     def translate_role(role):
#         return "assistant" if role == "model" else role
#
#     # Initialize chat session with retry logic
#     if "chat_session" not in st.session_state:
#         try:
#             with st.spinner("Initializing PhishGuard security protocols..."):
#                 st.session_state.chat_session = model.start_chat(history=[])
#                 # Properly structured message with content parameter
#                 custom_retry(st.session_state.chat_session.send_message)(
#                     content=system_instruction,
#                     generation_config=genai.types.GenerationConfig(
#                         max_output_tokens=200,
#                         temperature=0.3
#                     )
#                 )
#
#         except Exception as e:
#             st.error(f"Failed to initialize chat session: {str(e)}")
#             st.stop()
#
#     # Show conversation history (skip the first system message)
#     if "chat_session" in st.session_state:
#         for message in st.session_state.chat_session.history[1:]:
#             with st.chat_message(translate_role(message.role)):
#                 st.markdown(message.parts[0].text)
#
#     # Get user input
#     user_prompt = st.chat_input("🎣 Ask PhishGuard")
#     if user_prompt:
#         st.chat_message("user").markdown(user_prompt)
#
#         try:
#             with st.spinner("PhishGuard is analyzing your query..."):
#                 # Use the chat session from session_state
#                 response = custom_retry(st.session_state.chat_session.send_message)(
#                     content=user_prompt,
#                     generation_config=genai.types.GenerationConfig(
#                         max_output_tokens=200,
#                         temperature=0.3
#                     ),
#                     stream=False
#                 )
#
#             with st.chat_message("assistant"):
#                 st.markdown(response.text)
#
#         except google_exceptions.DeadlineExceeded:
#             with st.spinner(""):
#                 time.sleep(0.5)
#                 st.error("Our systems are experiencing high load. Please try again in a moment.")
#         except Exception as e:
#             with st.spinner(""):
#                 time.sleep(0.5)
#                 st.error(f"Security systems overloaded: {str(e)}")
#
#     # Status indicator
#     with st.sidebar:
#         st.caption("PhishGuard Status")
#         if "chat_session" in st.session_state:
#             st.success("✅ Operational")
#         else:
#             st.warning("⚠️ Initializing...")
#
#
# if __name__ == '__main__':
#     main()
import streamlit as st
import google.generativeai as genai
from google.api_core import retry
from google.api_core import exceptions as google_exceptions
import time


def main():
    # Initialize app with wide layout
    st.set_page_config(layout="wide")
    st.title("AI Assistant")
    st.markdown('---')

    # Header section with logo and title
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('uploadlogo.png', width=400)
    with col2:
        st.markdown(
            "<h1 style='font-size: 70px;margin-top:15px;' >Your AI-powered assistant designed to answer your questions about online security</h1 >",
            unsafe_allow_html=True)
        st.markdown('---')

    # Load Gemini API key from Streamlit secrets
    try:
        gemini_api_key = st.secrets["api"]["GEMINI_API_KEY"]
    except KeyError:
        st.error("GEMINI_API_KEY not found in Streamlit secrets. Please check your secrets.toml or Streamlit Cloud settings.")
        st.stop()

    # Configure Gemini with error handling
    try:
        with st.spinner("Connecting to PhishGuard AI..."):
            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel(
                'gemini-1.5-flash',
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=200,
                    temperature=0.3
                )
            )
    except Exception as e:
        st.error(f"Failed to configure Gemini: {str(e)}")
        st.stop()

    system_instruction = (
        "You are strictly a systems and security assistant chatbot. Your name is PhishGuard. "
        "If asked something which is not within your scope, answer with "
        "'I am just a systems and security assistant so I cannot help you with that.' "
        "You answer questions and give advice on how to secure systems and avoid exploitation. "
        "Keep your responses brief and limit them to 150 tokens. "
        "Answer respectfully when someone uses abusive language."
    )

    # Custom retry configuration
    custom_retry = retry.Retry(
        initial=1.0,
        maximum=10.0,
        multiplier=2.0,
        deadline=60.0,
        predicate=retry.if_exception_type(
            google_exceptions.DeadlineExceeded,
            google_exceptions.ServiceUnavailable
        )
    )

    # Function to display roles correctly
    def translate_role(role):
        return "assistant" if role == "model" else role

    # Initialize chat session with retry logic
    if "chat_session" not in st.session_state:
        try:
            with st.spinner("Initializing PhishGuard security protocols..."):
                st.session_state.chat_session = model.start_chat(history=[])
                custom_retry(st.session_state.chat_session.send_message)(
                    content=system_instruction,
                    generation_config=genai.types.GenerationConfig(
                        max_output_tokens=200,
                        temperature=0.3
                    )
                )
        except Exception as e:
            st.error(f"Failed to initialize chat session: {str(e)}")
            st.stop()

    # Show conversation history
    if "chat_session" in st.session_state:
        for message in st.session_state.chat_session.history[1:]:
            with st.chat_message(translate_role(message.role)):
                st.markdown(message.parts[0].text)

    # Get user input
    user_prompt = st.chat_input("🎣 Ask PhishGuard")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        try:
            with st.spinner("PhishGuard is analyzing your query..."):
                response = custom_retry(st.session_state.chat_session.send_message)(
                    content=user_prompt,
                    generation_config=genai.types.GenerationConfig(
                        max_output_tokens=200,
                        temperature=0.3
                    ),
                    stream=False
                )
            with st.chat_message("assistant"):
                st.markdown(response.text)

        except google_exceptions.DeadlineExceeded:
            with st.spinner(""):
                time.sleep(0.5)
                st.error("Our systems are experiencing high load. Please try again in a moment.")
        except Exception as e:
            with st.spinner(""):
                time.sleep(0.5)
                st.error(f"Security systems overloaded: {str(e)}")

    # Status indicator
    with st.sidebar:
        st.caption("PhishGuard Status")
        if "chat_session" in st.session_state:
            st.success("✅ Operational")
        else:
            st.warning("⚠️ Initializing...")


if __name__ == '__main__':
    main()
