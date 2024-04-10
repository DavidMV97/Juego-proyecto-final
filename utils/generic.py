from PIL import ImageTk, Image

def read_img(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.LANCZOS))

def center_window(window, aplication_width, aplication_height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x= int((screen_width / 2) - (aplication_width / 2) )
    y= int((screen_height / 2) - (aplication_height / 2) )
    return window.geometry(f"{aplication_width}x{aplication_height}+{x}+{y}")

    