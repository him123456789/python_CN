import socket
from typing import Optional


def connect(host: str, port: int, timeout: float = 5.0) -> bool:
    """Attempt to establish a TCP connection to *host* on *port*.

    Parameters
    ----------
    host: str
        Target hostname or IP address.
    port: int
        Destination TCP port.
    timeout: float, optional
        Connection timeout in seconds. Defaults to 5 seconds.

    Returns
    -------
    bool
        True if the connection succeeds, False otherwise.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
        except OSError:
            return False
    return True


if __name__ == "__main__":
    target_host = input("Enter host to connect: ")
    target_port = int(input("Enter port to connect: "))
    if connect(target_host, target_port):
        print(f"Successfully connected to {target_host}:{target_port}")
    else:
        print(f"Failed to connect to {target_host}:{target_port}")
