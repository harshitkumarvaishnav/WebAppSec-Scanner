import socket


COMMON_PORTS = {

    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt"

}


def scan_ports(ip):

    open_ports = []

    try:

        for port, service in COMMON_PORTS.items():

            sock = socket.socket()

            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))

            sock.close()

            if result == 0:

                open_ports.append({

                    "port": port,

                    "service": service

                })

        return {

            "total_open": len(open_ports),

            "ports": open_ports

        }

    except Exception as e:

        return {

            "error": str(e)

        }