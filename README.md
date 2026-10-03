# BÁO CÁO THỰC HÀNH BẢO MẬT THÔNG TIN NÂNG CAO

- **Họ và tên**: Bùi Đức Hoàn
- **Mã số sinh viên (MSSV)**: 2410060261
- **Môn học**: Thực hành Bảo mật thông tin nâng cao
- **GitHub Repository**: [https://github.com/Phong19666/buiduchoan_2410060261](https://github.com/Phong19666/buiduchoan_2410060261)

---

## 1. Kiểm tra môi trường & Cấu hình Git

```bash
# Kiểm tra phiên bản Python và Git
python --version
git --version

# Thiết lập thông tin tác giả Git
git config --global user.name "buiduchoan_2410060261"
git config --global user.email "Phong19666@users.noreply.github.com"

# Kiểm tra lại cấu hình
git config user.name
git config user.email
```

---

## 2. Hướng dẫn các câu lệnh chạy bài tập Lab 01

### 2.1. Thử nghiệm Hello World (Bài tập 1.6.1)
```bash
cd lab-01/ex01
python hello.py
```

### 2.2. Lập trình Python cơ bản (Bài tập 1.6.2)
```bash
cd lab-01/ex02

python ex02_01.py
python ex02_02.py
python ex02_03.py
python ex02_04.py
python ex02_05.py
python ex02_06.py
python ex02_07.py
python ex02_08.py
python ex02_09.py
python ex02_10.py
```

### 2.3. Cấu trúc dữ liệu List, Tuple, Dictionary (Bài tập 1.6.3)
```bash
cd lab-01/ex03

python ex03_01.py
python ex03_02.py
python ex03_03.py
python ex03_04.py
python ex03_05.py
python ex03_06.py
```

### 2.4. Lập trình hướng đối tượng OOP - Quản lý sinh viên (Bài tập 1.6.4)
```bash
cd lab-01/ex04

python Main.py
```

---

## 3. Hướng dẫn các câu lệnh chạy bài tập Lab 02

### 3.1. Cài đặt thư viện phụ thuộc
```bash
cd lab-02/ex01
pip install -r requirements.txt
```

### 3.2. Khởi chạy Flask REST API - Caesar & Playfair Cipher (Bài tập 2.5.1 & 2.5.4)
```bash
cd lab-02/ex01
python api.py
```
> Server API khởi chạy tại: `http://127.0.0.1:5000`
> 
> Các API endpoints chính:
> - `POST http://127.0.0.1:5000/api/caesar/encrypt`
> - `POST http://127.0.0.1:5000/api/caesar/decrypt`
> - `POST http://127.0.0.1:5000/api/playfair/creatematrix`
> - `POST http://127.0.0.1:5000/api/playfair/encrypt`
> - `POST http://127.0.0.1:5000/api/playfair/decrypt`

### 3.3. Khởi chạy Giao diện Web Flask Demo (Bài tập 2.5.6)
```bash
cd lab-02
python app.py
```
> Máy chủ Web khởi chạy tại: `http://127.0.0.1:5050`
> 
> Mở trình duyệt web truy cập:
> - Trang chủ: `http://127.0.0.1:5050/`
> - Giao diện Mã hóa/Giải mã Caesar: `http://127.0.0.1:5050/caesar`

---

## 4. Các lệnh Git quản lý nhánh (Branches)

```bash
# Xem danh sách các nhánh
git branch -a

# Chuyển đổi giữa các nhánh bài tập
git checkout main     # Nhánh chính
git checkout lab-01   # Nhánh chứa bài tập Lab 01
git checkout lab-02   # Nhánh chứa bài tập Lab 02
```
