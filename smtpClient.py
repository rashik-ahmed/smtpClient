from socket import *

def send_command(clientSocket, command, expected_code):
    clientSocket.send(command.encode())
    response = clientSocket.recv(1024).decode()
    if response[:3] != expected_code:
        print(f'{expected_code} reply not received from server. Response: {response}')
    return response

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # Receive the initial response from the server
    recv = clientSocket.recv(1024).decode()

    # Send HELO command
    send_command(clientSocket, 'HELO Alice\r\n', '250')

    # Send MAIL FROM command
    send_command(clientSocket, 'MAIL FROM:<rashikahmed2002@gmail.com>\r\n', '250')

    # Send RCPT TO command
    send_command(clientSocket, 'RCPT TO:<ra3197@nyu.edu>\r\n', '250')

    # Send DATA command
    send_command(clientSocket, 'DATA\r\n', '354')

    # Send message data
    clientSocket.send(msg.encode())

    # End message with a period and handle server response
    send_command(clientSocket, endmsg, '250')

    # Send QUIT command and handle server response
    send_command(clientSocket, 'QUIT\r\n', '221')

    # Close the socket
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
