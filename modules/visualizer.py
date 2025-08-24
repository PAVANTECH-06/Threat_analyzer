import matplotlib.pyplot as plt
import streamlit as st

def plot_failed_logins(df):
    if df.empty:
        st.info("No failed logins detected.")
        return
    
    counts = df['ip'].value_counts()
    plt.figure(figsize=(6,4))
    counts.plot(kind="bar", color="red")
    plt.xlabel("IP Address")
    plt.ylabel("Failed Attempts")
    plt.title("Failed Login Attempts by IP")
    st.pyplot(plt.gcf())
