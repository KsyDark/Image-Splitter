# Import necessary modules
# Импорт необходимых модулей
from tkinter import Tk, Button, filedialog, Label, CENTER, OUTSIDE, PhotoImage, Canvas, messagebox
from PIL import Image
from os import path

# Define a function to split an image into four equal parts
# Определить функцию для разбиения изображения на четыре равные части
def split_image(image_path, save_path):
    # Open the image using the PIL Image module
    # Открыть изображение с помощью модуля PIL Image
    image = Image.open(image_path)
    # Get the width and height of the image
    # Получить ширину и высоту изображения
    width, height = image.size
    # Calculate the new width and height for each of the four parts
    # Вычислить новую ширину и высоту для каждой из четырех частей
    new_width = width // 2
    new_height = height // 2

    # Use the crop method from the PIL Image module to create four new images
    # Использует метод кадрирования из модуля PIL Image для создания четырех новых изображений
    # Each image is a quarter of the original image
    # Каждое изображение представляет собой четверть исходного изображения
    image1 = image.crop((0, 0, new_width, new_height))
    image2 = image.crop((new_width, 0, width, new_height))
    image3 = image.crop((0, new_height, new_width, height))
    image4 = image.crop((new_width, new_height, width, height))

    # Get the filename and file extension of the original image
    # Получить имя файла и расширение файла исходного изображения
    filename, file_extension = path.splitext(path.basename(image_path))

    # Save each of the four new images using the original filename with a number added to it
    # Сохраняет каждое из четырех новых изображений, используя исходное имя файла с добавленным к нему номером
    # The images are saved in the specified save location
    # Изображения сохраняются в указанном месте сохранения
    image1.save(path.join(save_path, f'{filename}_1{file_extension}'))
    image2.save(path.join(save_path, f'{filename}_2{file_extension}'))
    image3.save(path.join(save_path, f'{filename}_3{file_extension}'))
    image4.save(path.join(save_path, f'{filename}_4{file_extension}'))

# Define a function to allow the user to select an image file using a file dialog
# Определяет функцию, позволяющую пользователю выбрать файл изображения с помощью диалогового окна файла
def select_file():
    global file_path
    file_path = filedialog.askopenfilename()

# Define a function to allow the user to select a save location using a directory dialog
# Определяет функцию, позволяющую пользователю выбрать место сохранения с помощью диалогового окна каталога
def select_save_location():
    global save_path
    save_path = filedialog.askdirectory(mustexist=True)

# Define a function to start splitting the selected image when the start button is clicked
# Определяет функцию, запускающую разбиение выбранного изображения при нажатии кнопки запуска
def start_splitting():
    if file_path and save_path:
        split_image(file_path, save_path)

# Start the help window with Button
# Запуск окна справки через кнопку
def reference():
    messagebox.showinfo("Help", "\"Image Splitter\" program is designed to split an image into 4 equal parts.\n\nHotkeys\nF1 = Help \nEsc = Close the window.\n\nico.ico - Icon for application window and taskbar. \nlogo.png - Background image 250x200.\n\n\"Image Splitter\" предназначен для разделения изображений на 4 равные части.\n\nГорячие клавиши\nF1 = Справка\nEsc = Закрыть окно.\n\nico.ico - Иконка для окна приложения и панели задач.\nlogo.png - Фоновое изображение 250x200.")

# Create a Tkinter root window and set its title and size
# Создааёт корневое окно Tkinter и задаёт его заголовок и размер
root = Tk()
root.title("Image Splitter")
root.resizable(width=False, height=False)
root.geometry('250x150')

# Try to set the window icon (this may not work on all systems)
# Попробует установить значок окна (это может работать не на всех системах)
try:
    root.iconbitmap(r'ico.ico')
except:
    pass

# Try to set a background image for the window (this may not work on all systems)
# Попробует установить фоновое изображение для окна (это может работать не на всех системах)
try:
    C = Canvas(root, height=200, width=250)
    filename = PhotoImage(file ='logo.png')
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
except:
    pass

# Initialize global variables for the selected file path and save path
# Инициализация глобальных переменных для выбранного пути к файлу и пути сохранения
file_path = None
save_path = None

# Create buttons for selecting an image file and save location and starting the splitting process
# Создаются кнопки для выбора файла изображения и места сохранения, а также для запуска процесса разбиения
select_file_button = Button(root, text="Select Image", command=select_file)
select_file_button.place(relx=0.50, rely=0.150, anchor=CENTER, height=40, width=150, bordermode=OUTSIDE)

select_save_location_button = Button(root, text="Select Save Location", command=select_save_location)
select_save_location_button.place(relx=0.50, rely=0.430, anchor=CENTER, height=40, width=150, bordermode=OUTSIDE)

start_button = Button(root, text="Start", command=start_splitting)
start_button.place(relx=0.50, rely=0.710, anchor=CENTER, height=40, width=150, bordermode=OUTSIDE)

reference = Button(root, text="Help", command=reference)
reference.place(relx=0.70, rely=0.860, height=19, width=70, bordermode=OUTSIDE)

# Define a function to exit the program when the Escape key is pressed
# Определяет функцию для выхода из программы при нажатии клавиши Escape
def exit_root(event):
    root.quit()
root.bind('<Escape>', exit_root)

# Start the help window with F1
# Запуск окна справки через F1
def reference1(event):
    messagebox.showinfo("Help", "\"Image Splitter\" program is designed to split an image into 4 equal parts.\n\nHotkeys\nF1 = Help \nEsc = Close the window.\n\nico.ico - Icon for application window and taskbar. \nlogo.png - Background image 250x200.\n\n\"Image Splitter\" предназначен для разделения изображений на 4 равные части.\n\nГорячие клавиши\nF1 = Справка\nEsc = Закрыть окно.\n\nico.ico - Иконка для окна приложения и панели задач.\nlogo.png - Фоновое изображение 250x200.")
root.bind('<F1>', reference1)

# Start the Tkinter main loop to display the window and handle user interaction
# Запуск главного цикла Tkinter для отображения окна и обработки взаимодействия с пользователем
root.mainloop()