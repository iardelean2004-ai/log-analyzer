# Log Analyzer

## What it does
This tool parses web server logs and prints simple statistics:
the most active IP addresses, the error rate and the number of requests per hour. It reads the file line by line, so it works on large files too.


## How to run
```bash
python3 -m venv venv
source venv/bin/activate
pip install pytest
python src/generate_logs.py
python -m src.main data/access.log --top 3
python -m pytest
```

## Example output
```
Top IPs:
   10.0.0.5: 279
   203.0.113.7: 249
   172.16.0.8: 242
Error rate: 34.1%
Requests per hour:
   00:00 80
   01:00 78
   02:00 84
   03:00 79
   04:00 73
   05:00 83
   06:00 91
   07:00 78
   08:00 74
   09:00 73
   10:00 72
   11:00 82
   12:00 53
```

## Project structure
- `parser.py` parses takes a log line and turns it into an object with IP, time and status.
- `stats.py` calculates top IPs, error rate and requests per hour.
- `main.py` reads the command-line arguments, prints the results.
- `generate_logs.py` generates a sample log file for testing.
