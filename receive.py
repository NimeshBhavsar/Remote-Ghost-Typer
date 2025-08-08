import socket
from keyboard1 import type_string
# --- Configuration ---
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 12345

def start_server():
    print(f"Starting server on {SERVER_HOST}:{SERVER_PORT}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((SERVER_HOST, SERVER_PORT))
            s.listen(5) # Increased backlog to 5 for more queued connections
            print("Server is listening for incoming connections...")

            while True: # Outer loop to continuously accept new client connections
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True: # Inner loop to receive multiple messages from the current client
                        data = conn.recv(1024)
                        if not data:
                            print(f"Client {addr} disconnected.")
                            break # Break from inner loop to accept new client
                        received_string = data.decode('utf-8')
                        print(f"Received string from {addr}: '{received_string}'")
                        type_string(received_string)

        except OSError as e:
            print(f"Error starting server: {e}. Make sure the port {SERVER_PORT} is not in use.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("Server closed.")
if __name__ == "__main__":
    start_server()
    input("Press Enter to exit...")  # Keep the server running until Enter is pressed
