import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Cargar la clave de API desde el archivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

# Configurar la página de Streamlit
st.set_page_config(page_title="Asistente IA", page_icon="🤖")


st.title("🤖 Asistente IA con OpenAI")

# Inicializar el historial de la conversación en la sesión
if "thread_id" not in st.session_state:
    thread = openai.beta.threads.create()
    st.session_state.thread_id = thread.id

# Entrada de usuario
if prompt := st.chat_input("Escribe tu pregunta..."):
    with st.chat_message("user"):
        st.write(prompt)
    
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
        
        with st.chat_message("assistant"):
            st.write(reply)