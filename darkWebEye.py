#!/usr/bin/env/python3
# This Python file uses the following encoding:utf-8

# ===== #
#   
# ▀█████████▄     ▄████████         Author: Jolanda de Koff | BullsEye
#   ███    ███   ███    ███         Websites: HackingPassion.com | Bullseye0.com / JolandaDeKoff.com
#   ███    ███   ███    █▀          GitHub: https://github.com/BullsEye0
#  ▄███▄▄▄██▀   ▄███▄▄▄             linkedin: https://www.linkedin.com/in/jolandadekoff
# ▀▀███▀▀▀██▄  ▀▀███▀▀▀             Facebook Group: https://www.facebook.com/groups/hack.passion/
#   ███    ██▄   ███    █▄          Facebook: https://www.facebook.com/profile.php?id=100069546190609
#   ███    ███   ███    ███         Facebook Page: https://www.facebook.com/ethical.hack.group
# ▄█████████▀    ██████████         Odysee: https://odysee.com/$/invite/@hackingpassion:9
#                                   Reddit: https://www.reddit.com/user/BullsEye_0/
#                                   Medium: https://medium.com/@bulls-eye
#                                   
#          BullsEye..!
# ===== #

# DarkWebEye v1 Created June 2024
# Copyright (c) 2024 Jolanda de Koff.

########################################################################

# A notice to all nerds and n00bs...
# If you copy the developer's work, it will not make you a hacker..!
# Respect all developers; we are doing this because it's fun...

########################################################################


import subprocess
import sys
import os
import json
import time
import signal

from colorama import init, Fore

init(autoreset=True)

interrupted = False

def in_virtualenv():
    return (
        hasattr(sys, 'real_prefix') or 
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )

