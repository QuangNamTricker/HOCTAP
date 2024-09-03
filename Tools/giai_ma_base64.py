# -*- coding: utf-8 -*-
import base64

def decode_file(input_file, output_file):
    """Giải mã nội dung của một file và lưu kết quả vào file đầu ra."""
    # Đọc dữ liệu từ file đầu vào
    with open(input_file, 'r') as f:
        exec_code = f.read()

    # Tìm đoạn mã đã mã hóa trong exec_code
    exec_code = exec_code.replace('import base64\nexec(base64.b64decode("""', '')
    exec_code = exec_code.replace('"""))', '')

    # Giải mã dữ liệu
    decoded_data = base64.b64decode(exec_code)

    # Ghi dữ liệu đã giải mã vào file đầu ra
    with open(output_file, 'wb') as f:
        f.write(decoded_data)

    print(f"File '{input_file}' đã được giải mã và lưu vào '{output_file}'.")

if __name__ == "__main__":
    input_file = input("Nhập tên file cần giải mã: ")
    output_file = input("Nhập tên file đầu ra (đã giải mã): ")
    decode_file(input_file, output_file)
