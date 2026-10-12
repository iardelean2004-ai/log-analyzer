import argparse
from src.stats import top_ips, error_rate, requests_per_hour

def main():
    parser= argparse.ArgumentParser(description= "Analyze web server logs.")
    parser.add_argument("logfile", help="path to the log file")
    parser.add_argument("--top", type=int, default=3, help="how many top IPs to show")
    args= parser.parse_args()
    print("Top IPs:")
    for ip, count in top_ips(args.logfile, args.top):
        print(f" {ip}: {count}")
        
    print(f"Error rate: {error_rate(args.logfile):.1%}")
    print("Requests per hour:")
    for hour, count in requests_per_hour(args.logfile):
        print(f" {hour:02d}:00 {count}")
        
if __name__ == "__main__":
    main()
        