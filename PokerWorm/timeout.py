import urllib.error
import urllib.request
import socket


try:
    response = urllib.request.urlopen("http://thepokerlogic.com/glossary", timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time Out')