import tls_client, os, sys, time
from threading import Thread

os.system("cls||clear")

token = "Authorization | user account token"
target_username = "test123"
target_username_holder = "1094436659120054372"
delay = 0.1

__xsuperproperties = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDEzIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTk4MzE4LCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMjI2NiwiY2xpZW50X3ZlcnNpb25fc3RyaW5nIjoiMS4wLjkwMTMifQ=="
__useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9013 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36"
headers = {"Authorization": token,"Accept-Encoding": "gzip, deflate","Origin": "https://discord.com","Accept": "*/*","X-Discord-Locale": "en-US","X-Super-Properties": __xsuperproperties,"User-Agent": __useragent,"Referer": "https://discord.com/channels/@me/pomelo","X-Debug-Options": "bugReporterEnabled","Content-Type": "application/json","X-Discord-Timezone": "Asia/Calcutta"}

session = tls_client.Session(client_identifier="chrome110")
session.headers.update(headers)

def snap():
    payload = {"userame": target_username}
    request = session.post("https://canary.discord.com/api/v9/users/@me/pomelo", json=payload)
    if request.status in (200, 201, 204):
        print("[+] %s claimed" % target_username)
        sys.exit()
    else:
        print("[-] Failed to snipe", request.text)
        sys.exit()

def fetch():
    request = session.get("https://canary.discord.com/api/v9/users/%s" % target_username_holder)
    if request.status_code in (200, 201, 204):
        if target_username not in request.text:
            snap()
            sys.exit()
        else:
            print("[+] %s is still taken" % target_username)
            sys.exit()
    elif request.status_code == 404:
        print("[-] %s invalid user" % target_username_holder)
        sys.exit()
    elif request.status_code == 429:
        rl = request.json()['retry_after']
        print("[-] ratelimit hit, sleeping for %s seconds" % rl)
        time.sleep(rl)
    else:
        print("[-] unknown error", request.text)
        sys.exit()

if __name__ == "__main__":
    time.sleep(delay)
    Thread(target=fetch).start()
