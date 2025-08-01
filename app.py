
import streamlit as st
from ego_vault import load_memories, add_memory_file, talk_to_twin
from reality_flow import simulate_timeline

st.set_page_config(page_title="Project NOVA", layout="centered")

st.title("🧠 Project NOVA — Your AI Twin + Timeline Forecaster")

st.sidebar.header("Upload Your Thoughts")
uploaded_file = st.sidebar.file_uploader("Upload .txt memory", type=["txt"])
if uploaded_file:
    st.sidebar.success("Memory uploaded")
    add_memory_file(uploaded_file)

st.sidebar.markdown("---")
if st.sidebar.button("Load Memories"):
    memories = load_memories()
    st.sidebar.success(f"{len(memories)} memory files loaded.")

st.header("Talk to Your AI Twin")
user_input = st.text_input("Say something to your twin:")
if user_input:
    response = talk_to_twin(user_input)
    st.markdown(f"**Twin:** {response}")

st.header("🕰️ Timeline Simulator")
scenario = st.text_area("Describe a hypothetical scenario:")
if st.button("Simulate Future"):
    forecast = simulate_timeline(scenario)
    st.success(forecast)
