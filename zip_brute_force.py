import pyzipper
from tqdm import tqdm  # For progress bar

def crack_zip(zip_path, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]
        
        with pyzipper.AESZipFile(zip_path) as zf:
            for password in tqdm(passwords, desc="Testing passwords"):
                try:
                    zf.extractall(path=".", pwd=password.encode())
                    print(f"\n[+] Password found: {password}")
                    return password
                except:
                    continue
        
        print("[-] Password not found in wordlist")
        return None
    
    except Exception as e:
        print(f"[!] Error: {e}")
        return None


crack_zip("/home/emma/Downloads/ziptest2.zip", "Download.txt")

