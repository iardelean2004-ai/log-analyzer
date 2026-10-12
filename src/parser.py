import re
from datetime import datetime
from dataclasses import dataclass
from typing import Optional
from typing import Iterator
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
def parse_file(path:str) -> Iterator[LogEntry]:
    with open(path) as f:
        for line in f:
            entry= parse_line(line)
            if entry:
                yield entry





