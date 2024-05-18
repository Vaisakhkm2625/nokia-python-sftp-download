import paramiko
import shutil
from base64 import decodebytes

# env variables - destination file path, remote file path, 
# make/get list of servers
destination_file_path = "./data/"
remote_directory= "./var/log"

server = "localhost" 
port = 22
username = "vaisakh"
password = "J35KLZ_ia"

keydata = b"""AAAAC3NzaC1lZDI1NTE5AAAAIE3CNn6MPOvEaVQ6qSGN/uK9CEVo+6/SMdB+2GE/jZKA"""
key = paramiko.Ed25519Key(data=decodebytes(keydata))

client = paramiko.SSHClient()
#client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.get_host_keys().add('localhost', 'ssh-ed25519', key)
client.connect(server,port=port,username=username,password=password)

sftp = client.open_sftp()

dirlist = sftp.listdir()
print(dirlist)


# clear the old files

# loop 

#  connect to server
#  make a sftp client
#  download file using get methord on ftp object

# unzip files

# upload files - selenium



