import subprocess
import os
import sys
import argparse
from art import text2art
from colorama import Fore, init, Style
import datetime
import shutil
import tempfile

init(autoreset=True)

TOOL_NAME = f"{Fore.CYAN}Tar-X Archiver{Fore.RESET}"
TOOL_VERSION = "1.1"
DEVELOPER = f"{Fore.MAGENTA}@ZORO2045. [ Telegram - GitHub ]{Fore.RESET}"
DESCRIPTION = f"{Fore.YELLOW}A tool to create non-compressed {Fore.BLUE}.tar{Fore.RESET}{Fore.YELLOW} archives using the standard (posix) tar command.{Fore.RESET}"
GITHUB_REPO = "https://github.com/ZORO2045/Tar-X-Archiver"
GITHUB_BRANCH = "main"

def print_banner():
    banner_text = text2art("TAR-X", font='tarty1')
    print(Fore.GREEN + banner_text)
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    formatted_time = now.strftime("%H:%M:%S")
    print(Fore.MAGENTA + f"Date: {formatted_date}   Time: {formatted_time}")
    print(Fore.MAGENTA + f"Developed by: ፚ Ꭷ Ꮢ Ꭷ ❥")
    print(Fore.CYAN + "_" * 75)
    print(f"{Fore.YELLOW}Tool:{Fore.RESET} {TOOL_NAME} v{TOOL_VERSION}")
    print(f"{Fore.YELLOW}Developer:{Fore.RESET} {DEVELOPER}")
    print(f"{Fore.YELLOW}Description:{Fore.RESET} {DESCRIPTION}")
    print("-" * 75 + Fore.RESET)

def get_input_path():
    while True:
        input_path = input(f"{Style.BRIGHT}{Fore.BLUE}Enter the path of the file to archive:{Fore.RESET}{Style.RESET_ALL} ").strip()
        if not input_path:
            print(f"{Fore.RED}Error: Input path cannot be empty.{Fore.RESET}", file=sys.stderr)
            continue
        if not os.path.exists(input_path):
            print(f"{Fore.RED}Error: The file '{input_path}' does not exist.{Fore.RESET}", file=sys.stderr)
            continue
        return input_path

def get_output_path():
    while True:
        output_path = input(f"{Style.BRIGHT}{Fore.BLUE}Enter the path for the output archive (.tar):{Fore.RESET}{Style.RESET_ALL} ").strip()
        if not output_path:
            print(f"{Fore.RED}Error: Output path cannot be empty.{Fore.RESET}", file=sys.stderr)
            continue
        if not output_path.lower().endswith(".tar"):
            print(f"{Fore.RED}Error: Output path must end with {Style.BRIGHT}{Fore.BLUE}.tar{Fore.RESET}{Style.RESET_ALL} extension.{Fore.RESET}",
                  file=sys.stderr)
            continue
        return output_path

def check_overwrite(output_path):
    if os.path.exists(output_path):
        while True:
            overwrite = input(f"{Fore.YELLOW}File '{output_path}' already exists. Overwrite? (y/n):{Fore.RESET} ").strip().lower()
            if overwrite == 'y':
                return True
            elif overwrite == 'n':
                return False
            else:
                print(f"{Fore.RED}Invalid input. Please enter 'y' or 'n'.{Fore.RESET}", file=sys.stderr)
    return True

def compress_with_posix_tar_no_compression(file_path, output_path):
    try:
        temp_dir = os.path.dirname(file_path)
        command = ['tar', 'cvf', output_path, '-C', temp_dir, os.path.basename(file_path)]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.stderr:
            if "Removing leading `/' from member names" in result.stderr:
                print(
                    f"{Fore.GREEN}Successfully created archive file {Fore.MAGENTA}{output_path}{Fore.RESET}{Fore.GREEN}. (Warning: Leading slashes were removed from filenames){Fore.RESET}")
            else:
                print(f"{Fore.RED}Error during tar: {result.stderr}{Fore.RESET}", file=sys.stderr)
        else:
            print(
                f"{Fore.GREEN}Successfully created archive file {Fore.MAGENTA}{output_path}{Fore.RESET}{Fore.GREEN}.{Fore.RESET}")
    except FileNotFoundError:
        print(f"{Fore.RED}Error: tar command not found. Ensure tar is installed and available in your PATH.{Fore.RESET}",
              file=sys.stderr)

