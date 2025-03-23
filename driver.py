import sys
import subprocess

# returns -1 if choices are empty
def getChoiceFromChoices(choices: list) -> int:
    if len(choices) == 0:
        return -1
    for i, choice in enumerate(choices):
        print(f"[{i}] {choice}")
    choice = input("Enter choice: ")
    while not choice.isdigit() or int(choice) not in range(len(choices)):
        print("Invalid choice")
        choice = input("Enter choice: ")
    return int(choice)

def getNewString(encrypt: bool) -> str:
    potentialChosenString = input(f'Enter alphabetical string to {"encrypt" if encrypt else "decrypt"}: ').strip().upper()
    return potentialChosenString


def getEncryptionString(history: list, encrypt: bool) -> str:
    # printing menu of encryption/decryption commands
    print()
    if len(history) > 0:
        choices = ["Choose string from history", "Enter new string"]
        chosen = getChoiceFromChoices(choices)
        if chosen == 0:
            print()
            chosenIndex = getChoiceFromChoices(history)
            return history[chosenIndex]
        else:
            return getNewString(encrypt)
    else:
        return getNewString(encrypt)
    

def driver(log_file):
    logger = subprocess.Popen(["python", "logger.py", log_file], stdin=subprocess.PIPE, encoding='utf8')
    encryptor = subprocess.Popen(["python", "encryption.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
    
    # history maintains the history of strings encrypted/decrypted in order
    history = []

    # historySet maintains unique string encrypted/decrypted in history
    historySet = set()

    def updateHistory(text: str):
        if text not in historySet:
            history.append(text)
            historySet.add(text)
    
    def log(message):
        logger.stdin.write(message + "\n")
        logger.stdin.flush()

    def executeAndLogEncryptionCommand(cmd: str, text: str):
        if cmd == "ENCRYPT" or cmd == "DECRYPT" or cmd == "PASS":
            encryptor.stdin.write(f"{cmd} {text}\n")
            encryptor.stdin.flush()
            result = encryptor.stdout.readline().strip()
            resultParts = result.split()
            if resultParts[0] == "RESULT" and len(resultParts) == 2:
                updateHistory(resultParts[1])
            log(result)
            print(result + "\n")
            return result
        if cmd == "QUIT":
            encryptor.stdin.write("QUIT\n")
            encryptor.stdin.flush()

    
    log("START Logging started")
    
    while True:
        command = input("Enter command (PASSWORD, ENCRYPT, DECRYPT, HISTORY, QUIT): ").strip().lower()

        if command == "password":
            log("PASSWORD Attempting to set password")
            password = input("Enter passkey: ").strip().upper()
            result = executeAndLogEncryptionCommand("PASS", password)
        elif command == "encrypt":
            text = getEncryptionString(history, encrypt=True)
            log(f"ENCRYPT Attempting to encrypt {text}")
            updateHistory(text)
            result = executeAndLogEncryptionCommand("ENCRYPT", text)
        elif command == "decrypt":
            text = getEncryptionString(history, encrypt=False)
            log(f"ENCRYPT Attempting to decrypt {text}")
            updateHistory(text)
            result = executeAndLogEncryptionCommand("DECRYPT", text)
        elif command == "history":
            log(f"HISTORY {history}")
            print(f"HISTORY {history}\n")
        elif command == "quit":
            executeAndLogEncryptionCommand("QUIT", "")
            log("QUIT Exiting...")
            break
        else:
            print("Invalid command\n")
    
    encryptor.wait()
    logger.wait()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python driver.py <log_file>", file=sys.stderr)
        sys.exit(1)
    driver(sys.argv[1])