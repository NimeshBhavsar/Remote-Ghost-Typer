import socket
import streamlit as st

# --- Configuration ---
# Default values for HOST and PORT
DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 12345

def send_string(host: str, port: int, message: str):
    """
    Connects to the server and sends a string.
    Displays status messages using Streamlit.
    """
    if not message:
        st.warning("Please enter a message to send.")
        return

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Connect to the server
            st.info(f"Attempting to connect to {host}:{port}...")
            s.connect((host, port))
            st.success(f"Connected to server at {host}:{port}")

            # Encode the string to bytes before sending
            s.sendall(message.encode('utf-8'))
            st.success(f"Sent: '{message}'")

        except ConnectionRefusedError:
            st.error(f"Connection refused. Is the server running on {host}:{port} and accessible?")
            st.error("Please ensure the server script is running and its firewall allows connections on this port.")
        except socket.gaierror:
            st.error(f"Invalid host address: '{host}'. Please check the IP address or hostname.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

# --- Streamlit UI ---
st.set_page_config(layout="centered", page_title="Network String Sender")

st.title("🌐 Network String Sender")
st.markdown("Enter the host IP/hostname, port, and your message to send it over the network.")

# Input fields for Host and Port
host_input = st.text_input("Host IP Address / Hostname", value=DEFAULT_HOST, help="e.g., localhost or 192.168.1.100")
port_input = st.number_input("Port Number", value=DEFAULT_PORT, min_value=1, max_value=65535, help="Must match the server's listening port")

# Text area for the message to send
message_to_send = st.text_area("Message to Send", height=100, help="Type your message here.")

# Send button
if st.button("🚀 Send Message"):
    try:
        # Convert port input to integer
        port = int(port_input)
        send_string(host_input, port, message_to_send)
        st.rerun()
    except ValueError:
        st.error("Invalid port number. Please enter a valid integer.")