def install_module(module_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
    except subprocess.CalledProcessError:
        return False
    return True

def create_virtualenv():
    if not os.path.exists('env'):
        try:
            subprocess.check_call([sys.executable, "-m", "venv", "env"])
            print(Fore.LIGHTGREEN_EX + "Virtual environment created successfully.")
        except subprocess.CalledProcessError as e:
            print(Fore.LIGHTRED_EX + f"Failed to create virtual environment: {e}")
            sys.exit(1)

def activate_and_run():
    env_activate = os.path.join('env', 'bin', 'activate') if os.name == 'posix' else os.path.join('env', 'Scripts', 'activate')
    if os.name == 'posix':
        subprocess.call(['bash', '-c', f'source {env_activate} && python {sys.argv[0]}'])
    else:
        subprocess.call(['cmd.exe', '/k', f'env\\Scripts\\activate && python {sys.argv[0]}'])
    os._exit(0)

def install_modules_in_virtualenv():
    env_python = os.path.join('env', 'bin', 'python') if os.name == 'posix' else os.path.join('env', 'Scripts', 'python.exe')
    for module in required_modules:
        try:
            subprocess.check_call([env_python, "-m", "pip", "install", module])
        except subprocess.CalledProcessError as e:
            print(Fore.LIGHTRED_EX + f"Failed to install {module} in virtual environment: {e}")
            sys.exit(1)

def check_and_install_modules():
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(Fore.LIGHTYELLOW_EX + f"Module {module} not found. Installing...")
            if not install_module(module):
                print(Fore.LIGHTRED_EX + f"Failed to install {module}.")
                print_virtualenv_prompt()
                choice = input("Create a virtual environment and install the required modules? (yes/no): ").strip().lower()
                if choice == 'yes':
                    create_virtualenv()
                    install_modules_in_virtualenv()
                    activate_and_run()
                else:
                    print(Fore.LIGHTRED_EX + "Modules not installed. Exiting...")
                    sys.exit(1)

def print_virtualenv_prompt():
    print(Fore.RED + """
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀ █     █░▓█████  ▄▄▄▄   ▓█████▓██   ██▓▓█████ 
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒ ▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓█   ▀ ▒██  ██▒▓█   ▀ 
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ ▒█░ █ ░█ ▒███   ▒██▒ ▄██▒███    ▒██ ██░▒███   
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ▒▓█  ▄  ░ ▐██▓░▒▓█  ▄ 
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄░░██▒██▓ ░▒████▒░▓█  ▀█▓░▒████▒ ░ ██▒▓░░▒████▒
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░  ▒ ░ ░   ░ ░  ░▒░▒   ░  ░ ░  ░▓██ ░▒░  ░ ░  ░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░   ░   ░     ░    ░    ░    ░   ▒ ▒ ░░     ░   
   ░          ░  ░   ░     ░  ░       ░       ░  ░ ░         ░  ░░ ░        ░  ░  
    """ + Fore.RESET)
    print(Fore.LIGHTBLUE_EX + "\t           Where Curiosity Meets the Hidden")
    time.sleep(0.5)
    print(Fore.LIGHTBLUE_EX + "\tJourney Through the Dark - Seeking Secrets in the Shadows\n\n")
    time.sleep(0.3)
    print(Fore.LIGHTYELLOW_EX + "\tHow about creating a virtual environment?")
    print(Fore.LIGHTYELLOW_EX + "\tHere’s why it's a good idea:")
    print(Fore.LIGHTYELLOW_EX + "\t1. It keeps this project's libraries separate from others.")
    print(Fore.LIGHTYELLOW_EX + "\t2. It avoids version conflicts.")
    print(Fore.LIGHTYELLOW_EX + "\t3. It makes it easy to manage and remove dependencies.")
    print(Fore.LIGHTYELLOW_EX + "\t4. It keeps your main Python installation clean.\n")
    print(Fore.LIGHTWHITE_EX + "\tModule Installation Notice:")
    print(Fore.LIGHTWHITE_EX + "\tThis script will install necessary Python modules.")
    print(Fore.LIGHTWHITE_EX + "\tThese modules are required for the tool to function properly.")
    print(Fore.LIGHTWHITE_EX + "\tFor more information, visit the GitHub page: https://github.com/BullsEye0\n")

required_modules = [
    'fpdf',
    'colorama',
    'requests'
]

def signal_handler(sig, frame):
    global interrupted
    if not interrupted:
        interrupted = True
        print("\n\n\t\033[1;91m[!] I like to See Ya \033[0m😃")
        sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)

if not in_virtualenv():
    if not os.path.exists('env'):
        print("\nThis tool is not running in a virtual environment.")
        print_virtualenv_prompt()
        choice = input("Create a virtual environment and install the required modules? (yes/no): ").strip().lower()
        if choice == 'yes':
            create_virtualenv()
            install_modules_in_virtualenv()
            activate_and_run()
        else:
            print(Fore.LIGHTRED_EX + "Modules not installed. Exiting...")
            print("\n\t\033[1;91m[!] I like to See Ya \033[0m😃")
            sys.exit(1)
    else:
        activate_and_run()
else:
    check_and_install_modules()

from fpdf import FPDF
import requests
from html.parser import HTMLParser

def clear_screen(title=None):
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
        if title:
            print(f"\033]0;{title}\007", end='')

def print_darkwebeye_title():
    print(Fore.RED + '''
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀ █     █░▓█████  ▄▄▄▄   ▓█████▓██   ██▓▓█████ 
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒ ▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓█   ▀ ▒██  ██▒▓█   ▀ 
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ ▒█░ █ ░█ ▒███   ▒██▒ ▄██▒███    ▒██ ██░▒███   
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ▒▓█  ▄  ░ ▐██▓░▒▓█  ▄ 
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄░░██▒██▓ ░▒████▒░▓█  ▀█▓░▒████▒ ░ ██▒▓░░▒████▒
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░  ▒ ░ ░   ░ ░  ░▒░▒   ░  ░ ░  ░▓██ ░▒░  ░ ░  ░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░   ░   ░     ░    ░    ░    ░   ▒ ▒ ░░     ░   
   ░          ░  ░   ░     ░  ░       ░       ░  ░ ░         ░  ░░ ░        ░  ░
 ░    ''' + Fore.RESET)

    print(Fore.LIGHTBLUE_EX + "\t           Where Curiosity Meets the Hidden")
    time.sleep(0.5)
    print(Fore.LIGHTBLUE_EX + "\tJourney Through the Dark - Seeking Secrets in the Shadows\n\n")
    time.sleep(0.3)

class DarkWebSearchParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.results = []
        self.current_title = None
        self.current_link = None
        self.current_onion_link = None
        self.current_description = None
        self.current_time = None
        self.in_result = False
        self.in_description = False
        self.in_title = False
        self.in_link = False
        self.in_time = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'li' and ('class', 'result') in attrs:
            self.in_result = True
            self.current_title = ''
            self.current_link = ''
            self.current_onion_link = ''
            self.current_description = ''
            self.current_time = ''
        elif self.in_result and tag == 'h4':
            self.in_title = True
        elif self.in_result and tag == 'a' and 'href' in attrs_dict:
            href = attrs_dict['href']
            self.current_link = href
            if 'redirect_url=' in href:
                self.current_onion_link = href.split('redirect_url=')[1]
            self.in_link = True
        elif self.in_result and tag == 'span' and 'class' in attrs_dict and attrs_dict['class'] == 'result-date':
            self.in_time = True
        elif self.in_result and tag == 'p':
            self.in_description = True

    def handle_data(self, data):
        if self.in_title:
            self.current_title += data.strip()
        elif self.in_description:
            self.current_description += data.strip()
        elif self.in_time:
            self.current_time += data.strip()

    def handle_endtag(self, tag):
        if tag == 'li' and self.in_result:
            self.in_result = False
            self.in_title = False
            self.in_description = False
            self.in_link = False
            self.in_time = False
            self.results.append({
                'title': self.current_title,
                'description': self.current_description,
                'onion_link': self.current_onion_link,
                'direct_link': self.current_link + f' — {self.current_time}' if self.current_time else self.current_link
            })
            self.current_title = None
            self.current_link = None
            self.current_onion_link = None
            self.current_description = None
            self.current_time = None
        elif tag == 'h4':
            self.in_title = False
        elif tag == 'a' and self.in_link:
            self.in_link = False
        elif tag == 'span' and self.in_time:
            self.in_time = False
        elif tag == 'p' and self.in_description:
            self.in_description = False

def search_ahmia(query, time_filter):
    base_url = "https://ahmia.fi/search/"
    search_url = f"{base_url}?q={query}&d={time_filter}"

    try:
        start_time = time.time()
        response = requests.get(search_url)
        elapsed_time = time.time() - start_time

        if response.status_code == 200:
            parser = DarkWebSearchParser()
            parser.feed(response.text)
            results = parser.results
            for result in results:
                print(Fore.LIGHTBLUE_EX + f"Title: {result['title']}")
                print(f"Description: {result['description'] if result['description'] else 'No description provided'}")
                print(f"Onion Link: {result['onion_link'] if result['onion_link'] else 'None'}")
                print(f"Direct Link: {result['direct_link'] if result['direct_link'] else 'None'}")
                print(Fore.LIGHTBLUE_EX + "+==================================================================================================+")
            print(f"\nOmitted very similar entries. Displaying {len(results)} matches in {elapsed_time:.2f} seconds.")
            return results
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_results(results, file_type, save_path):
    if file_type == '1':
        file_path = os.path.join(save_path, 'results.txt')
        with open(file_path, 'w') as f:
            for result in results:
                f.write(f"Title: {result['title']}\n")
                f.write(f"Description: {result['description']}\n")
                f.write(f"Onion Link: {result['onion_link']}\n")
                f.write(f"Direct Link: {result['direct_link']}\n")
                f.write("+=======================================================================================================+\n")
        print(f"Results saved as {file_path}")
    elif file_type == '2':
        file_path = os.path.join(save_path, 'results.json')
        with open(file_path, 'w') as f:
            json.dump(results, f, indent=4)
        print(f"Results saved as {file_path}")
    elif file_type == '3' and 'fpdf' in sys.modules:
        file_path = os.path.join(save_path, 'results.pdf')
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for result in results:
            pdf.cell(200, 10, txt=f"Title: {result['title']}".encode('latin1', 'replace').decode('latin1'), ln=True)
            pdf.multi_cell(0, 10, txt=f"Description: {result['description']}".encode('latin1', 'replace').decode('latin1'))
            pdf.cell(200, 10, txt=f"Onion Link: {result['onion_link']}".encode('latin1', 'replace').decode('latin1'), ln=True)
            pdf.cell(200, 10, txt=f"Direct Link: {result['direct_link']}".encode('latin1', 'replace').decode('latin1'), ln=True)
            pdf.cell(200, 10, txt="+=======================================================================================================+", ln=True)
        pdf.output(file_path)
        print(f"Results saved as {file_path}")
    elif file_type == '3':
        print("\tPDF saving is not available because the 'fpdf' module is not installed.")
    else:
        print("\tInvalid file type selected.")

