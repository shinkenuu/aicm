import streamlit as st

from challenges import roundrobin_challenges
from constants import (
    AI_EMOTICON,
    HUMAN_EMOTICON,
    AI,
    HUMAN,
    CHALLENGE,
    USER_CHOICE,
    ARE_CHOICES_DISABLED,
)
from callbacks import reset_challenge, set_user_choice


st.set_page_config(
    "AICM Turing Test",
    page_icon=":question:",
    layout="wide",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": "AICM Turing Test game for Data Expo 2024",
    },
)


if "challenges" not in st.session_state:
    st.session_state["challenges"] = roundrobin_challenges()
    st.session_state[CHALLENGE] = next(st.session_state["challenges"])
    st.session_state[ARE_CHOICES_DISABLED] = False


# st.write(st.session_state)

# ==================================== HEADER

st.markdown(
    f"### Who wrote this thematic description for *{st.session_state[CHALLENGE]['format']}* ?"
)

st.markdown(f"## {st.session_state[CHALLENGE]['description']}")
st.markdown("---")


# ==================================== BODY
_, mid_column, _ = st.columns(3)

with mid_column:
    st.button(
        HUMAN_EMOTICON,
        on_click=lambda: set_user_choice(HUMAN),
        disabled=st.session_state[ARE_CHOICES_DISABLED],
    )

    st.button(
        AI_EMOTICON,
        on_click=lambda: set_user_choice(AI),
        disabled=st.session_state[ARE_CHOICES_DISABLED],
    )


st.markdown("---")
# st.write(st.session_state)


if st.session_state.get(USER_CHOICE):
    if st.session_state[USER_CHOICE] == st.session_state[CHALLENGE]["written_by"]:
        st.toast("You are correct!")
        st.balloons()
    else:
        st.toast("Oops, try again with the next one")

    _, _, footer_column, _, _ = st.columns(5)

    with footer_column:
        st.button(
            "Next description",
            type="primary",
            on_click=reset_challenge,
        )
