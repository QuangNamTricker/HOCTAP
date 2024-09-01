import time
import os
import requests
import webbrowser
from colorama import Fore, Style, init

# Khởi tạo colorama
init(autoreset=True)

def print_colored_text(text, color, delay=0.1):
    print(color + text + Style.RESET_ALL)
    time.sleep(delay)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def execute_code_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        exec(response.text)
    except requests.exceptions.RequestException as e:
        print_colored_text(f"Không thể tải mã từ URL: {e}", Fore.RED)

def choose_teacher(teachers):
    clear_screen()
    print_colored_text("Chọn thầy cô dạy:", Fore.CYAN)

    for idx, teacher in enumerate(teachers, start=1):
        print_colored_text(f"{idx}. {teacher[0]}", Fore.GREEN)

    try:
        choice = int(input(Fore.YELLOW + "Nhập lựa chọn của bạn: "))
        if 1 <= choice <= len(teachers):
            print_colored_text(f"Đang thực thi mã từ {teachers[choice-1][0]}", Fore.GREEN)
            execute_code_from_url(teachers[choice-1][1])
        else:
            print_colored_text("Lựa chọn không hợp lệ.", Fore.RED)
    except ValueError:
        print_colored_text("Lựa chọn không hợp lệ. Vui lòng nhập số.", Fore.RED)

    time.sleep(2)

def math_mode():
    clear_screen()
    print_colored_text("Chế độ Toán đã được chọn.", Fore.CYAN)
    teachers = [
        ("Thầy A", "https://raw.githubusercontent.com/QuangNamTricker/APP/main/Thay_Co/Toan/NGUY%E1%BB%84N_PHAN_TI%E1%BA%BEN.py"),
        ("Thầy B", "https://raw.githubusercontent.com/user/repo/main/thay_b.py")
    ]
    choose_teacher(teachers)

def literature_mode():
    clear_screen()
    print_colored_text("Chế độ Văn đã được chọn.", Fore.CYAN)
    teachers = [
        ("Cô C", "https://raw.githubusercontent.com/user/repo/main/co_c.py"),
        ("Cô D", "https://raw.githubusercontent.com/user/repo/main/co_d.py")
    ]
    choose_teacher(teachers)

def english_mode():
    clear_screen()
    print_colored_text("Chế độ Anh đã được chọn.", Fore.CYAN)
    teachers = [
        ("Thầy E", "https://raw.githubusercontent.com/user/repo/main/thay_e.py"),
        ("Cô F", "https://raw.githubusercontent.com/user/repo/main/co_f.py")
    ]
    choose_teacher(teachers)

def physics_mode():
    clear_screen()
    print_colored_text("Chế độ Lý đã được chọn.", Fore.CYAN)
    teachers = [
        ("Thầy G", "https://raw.githubusercontent.com/user/repo/main/thay_g.py"),
        ("Cô H", "https://raw.githubusercontent.com/user/repo/main/co_h.py")
    ]
    choose_teacher(teachers)

def chemistry_mode():
    clear_screen()
    print_colored_text("Chế độ Hóa đã được chọn.", Fore.CYAN)
    teachers = [
        ("Thầy I", "https://raw.githubusercontent.com/user/repo/main/thay_i.py"),
        ("Thầy J", "https://raw.githubusercontent.com/user/repo/main/thay_j.py")
    ]
    choose_teacher(teachers)

def biology_mode():
    clear_screen()
    print_colored_text("Chế độ Sinh đã được chọn.", Fore.CYAN)
    teachers = [
        ("Cô K", "https://raw.githubusercontent.com/user/repo/main/co_k.py"),
        ("Thầy L", "https://raw.githubusercontent.com/user/repo/main/thay_l.py")
    ]
    choose_teacher(teachers)

def contact_us():
    clear_screen()
    print_colored_text("Running Contact US...", Fore.CYAN)
    
    options = [
        ("1. Facebook", Fore.BLUE),
        ("2. Instagram", Fore.GREEN),
        ("3. GitHub", Fore.MAGENTA)
    ]
    
    for option, color in options:
        print_colored_text(option, color)
    
    try:
        n = int(input(Fore.YELLOW + "Nhập Lựa Chọn: "))
    except ValueError:
        print_colored_text("Lựa chọn không hợp lệ. Vui lòng nhập số.", Fore.RED)
        return

    if n == 1:
        print_colored_text("Đang chuyển hướng đến Facebook", Fore.GREEN)
        open_tab("https://facebook.com/tuquangnam07")
    elif n == 2:
        print_colored_text("Đang chuyển hướng đến Instagram", Fore.GREEN)
        open_tab("https://www.instagram.com/tuquangnam07")
    elif n == 3:
        print_colored_text("Đang chuyển hướng đến GitHub", Fore.GREEN)
        open_tab("https://github.com/tuquangnam07")
    else:
        print_colored_text("Lựa chọn không hợp lệ.", Fore.RED)

    time.sleep(2)

def exit_application():
    print_colored_text("Exiting... Goodbye!", Fore.RED)

def main():
    tool_info = [
        "************************************",
        "*         WELCOME TO               *",
        "*          TQN-TOOL                *",
        "************************************",
        "*  The Ultimate Utility Tool:      *",
        "*  1. Powerful and Flexible        *",
        "*  2. Easy to Use                  *",
        "*  3. Optimized for Performance    *",
        "*  4. Continuous Updates           *",
        "************************************",
        
        "************************************"
    ]

    colors = [
        Fore.GREEN,         # Dòng 1
        Fore.RED,           # Dòng 2
        Fore.BLUE,          # Dòng 3
        Fore.YELLOW,        # Dòng 4
        Fore.CYAN,          # Dòng 5
        Fore.MAGENTA,       # Dòng 6
        Fore.WHITE,         # Dòng 7
        Fore.LIGHTBLACK_EX, # Dòng 8
        Fore.LIGHTWHITE_EX, # Dòng 9
        Fore.RED            # Dòng 10
    ]

    clear_screen()
    for line, color in zip(tool_info, colors):
        print_colored_text(line, color)

    menu_options = [
        ("Please select an option to continue:", Fore.CYAN),
        ("1. Toán", Fore.GREEN),
        ("2. Văn", Fore.GREEN),
        ("3. Anh", Fore.GREEN),
        ("4. Lý", Fore.GREEN),
        ("5. Hoá", Fore.GREEN),
        ("6. Sinh", Fore.GREEN),
        ("7. ConTact US", Fore.GREEN),
        ("8. Exit", Fore.RED)
    ]

    for option, color in menu_options:
        print_colored_text(option, color)

    choice = input(Fore.YELLOW + "Enter your choice (1-8): ")
    
    if choice == "1":
        math_mode()
    elif choice == "2":
        literature_mode()
    elif choice == "3":
        english_mode()
    elif choice == "4":
        physics_mode()
    elif choice == "5":
        chemistry_mode()
    elif choice == "6":
        biology_mode()
    elif choice == "7":
        contact_us()
    elif choice == "8":
        exit_application()
    else:
        print_colored_text("Lựa chọn không hợp lệ. Vui lòng khởi động lại ứng dụng và thử lại.", Fore.RED)

if __name__ == "__main__":
    main()
