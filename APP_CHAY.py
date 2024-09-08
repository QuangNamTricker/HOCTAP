import time
import os
import requests
from colorama import Fore, Style, init
import webbrowser

# Khởi tạo colorama
init(autoreset=True)

#====================================================================================================================================================================
def print_colored_text(text, color, delay=0):
    print(color + text + Style.RESET_ALL)
    time.sleep(delay)

#====================================================================================================================================================================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#====================================================================================================================================================================
def execute_code_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        exec(response.text)
    except requests.exceptions.RequestException as e:
        print_colored_text(f"Không thể tải mã từ URL: {e}", Fore.RED)

#====================================================================================================================================================================
def choose_teacher(teachers):
    while True:
        clear_screen()
        print_colored_text("""
+---------------------------------------------------------------+
|                                                               |
|     _____               _                 _     _     _       |
|    |_   _|__  __ _  ___| |__   ___ _ __  | |   (_)___| |_     |
|      | |/ _ \/ _` |/ __| '_ \ / _ \ '__| | |   | / __| __|    |
|      | |  __/ (_| | (__| | | |  __/ |    | |___| \__ \ |_     |
|      |_|\___|\__,_|\___|_| |_|\___|_|    |_____|_|___/\__|    |
|                                                               |
+---------------------------------------------------------------+
Chọn thầy cô dạy (nhập 0 để quay lại):
""", Fore.CYAN)

        for idx, teacher in enumerate(teachers, start=1):
            print_colored_text(f"{idx}. {teacher[0]}", Fore.GREEN)

        try:
            choice = int(input(Fore.YELLOW + "Nhập lựa chọn của bạn: "))
            if choice == 0:
                return  # Quay lại màn hình trước
            elif 1 <= choice <= len(teachers):
                clear_screen()
                print_colored_text(f"Đang thực thi mã từ {teachers[choice-1][0]}", Fore.GREEN)
                execute_code_from_url(teachers[choice-1][1])
                input(Fore.YELLOW + "Nhấn Enter để tiếp tục...")  # Chờ người dùng nhấn Enter trước khi quay lại menu
            else:
                print_colored_text("Lựa chọn không hợp lệ.", Fore.RED)
        except ValueError:
            print_colored_text("Lựa chọn không hợp lệ. Vui lòng nhập số.", Fore.RED)

