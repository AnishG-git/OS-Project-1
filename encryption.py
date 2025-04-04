import sys

def vigenere_cipher(text, key, decrypt=False):
    key = key.upper()
    text = text.upper()
    key_length = len(key)
    result = []
    
    for i, char in enumerate(text):
        if not char.isalpha():
            result.append(char)
            continue
        key_char = key[i % key_length]
        shift = ord(key_char) - ord('A')
        if decrypt:
            shift = -shift
        new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        result.append(new_char)
    return "".join(result)

def isValidInput(text: str) -> bool:
    if not text.isalpha():
        return False
    return True

def main():
    passkey = None
    
    while True:
        command = sys.stdin.readline().strip()
        if not command:
            continue
        
        parts = command.split(" ", 1)
        action = parts[0]
        argument = parts[1] if len(parts) > 1 else ""
        
        if action == "PASS":
            if argument == "":
                print("ERROR Password not set, using previous password if one exists", flush=True)
                continue
            passkey = argument
            print("RESULT Password set", flush=True)
        elif action == "ENCRYPT":
            if passkey is None:
                print("ERROR Password not set", flush=True)
            elif not isValidInput(argument):
                print("ERROR Invalid input", flush=True)
            else:
                print("RESULT", vigenere_cipher(argument, passkey), flush=True)
        elif action == "DECRYPT":
            if passkey is None:
                print("ERROR Password not set", flush=True)
            elif not isValidInput(argument):
                print("ERROR Invalid input", flush=True)
            else:
                print("RESULT", vigenere_cipher(argument, passkey, decrypt=True), flush=True)
        elif action == "QUIT":
            break
        else:
            print("ERROR Invalid command", flush=True)

if __name__ == "__main__":
    main()
