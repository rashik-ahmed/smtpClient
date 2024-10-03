from socket import *

def send_command(clientSocket, command, expected_code):
    # Sends a command to the SMTP server and waits for the response.
    
    # Encode the command string to bytes and send it over the client socket.
    clientSocket.send(command.encode())
    
    # Receives the server's response, decodes it from bytes to a string.
    response = clientSocket.recv(1024).decode()
    
    # Checks if the server's response code matches the expected_code.
    if response[:3] != expected_code:
        # If the response does not start with the expected code, print an error message.
        print(f'{expected_code} reply not received from server. Response: {response}')
    
    # Returns the server's response.
    return response

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # Receive the initial response from the server
    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.'

    # Send HELO command
    send_command(clientSocket, 'HELO Alice\r\n', '250')

    # Send MAIL FROM command and handle server response.
    send_command(clientSocket, 'MAIL FROM:<rashikahmed2002@gmail.com>\r\n', '250')

    # Send RCPT TO command and handle server response.
    send_command(clientSocket, 'RCPT TO:<ra3197@nyu.edu>\r\n', '250')

    # Send DATA command and handle server response.
    send_command(clientSocket, 'DATA\r\n', '354')

    # Send message data.
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    send_command(clientSocket, endmsg, '250')

    # Send QUIT command and handle server response.
    send_command(clientSocket, 'QUIT\r\n', '221')

    # Close the socket
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