#====================================================================================================================================================================
#====================================================================================================================================================================
#====================================================================================================================================================================
#====================================================================================================================================================================
#====================================================================================================================================================================
def math_mode():
    teachers = [
    ("THẦY NGUYỄN TIẾN ĐẠT", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/TOAN/NTD.py"),
    ("THẦY ĐẶNG THÀNH NAM - VTED", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/TOAN/DTN.py"),
    ("THẦY TRỊNH ĐÌNH THÀNH - DPAD", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/TOAN/TDT_DPAD.py"),
    ("THẦY NGUYỄN ĐĂNG ÁI - TDM", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/TOAN/NDA_TDM.py"),
    ("TRỊNH ĐỊNH TRIỂN - LIM C", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/TOAN/TDT_LIMC.py"),
    ("SHIPER TOÁN", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/TOAN/SPT.py"),
    ("THẦY NGUYỄN PHAN TIẾN", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/TOAN/NPT.py")

    ]
    choose_teacher(teachers)

#====================================================================================================================================================================
def literature_mode():
    teachers = [
    ("THẦY PHẠM MINH NHẬT", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Van/PMH.py"),
    ("THƯỞNG THỨC SÁCH", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Van/TTS.py"),
    ("CÔ SƯƠNG MAI", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Van/SM.py")
    ]
    choose_teacher(teachers)

#====================================================================================================================================================================
def english_mode():
    teachers = [
    ("CÔ TRANG ANH", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Anh/TA.py"),
    ("CÔ MAI PHƯƠNG", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Anh/MP.py"),
    ("CÔ PHẠM LIỄU", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Anh/PL.py")
    ]
    choose_teacher(teachers)

#====================================================================================================================================================================
def physics_mode():
    teachers = [
    ("THẦY VŨ TUẤN ANH", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Ly/VTA.py"),
    ("THẦY VŨ NGỌC ANH", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Ly/VNA.py"),
    ("THẦY CHU VĂN BIÊN", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Ly/CVB.py"),
    ("THẦY BÙI XUÂN ĐẠT", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Ly/BXD.py"),
    ("THẦY NGUYỄN ĐĂNG ÁI - TDM", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Ly/NDA_TDM.py"),
    ("THẦY VŨ HOÀNG QUÂN", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Ly/VHQ.py"),
    ("THẦY ĐỖ NGỌC HÀ", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Ly/DNH.py")

    ]
    choose_teacher(teachers)

#====================================================================================================================================================================
def chemistry_mode():
    teachers = [
    ("THẦY PHẠM VĂN THUẬN", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Hoa/PVThuan.py"),
    ("THẦY NGUYỄN ANH PHONG - NAP", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Hoa/NAP.py"),
    ("THẦY PHẠM THẮNG - TYHH", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Hoa/PT-TYHH.py"),
    ("THẦY PHẠM VĂN TRỌNG", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Hoa/PVTrong.py"),
    ("THÂN THỊ LIÊN", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Hoa/TTL.py"),
    ("TEAM PHẾ", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Hoa/TP.py")
    ]
    choose_teacher(teachers)

#====================================================================================================================================================================
def biology_mode():
    teachers = [
            ("THẦY PHAN KHÁC NGHỆ", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Sinh/PKN.py"),
            ("THẦY TRƯƠNG CÔNG KIÊN", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Sinh/TCK.py")
    ]
    choose_teacher(teachers)

#====================================================================================================================================================================
def history_mode():
    teachers = [
            ("THẦY PHAN KHÁC NGHỆ", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Sinh/PKN.py"),
            ("THẦY TRƯƠNG CÔNG KIÊN", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Sinh/TCK.py")
    ]
    choose_teacher(teachers)

#====================================================================================================================================================================
def geography_mode():
    teachers = [
            ("THẦY PHAN KHÁC NGHỆ", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Sinh/PKN.py"),
            ("THẦY TRƯƠNG CÔNG KIÊN", "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/MON_HOC/Sinh/TCK.py")
    ]
    choose_teacher(teachers)

#====================================================================================================================================================================
#====================================================================================================================================================================
#====================================================================================================================================================================
def chrome_extensions():
    clear_screen()
    print_colored_text("""+--------------------------------------------------------------+
|                                                              |
|    _______  _______ _____ _   _ ____ ___ ___  _   _ ____     |
|   | ____\ \/ /_   _| ____| \ | / ___|_ _/ _ \| \ | / ___|    |
|   |  _|  \  /  | | |  _| |  \| \___ \| | | | |  \| \___ \    |
|   | |___ /  \  | | | |___| |\  |___) | | |_| | |\  |___) |   |
|   |_____/_/\_\ |_| |_____|_| \_|____/___\___/|_| \_|____/    |
|                                                              |
+--------------------------------------------------------------+\nChọn loại Extension Chrome:""", Fore.CYAN)
    
    options = [
        ("1. Extension của TQN", Fore.GREEN),
        ("2. Extension có sẵn trên Chrome Web Store", Fore.GREEN),
    ]
    
    for option, color in options:
        print_colored_text(option, color)
    
    try:
        choice = int(input(Fore.YELLOW + "Nhập số để chọn loại extension (1-2): "))
        
        if choice == 1:
            custom_extensions()
        elif choice == 2:
            standard_extensions()
        else:
            print_colored_text("Lựa chọn không hợp lệ. Vui lòng nhập số 1 hoặc 2.", Fore.RED)
    except ValueError:
        print_colored_text("Lựa chọn không hợp lệ. Vui lòng nhập số.", Fore.RED)

    input(Fore.YELLOW + "Nhấn Enter để tiếp tục...")

def custom_extensions():
    clear_screen()
    print_colored_text("""+--------------------------------------------------------------+
|                                                              |
|    _______  _______ _____ _   _ ____ ___ ___  _   _ ____     |
|   | ____\ \/ /_   _| ____| \ | / ___|_ _/ _ \| \ | / ___|    |
|   |  _|  \  /  | | |  _| |  \| \___ \| | | | |  \| \___ \    |
|   | |___ /  \  | | | |___| |\  |___) | | |_| | |\  |___) |   |
|   |_____/_/\_\ |_| |_____|_| \_|____/___\___/|_| \_|____/    |
|                                                              |
+--------------------------------------------------------------+\nCác Extension TQN Tạo:""", Fore.CYAN)
    
    extensions = [
        ("1. C3C-Dev_C03.rar", "https://drive.google.com/file/d/1Mw8rhalUJLr4Rso01S6LnbvS3XORYvcN/view?usp=drive_link", "https://tqn-tool.blogspot.com/p/huong-dan-su-dung-tien-ich-mo-rong.html"),  # Thay đổi URL cho các extension của bạn
        ("2. Khoá_Chrome.zip", "https://drive.google.com/file/d/1wWIHM8Tj-GusFcrhIF7iU1m7onvGH7uU/view?usp=drive_link", "https://tqn-tool.blogspot.com/p/huong-dan-su-dung-extension.html"),
        ("3. Chrome_lock_By_TQN-TOOL.zip", "https://drive.google.com/file/d/1ri99ArmaguI1NSgrwLPTawk9eGUEilxt/view?usp=drive_link", "https://tqn-tool.blogspot.com/p/huong-dan-su-dung-extension_4.html"),
        # Thêm các extension khác của bạn vào đây
    ]
    
    for name, _, _ in extensions:
        print_colored_text(name, Fore.GREEN)
    
    try:
        choice = int(input(Fore.YELLOW + "Nhập số để chọn extension (1-3): "))
        if 1 <= choice <= len(extensions):
            download_url, guide_url = extensions[choice - 1][1:]
            print_colored_text(f"Mở các tab cho {extensions[choice - 1][0]}", Fore.GREEN)
            webbrowser.open_new_tab(download_url)
            webbrowser.open_new_tab(guide_url)
        else:
            print_colored_text("Lựa chọn không hợp lệ. Vui lòng nhập số đúng.", Fore.RED)
    except ValueError:
        print_colored_text("Lựa chọn không hợp lệ. Vui lòng nhập số.", Fore.RED)

def standard_extensions():
    clear_screen()
    print_colored_text("""+--------------------------------------------------------------+
|                                                              |
|    _______  _______ _____ _   _ ____ ___ ___  _   _ ____     |
|   | ____\ \/ /_   _| ____| \ | / ___|_ _/ _ \| \ | / ___|    |
|   |  _|  \  /  | | |  _| |  \| \___ \| | | | |  \| \___ \    |
|   | |___ /  \  | | | |___| |\  |___) | | |_| | |\  |___) |   |
|   |_____/_/\_\ |_| |_____|_| \_|____/___\___/|_| \_|____/    |
|                                                              |
+--------------------------------------------------------------+\nCác Extension Chrome Hữu Ích:""", Fore.CYAN)
    
    extensions = [
        ("0. Đang Cập Nhật", ""),
    ]
    
    for name, _ in extensions:
        print_colored_text(name, Fore.GREEN)
    
    try:
        choice = int(input(Fore.YELLOW + "Nhập số để chọn extension (1-11): "))
        if 1 <= choice <= len(extensions):
            url = extensions[choice - 1][1]
            print_colored_text(f"Mở {extensions[choice - 1][0]}", Fore.GREEN)
            webbrowser.open(url)
        else:
            print_colored_text("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 11.", Fore.RED)
    except ValueError:
        print_colored_text("Lựa chọn không hợp lệ. Vui lòng nhập số.", Fore.RED)

#====================================================================================================================================================================
from pynput import keyboard
from colorama import init, Fore, Style
import os
import webbrowser

init()
options = [
    ("""+---------------------------------------------------------------+
  |                                                               |
  |      ____ ___  _   _ _____  _    ____ _____   _   _ ____      |
  |     / ___/ _ \| \ | |_   _|/ \  / ___|_   _| | | | / ___|     |
  |    | |  | | | |  \| | | | / _ \| |     | |   | | | \___ \     |
  |    | |__| |_| | |\  | | |/ ___ \ |___  | |   | |_| |___) |    |
  |     \____\___/|_| \_| |_/_/   \_\____| |_|    \___/|____/     |
  |                                                               |
  |    Lưu Ý: Sử Dụng Nút Lên Xuống Để Chọn                       |
  +---------------------------------------------------------------+""", None),
    ("Facebook", "https://facebook.com/tuquangnam07"),
    ("YouTube", "https://youtube.com/@TuQuangNam"),
    ("GitHub", "https://github.com/tuquangnam007"),
    ("Instagram", "https://www.instagram.com/tuquangnam07"),
    ("TikTok", "https://tiktok.com/@tuquangnam07")
]

selected = 1

def display_menu(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, (name, _) in enumerate(options):
        if i == selected:
            print(Fore.BLACK + Style.BRIGHT + f"> {name}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"  {name}" + Style.RESET_ALL)

def on_press(key):
    global selected
    try:
        if key == keyboard.Key.up and selected > 0:
            selected -= 1
            display_menu()
        elif key == keyboard.Key.down and selected < len(options) - 1:
            selected += 1
            display_menu()
        elif key == keyboard.Key.enter:
            webbrowser.open(options[selected][1])  # Sử dụng trình duyệt mặc định
            return False  # Dừng listener sau khi chọn
    except AttributeError:
        pass

def contact_us():    
    display_menu()
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Chờ cho đến khi listener dừng

    print(Fore.CYAN + "Chương trình đã dừng.")  # Thông báo khi chương trình dừng

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, (name, _) in enumerate(options):
        if i == selected:
            print(Fore.BLACK + Style.BRIGHT + f"> {name}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"  {name}" + Style.RESET_ALL)


#====================================================================================================================================================================
def tools():
    clear_screen()
    print_colored_text("""
+----------------------------------------------------------------------------+
|                                                                            |
|    __  __    _    ___ _   _ _____ _____ _   _    _    _   _  ____ _____    |
|   |  \/  |  / \  |_ _| \ | |_   _| ____| \ | |  / \  | \ | |/ ___| ____|   |
|   | |\/| | / _ \  | ||  \| | | | |  _| |  \| | / _ \ |  \| | |   |  _|     |
|   | |  | |/ ___ \ | || |\  | | | | |___| |\  |/ ___ \| |\  | |___| |___    |
|   |_|  |_/_/   \_\___|_| \_| |_| |_____|_| \_/_/   \_\_| \_|\____|_____|   |
|                                                                            |
+----------------------------------------------------------------------------+
""", Fore.CYAN)


    input(Fore.YELLOW + "Nhấn Enter để quay lại trang chủ!")

#====================================================================================================================================================================
def notification():
    clear_screen()
    print_colored_text("""+----------------------------------------------------------------------+
|                                                                      |
|    _   _  ___ _____ ___ _____ ___ ____    _  _____ ___ ___  _   _    |
|   | \ | |/ _ \_   _|_ _|  ___|_ _/ ___|  / \|_   _|_ _/ _ \| \ | |   |
|   |  \| | | | || |  | || |_   | | |     / _ \ | |  | | | | |  \| |   |
|   | |\  | |_| || |  | ||  _|  | | |___ / ___ \| |  | | |_| | |\  |   |
|   |_| \_|\___/ |_| |___|_|   |___\____/_/   \_\_| |___\___/|_| \_|   |
|                                                                      |
+----------------------------------------------------------------------+""", Fore.CYAN)

    # URL chứa mã nguồn bạn muốn tải
    url = "https://raw.githubusercontent.com/QuangNamTricker/HOCTAP/main/THONG_BAO/thongbao.py"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        code = response.text
        
        # In mã nguồn
        print_colored_text("Mã nguồn từ URL:", Fore.GREEN)
        print_colored_text(code, Fore.WHITE)
        
    except requests.exceptions.RequestException as e:
        print_colored_text(f"Không thể tải mã từ URL: {e}", Fore.RED)

    input(Fore.YELLOW + "Nhấn Enter để tiếp tục...")

#====================================================================================================================================================================
def exit_application():
    print_colored_text("Exiting... Goodbye!", Fore.RED)

#====================================================================================================================================================================
def main():
    tool_info = [
        "************************************",
        "*       WELCOME TO TQN-TOOL        *",
        "*      Author: Từ Quang Nam        *",
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

    menu_options = [
        ("1. Toán", Fore.GREEN, math_mode),
        ("2. Văn", Fore.GREEN, literature_mode),
        ("3. Anh", Fore.GREEN, english_mode),
        ("4. Lý", Fore.GREEN, physics_mode),
        ("5. Hoá", Fore.GREEN, chemistry_mode),
        ("6. Sinh", Fore.GREEN, biology_mode),
        ("7. Sử", Fore.GREEN, history_mode),
        ("8. Địa", Fore.GREEN, geography_mode),


        ("9. Thông Báo", Fore.CYAN, notification),
        ("10. Tool", Fore.CYAN, tools),
        ("11. Extension Chrome Hữu Ích", Fore.CYAN, chrome_extensions),
        ("12. ConTact US", Fore.CYAN, contact_us),
        ("13. Exit", Fore.RED, exit_application)
    ]

    while True:
        clear_screen()
        for line, color in zip(tool_info, colors):
            print_colored_text(line, color)

        for option, color, action in menu_options:
            print_colored_text(option, color)

        choice = input(Fore.YELLOW + "Nhập lựa chọn của bạn (1-11): ")

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
            history_mode()
        elif choice == "8":
            geography_mode()

        elif choice == "9":
            notification()
        elif choice == "10":
            tools()
        elif choice == "11":
            chrome_extensions()
        elif choice == "12":
            contact_us()
        elif choice == "13":
            exit_application()
            break
        else:
            print_colored_text("Lựa chọn không hợp lệ. Vui lòng khởi động lại ứng dụng và thử lại.", Fore.RED)

if __name__ == "__main__":
    main()
