import webbrowser

# Danh sách bài học với tên và link YouTube tương ứng
bai_hoc = {
    1: {"ten": " - Bài giảng 1", "link": "https://www.youtube.com/watch?v=link1"},
    2: {"ten": " - Bài giảng 2", "link": "https://www.youtube.com/watch?v=link2"},
    3: {"ten": " - Bài giảng 3", "link": "https://www.youtube.com/watch?v=link3"},
    4: {"ten": " - Bài giảng 4", "link": "https://www.youtube.com/watch?v=link4"},
    5: {"ten": " - Bài giảng 5", "link": "https://www.youtube.com/watch?v=link5"},
    6: {"ten": " - Bài giảng 6", "link": "https://www.youtube.com/watch?v=link6"},
}

# Hiển thị danh sách bài học
print("Danh sách bài học:")
for key, value in bai_hoc.items():
    print(f"{key}. {value['ten']}")

# Người dùng nhập số để chọn bài học
chon = int(input("Nhập số để chọn bài học: "))

# Kiểm tra lựa chọn của người dùng và mở link tương ứng
if chon in bai_hoc:
    webbrowser.open(bai_hoc[chon]["link"])
    print(f"Đang mở {bai_hoc[chon]['ten']} trên YouTube...")
else:
    print("Lựa chọn không hợp lệ!")
