import sys
import datetime

def log_message(log_file):
    with open(log_file, 'a') as f:
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                continue

            parts = line.split(maxsplit=1)
            if len(parts) < 2:
                continue
            
            action, message = parts[0], parts[1]
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            log_entry = f"{timestamp} [{action}] {message}\n"
            f.write(log_entry)
            f.flush()
            if action == "QUIT":
                f.write("\n")
                f.flush()
                f.close()
                break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python logger.py <log_file>", file=sys.stderr)
        sys.exit(1)
    
    log_message(sys.argv[1])
