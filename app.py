import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Cargar la clave de API desde el archivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

# Configurar la página de Streamlit con un diseño más atractivo
st.set_page_config(page_title="Asistente IA", page_icon="🤖", layout="wide")

# Estilos personalizados
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
        .stChatMessageUser {
            background-color: #d1e7dd;
            text-align: right;
        }
        .stChatMessageAssistant {
            background-color: #f8d7da;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🤖 Asistente IA con OpenAI")
# Inicializar el historial de la conversación en la sesión
if "thread_id" not in st.session_state:
    thread = openai.beta.threads.create()
    st.session_state.thread_id = thread.id

# Entrada de usuario
tab1, tab2 = st.tabs(["Chat", "Acerca de"])

with tab1:
    if prompt := st.chat_input("Escribe tu pregunta..."):
        with st.chat_message("user", avatar="👤"):
            st.markdown(f"**Tú:** {prompt}")
    
        # Enviar mensaje al asistente
        openai.beta.threads.messages.create(
            thread_id=st.session_state.thread_id,
            role="user",
            content=prompt
        )
    
        with st.spinner("Pensando..."):
            run = openai.beta.threads.runs.create(
                thread_id=st.session_state.thread_id,
                assistant_id=ASSISTANT_ID
            )
            
            # Esperar la respuesta del asistente
            while run.status not in ["completed", "failed"]:
                run = openai.beta.threads.runs.retrieve(
                    thread_id=st.session_state.thread_id,
                    run_id=run.id
                )
            
        if run.status == "completed":
            messages = openai.beta.threads.messages.list(thread_id=st.session_state.thread_id)
            for msg in messages.data[::-1]:
                if msg.role == "assistant":
                    reply = msg.content[0].text.value
                    break
            
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(f"**Asistente:** {reply}")

with tab2:
    st.subheader("Acerca del Asistente")
    st.write(
        "Este chatbot ha sido desarrollado con Streamlit y la API de OpenAI para ofrecer respuestas en lenguaje natural."
    )