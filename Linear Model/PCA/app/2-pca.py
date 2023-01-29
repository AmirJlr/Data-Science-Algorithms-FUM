import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

from mpl_toolkits import mplot3d

st.title('Principal Component Analysis')

# prepare data
digits = load_digits()

st.header('Data :')
data_digit = pd.DataFrame(digits.data, columns = digits.feature_names)
st.dataframe(data_digit)

X, y =digits.data, digits.target


# n component PCA

d= X.shape[1]

n = st.slider('Select n for Component :', min_value=1, max_value=d)



columns=[]
for i in range(1, n+1):
    columns.append(f"PC {i}")

pca_n = PCA(n_components=n)
n_proj = pca_n.fit_transform(X)
n_df = pd.DataFrame(n_proj, columns=columns)


# 2-d plotting
if n == 2:
    fig=plt.figure(figsize=(8,6))
    plt.style.use('seaborn')
    plt.scatter(n_df['PC 1'], n_df['PC 2'], c=y, cmap = plt.cm.get_cmap('nipy_spectral',10))
    plt.colorbar()
    st.pyplot(fig)




if n==3 :
    plt.style.use('seaborn')
    fig=plt.figure(figsize=(8,6))
    ax = plt.axes(projection = '3d')
    plt.title('3D Scatter')
    sctt = ax.scatter3D(n_df['PC 1'], n_df['PC 2'],n_df['PC 3'], c=y, cmap = plt.cm.get_cmap('nipy_spectral',10))
    # plt.colorbar()
    st.pyplot(fig)
    

st.header('Principal Component :')
st.dataframe(n_df)

