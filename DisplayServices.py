import subprocess

class GlobalVars:
    services = None

try: 
    services = subprocess.Popen("service --status-all", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
    services = services[:-1]
    services = services.replace("[ - ] ", "Stopped")
    services = services.replace("[ + ] ", "Running")
    services = services.split("\n")
    GlobalVars.services = [[x for x in line.strip().split(' ')] for line in services]
    print(GlobalVars.services)
except Exception as e:
    print("Unable to retrieve system services.", e)