import re
import csv

def parse_logs(log_file, output_file):
    # Regex pattern to match failed SSH login attempts
    failed_login_pattern = re.compile(r"Failed password for (invalid user )?(?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)")
    
    suspicious_activity = []

    try:
        with open(log_file, "r") as file:
            for line in file:
                match = failed_login_pattern.search(line)
                if match:
                    # Extract the targeted username and attacking IP address
                    user = match.group('user')
                    ip = match.group('ip')
                    suspicious_activity.append([user, ip])
                    
        if suspicious_activity:
            # Export to CSV for business intelligence/analytics tools
            with open(output_file, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Targeted Username", "Attacker IP Address"])
                writer.writerows(suspicious_activity)
            print(f"[+] Analysis complete. {len(suspicious_activity)} failed login attempts exported to {output_file}.")
        else:
            print("[-] No failed logins detected in the log file.")
            
    except FileNotFoundError:
        print(f"[!] Error: The file {log_file} was not found. Please ensure it is in the same directory.")

if __name__ == "__main__":
    print("-" * 45)
    print("Starting Security Log Analyzer...")
    print("-" * 45)
    parse_logs("server.log", "failed_logins.csv")
