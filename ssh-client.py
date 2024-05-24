import paramiko

host = "127.0.0.1"
user = "kali"
passwd = "kali"

client_ssh = paramiko.SSHClient()
client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client_ssh.connect(host, username=user, password=passwd)

while True:
    stdin, stdout, stderr = client_ssh.exec_command(input("\nDigite seu comando: "))
    for line in stdout.readlines():
        print(line.strip())

    erros = stderr.readlines()
    if erros:
        print(erros)