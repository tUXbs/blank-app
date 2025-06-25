import streamlit as st

st.set_page_config(page_title="JOMO - Joy Of Missing Out", layout="centered")

st.markdown("""
    <style>
    .event-button {
        border: 1px solid #4A5568;
        border-radius: 0.5rem;
        padding: 0.75rem 1.5rem;
        text-align: center;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .event-button.selected {
        background-color: #4A5568;
        color: white;
    }
    .event-button:hover {
        background-color: #E2E8F0;
    }
    .event-button.selected:hover {
        background-color: #2D3748;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background-color: #FFF7ED; padding: 2rem; border-radius: 1rem; margin-bottom: 3rem;'>
    <h1 style='text-align: center; font-size: 4rem; color: #1E3A8A;'>JOMO</h1>
    <p style='text-align: center; font-size: 1.5rem; font-weight: 600; color: #374151;'>Joy Of Missing Out</p>
    <p style='text-align: center; font-size: 1.25rem; color: #4B5563;'>Kies de evenementen waar je <u><b>niet</b></u> naar toe gaat!</p>
</div>
""", unsafe_allow_html=True)

st.write("\n")

events = [
    {"id": "DTRH", "name": "Down The Rabbit Hole"},
    {"id": "lowlands", "name": "Lowlands"},
    {"id": "pinkpop", "name": "Pinkpop"},
    {"id": "draaimolen", "name": "Draaimolen"},
    {"id": "le-guess-who", "name": "Le Guess Who?"},
    {"id": "mysteryland", "name": "Mysteryland"},
    {"id": "defqon", "name": "Defqon.1"},
    {"id": "into-the-great-wide-open", "name": "Into The Great Wide Open"},
]

if 'selected' not in st.session_state:
    st.session_state.selected = []

# UI buttons in 2 kolommen
cols = st.columns(2)
for index, event in enumerate(events):
    col = cols[index % 2]
    selected = event["id"] in st.session_state.selected
    btn_label = f"✅ {event['name']}" if selected else event['name']
    if col.button(btn_label, key=event["id"]):
        if selected:
            st.session_state.selected.remove(event["id"])
        else:
            st.session_state.selected.append(event["id"])

# Calculate totals
selected_count = len(st.session_state.selected)
total_savings = selected_count * 175
total_energy = selected_count * 20

st.markdown("---")
st.subheader("Besparingen")
st.markdown(f"""
<div style='border: 1px solid #CBD5E0; border-radius: 0.375rem; padding: 0.5rem 1rem; display: inline-block; font-size: 1.5rem;'>
    € {total_savings},-
</div>
""", unsafe_allow_html=True)

st.subheader("Levensenergie")
progress_value = min(1.0, total_energy / 100)
st.progress(progress_value)

# Beleggingsknop
if st.button("Zet mijn besparing aan het werk 💸"):
    st.success("Mooi! Je besparing is virtueel belegd.")

