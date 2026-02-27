import tkinter as tk
from tkinter import messagebox

def calculate_sleep():
    try:
        sleep = float(entry_sleep.get())
        wake_up = float(entry_wake.get())

        sleeping_behavior = (wake_up + 24) - sleep

        if sleeping_behavior < 6:
            result = (
                f"พฤติกรรมการนอนของคุณ คือ {sleeping_behavior:.2f} ชั่วโมง\n"
                "แปลผล คือ นอนน้อย\n"
                "คำแนะนำ คือ นอนให้เพียงพอ"
            )
        elif sleeping_behavior < 8:
            result = (
                f"พฤติกรรมการนอนของคุณ คือ {sleeping_behavior:.2f} ชั่วโมง\n"
                "แปลผล คือ นอนพอดี\n"
                "คำแนะนำ คือ รักษาการนอนให้เพียงพอแบบนี้ไว้เพื่อสุขภาพ"
            )
        else:
            result = (
                f"พฤติกรรมการนอนของคุณ คือ {sleeping_behavior:.2f} ชั่วโมง\n"
                "แปลผล คือ นอนมากเกินไป\n"
                "คำแนะนำ คือ นอนมากก็ไม่ดีนะ ควรนอนให้พอดี"
            )

        label_result.config(text=result)

    except ValueError:
        messagebox.showerror("Error", "กรุณาใส่ตัวเลขให้ถูกต้อง เช่น 22.00")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณพฤติกรรมการนอน")
root.geometry("400x320")
root.configure(bg="orange")

# 🔴 ลวดลายสีแดง (แถบบน)
top_bar = tk.Frame(root, bg="red", height=10)
top_bar.pack(fill="x")

# เนื้อหา
tk.Label(root, text="เวลาเข้านอน (เช่น 22.00)", bg="orange").pack(pady=5)
entry_sleep = tk.Entry(root)
entry_sleep.pack()

tk.Label(root, text="เวลาตื่นนอน (เช่น 05.00)", bg="orange").pack(pady=5)
entry_wake = tk.Entry(root)
entry_wake.pack()

tk.Button(root, text="คำนวณ", command=calculate_sleep, bg="white").pack(pady=10)

label_result = tk.Label(root, text="", justify="left", fg="blue", bg="orange")
label_result.pack(pady=10)

# 🔴 ลวดลายสีแดง (แถบล่าง)
bottom_bar = tk.Frame(root, bg="red", height=10)
bottom_bar.pack(fill="x", side="bottom")

# เริ่มโปรแกรม
root.mainloop()
