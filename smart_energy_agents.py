import streamlit as st
import requests

# n8n webhook URL
n8n_webhook_url = "https://safeek05.app.n8n.cloud/webhook-test/energy-ai"

st.title("Smart Energy AI Agents")

uploaded_file = st.file_uploader("Upload CSV or JSON file", type=["csv", "json"])
tariff_rate = st.number_input("Enter your tariff rate (₹ per unit)", value=1.2)

if st.button("Run AI Agents 🚀"):
    if uploaded_file:
        files = {'file': (uploaded_file.name, uploaded_file, uploaded_file.type)}
        data = {"tariff_rate": tariff_rate}

        with st.spinner("Running AI Agents..."):
            response = requests.post(n8n_webhook_url, files=files, data=data)

        if response.status_code == 200:
            st.success("AI Analysis Complete")
            st.json(response.json())  # Display AI result from n8n
        else:
            st.error(f"Error: {response.status_code}")
    else:
        st.warning("Please upload a file.")


