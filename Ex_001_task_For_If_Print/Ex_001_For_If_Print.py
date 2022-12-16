# max = 10
# for i in range(max+1):
#     for j in range(max+1):
#         if i == j or i == max - j or i in [0, max] or j in [0, max]:
#             print('#', end='')
#         else:
#             print(' ', end='')
#     print('\r')


from tkinter import *

root = Tk()     # создаем корневой объект - окно
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
root.geometry("300x250")    # устанавливаем размеры окна

label = Label(text="Hello METANIT.COM") # создаем текстовую метку
label.pack()    # размещаем метку в окне

root.mainloop()