import requests
import time
import hashlib, os
import colorama

def rooooo(filename):

    hasher = hashlib.sha256()
    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(4096) 
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

uncovershitpleasecomebacklululepu = "https://api.uncover.us.kg/upload"

uhncivcjrijrri = """
 __    __                                                                     ______   __    __  ______ 
/  |  /  |                                                                   /      \ /  |  /  |/      |
$$ |  $$ | _______    _______   ______   __     __  ______    ______        /$$$$$$  |$$ |  $$ |$$$$$$/ 
$$ |  $$ |/       \  /       | /      \ /  \   /  |/      \  /      \       $$ | _$$/ $$ |  $$ |  $$ |  
$$ |  $$ |$$$$$$$  |/$$$$$$$/ /$$$$$$  |$$  \ /$$//$$$$$$  |/$$$$$$  |      $$ |/    |$$ |  $$ |  $$ |  
$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ | $$  /$$/ $$    $$ |$$ |  $$/       $$ |$$$$ |$$ |  $$ |  $$ |  
$$ \__$$ |$$ |  $$ |$$ \_____ $$ \__$$ |  $$ $$/  $$$$$$$$/ $$ |            $$ \__$$ |$$ \__$$ | _$$ |_ 
$$    $$/ $$ |  $$ |$$       |$$    $$/    $$$/   $$       |$$ |            $$    $$/ $$    $$/ / $$   |
 $$$$$$/  $$/   $$/  $$$$$$$/  $$$$$$/      $/     $$$$$$$/ $$/              $$$$$$/   $$$$$$/  $$$$$$/ 
 
 - made by handler six | https://github.com/handlersix
                                                                                                        
"""
os.system("cls")
print(colorama.Fore.BLUE+uhncivcjrijrri)
file = input("put ur file here (EXE AND BAT ONLY) and dont include the quotations ALSO IT HAS TO BE UNDER 100 MB\n>> ")
bell = int(input("what do u want the delay to be (10 - 30, set depending on file size.): "))


harsh = rooooo(filename=file)

with open(file, 'rb') as zfile:
    file_data = zfile.read()  
    files = {'file': ('filename', file_data)}
    try:
        response = requests.post(uncovershitpleasecomebacklululepu, files=files, timeout=60)
        response.raise_for_status()
    except Exception as e:
        print(f"ignore this")

time.sleep(bell)
zetg = requests.get(f"https://api.uncover.us.kg/sample/{harsh}")
configahaha = zetg.json()
cnfig = configahaha.get("config")
familykyykk = configahaha.get("family")
print(f"found config from uncovershit...")
print(f"Malware Config:\n{cnfig}".replace("<br>", "| "))
