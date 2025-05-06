from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time
import os

# 사용자 ID/PW
user_id = "high6969"
user_pw = "0815"

# CYBOS 실행
os.startfile(r"C:\Users\chhwang\Desktop\CybosPlus.lnk")
time.sleep(5)

# 로그인 창 연결
app = Application(backend="uia").connect(title_re="CYBOS.*")
dlg = app.window(title_re="CYBOS.*")
dlg.wait("visible", timeout=15)

# ID 입력
edit_id = dlg.child_window(auto_id="6977", control_type="Edit")
edit_id.set_focus()
edit_id.type_keys(user_id)
time.sleep(0.5)

# PW 입력
edit_pw = dlg.child_window(auto_id="6978", control_type="Edit")
edit_pw.set_focus()
edit_pw.type_keys(user_pw)
time.sleep(0.5)

# Enter 키 입력해서 로그인
send_keys("{ENTER}")
time.sleep(25)  # 로그인 후 대기

send_keys("{ENTER}")
time.sleep(7)  # 로그인 후 대기
# 로그인 후 뜨는 공지사항 창 닫기
try:
    popup_app = Application(backend="uia").connect(title="공지사항", timeout=10)
    popup_dlg = popup_app.window(title="공지사항")

    if popup_dlg.exists():
        print("📢 공지사항 창 감지됨 → 닫는 중")
        close_btn = popup_dlg.child_window(title="닫기", control_type="Button")
        close_btn.click_input()
except Exception as e:
    print(f"공지사항 창 닫기 실패: {e}")