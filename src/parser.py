import re
from datetime import datetime
LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ '
    r'\[(?P<time>[^\]]+)\] '
    r'"(?P<method>[A-Z]+) (?P<path>\S+) [^"]+" '
    r'(?P<status>\d{3}) (?P<size>\d+|-)'
)
linie= '192.168.1.10 - - [01/Oct/2026:00:00:42 +0000] "GET /login HTPP/ 1.1" 404 3127'
m = LOG_PATTERN.match(linie)
print(m["ip"])
print(m["time"])
print(m["method"])
print(m["path"])
print(m["status"])
print(m["size"])



