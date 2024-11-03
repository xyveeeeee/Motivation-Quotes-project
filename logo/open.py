import tkinter
from tkinter import Label
from PIL import Image, ImageTk

# Resize splash logo image
image_path = 'D:/logo/motologo5.png'
img = Image.open(image_path)
resized_img = img.resize((430, 750))
resized_img.save("temp_logo.png", "PNG")  # Optional: save if you need to keep a resized version

# Splash screen
splash_root = tkinter.Tk()
splash_root.geometry("430x750")
splash_root.title("Motivation Quotes")
splash_root.iconbitmap('logo2.ico')

splash_label = Label(splash_root, text="Empower your journey with the right mindset", font=("Raleway", 10))
splash_label.place(x=130, y=50)

# Splash logo
logo_image = ImageTk.PhotoImage(resized_img)
lbl = Label(splash_root, image=logo_image)
lbl.pack()

# Main window
def main_window():
    root = tkinter.Tk()
    root.title('Main')
    root.iconbitmap('logo2.ico')
    root.geometry("430x750")
    root.config(bg='#001F3F')

    # Load and display main window logo
    main_image_path = 'khakilogo.png'
    main_img = Image.open(main_image_path).convert("RGBA")
    new_data = [(255, 255, 255, 0) if pixel[:3] == (255, 255, 255) else pixel for pixel in main_img.getdata()]
    main_img.putdata(new_data)

    resized_main_img = main_img.resize((44, 44), Image.LANCZOS)
    main_logo_image = ImageTk.PhotoImage(resized_main_img)
    main_label = Label(root, image=main_logo_image, bg='#001F3F')
    main_label.image = main_logo_image
    main_label.place(rely=0.02, relx=0.02)

    # Logo title
    title_label = Label(root, text="MOTIVATION QUOTES", font=("Raleway", 12, 'bold'), bg="#001F3F", fg="white")
    title_label.place(x=60, y=25)

    # Add button
    add_photo = Image.open('addbutton.png').resize((43, 36))
    photo_img = ImageTk.PhotoImage(add_photo)
    add_button = Label(root, image=photo_img, bg='#001F3F')
    add_button.image = photo_img
    add_button.place(x=360, y=16)

    # Image Slider
    images = ['m1.jpg', 'm2.png', 'm3.jpg', 'm4.png', 'm5.png', 'm6.jpg', 'm7.png', 'm8.jpg', 'm9.png', 'm10.png',]
    current_image = 0
    slider_width = 430  # customize width 
    slider_height = 220  # customize height
    
    slider_label = Label(root, bg='#001F3F')
    slider_label.place(x=-2, y=75)  # position
    
    def update_image():
        nonlocal current_image

        image = Image.open(images[current_image]).resize((slider_width, slider_height))
        photo = ImageTk.PhotoImage(image)
        slider_label.config(image=photo)
        slider_label.image = photo
        

        current_image = (current_image + 1) % len(images)
        root.after(8000, update_image) #speed

    # slideshow
    update_image()
   # Buttons
    life_button_img = ImageTk.PhotoImage(Image.open('rounded.png').resize((140, 38)))
    life_button = tk.Button(root, image=life_button_img, text='Life', font=('Raleway', 14, 'bold'),
    compound="center", fg="#001F3F", bg='#001F3F', borderwidth=0,
    activebackground='#001F3F', cursor='hand2')
    life_button.image = life_button_img
    life_button.place(x=15, y=320)

    edu_button_img = ImageTk.PhotoImage(Image.open('rounded2.png').resize((140, 38)))
    edu_button = tk.Button(root, image=edu_button_img, text='Education', font=('Raleway', 14, 'bold'),
    compound="center", fg="#201E43", bg='#001F3F', borderwidth=0,
    activebackground='#001F3F', activeforeground='#EAD8B1', cursor='hand2')
    edu_button.image = edu_button_img
    edu_button.place(x=162, y=320) 

    success_button_img = ImageTk.PhotoImage(Image.open('rounded2.png').resize((140, 38)))
    success_button = tk.Button(root, image=success_button_img, text='Success', font=('Raleway', 14, 'bold'),
    compound="center", fg="#201E43", bg='#001F3F', borderwidth=0,
    activebackground='#001F3F', activeforeground='#EAD8B1', cursor='hand2')
    success_button.image = success_button_img
    success_button.place(x=309, y=320)
    

# screen delay
splash_root.after(3000, lambda: [splash_root.destroy(), main_window()])

# splash screen
splash_root.mainloop()
