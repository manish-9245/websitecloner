
# 🌀 Clone Any Website to Localhost

A Streamlit-based tool that **clones and proxies any website** to your local machine by spinning up a temporary HTTP proxy server. Enter any public website URL, and it will render the site locally on a new port via `http://localhost:<random-port>`.

---

## 🔧 Features

- ✅ Clone any public website to your localhost
- 🌐 Automatically detects and proxies GET requests
- 🚀 Runs a temporary HTTP proxy server on a random port
- 📦 Interactive progress and status updates via Streamlit
- 🧠 Built-in validation for URLs
- 🔒 Fully local – no data is stored or shared

---

## 📸 Preview
![Clone Website to Localhost - UI](hehe.gif)


---

## 🧠 How It Works ?

### 📊 Architecture Diagram

```plaintext
┌────────────────────────────┐
│      Streamlit UI          │
│ ────────────────────────── │
│ [User enters website URL]  │
│ [Click "Start Cloning"]    │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Validate & Parse URL       │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Start Proxy Server Thread  │
│ (random port 9000–9999)    │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ HTTP Proxy Handler         │
│ (requests.get to target)   │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Serve to http://localhost  │
└────────────────────────────┘
```

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.8+
- pip
- Streamlit

### 🛠️ Installation

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/clone-website-localhost.git
cd clone-website-localhost
```

2. **Create a Virtual Environment (optional)**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scriptsctivate`
```

3. **Install Requirements**
```bash
pip install -r requirements.txt
```

> `requirements.txt`:
```txt
streamlit
requests
```

4. **Run the App**
```bash
streamlit run app.py
```

---

## 🧪 Example

- Input: `https://example.com`
- Output: `http://localhost:9324` (random port)

---

## 📁 File Structure

```bash
.
├── app.py               # Main Streamlit app
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
```

---

## 🔐 Limitations

- This proxy only supports **GET requests**
- JavaScript-heavy sites may not behave exactly the same (since it's a basic proxy)
- Only works with publicly accessible URLs

---

## 📄 License

MIT License © 2025 Manish Tiwari

---

## 🙋 FAQ

**Q: Does this download the entire website?**  
No. It proxies all GET requests in real-time.

**Q: Can I interact with forms or buttons?**  
You may see the UI, but POST/JS-based interactions will likely fail.

**Q: Is this secure?**  
Yes. Everything runs locally and is never sent outside.

---

## 💬 Credits

Built using:
- [Streamlit](https://streamlit.io/)
- [Python Requests](https://docs.python-requests.org/)
- [http.server](https://docs.python.org/3/library/http.server.html)
