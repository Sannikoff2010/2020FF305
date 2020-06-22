import multiprocessing.connection

def remote_file_text(file_name: str, ip_port: (str, int), authkey: bytes) -> bytes:
    with multiprocessing.connection.Client(ip_port, authkey=authkey) as conn:
        conn.send(file_name)
        try:
            return conn.recv_bytes()
        except:
            raise FileNotFoundError(f'{ip_port} {file_name}')

if __name__ == '__main__':
    file_name = '‪C:\\Windows\\Logs\\DISM\\dism.log'
    ipp = ('192.168.56.1', 9090)
    b = remote_file_text(file_name=file_name, ip_port=ipp, authkey=b'secret')  # b'my text'
    text = b.decode('utf-8', errors='ignore')  # "my text"
    print(text)