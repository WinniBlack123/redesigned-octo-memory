import time
import pyautogui

def clicker(num_clicks, interval):
    print("连点器启动，点击 Ctrl+C 停止...")
    try:
        for _ in range(num_clicks):
            pyautogui.click()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("连点器停止")

if __name__ == "__main__":
    num_clicks = int(input("请输入要点击的次数："))
    interval = float(input("请输入点击间隔（秒）："))

    clicker(num_clicks, interval)
