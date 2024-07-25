import streamlit as st

@st.experimental_dialog("Cast your votes")
def vote(item):
  st.write(f"Why is {item} your favorite?")
  reason = st.text_input("Your reason")
  if st.button("Submit"):
    st.session_state.vote = {"item": item, "reason": reason}
    st.rerun()

if "vote" not in st.session_state:
  st.write("Vote for your favorite")
  if st.button("Cricket"):
      vote("Cricket")
  if st.button("Football"):
      vote("Football")
else:
  f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"