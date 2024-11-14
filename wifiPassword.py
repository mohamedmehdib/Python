import subprocess

def get_wifi_passwords():

    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in profiles_data if "All User Profile" in i]


    for profile in profiles:
        results = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear').decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print(f"Profile: {profile}, Password: {results[0]}")
        except IndexError:
            print(f"Profile: {profile}, Password: None")
            
get_wifi_passwords()