def main():
    try:
        while True:
            clear_screen("\tDarkWebEye")
            print(Fore.LIGHTBLUE_EX + "+==============================+")
            print(Fore.LIGHTBLUE_EX + "Created by Jolanda de Koff / BullsEye 🎯")
            print(Fore.LIGHTBLUE_EX + "Github:  https://github.com/BullsEye0")
            print(Fore.LIGHTBLUE_EX + "Website: https://HackingPassion.com")
            print(Fore.LIGHTBLUE_EX + "Odysee: https://odysee.com/$/invite/@hackingpassion:9")
            print(Fore.LIGHTYELLOW_EX + "Hi There, Shall We Play a Game..?")
            print(Fore.LIGHTBLUE_EX + "+==============================+\n")
            time.sleep(0.5)
            print_darkwebeye_title()
            
            search_query = input(Fore.LIGHTYELLOW_EX + "\n\tEnter your search query or (type 'exit' to quit): ")
            if search_query.lower() == 'exit':
                print("\n\t\033[1;91m[!] I like to See Ya \033[0m😃\n\n")
                time.sleep(0.5)
                sys.exit(1)

            print(Fore.LIGHTYELLOW_EX + "\tChoose a time filter:")
            print("\t1. Any Time")
            print("\t2. Last Day")
            print("\t3. Last Week")
            print("\t4. Last Month")
            
            time_choice = input("\tEnter the number of your choice: ")
            
            if time_choice == '1':
                time_filter = 'all'
            elif time_choice == '2':
                time_filter = '1'
            elif time_choice == '3':
                time_filter = '7'
            elif time_choice == '4':
                time_filter = '30'
            else:
                print("Invalid choice. Defaulting to Any Time.")
                time_filter = 'all'

            results = search_ahmia(search_query, time_filter)
            
            if results:
                print(Fore.LIGHTYELLOW_EX + "\t\nChoose a file format to save the results:")
                print("\t1. Save as .txt")
                print("\t2. Save as .json")
                print("\t3. Save as .pdf")
                print("\t4. Do not save")
                file_choice = input("\tEnter the number of your choice: ")
                if file_choice in ['1', '2', '3']:
                    save_path = input(Fore.LIGHTYELLOW_EX + "\tEnter the directory to save the file (leave empty for current directory): ").strip()
                    if not save_path:
                        save_path = os.getcwd()
                    save_results(results, file_choice, save_path)
                elif file_choice == '4':
                    print("\tResults will not be saved.")

            input("\n\n\n\tPress Enter to search again.")

    except KeyboardInterrupt:
        pass 

if __name__ == "__main__":
    main()
