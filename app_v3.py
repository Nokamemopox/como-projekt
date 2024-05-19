import streamlit as st
import random

st.header("Kámen Nužky Papír teď")
moznosti = ["kámen", "nůžky", "papír"]
volba_pocitace = random.choice(moznosti)

vysledek = None
col_moznost_volby = st.columns(3)
with col_moznost_volby[0]:
    tlacitko_kamen = st.button("kámen", use_container_width=True)
    if tlacitko_kamen:
        volba_hrace = "kámen"
        if volba_pocitace == "kámen":
            vysledek = "remiza"
        if volba_pocitace == "nůžky":
           vysledek = "výhra"
        if volba_pocitace == "papír":
            vysledek = "prohra"
with col_moznost_volby[1]:
    tlacitko_nuzky = st.button("nůžky", use_container_width=True)
    if tlacitko_nuzky:
        volba_hrace = "nůžky"
        if volba_pocitace == "kámen":
            vysledek = "prohra"
        if volba_pocitace == "nůžky":
           vysledek = "remíza"
        if volba_pocitace == "papír":
            vysledek = "výhra"
with col_moznost_volby[2]:
    tlacitko_papir = st.button("papír",use_container_width=True)    
    if tlacitko_papir:
        volba_hrace = "papír"
        if volba_pocitace == "kámen":
            vysledek = "výhra"
        if volba_pocitace == "nůžky":
           vysledek = "prohra"
        if volba_pocitace == "papír":
            vysledek = "remíza"

if vysledek == "remiza":
    st.warning(f"Počítač zvolil {volba_pocitace}, Vy {volba_hrace}. Remíza!")
if vysledek == "výhra":
    st.success(f"Počítač zvolil {volba_pocitace}, Vy {volba_hrace}. Vyhrál jste!")
if vysledek == "prohra":
    st.error(f"Počítač zvolil {volba_pocitace}, Vy {volba_hrace}. Prohrál jste!")
