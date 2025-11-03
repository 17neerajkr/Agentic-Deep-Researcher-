import os
import subprocess
import time
import streamlit as st
import ollama

# ===============================# 🔧 GPU Configuration# ===============================os.environ["OLLAMA_NUM_GPU"] = "1"os.environ["OLLAMA_USE_CUDA"] = "1"# ===============================# ⚙️ Streamlit Configuration# ===============================st.set_page_config(page_title="🔍 Agentic Deep Researcher", layout="wide")

# ===============================# 🧠 Helper Functions# ===============================def start_ollama_service():
    """Start Ollama if it isn't already running."""    try:
        # Check if Ollama is already active        result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        if result.returncode == 0:
            return True    except Exception:
        pass    st.warning("🧩 Ollama is not running. Starting it automatically...")
    try:
        # Start Ollama as a background process        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)  # Wait for Ollama to initialize        return True    except Exception as e:
        st.error(f"❌ Failed to start Ollama service automatically: {e}")
        return Falsedef check_deepseek_model():
    """Verify if DeepSeek model exists locally."""    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        return "deepseek-r1" in result.stdout
    except Exception:
        return False# ===============================# 💬 Chat State Management# ===============================if "messages" not in st.session_state:
    st.session_state.messages = []

def reset_chat():
    st.session_state.messages = []

# ===============================# ⚙️ Startup Check# ===============================ollama_ready = start_ollama_service()
deepseek_ready = check_deepseek_model()

# ===============================# 🧩 Sidebar Configuration# ===============================with st.sidebar:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://avatars.githubusercontent.com/u/175112039?s=200&v=4", width=65)
    with col2:
        st.header("DeepSeek Configuration")
        st.write("💻 Local GPU Mode")

    st.markdown("---")

    if not ollama_ready:
        st.error("❌ Ollama is not running. Try restarting manually:\n```bash\nollama serve\n```")
    elif not deepseek_ready:
        st.warning("⚠️ DeepSeek model not found.\nDownload it using:\n```bash\nollama pull deepseek-r1:latest\n```")
    else:
        st.success("✅ Ollama and DeepSeek model are active!")

    st.info("GPU acceleration enabled (CUDA) 🚀")
    st.button("Clear ↺", on_click=reset_chat)

# ===============================# 🧠 Header# ===============================col1, col2 = st.columns([6, 1])
with col1:
    st.markdown("<h2 style='color: #0066cc;'>🔍 Agentic Deep Researcher</h2>", unsafe_allow_html=True)
    st.markdown("""        <div style='display: flex; align-items: center; gap: 10px; margin-top: 5px;'>            <span style='font-size: 20px; color: #666;'>Powered by</span>            <img src="https://cdn.prod.website-files.com/66cf2bfc3ed15b02da0ca770/66d07240057721394308addd_Logo%20(1).svg" width="80">            <span style='font-size: 20px; color: #666;'>and</span>            <img src="https://framerusercontent.com/images/wLLGrlJoyqYr9WvgZwzlw91A8U.png?scale-down-to=512" width="100">        </div>    """, unsafe_allow_html=True)

# ===============================# 💬 Chat Display# ===============================st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ===============================# 💬 User Input# ===============================prompt = st.chat_input("Ask your research question...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if not ollama_ready or not deepseek_ready:
        reply = "⚠️ DeepSeek is not ready. Please make sure Ollama is running and the DeepSeek model is downloaded."    else:
        with st.spinner("🧠 DeepSeek is analyzing your query..."):
            try:
                response = ollama.chat(
                    model="deepseek-r1:latest",
                    messages=[
                        {"role": "system", "content": "You are a powerful research assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                reply = response["message"]["content"]
            except Exception as e:
                reply = f"⚠️ Could not reach DeepSeek model:\n\n`{e}`"    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})


