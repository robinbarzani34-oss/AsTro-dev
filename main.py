from src.imports import *
from src.utils import *

CREATE_TEMP_EMAIL_URL = "https://api.guerrillamail.com/ajax.php?f=get_email_address"
SITE_URL_1="https://doxbean.cc/@nicram"
SITE_URL_2 = "https://nicram-code.github.io/"

colorama.init()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    reset = "\033[0m"
    print(
        "\033[38;2;255;50;50m"   + " /$$$$$$$$                                      /$$      /$$           /$$ /$$        /$$$$$$  /$$ /$$" + "\n" +
        "\033[38;2;255;80;80m"   + "|__  $$__/                                     | $$$    /$$$          |__/| $$       /$$__  $$| $$|__/" + "\n" +
        "\033[38;2;255;110;110m" + "   | $$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$$$  /$$$$  /$$$$$$  /$$| $$      | $$  \__/| $$ /$$" + "\n" +
        "\033[38;2;255;140;140m" + "   | $$ /$$__  $$| $$_  $$_  $$ /$$__  $$      | $$ $$/$$ $$ |____  $$| $$| $$      | $$      | $$| $$" + "\n" +
        "\033[38;2;255;170;170m" + "   | $$| $$$$$$$$| $$ \ $$ \ $$| $$  \ $$      | $$  $$$| $$  /$$$$$$$| $$| $$      | $$      | $$| $$" + "\n" +
        "\033[38;2;255;200;200m" + "   | $$| $$_____/| $$ | $$ | $$| $$  | $$      | $$\  $ | $$ /$$__  $$| $$| $$      | $$    $$| $$| $$" + "\n" +
        "\033[38;2;255;225;225m" + "   | $$|  $$$$$$$| $$ | $$ | $$| $$$$$$$/      | $$ \/  | $$|  $$$$$$$| $$| $$      |  $$$$$$/| $$| $$" + "\n" +
        "\033[38;2;255;240;240m" + "   |__/ \_______/|__/ |__/ |__/| $$____/       |__/     |__/ \_______/|__/|__/       \______/ |__/|__/" + "\n" +
        "\033[38;2;255;248;248m" + "                               | $$                                                                   " + "\n" +
        "\033[38;2;255;252;252m" + "                               | $$                                                                   " + "\n" +
        "\033[38;2;255;255;255m" + "                               |__/                                                                   " + "\n" +
        "\033[38;2;255;255;255m" + "    ───────────────────────────────────────────────────────────────────────────────────────────────" +
        reset + "\n"
    )

def choose_mode():
    print(
        f"\n{Fore.RED}[{Style.RESET_ALL}1{Fore.RED}]{Style.RESET_ALL} Create a new temporary email address\n"
        f"{Fore.RED}[{Style.RESET_ALL}2{Fore.RED}]{Style.RESET_ALL} View existing email addresses // SOON\n"
        f"{Fore.RED}[{Style.RESET_ALL}3{Fore.RED}]{Style.RESET_ALL} Help\n"
        f"{Fore.RED}[{Style.RESET_ALL}S{Fore.RED}]{Style.RESET_ALL} Visit my website\n"
        f"{Fore.RED}[{Style.RESET_ALL}99{Fore.RED}]{Style.RESET_ALL} Exit"
    )

def create_email():
    r = requests.get(CREATE_TEMP_EMAIL_URL)
    if r.status_code == 200:
        data = r.json()
        email = data['email_addr']
        sid = data['sid_token']
        print(f"\n{Fore.RED}Your new temporary email address is: {Fore.GREEN}{email}{Style.RESET_ALL}")
        print(f"{Fore.RED}Your sid_token is: {Fore.GREEN}{sid}{Style.RESET_ALL}")
        open_inbox_after_creation(email, sid)
        return email, sid
    else:
        print(f"{Fore.RED}Error creating email address. Please try again.{Style.RESET_ALL}")
        input(f"{Fore.RED}Press Enter to return to the main menu...{Style.RESET_ALL}")
        clear()

