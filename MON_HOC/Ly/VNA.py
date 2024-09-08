import webbrowser
from colorama import Fore, init

# Khởi tạo colorama
init(autoreset=True)

# Danh sách bài học với tên và link YouTube tương ứng
bai_hoc = {

    "Bài 0101: Nhiệt độ - Thang nhiệt độ - Nhiệt kế": "https://www.youtube.com/playlist?list=PLKoTDnp1l4EBR7MupTg8Hk6JxI3-tM8_7",
    "Bài 0102: Sự chuyển thể của chất": "https://www.youtube.com/playlist?list=PLKoTDnp1l4EAFWto0pe3_P_EX54AIgEl0",
    "Bài 0103: Mô hình động học phân tử": "https://www.youtube.com/playlist?list=PLKoTDnp1l4EBugmiE6g2hg3vMQUFuhD89",
    "Bài 0104: Nội năng và Định luật 1 của nhiệt động lực học": "https://www.youtube.com/playlist?list=PLKoTDnp1l4EAlUwSRTXBbLqwxmWaW84R0",
    "[TEST] - Đề kiểm tra bắt buộc - Số 1": "https://www.youtube.com/watch?v=sKfJJNh5k_0&feature=youtu.be",
    "Bài 0105: Động cơ nhiệt": "https://www.youtube.com/playlist?list=PLKoTDnp1l4ECgtC_K2lXapebYbtJ4jcUy",
    "Bài 0106: Nhiệt dung riêng": "https://www.youtube.com/playlist?list=PLKoTDnp1l4EAO4-L7WMD-OrezlRcW5BFx",
    "Luyện tập số 01": "https://www.youtube.com/watch?v=8queN7OzOh4",
    "Bài 0107: Nhiệt nóng chảy riêng": "https://www.youtube.com/playlist?list=PLKoTDnp1l4EBkLipJlc-BkWP_BT0SNYTS",
    "Bài 0108: Nhiệt hóa hơi P1": "https://www.youtube.com/watch?v=lu8owF18r8A",
    "Bài 0108: Nhiệt hóa hơi P2": "https://www.youtube.com/watch?v=2CsLAiCjSnI",
    "Tăng cường nhiệt học": "https://www.youtube.com/playlist?list=PLKoTDnp1l4EC4Evf6snQ6CNO_uRcYipzA",


    "Bài 0201 - Mô hình động học phân tử khí": "https://www.youtube.com/playlist?list=PLKoTDnp1l4EA2tIrc4x75ZflNVxl83w7V",
    "Bài 0202 - Định luật Boyle về quá trình đẳng nhiệt": "https://www.youtube.com/playlist?list=PL_9M52vXyLojKwJf4xclUGowdNki35rDU",
    "Luyện tập các dạng toán Áp Suất Chất Lỏng và Chất Khí": "https://www.youtube.com/playlist?list=PLKoTDnp1l4EAqd5TYZO_LnI0vJiLtN7TE",    
    "Bài 0203 - Định luật Charles về quá trình đẳng áp": "https://www.youtube.com/playlist?list=PLKoTDnp1l4EDRBJz6tQ92s1EKhsuAqXsL",
    "Bài 0204 - Phương trình trạng thái của khí lý tưởng": "https://www.youtube.com/playlist?list=PLKoTDnp1l4ECI5GodX4I_wfZN3YOC9aiw",
    "Luyện tập Đồ thị trạng thái khí Lý Tưởng Dùng Phương Trình Clapeyron": "https://www.youtube.com/watch?v=GnJlBv22xwQ",
    "CHỮA 30 CÂU CƠ BẢN PHƯƠNG TRÌNH TRẠNG THÁI KHÍ LÍ TƯỞNG": "https://www.youtube.com/watch?v=193CnBLzeG8",
    "DẠNG 2 SỬ DỤNG PT KHÍ LÝ TƯỞNG": "https://www.youtube.com/watch?v=XWMQG8a1aJQ",
    "DẠNG 3 NGUYÊN LÝ PASCAL": "https://www.youtube.com/watch?v=BEm4FRlFHV8",
    "Bài 0205: Áp suất khí và động năng trung bình phân tử khí": "https://drive.google.com/file/d/1y_1-VXMJM--nCVztxTjqk1-M9N4EG0ow/view",


    "Đại cương về từ trường": "https://www.youtube.com/watch?v=EV7_0rtJBQs",
    "Tương tác từ và cảm ứng từ": "https://www.youtube.com/watch?v=tYOM34kWDd4",
    "Luyện tập quy tắc bàn tay trái": "https://www.youtube.com/watch?v=SspExvSpdVA&feature=youtu.be",


    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",

    "Đang Upate": "None"
}

# Tạo danh sách bài học với số tự động
bai_hoc_voi_so = {i+1: {"ten": ten, "link": link} for i, (ten, link) in enumerate(bai_hoc.items())}

# Hiển thị danh sách bài học với màu sắc
print(Fore.CYAN + "Danh sách bài học:")
for key, value in bai_hoc_voi_so.items():
    print(f"{Fore.YELLOW}{key}. {value['ten']}")

# Người dùng nhập số để chọn bài học
chon = int(input(Fore.GREEN + "Nhập số để chọn bài học: "))

# Kiểm tra lựa chọn của người dùng và mở link tương ứng
if chon in bai_hoc_voi_so:
    webbrowser.open(bai_hoc_voi_so[chon]["link"])
    print(Fore.BLUE + f"Đang mở {bai_hoc_voi_so[chon]['ten']} trên YouTube...")
else:
    print(Fore.RED + "Lựa chọn không hợp lệ!")
