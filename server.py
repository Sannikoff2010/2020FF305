import multiprocessing.connection, threading, socket, logging

def server_start(port: int, ip_list: tuple, authkey: bytes) -> dict:
    servers = {}
    for ip in ip_list:
        ip_port = (ip, port)
        t = lambda ipp=ip_port: worker(ipp, authkey, work=job, servers=servers)
        servers[ip_port] = threading.Thread(target=t, daemon=False)
        servers[ip_port].start()
    return servers

def worker(ip_port: (str, int), authkey: bytes, work: 'callable', servers: dict, error='') -> None:
    while servers.get(ip_port):
        with multiprocessing.connection.Listener(ip_port, authkey=authkey) as listener:
            with listener.accept() as conn:
                try:
                    conn.send_bytes(work(conn.recv()))
                except:
                    conn.send(error)
                    logging.error(conn, exc_info=True)

def job(file_name: str) -> bytes:
    with open(file_name, 'rb') as f:
        return f.read()

if __name__ == '__main__':
    h = socket.gethostbyname_ex(socket.gethostname())  # ('DESKTOP-GMS1C57', [], ['192.168.1.44', '17...'])
    servers = server_start(port=9090, ip_list=tuple(h[2]), authkey=b'secret')
    print(servers)  # {('192.168.1.44', 8080): <Thread(Thread-1, started 11420)>, ('17...', 8080): <Thread(Thread-2, started 4364)>}