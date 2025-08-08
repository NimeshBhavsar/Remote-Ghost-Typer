import socket
import streamlit as st
import time

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
            s.connect((host, port))
            s.sendall(message.encode('utf-8'))
            st.success(f"Message has been sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")

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

# This is a callback function that will be called by the button.
# It contains the logic to send the message and clear the text area.
def send_and_clear_message():
    """Sends the message and clears the text area using session state."""
    host = st.session_state.host_input
    port = st.session_state.port_input
    message = st.session_state.message_input
    
    if message:
        send_string(host, port, message)
        # Clear the message text area by updating the session state
        st.session_state.message_input = ""

# Use a form to group the input widgets and the button.
with st.form("network_sender_form"):
    # Input fields for Host and Port
    host_input = st.text_input("Host IP Address / Hostname", value=DEFAULT_HOST, help="e.g., localhost or 192.168.1.100", key="host_input")
    port_input = st.number_input("Port Number", value=DEFAULT_PORT, min_value=1, max_value=65535, help="Must match the server's listening port", key="port_input")

    # Text area for the message to send, using session state
    st.text_area(
        "Message to Send",
        key='message_input',
        height=300,
        help="Type your message here."
    )

    # Send button with an on_click callback
    st.form_submit_button("🚀 Send Message", on_click=send_and_clear_message)
input()