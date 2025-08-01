
import os

def load_memories():
    memory_dir = "data/user_texts"
    return [f for f in os.listdir(memory_dir) if f.endswith(".txt")]

def add_memory_file(uploaded_file):
    with open(f"data/user_texts/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())

def talk_to_twin(prompt):
    return f'(Simulated Twin) I read everything you wrote. Regarding: "{prompt}", I feel... optimistic.'
