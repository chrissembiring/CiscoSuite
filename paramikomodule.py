import paramiko
import time

def connect(dest_ip, dest_port, user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(dest_ip, port = dest_port, username = user, password = passwd, look_for_keys = False, allow_agent = False)
    return client

def get_shell(client):
    connection = client.invoke_shell()
    return connection

def send_command(connection, command):
    connection.send(command + '\n')
    time.sleep(2)
    output = connection.recv(4096)
    return output

def request_config(connection):
    connection.send('show run\n')
    time.sleep(5)
    outputConfig = connection.recv(16384)
    return outputConfig

def close(client):
    if client.get_transport().is_active():
        client.close()