def open_inbox(email, sid):
    clear()
    banner()
    print(f"{Fore.RED}Inbox for: {Fore.GREEN}{email}{Style.RESET_ALL}")
    print(f"{Fore.RED}{'─' * 60}{Style.RESET_ALL}\n")
    print(f"{Fore.RED}[*]{Style.RESET_ALL} Waiting for new emails... {Fore.RED}(Ctrl+C to go back){Style.RESET_ALL}\n")

    seen = set()  

    try:
        while True:
            inbox = requests.get(
                f"https://api.guerrillamail.com/ajax.php?f=get_email_list&offset=0&sid_token={sid}"
            ).json().get("list", [])

            if not inbox:
                print(f"\r{Fore.RED}[*]{Style.RESET_ALL} Inbox is empty...", end="")
            else:
                for msg in inbox:
                    if msg['mail_id'] not in seen:
                        seen.add(msg['mail_id'])
                        print(f"{Fore.RED}[ From    ]{Style.RESET_ALL} {msg['mail_from']}")
                        print(f"{Fore.RED}[ Subject ]{Style.RESET_ALL} {msg['mail_subject']}")
                        print(f"{Fore.RED}[ Date    ]{Style.RESET_ALL} {msg['mail_date']}")
                        print(f"{Fore.RED}[ ID      ]{Style.RESET_ALL} {msg['mail_id']}")
                        print(f"{Fore.RED}{'─' * 60}{Style.RESET_ALL}")

            time.sleep(5) 
    except KeyboardInterrupt:
        
        clear()
        main()

def open_inbox_after_creation(email, sid):
    open_inbox_input = input(f"\n{Fore.RED}Do you want to open the inbox for this email address now? (y/n): {Style.RESET_ALL}")
    if open_inbox_input.lower() == "y":
        open_inbox(email, sid)
    elif open_inbox_input.lower() == "n":
        clear()
        main()
    else:
        print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

def view_emails():
    clear()
    banner()
    print(f"\n{Fore.RED}This feature is coming soon!{Style.RESET_ALL}")
    input(f"{Fore.RED}Press Enter to return to the main menu...{Style.RESET_ALL}")
    clear()
    main()
    pass

def open_site():
    webbrowser.open(SITE_URL_1)
    webbrowser.open(SITE_URL_2)

def help_menu():
    banner()
    print(f"\n{Fore.RED}{'─' * 40}{Style.RESET_ALL}")
    print(f"  {Fore.RED}[{Style.RESET_ALL} Help Center {Fore.RED}]{Style.RESET_ALL}")
    print(f"{Fore.RED}{'─' * 40}{Style.RESET_ALL}\n")

    print(f"  {Fore.RED}[{Style.RESET_ALL}1{Fore.RED}]{Style.RESET_ALL} Create new email")
    print(f"      Generate a random temporary email address\n")

    print(f"  {Fore.RED}[{Style.RESET_ALL}2{Fore.RED}]{Style.RESET_ALL} View existing emails")
    print(f"      Check inbox of a previously created address\n")

    print(f"  {Fore.RED}[{Style.RESET_ALL}3{Fore.RED}]{Style.RESET_ALL} Help")
    print(f"      Show this help menu\n")

    print(f"  {Fore.RED}[{Style.RESET_ALL}99{Fore.RED}]{Style.RESET_ALL} Exit")
    print(f"      Quit the program\n")

    print(f"{Fore.RED}{'─' * 40}{Style.RESET_ALL}")
    print(f"  {Fore.RED}[{Style.RESET_ALL}*{Fore.RED}]{Style.RESET_ALL} Powered by Guerrilla Mail API")
    print(f"  {Fore.RED}[{Style.RESET_ALL}*{Fore.RED}]{Style.RESET_ALL} Emails expire after ~1h")
    print(f"  {Fore.RED}[{Style.RESET_ALL}*{Fore.RED}]{Style.RESET_ALL} No registration required")
    print(f"{Fore.RED}{'─' * 40}{Style.RESET_ALL}\n")
    input(f"{Fore.RED}Press Enter to return to the main menu...{Style.RESET_ALL}")
    clear()
    main()

def main():
    clear()
    banner()
    choose_mode()
    hostname = check_platform()

    while True:
        choice = input(f"\n{Fore.RED}{hostname}@tempmail >  {Style.RESET_ALL}")
        if choice == "1":
            clear()
            banner()
            create_email()
        elif choice == "2":
            view_emails()
        elif choice == "3":
            help_menu()
        elif choice.lower() == "s":
            open_site()
        elif choice == "99":
            print(f"\n{Fore.RED}Exiting...{Style.RESET_ALL}")
            time.sleep(0.3)
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    clear()
    main()