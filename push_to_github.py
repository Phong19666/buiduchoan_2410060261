import subprocess
import getpass
import sys

def run_cmd(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, shell=True)
    return res.returncode == 0

print("=" * 60)
print("HƯỚNG DẪN PUSH CODE LÊN GITHUB (BÙI ĐỨC HOÀN - 2410060261)")
print("=" * 60)
print("Lưu ý: GitHub không còn hỗ trợ mật khẩu thông thường qua HTTPS,")
print("mà yêu cầu Personal Access Token (PAT).")
print("Các bước lấy Token (như hướng dẫn trang 40 PDF):")
print("1. Vào https://github.com/settings/tokens")
print("2. Chọn 'Generate new token (classic)'")
print("3. Tích chọn quyền 'repo' và nhấn 'Generate token'")
print("4. Copy chuỗi token bắt đầu bằng ghp_...")
print("=" * 60)

token = input("Dán Personal Access Token của bạn vào đây (hoặc Enter để thử push mặc định): ").strip()

if token:
    remote_url = f"https://Phong19666:{token}@github.com/Phong19666/buiduchoan_2410060261.git"
    run_cmd(f'git remote set-url origin "{remote_url}"')

print("\n--- Đang đẩy nhánh main ---")
run_cmd("git push -u origin main")

print("\n--- Đang đẩy nhánh lab-01 ---")
run_cmd("git push -u origin lab-01")

print("\n--- Đang đẩy nhánh lab-02 ---")
run_cmd("git push -u origin lab-02")

print("\nHoàn tất! Kiểm tra lại trên website https://github.com/Phong19666/buiduchoan_2410060261")
