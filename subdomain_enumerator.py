import requests
import sys
try :
  with open("/usr/share/wordlists/rockyou.txt", 'r', encoding='utf-8', errors='ignore') as file:
    sub_list = file.read()
except Exception as e:
  print("Error occured : {e}")
  sys.exit(1)

subdoms = sub_list.splitlines()  #directories = sub_list.splitlines()
for sub in subdoms:  # sub=dir
  sub_domains = f"http://{sub}.{sys.argv[1]}"   # dir_enum = f"http://{sys.argv[1]}/{sub}.html
  try:
      requests.get(sub_domains)       #sub_domains = dir_enum
  except requests.ConnectionError:
         pass
  else:
         print("Valid domain: ",sub_domains)  #sub_domains = dir_enum
