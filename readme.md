
# 👻 Remote Ghost Typer

**Remote Ghost Typer** is a fun and practical Python tool that lets you send text over a network from one machine and have it automatically typed on another — as if a ghost were using the keyboard!

---

## 📦 Features
- Send text from a client app (Streamlit UI).
- Receive and automatically type text on a remote machine.
- Randomized typing delays for a more natural effect.
- Works across local network or via port forwarding.
- Simple to set up and run.

---

## 🛠 Requirements

- **Python 3.8+**
- The following Python packages:
  - `socket` *(standard library, no install needed)*
  - `keyboard`
  - `streamlit`

---

## 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/remote-ghost-typer.git
   cd remote-ghost-typer
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   **`requirements.txt`**

   ```
   keyboard
   streamlit
   ```

3. **(Windows only)**
   Run the terminal or IDE as **Administrator**, because the `keyboard` module needs elevated permissions to simulate keystrokes.

---

## 🚀 Usage

The project consists of **two scripts**:

### 1️⃣ Server (Receiver & Typer)

Runs on the machine that will *type* the received messages.

```bash
python receive.py
```

* Listens on `0.0.0.0:12345` by default.
* When a message is received, it types it out automatically.
* You have 5 seconds before typing starts (time to switch to the target application).

---

### 2️⃣ Client (Sender)

Runs on any machine (same network or connected remotely). Provides a Streamlit UI to send messages.

```bash
streamlit run sender.py
```
or 
```bash
python wrapper.py
```

* Enter the **Server IP**, **Port**, and your message.
* Click **🚀 Send Message**.
* The message will be sent and typed on the remote machine.

---

## 🌐 Network Setup

* For local testing, keep `host` as `localhost` or your local IP.
* For LAN use, set the `host` in the client to the server machine’s local IP (e.g., `192.168.1.100`).
* For WAN/Internet access, set up port forwarding on your router and ensure the firewall allows connections.

---

## ⚠ Important Notes

* **Use responsibly!** This tool can control another machine’s keyboard — only run it on devices you own or have permission to use.
* The `keyboard` library may require **admin/root** privileges.
* If antivirus software flags it, whitelist the script (keyboard automation can trigger alerts).
* This can give backdoor access to intruders **`(USE CAREFULLY AT YOUR OWN RISK)`**
---
## Special Use
You can access UI from your mobile if your device and host device are on same network. You can access ui on hostmachine ip address on port 8501

Steps:
    - In cmd type ```ipconfig ```
    - Locate  IPv4 Address Address on your WIFI or LAN connected
    - In your mobile open this URL: **http://Your_IPV4_ADDRESS:8501**

With this you can type the question in your exam to GPT on you mobile, then copy the answer to application website. Your host machine will start typing the answers. 

Undetected in mettl, HackerEarth, HireVue

---

## 📄 License

MIT License — Feel free to modify and share. PR will be merged if functionality is found useful.

---

## 👤 Author

Created by **Nimesh Bhavsar**
Inspired by the idea of making typing magically happen from afar!