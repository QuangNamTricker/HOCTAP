import webbrowser
from colorama import Fore, init

# Khởi tạo colorama
init(autoreset=True)

# Danh sách bài học với tên và link YouTube tương ứng
bai_hoc = {
    #HÀM SỐ

    "Bài 1. Tính đơn điệu của hàm số buổi 1 ( bài tập )": "https://drive.google.com/file/d/1oixogsH6fPaILUSjrattYreSl3BhiF4s/view",
    "Bài 1. Tính đơn điệu của hàm số buổi 1 ( bài giảng )": "https://www.youtube.com/watch?v=8Y9she4u3Q0&feature=youtu.be",

    "Bài 2. Tính đơn điệu của hàm số buổi 2 ( bài tập )": "https://drive.google.com/file/d/1VNn_LvmoVzULOaLjgJjs7VPkYdaD6bjI/view",
    "Bài 2. Tính đơn điệu của hàm số buổi 2 ( bài giảng )": "https://www.youtube.com/watch?v=2KqTuhYT_pE&feature=youtu.be",

    "Bài 3. Cực trị hàm số ( bài tập )": "https://drive.google.com/file/d/1fsf5ucS5YZFtuu61kqdk1_4pLyKwcWmk/view",
    "Bài 3. Cực trị hàm số bài giảng": "https://www.youtube.com/watch?v=HJrX7H4-9Cs",

    "Bài 4. GTLN-GTNN của hàm số bài tập": "https://drive.google.com/file/d/1M1K8_QKzRQeehim7z2hDzDN0VAVqmwmJ/view",
    "Bài 4. GTLN-GTNN của hàm số bài giảng": "https://www.youtube.com/watch?v=yBwk0RnA1sw",

    "Bài 5. Đường tiệm cận bài tập": "https://drive.google.com/file/d/1HBluKuF-9qdDle2sCdBiIieaOT8SKNmG/view",
    "Bài 5. Đường tiệm cận bài giảng": "https://www.youtube.com/watch?v=zBYJoLrJ8_8",

    "Bài 6. Tương giao bài tập": "https://drive.google.com/file/d/162syR168GYDG66MKPU48na0c1OkTWJOF/view",
    "Bài 6. Tương giao bài giảng": "https://www.youtube.com/watch?v=zxp0hvi6Zyg",

    "Bài 7. Bài toán thực tế bài tập": "https://drive.google.com/file/d/1lzGV7svGlEGC--KJhKvITQDuHEuNpPsc/view",
    "Bài 7. Bài toán thực tế bài giảng": "https://www.youtube.com/watch?v=ZpgiH8Pmcr4",

    "ĐỀ SỐ 1. ÔN TẬP CƠ BẢN": "https://drive.google.com/file/d/11sHajDX464JUQh4gSIpya43c9ra1GHX8/view",
    "ĐỀ SỐ 2. ÔN TẬP CƠ BẢN": "https://drive.google.com/file/d/1MvuPdNZVE7HnYNkHI8yRDhnm9Walwo6-/view",
    "ĐỀ SỐ 3. ÔN TẬP CƠ BẢN": "https://drive.google.com/file/d/1ZS9U3tIqZ9SiiPQ-7jc_SZj22d_idXCH/view",

    "Bài 8. Skill xấp xỉ nghiệm, ốc sên bài tập": "https://drive.google.com/drive/folders/1SduecCQNFIK82ODXHO6xFv_pX92-hGm0",
    "Bài 8. Skill xấp xỉ nghiệm, ốc sên bài giảng": "https://www.youtube.com/watch?v=2S3wmj6TviI",

    "Bài 9. Đơn điệu và cực trị nâng cao bài tập": "https://drive.google.com/drive/folders/1SduecCQNFIK82ODXHO6xFv_pX92-hGm0",
    "Bài 9. Đơn điệu và cực trị nâng cao bài giảng": "https://www.youtube.com/watch?v=uSltMXKFPYY",

    "Bài 10. Minmax nâng cao bài tập": "https://drive.google.com/drive/folders/1SduecCQNFIK82ODXHO6xFv_pX92-hGm0",
    "Bài 10. Minmax nâng cao bài giảng": "https://www.youtube.com/watch?v=4LLh5dAg244",

    "Bài 11. Tham số m nâng cao bài tập": "https://drive.google.com/drive/folders/1SduecCQNFIK82ODXHO6xFv_pX92-hGm0",
    "Bài 11. Tham số m nâng cao bài giảng": "https://www.youtube.com/watch?v=adAVMp2zAUA",

    "Bài 12. Tư duy toán thực tế bài tập": "https://drive.google.com/drive/folders/1SduecCQNFIK82ODXHO6xFv_pX92-hGm0",
    "Bài 12. Tư duy toán thực tế bài giảng": "https://www.youtube.com/watch?v=72H0k8GZqqc",

    "TOÁN THỰC TẾ ĐỀ SỐ 1": "https://drive.google.com/file/d/1aHdLUGflxcMKYBJTbJ8b2pv-dwyWAcN8/view?usp=drive_link",
    "TOÁN THỰC TẾ ĐỀ SỐ 2": "https://drive.google.com/file/d/1JtrBokzPB8SJyGWQfYWs4sdcEI7WduGx/view",
#TỌA ĐỘ VECTƠ TRONG KHÔNG GIAN
    "!! TỌA ĐỘ VECTƠ TRONG KHÔNG GIAN !! [ None ]": "none",

    "Bài 1. Vecto trong không gian cơ bản bài tập": "https://drive.google.com/file/d/14GRLU4xE0bd-K8QpkWXUgefM62Mpcy4h/view",
    "Bài 1. Vecto trong không gian cơ bản bài giảng": "https://www.youtube.com/watch?v=2x1X2bG3NCY",

    "Bài 2. Vecto trong không gian nâng cao bài tập": "https://drive.google.com/file/d/1Yn4qN5W9mhldRvC71RNL1p-PfTposPwD/view",
    "Bài 2. Vecto trong không gian nâng cao bài giảng": "https://www.youtube.com/watch?v=ZPuwIgKzmQU",

    "Bài 3. Biểu thức tọa độ của vecto cơ bản bài tập": "https://drive.google.com/file/d/1uEIK1T0PxA3yP29etYeH2Wx6QWnFg0zZ/view",
    "Bài 3. Biểu thức tọa độ của vecto cơ bản bài giảng": "https://www.youtube.com/watch?v=W9s4GZnt6Zo",

    "Bài 4. Biểu thức tọa độ của vecto nâng cao bài tập": "https://drive.google.com/file/d/13LiNoSLkF0pOhB3Elnt-1lpww00ydQ8O/view",
    "Bài 4. Biểu thức tọa độ của vecto nâng cao bài giảng": "https://www.youtube.com/watch?v=aJnIhIRBnA8",

    "Bài 5. Toán thực tế bài tập": "https://drive.google.com/file/d/1u0HOYUkAWaTF0DkDARVI68QDxfXyZjuT/view",
    "Bài 5. Toán thực tế bài giảng": "https://www.youtube.com/watch?v=D3KW4Tf2QE0",

    "Bài 6. Tâm tỉ cự bài tập": "https://drive.google.com/drive/folders/1SduecCQNFIK82ODXHO6xFv_pX92-hGm0",
    "Bài 6. Tâm tỉ cự bài giảng": "https://www.youtube.com/watch?v=DkQUlOWO8yc&feature=youtu.be",

    "ĐỀ ÔN TẬP SỐ 1": "https://drive.google.com/file/d/1s_4yZp046qPnoNDgMR_ADUjrFU4bJhSS/view",
    "ĐỀ ÔN TẬP SỐ 2": "https://drive.google.com/file/d/1dqlaDtUJeOck5VtrbyJ43MynLtNnlIhy/view",
    "ĐỀ ÔN TẬP SỐ 3": "https://drive.google.com/file/d/1GPuB8upYjIiPNDOU6plZF1zVc8r-8hcD/view",

#

    "Bài 1. Khoảng biến thiên và khoảng tứ phân vị bài tập": "https://drive.google.com/file/d/12UdnZ4D2WlawsTI76nNp2Lo76VZNroCq/view",
    "Bài 1. Khoảng biến thiên và khoảng tứ phân vị bài giảng": "https://www.youtube.com/watch?v=93r3MLedoiQ&feature=youtu.be",

    "Bài 2. Phương sai và độ lệch chuẩn bài tập": "https://drive.google.com/file/d/1_A9NvU-UVvTgZfKRuBV9rGZ8XYekT-1J/view",
    "Bài 2. Phương sai và độ lệch chuẩn bài giảng": "https://www.youtube.com/watch?si=UDCaVVdgiJWQQBXh&v=vx1xis2eOyo&feature=youtu.be",

    "Đề kiểm tra chương số 1": "https://drive.google.com/drive/folders/1SduecCQNFIK82ODXHO6xFv_pX92-hGm0",
    "Đề kiểm tra chương số 2": "https://drive.google.com/drive/folders/1SduecCQNFIK82ODXHO6xFv_pX92-hGm0",

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
