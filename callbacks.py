import streamlit as st

from constants import CHALLENGE, USER_CHOICE, ARE_CHOICES_DISABLED


def set_user_choice(user_choice: str):
    st.session_state[USER_CHOICE] = user_choice
    st.session_state[ARE_CHOICES_DISABLED] = True


def reset_challenge():
    st.session_state[USER_CHOICE] = ""
    st.session_state[CHALLENGE] = next(st.session_state["challenges"])
    st.session_state[ARE_CHOICES_DISABLED] = False
