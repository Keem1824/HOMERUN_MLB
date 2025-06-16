
import streamlit as st
from data.live_roster import get_all_teams

teams = get_all_teams()
st.title("✅ MLB StatsAPI Live Test")
st.selectbox("Select an MLB team", teams)
