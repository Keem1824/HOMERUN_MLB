
import streamlit as st
from data.live_roster import get_all_teams

teams = get_all_teams()
st.title("✅ MLB Team Picker (Live Roster Test)")
st.selectbox("Select a team", teams)
