import sys
import subprocess

def isValidEncryptionInput(text: str) -> bool:
    if not text.isalpha():
        return False
    return True

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
    if len(history) > 0:
        choices = ["Choose string from history", "Enter new string"]
        chosen = getChoiceFromChoices(choices)
        if chosen == 0:
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

    def executeEncryptionCommand(cmd: str, text: str):
        if cmd == "ENCRYPT" or cmd == "DECRYPT" or cmd == "PASS":
            encryptor.stdin.write(f"{cmd} {text}\n")
            encryptor.stdin.flush()
            result = encryptor.stdout.readline().strip()
            resultParts = result.split(" ", 1)
            if resultParts[0] == "RESULT" and len(resultParts) > 1:
                updateHistory(resultParts[1])
            return result
        if cmd == "QUIT":
            encryptor.stdin.write("QUIT\n")
            encryptor.stdin.flush()

    
    log("START Driver started")
    
    while True:
        command = input("Enter command (password, encrypt, decrypt, history, quit): ").strip().lower()
        log(f"COMMAND {command}")
        
        if command == "password":
            password = input("Enter passkey: ").strip().upper()
            print(executeEncryptionCommand("PASS", password))
        elif command == "encrypt":
            text = getEncryptionString(history, True)
            updateHistory(text)
            print(executeEncryptionCommand("ENCRYPT", text))
        elif command == "decrypt":
            text = getEncryptionString(history, False)
            updateHistory(text)
            print(executeEncryptionCommand("DECRYPT", text))
        elif command == "history":
            print("History:", history)
        elif command == "quit":
            executeEncryptionCommand("QUIT", "")
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