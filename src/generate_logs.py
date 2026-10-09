
import random
from datetime import datetime, timedelta

IPS = ["192.168.1.10", "10.0.0.5", "172.16.0.8", "203.0.113.7"]
PATHS = ["/", "/login", "/api/users", "/about", "/admin"]
STATUS = [200, 200, 200, 301, 404, 500]

def generate(n=1000, out="data/access.log"):
    t = datetime(2026, 10, 1)
    with open(out, "w") as f:
        for _ in range(n):
            t += timedelta(seconds=random.randint(1, 90))
            ip = random.choice(IPS)
            path = random.choice(PATHS)
            status = random.choice(STATUS)
            f.write(f'{ip} - - [{t:%d/%b/%Y:%H:%M:%S} +0000] '
                    f'"GET {path} HTTP/1.1" {status} {random.randint(200, 5000)}\n')

if __name__ == "__main__":
    generate()
    
    
    
            