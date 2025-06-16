
import streamlit as st
from data.live_roster import get_all_teams

st.title("✅ MLB Team Selector (Bundled API)")
teams = get_all_teams()
st.selectbox("Choose Team", teams)
