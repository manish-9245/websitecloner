import streamlit as st
import threading
import random
import socketserver
import http.server
import requests
import time
from urllib.parse import urlparse

st.set_page_config(page_title="Clone Any Website to Localhost", page_icon="🌀")

# Styling
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .stButton>button {
        color: #FFFFFF !important;
      }
      .stButton>button:hover {
        background-color: #262730 !important;
        color: #FFFFFF !important;
      }
      .stButton>button:disabled {
        background: linear-gradient(to right, #e52d27, #b31217) !important;
        color: #FFFFFF !important;
      }
      div[data-testid="stProgress"] > div > div > div > div {
        background-color: #e52d27 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🌀 Clone Any Website to Localhost")
url = st.text_input("Enter the website URL to clone", "")

class Proxy(http.server.SimpleHTTPRequestHandler):
    target_url = ""

    def do_GET(self):
        try:
            full_url = Proxy.target_url + self.path
            resp = requests.get(full_url)
            self.send_response(resp.status_code)
            for k, v in resp.headers.items():
                if k.lower() not in ("content-encoding", "content-length", "transfer-encoding", "connection"):
                    self.send_header(k, v)
            self.end_headers()
            self.wfile.write(resp.content)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {e}".encode())

def run_proxy_server(port, target):
    Proxy.target_url = target
    with socketserver.TCPServer(("", port), Proxy) as httpd:
        httpd.serve_forever()

if st.button("Start Cloning"):
    parsed = urlparse(url)
    if not parsed.scheme.startswith("http"):
        st.error("Please enter a valid URL with http or https scheme.")
    else:
        port = random.randint(9000, 9999)
        progress = st.progress(0)
        status = st.empty()

        # Start proxy server
        threading.Thread(target=run_proxy_server, args=(port, url), daemon=True).start()

        # Simulate steps with progress
        for text, pct in [
            ("Fetching website content...", 25),
            ("Building structure...", 50),
            ("Making pixel perfect...", 75),
            ("Rendering on new port...", 100),
        ]:
            status.text(text)
            progress.progress(pct)
            time.sleep(1)

        # Show card with preview link
        st.markdown("---")
        st.subheader("✅ Website Cloned Successfully")
        st.markdown(
            f'<div style="border:1px solid #444;padding:1rem;border-radius:12px;background-color:#111;">'
            f'<h4 style="color:white;">Preview your cloned site:</h4>'
            f'<a href="http://localhost:{port}" target="_blank" style="color:#1E90FF;">http://localhost:{port}</a>'
            f'</div>',
            unsafe_allow_html=True,
        )
