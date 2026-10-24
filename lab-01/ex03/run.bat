@echo off
chcp 65001 > nul
:menu
cls
echo ========================================================
echo   CHỌN BÀI TẬP LIST, TUPLE, DICTIONARY ĐỂ CHẠY (lab-01/ex03)
echo ========================================================
echo [1] ex03_01.py - Tính tổng các số chẵn trong List
echo [2] ex03_02.py - Đảo ngược các phần tử trong List
echo [3] ex03_03.py - Tạo Tuple từ List
echo [4] ex03_04.py - Truy cập phần tử đầu và cuối của Tuple
echo [5] ex03_05.py - Đếm số lần xuất hiện của các từ bằng Dictionary
echo [6] ex03_06.py - Xóa phần tử trong Dictionary theo key
echo [0] Thoát
echo ========================================================
set /p choice="Nhập số bài tập muốn chạy (0-6): "

if "%choice%"=="1" ( cls & python ex03_01.py & pause & goto menu )
if "%choice%"=="2" ( cls & python ex03_02.py & pause & goto menu )
if "%choice%"=="3" ( cls & python ex03_03.py & pause & goto menu )
if "%choice%"=="4" ( cls & python ex03_04.py & pause & goto menu )
if "%choice%"=="5" ( cls & python ex03_05.py & pause & goto menu )
if "%choice%"=="6" ( cls & python ex03_06.py & pause & goto menu )
if "%choice%"=="0" exit
goto menu
