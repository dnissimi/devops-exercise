import requests, sys

#r = requests.get("http://127.0.0.1:8080/api/v1.0/about")
r = requests.get(sys.argv[1])

if r.status_code != 200:
    print (r.status_code)
    exit(1)
