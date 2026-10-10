import re
from datetime import datetime
from dataclasses import dataclass
LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ '
    r'\[(?P<time>[^\]]+)\] '
    r'"(?P<method>[A-Z]+) (?P<path>\S+) [^"]+" '
    r'(?P<status>\d{3}) (?P<size>\d+|-)'
)
@dataclass
class LogEntry:
    ip:str
    time:datetime
    method:str
    path:str
    status:int
    size:int 
linie= '192.168.1.10 - - [01/Oct/2026:00:00:42 +0000] "GET /login HTPP/ 1.1" 404 3127'
m = LOG_PATTERN.match(linie)
print(m["ip"])
print(m["time"])
print(m["method"])
print(m["path"])
print(m["status"])
print(m["size"])
e= LogEntry ("1.1.1.1" , datetime.now(), "GET", "/", 200, 100)
print(e)
print(e.status +1)




