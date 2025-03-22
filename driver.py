import sys
import subprocess

def driver(log_file):
    logger = subprocess.Popen(["python", "logger.py", log_file], stdin=subprocess.PIPE, encoding='utf8')
    
    def log(message):
        logger.stdin.write(message + "\n")
        logger.stdin.flush()

    commands = {"password", "encrypt", "decrypt", "history", "quit"}
    
    log("START Driver started")
    
    while True:
        command = input("Enter command (password, encrypt, decrypt, history, quit): ").strip().lower()
        log(f"COMMAND {command}")
        
        if command not in commands:
            print("Invalid command")
            continue

        if command == "quit":
            logger.stdin.write("QUIT\n")
            logger.stdin.flush()
            break
        
    log("EXIT Driver exiting")
    logger.wait()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python driver.py <log_file>", file=sys.stderr)
        sys.exit(1)
    driver(sys.argv[1])
