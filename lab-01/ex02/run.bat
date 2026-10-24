@echo off
chcp 65001 > nul
:menu
cls
echo ========================================================
echo   CHỌN BÀI TẬP PYTHON CƠ BẢN ĐỂ CHẠY (lab-01/ex02)
echo ========================================================
echo [1]  ex02_01.py - Nhập tên, tuổi và in lời chào
echo [2]  ex02_02.py - Tính diện tích hình tròn
echo [3]  ex02_03.py - Kiểm tra số chẵn / số lẻ
echo [4]  ex02_04.py - Tìm số chia hết cho 7, không chia hết cho 5
echo [5]  ex02_05.py - Tính tiền lương thực lĩnh nhân viên
echo [6]  ex02_06.py - Xây dựng mảng 2 chiều X x Y
echo [7]  ex02_07.py - Nhập các dòng chữ và chuyển sang in hoa
echo [8]  ex02_08.py - Lọc các số nhị phân chia hết cho 5
echo [9]  ex02_09.py - Kiểm tra số nguyên tố
echo [10] ex02_10.py - Đảo ngược chuỗi ký tự
echo [0]  Thoát
echo ========================================================
set /p choice="Nhập số bài tập muốn chạy (0-10): "

if "%choice%"=="1" ( cls & python ex02_01.py & pause & goto menu )
if "%choice%"=="2" ( cls & python ex02_02.py & pause & goto menu )
if "%choice%"=="3" ( cls & python ex02_03.py & pause & goto menu )
if "%choice%"=="4" ( cls & python ex02_04.py & pause & goto menu )
if "%choice%"=="5" ( cls & python ex02_05.py & pause & goto menu )
if "%choice%"=="6" ( cls & python ex02_06.py & pause & goto menu )
if "%choice%"=="7" ( cls & python ex02_07.py & pause & goto menu )
if "%choice%"=="8" ( cls & python ex02_08.py & pause & goto menu )
if "%choice%"=="9" ( cls & python ex02_09.py & pause & goto menu )
if "%choice%"=="10" ( cls & python ex02_10.py & pause & goto menu )
if "%choice%"=="0" exit
goto menu
