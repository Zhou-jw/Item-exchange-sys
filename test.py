import tkinter as tk

# 创建窗口
window =tk.Tk()

# 设置回调函数
def callback():
    print ("click me!")
# 使用按钮控件调用函数
b = tk.Button(window, text="点击执行回调函数", command=callback).pack()
# 显示窗口
tk.mainloop()