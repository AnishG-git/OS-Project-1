import sys
import subprocess

def driver(log_file):
    logger = subprocess.Popen(["python", "logger.py", log_file], stdin=subprocess.PIPE, encoding='utf8')
    encryptor = subprocess.Popen(["python", "encryption.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
    
    history = []
    
    def log(message):
        logger.stdin.write(message + "\n")
        logger.stdin.flush()
    
    log("START Driver started")
    
    while True:
        command = input("Enter command (password, encrypt, decrypt, history, quit): ").strip().lower()
        log(f"COMMAND {command}")
        
        if command == "password":
            password = input("Enter passkey: ").strip().upper()
            encryptor.stdin.write(f"PASS {password}\n")
            encryptor.stdin.flush()
            print(encryptor.stdout.readline().rstrip())
        elif command == "encrypt":
            text = input("Enter text to encrypt: ").strip().upper()
            history.append(text)
            encryptor.stdin.write(f"ENCRYPT {text}\n")
            encryptor.stdin.flush()
            print(encryptor.stdout.readline().strip())
        elif command == "decrypt":
            text = input("Enter text to decrypt: ").strip().upper()
            history.append(text)
            encryptor.stdin.write(f"DECRYPT {text}\n")
            encryptor.stdin.flush()
            print(encryptor.stdout.readline().strip())
        elif command == "history":
            print("History:", history)
        elif command == "quit":
            encryptor.stdin.write("QUIT\n")
            encryptor.stdin.flush()
            logger.stdin.write("QUIT\n")
            logger.stdin.flush()
            break
        else:
            print("Invalid command")
    
    log("EXIT Driver exiting")
    encryptor.wait()
    logger.wait()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python driver.py <log_file>", file=sys.stderr)
        sys.exit(1)
    driver(sys.argv[1])
