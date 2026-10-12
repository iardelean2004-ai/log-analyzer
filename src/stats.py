from collections import Counter
from src.parser import parse_file

def top_ips(path, n=3):
    counter=Counter()
    for entry in parse_file(path):
        counter[entry.ip] +=1
    return counter.most_common(n)
def error_rate(path):
    total=0
    errors=0
    for entry in parse_file(path):
        total +=1
        if entry.status >= 400:
            errors+=1
    return errors / total if total else 0.0
print(top_ips("data/access.log"))
print(f"{error_rate('data/access.log'): .1%}")