def update_self():
    try:
        print(f"{Fore.YELLOW}Cloning the latest version...{Fore.RESET}")

        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        temp_dir = tempfile.mkdtemp()

        clone_command = ["git", "clone", "-b", GITHUB_BRANCH, GITHUB_REPO, temp_dir]
        subprocess.run(clone_command, check=True, capture_output=True)

        print(f"{Fore.GREEN}Download Complete.{Fore.RESET}")
        print(f"{Fore.YELLOW}Replacing current directory content...{Fore.RESET}")
        
        for item in os.listdir(script_dir):
           item_path = os.path.join(script_dir, item)
           if item_path != script_path:
             if os.path.isfile(item_path):
                os.remove(item_path)
             elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

        for item in os.listdir(temp_dir):
          item_path = os.path.join(temp_dir, item)
          dest_path = os.path.join(script_dir, item)
          if os.path.isfile(item_path):
            shutil.copy2(item_path, dest_path)
          elif os.path.isdir(item_path):
             shutil.copytree(item_path, dest_path)
        
        print(f"{Fore.GREEN}Script updated successfully.{Fore.RESET}")
        print(f"{Fore.YELLOW}Please restart the application.{Fore.RESET}")
        shutil.rmtree(temp_dir)
        sys.exit(0)

    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error during git clone: {e.stderr.decode('utf-8')}{Fore.RESET}", file=sys.stderr)
        if temp_dir:
            shutil.rmtree(temp_dir)
    except OSError as e:
        print(f"{Fore.RED}Error replacing directory content: {e}{Fore.RESET}", file=sys.stderr)
        if temp_dir:
            shutil.rmtree(temp_dir)
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred during update: {e}{Fore.RESET}", file=sys.stderr)
        if temp_dir:
            shutil.rmtree(temp_dir)

def check_for_updates():
        while True:
            update_choice = input(f"{Fore.BLUE}Do you want to update? (y/n):{Fore.RESET} ").strip().lower()
            if update_choice == 'y':
                update_self()
                break
            elif update_choice == 'n':
                print(f"{Fore.YELLOW}Update cancelled.{Fore.RESET}")
                break
            else:
                print(f"{Fore.RED}Invalid input. Please enter 'y' or 'n'.{Fore.RESET}", file=sys.stderr)

def main_menu():
    while True:
        print(f"\n{Fore.YELLOW}Choose an option:{Fore.RESET}")
        print(f"{Fore.BLUE}1.{Fore.RESET} Create Archive")
        print(f"{Fore.BLUE}2.{Fore.RESET} Check for Updates")
        print(f"{Fore.RED}3.{Fore.RESET} Exit")
        choice = input(f"{Fore.YELLOW}Enter your choice (1, 2, or 3): {Fore.RESET}").strip()

        if choice == '1':
             input_file = get_input_path()
             output_file = get_output_path()

             if not check_overwrite(output_file):
                 continue

             compress_with_posix_tar_no_compression(input_file, output_file)

             while True:
                  repeat = input(f"{Fore.BLUE}Create another archive? (y/n): {Fore.RESET}").strip().lower()
                  if repeat == 'y':
                      break
                  elif repeat == 'n':
                     break
                  else:
                      print(f"{Fore.RED}Invalid input. Please enter 'y' or 'n'.{Fore.RESET}", file=sys.stderr)

        elif choice == '2':
            check_for_updates()
        elif choice == '3':
            print(f"{Fore.CYAN}Goodbye 👋{Fore.RESET}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}Invalid choice. Please enter 1, 2, or 3.{Fore.RESET}", file=sys.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"{Style.BRIGHT}Version: {TOOL_VERSION}{Fore.RESET}{Style.RESET_ALL}",
        help="show program's version number and exit."
    )
    args = parser.parse_args()
    print_banner()
    main_menu()
