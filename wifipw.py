import subprocess

class GetWifiPassword:

    def __init__(self):
        self.GetPassword()

    def GetPassword(self):
        self.data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')

        self.profiles = [i.split(":")[1][1:-1] for i in self.data if "All User Profile" in i]
        for i in self.profiles:
            try:
                self.results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                self.results = [b.split(":")[1][1:-1] for b in self.results if "Key Content" in b]
                try:
                    print(f"{i} | {self.results[0]}")
                except IndexError:
                    print(f"| {i}")
            except subprocess.CalledProcessError:
                print("ENCODING ERROR")


GetWifiPassword()