# 🤖 Asistente IA con OpenAI

Este proyecto es un chatbot basado en la API de OpenAI, desarrollado con Streamlit para proporcionar una interfaz interactiva.

## 🚀 Características

- Interfaz simple e intuitiva con Streamlit
- Integración con la API de OpenAI
- Historial de conversación dentro de la sesión

## 📋 Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.8+
- Streamlit
- OpenAI
- Python-dotenv

## 📦 Instalación

1. Clona este repositorio:
    
    ```bash
    git clone <https://github.com/tu-usuario/asistente-ia.git>
    cd asistente-ia
    
    ```
    
2. Crea un entorno virtual y actívalo:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # En macOS/Linux
    venv\\Scripts\\activate  # En Windows
    ```
    
3. Instala las dependencias:
    
    ```bash
    pip install -r requirements.txt
    ```
    

## ⚙️ Configuración

1. Crea un archivo `.env` en la raíz del proyecto y agrega:
    
    ```
    OPENAI_API_KEY=tu_clave_aquí
    ASSISTANT_ID=tu_assistant_id_aquí
    ```
    
2. Asegúrate de que la clave de OpenAI sea válida y que tengas acceso a la API.

## ▶️ Ejecución

Para ejecutar el chatbot, usa el siguiente comando:

```bash
streamlit run app.py
```

Esto abrirá la aplicación en tu navegador, donde podrás interactuar con el asistente IA.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Siéntete libre de modificar y distribuir según tus necesidades.

---

Hecho con ❤️ usando Streamlit y OpenAI.