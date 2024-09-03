# -*- coding: utf-8 -*-
import base64

def encode_to_exec_code(input_file, output_file):
    """Mã hóa nội dung của một file và tạo file mới chứa đoạn mã Python để giải mã và thực thi nội dung đó."""
    # Đọc dữ liệu từ file đầu vào
    with open(input_file, 'rb') as f:
        file_data = f.read()

    # Mã hóa dữ liệu
    encoded_data = base64.b64encode(file_data).decode('utf-8')

    # Tạo đoạn mã Python chứa lệnh exec
    exec_code = f"import base64\nexec(base64.b64decode(\"\"\"{encoded_data}\"\"\"))"

    # Ghi đoạn mã Python vào file đầu ra
    with open(output_file, 'w') as f:
        f.write(exec_code)

    print(f"File '{input_file}' đã được mã hóa và lưu vào '{output_file}'.")

if __name__ == "__main__":
    input_file = input("Nhập tên file cần mã hóa: ")
    output_file = input("Nhập tên file đầu ra (đã mã hóa): ")
    encode_to_exec_code(input_file, output_file)
