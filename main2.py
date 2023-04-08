# Library
import streamlit as st

# write
st.title ('SOFTWARE PERKALIAN')
st.subheader('Ini adalah aplikasi untuk mengalikan bilangan bulat')

# input bilangan pertama
number1= st.number_input('Masukkan bilangan pertama ', format='%.4f')
st.write(f'Bilangan pertama adalah {number1}')

# input bilangan kedua
number2= st.number_input('Masukkan bilangan kedua', format='%.4f')
st.write(f'Bilangan pertama adalah {number2}')

#hasil kali
hasil=number1*number2

if st.button('Hitung'):
    st.write(f'hasil kali antara {number1} dan {number2} adalah {hasil} good chooise :cry:')
else:
    st.write('silahkan pencet tombol hitung!')
    
import numpy as np
array1 = np.random.randint(10,40, size=(10,))
array2 = np.random.randint(10,40, size=(10,))

import pandas as pd
st.dataframe(pd.DataFrame({'Kelas A' : array1,
                           'Kelas B' : array2
                          })
            )
    
import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
    
import streamlit as st

st.balloons()
    
    