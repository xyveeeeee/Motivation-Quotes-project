import tkinter as tk
from tkinter import Label, messagebox, filedialog
from PIL import Image, ImageTk
import customtkinter as ctk

image_path = 'D:/logo/motologo5.png'
img = Image.open(image_path)
resized_img = img.resize((430, 750))
resized_img.save("temp_logo.png", "PNG")

splash_root = tk.Tk()
splash_root.geometry("430x750")
splash_root.title("Motivation Quotes")
splash_root.iconbitmap('logo2.ico')

splash_label = Label(splash_root, text="Empower your journey with the right mindset", font=("Raleway", 10))
splash_label.place(x=130, y=50)

# Splash logo img
logo_image = ImageTk.PhotoImage(resized_img)
lbl = Label(splash_root, image=logo_image)
lbl.image = logo_image
lbl.pack()

# Main window
def main_window():
    root = tk.Tk()
    root.title('Main')
    root.iconbitmap('logo2.ico')
    root.geometry("430x750")
    root.config(bg='#001F3F')
    root.resizable(width=False, height=True)

    # display main window
    main_image_path = 'khakilogo.png'
    main_img = Image.open(main_image_path)
    resized_main_img = main_img.resize((44, 44), Image.LANCZOS)
    main_logo_image = ImageTk.PhotoImage(resized_main_img)
    main_label = Label(root, image=main_logo_image, bg='#001F3F')
    main_label.image = main_logo_image
    main_label.place(rely=0.02, relx=0.02)

    line_img = ImageTk.PhotoImage(Image.open('line.png'))
    bgline = Label(root, image=line_img, bg='#001f3f', width= 440)
    bgline.image = line_img
    bgline.place(x=0, y=590)


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
    images = ['m1.jpg', 'm2.png', 'm3.jpg', 'm4.png', 'm5.png', 'm6.jpg', 'm7.png', 'm8.jpg', 'm9.png', 'm10.png']
    current_image = 0
    slider_width = 430
    slider_height = 220
    
    slider_label = Label(root, bg='#001F3F')
    slider_label.place(x=-2, y=75)
    
    def update_image():
        nonlocal current_image
        image = Image.open(images[current_image]).resize((slider_width, slider_height))
        photo = ImageTk.PhotoImage(image)
        slider_label.config(image=photo)
        slider_label.image = photo
        current_image = (current_image + 1) % len(images)
        root.after(5000, update_image)

    # Starter
    update_image()
    
    navigation_frame = ctk.CTkFrame(root, width=400, height=80, fg_color='#001F3F')
    navigation_frame.place(x=15, y=315)

    # content scrol
    scrollable_frame = ctk.CTkScrollableFrame(root, width=365, height=250, corner_radius=25, fg_color='#EAD8B1')
    scrollable_frame.place(x=15, y=375)

    # text category
    lifequotes = [
        "Each day you must choose the pain of discipline, or the pain of regret.",
        "Be the reason someone feels welcomed, seen, heard, valued, loved and supported.",
        "One day, you'll be living the life you once prayed for.",
        "Accept both compliments and criticism. It takes both sun and rain for a flower to grow.",
        "Psychology says 'You'll never live a happy life if you always care about what others think about you.'",
        "Psychology says 'Ships don't sink because of the water around them. Ships sink because of the water that gets in them.'",
        "Life isn't about finding yourself. It's about creating yourself.",
        "You cannot live when you are untouchable. Embrace vulnerability.",
        "Use the weekend to build the life you want instead of trying to escape the life you have.",
        "An inch of MOVEMENT will bring you closer to your goals than a mile of INTENTION."
    ]
    educationquotes = [
        "IF YOU NEVER TRY, YOU'LL NEVER KNOW.",
        "If you don't sacrifice for what you want, what you want becomes the sacrifice",
        "Win through your actions, never through argument",
        "The only thing that's keeping you from getting what you want is the story you keep telling yourself about why you can't have it",
        "MINDSET IS WHAT SEPARATES THE BEST FROM THE REST.",
        "THE DOORS WILL BE OPENED TO THOSE WHO ARE BOLD ENOUGH TO KNOCK",
        "Your passion is your greatest asset use it to fuel your hustle",
        "You can't have a million-dollar goal with a one-dollar work ethic",
        "All progress takes place outside the comfort zone",
        "success is not given, but earned through hard work, determination, and a relentless spirit"
    ]
    successquotes = [
        "The future depends on what you do today.",
        "If you know you can do better, then do better.",
        "Don't complain about something that you can actually do something.",
        "Progress is impossible without change, and those who cannot change their minds cannot change anything.",
        "DON'T BURN YOUR OPPORTUNITIES FOR A TEMPORARY COMFORT",
        "Enjoy the journey. Just because you're not there yet, doesn't mean you never will be",
        "No matter if it seems impossible. No matter if it takes time. Wake up early and start studying for your future. Just remember that the feeling of success is the best feeling in the world.",
        "Only compare yourself to your previous self.",
        "CHALLENGE YOURSELF, STUDY DILIGENTLY, AND LET YOUR GRADES BE THE REWARD. STUDY MOTIVATION",
        "Are You Satisfied With An Average Life?"
    ]

    # icon book & fav
    book_mark_img = ImageTk.PhotoImage(Image.open('save.png').resize((25, 25)))
    fav_orite_img = ImageTk.PhotoImage(Image.open('favcont.png').resize((32, 32)))
 
    Favorite = []

    def add_or_remove(quote, favorite):
        if quote in favorite:
            favorite.remove(quote)
            messagebox.showinfo("Motivational Quoute Collection","Sucessfully removed from Favorite")
            print("Successfully Removed!")
        else:
            favorite.append(quote)
            messagebox.showinfo("Motivational Quoute Collection","Sucessfully added to Favorite")
            print("Successfully Removed!")

    def add_or_remove_book(quote, bookmark):
        if quote in bookmark:
            bookmark.remove(quote)
            messagebox.showinfo("Motivational Quoute Collection","Sucessfully removed from Bookmark")
            print("Successfully Removed!")
        else:
            bookmark.append(quote)
            messagebox.showinfo("Motivational Quoute Collection","Sucessfully added to Bookmark")
            print("Successfully Removed!")

    # display th qoute
    def display_quotes(quotes):
        # destroy curnt content
        for content in scrollable_frame.winfo_children():
            content.destroy()

    # qoute in scroll
        for quote in quotes:
            home_label = ctk.CTkLabel(
                scrollable_frame, 
                text=quote,
                font=('Raleway', 18, 'bold'), 
                text_color='#EAD8B1', 
                fg_color='#634345', 
                width=360, 
                height=160, 
                corner_radius=20, 
                wraplength=280
            )
            home_label.pack(pady=(5, 0))

            # buttonsicon
            fav_orite = tk.Button(home_label, image=fav_orite_img, borderwidth=0, bg='#634345', activebackground='#634345',cursor='hand2', 
                                  command=lambda quote=quote: add_or_remove(quote, Favorite))
            fav_orite.image = fav_orite_img
            fav_orite.place(x=310, y=115)

            def saveFile(quote):
                file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File", ".txt"), ("HTML File", ".html"), ("All Files", ".*")])
                if file is None: 
                    return
                file.write(quote)
                file.close()

            book_mark = tk.Button(home_label, image=book_mark_img, borderwidth=0, bg='#634345', activebackground='#634345', cursor='hand2',
                                   command=lambda quote=quote: saveFile(quote))
            book_mark.image = book_mark_img
            book_mark.place(x=15, y=12)

    life_button_active_img = ImageTk.PhotoImage(Image.open('rounded.png').resize((140, 38)))
    life_button_inactive_img = ImageTk.PhotoImage(Image.open('rounded2.png').resize((140, 38)))     
    def active_button(button):
        # images to inactive
        life_button.config(image=life_button_inactive_img)
        edu_button.config(image=life_button_inactive_img)
        success_button.config(image=life_button_inactive_img)

        button.config(image=button.active_image)

    # buttons
    life_button = tk.Button(navigation_frame, image=life_button_inactive_img, text='Life', font=('Raleway', 14, 'bold'),
                            compound="center", fg="#001F3F", bg='#001F3F', borderwidth=0, activebackground='#001F3F', cursor='hand2',
                            command=lambda: [display_quotes(lifequotes), active_button(life_button)])
    life_button.active_image = life_button_active_img
    life_button.place(x=0, y=0)

    edu_button = tk.Button(navigation_frame, image=life_button_inactive_img, text='Education', font=('Raleway', 14, 'bold'),
                           compound="center", fg="#201E43", bg='#001F3F', borderwidth=0, activebackground='#001F3F', cursor='hand2',
                           command=lambda: [display_quotes(educationquotes), active_button(edu_button)])
    edu_button.active_image = life_button_active_img
    edu_button.place(x=150, y=0)

    success_button = tk.Button(navigation_frame, image=life_button_inactive_img, text='Success', font=('Raleway', 14, 'bold'),
                               compound="center", fg="#201E43", bg='#001F3F', borderwidth=0, activebackground='#001F3F', cursor='hand2',
                               command=lambda: [display_quotes(successquotes), active_button(success_button)])
    success_button.active_image = life_button_active_img
    success_button.place(x=300, y=0)

    # starting nav
    active_button(life_button)
    # startup
    display_quotes(lifequotes)

                    # navigation content
    custom_frame2 = ctk.CTkFrame(root, width=130, height=55, corner_radius=35, fg_color='#EAD8B1')
    custom_frame2.place(x=150, y=686)  
                    
    # Inactive & active images fav & save
    home_inactive = ImageTk.PhotoImage(Image.open('home2.png').resize((32, 32)))
    home_active = ImageTk.PhotoImage(Image.open('home1.png').resize((32, 32)))
    fav_inactive = ImageTk.PhotoImage(Image.open('fav.png').resize((30, 25)))
    fav_active = ImageTk.PhotoImage(Image.open('favorite.png').resize((30, 25)))

    # f t button images
    def page_button(active_button, active_image, inactive_image):
        # Restt
        home_frame.config(image=home_inactive)
        favorite_frame.config(image=fav_inactive)
        
        # button to click active
        active_button.config(image=active_image)

    home_frame = tk.Button(
        root, image=home_inactive, bg='#ead8b1', cursor='hand2', borderwidth=0,
        activebackground='#ead8b1',
        command=lambda: [display_quotes(lifequotes), page_button(home_frame, home_active, fav_inactive)]
    )
    home_frame.image = home_active
    home_frame.place(x=163, y=696)

    favorite_frame = tk.Button(
        root, image=fav_inactive, bg='#ead8b1', cursor='hand2', borderwidth=0,
        activebackground='#ead8b1',
        command=lambda: [display_quotes(Favorite), page_button(favorite_frame, fav_active, home_inactive)]
    )
    favorite_frame.image = fav_active
    favorite_frame.place(x=228, y=701)

    page_button(home_frame, home_active, fav_inactive)
                
    
# Screen delay
splash_root.after(3000, lambda: [splash_root.destroy(), main_window()])

# Splash screen mainloop
splash_root.mainloop()
