import joblib
import numpy as np
import streamlit as st

# Load model yang sudah dilatih (pastikan file model_regresi.pkl ada di GitHub)
model = joblib.load('model_regresi.pkl')

st.title('GAS CONSUMPTION GT BLOK 3 PLTGU GRATI')
st.write('Beban Gas Turbine.')

# Input nilai dari user
nilai_x = st.number_input('Masukkan Beban MW (X):', value=0.0)

if st.button('Calculate by Didik'):
  # Lakukan prediksi menggunakan model linear regression
  prediksi = model.predict(np.array([[nilai_x]]))
  st.success(f'GAS CONSUMPTION MMBTUD (Y): {prediksi[0]:.2f}')
