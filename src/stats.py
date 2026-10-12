from collections import Counter
from src.parser import parse_file

def top_ips(path, n=3):
    counter=Counter()
    for entry in parse_file(path):
        counter[entry.ip] +=1
    return counter.most_common(n)
print(top_ips("data/access.log"))
