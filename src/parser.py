import re
from datetime import datetime
from dataclasses import dataclass
from typing import Optional
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
def parse_line(line:str) -> Optional [LogEntry]:
    match= LOG_PATTERN.match(line)
    if not match:
        return None
    d= match.groupdict()
    return LogEntry(
        ip=d["ip"],
        time=datetime.strptime(d["time"], "%d/%b/%Y:%H:%M:%S %z"),
        method=d["method"],
        path=d["path"],
        status=int(d["status"]),
        size=0 if d["size"] == "-" else int (d["size"]),
    )
linie = '192.168.1.10 - - [01/Oct/2026:00:00:42 +0000] "GET /login HTTP/1.1" 404 3127'
print(parse_line(linie))
print(parse_line("linie stricata"))




