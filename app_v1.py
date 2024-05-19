import streamlit as st
import random


moznosti = ["kámen", "nůžky", "papír"] # k - kámen, n - nůžky, p-papír
volba_pocitace = random.choice(moznosti)

volba_hrace = st.selectbox("Vyber kámen, nůžky nebo papír", options=moznosti, key="volba hrace")
#    volba_hrace = st.columns("Kámen", key="kamen") #("Nůžky", key="nůžky"), ("Papír", key="papír")
hrat = st.button("Hrát", key="hrat")
if hrat:

    if volba_hrace == volba_pocitace:
        st.warning(f"Počítač zvolil {volba_pocitace}, Vy {volba_hrace} a výsledkem je remíza")
    elif (volba_pocitace == "kámen" and volba_hrace == "nůžky") or (volba_pocitace == "papír" and volba_hrace == "kámen") or (volba_pocitace == "nůžky" and volba_hrace == "papír"):
        st.error (f"Počítač zvolil {volba_pocitace}, Vy {volba_hrace} a výsledkem je prohra!")
    else:
        st.success(f"Počítač zvolil {volba_pocitace}, Vy {volba_hrace} a výsledkem je výhra!")
