import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk


# Account and Book classes
class Account:
    def __init__(self, name, email, username, role):
        self.name = name
        self.email = email
        self.username = username
        self.role = role


class Book:
    def __init__(self, item_num, title, author, price, seller):
        self.item_num = item_num
        self.title = title
        self.author = author
        self.price = price
        self.seller = seller
        self.status = "Available"

users = {
    "admin": Account("Admin", "admin@example.com", "admin", "Admin"),
    "seller1": Account("Seller One", "seller1@example.com", "seller1", "Seller"),
    "buyer1": Account("Buyer One", "buyer1@example.com", "buyer1", "Buyer"),
}
books = {}
def front_page():
    global front_page_frame 

    # Check if front_page_frame exists, if not create it
    if not hasattr(root, 'front_page_frame'):
        front_page_frame = tk.Frame(root, bg="#333333")

        # Header Label: "Welcome to MGA Bookstore"
        header_label = tk.Label(front_page_frame, text="Welcome to Knights BookExchange!", 
                                bg="#333333", fg="#FFFFFF", font=("Arial", 24, "bold"))
        header_label.pack(pady=20)

        # Add an image above the buttons
        try:
            # Load the image using tk.PhotoImage (if using .png or .gif)
            image = PhotoImage(file="images/logo.jpg")  # Replace with your image file
        except:
            # Using PIL for other image formats (e.g., .jpg)
            image = Image.open("images/logo.jpg")  # Replace with your image file
            image = ImageTk.PhotoImage(image.resize((200, 200)))  # Resize if needed

        image_label = tk.Label(front_page_frame, image=image, bg="#333333")
        image_label.image = image  # Keep reference to avoid garbage collection
        image_label.pack(pady=10)

        # Create the "Start" button for login
        login_button = tk.Button(front_page_frame, 
                                  text="Start", 
                                  width=20,
                                  height=2,  
                                  bg="#9d00ff",  
                                  fg="white",  
                                  font=("Arial", 14),  
                                  command=login_page)  # Ensure login_page is the command
        login_button.place(relx=0.5, rely=0.5, anchor="center")

        # Create the "Exit" button to quit the application
        exit_button = tk.Button(front_page_frame, 
                                 text="Exit", 
                                 width=20,
                                 height=2,  
                                 bg="#9d00ff",  
                                 fg="white",  
                                 font=("Arial", 14),
                                 command=root.quit)
        exit_button.place(relx=0.5, rely=0.6, anchor="center")

    # Hide all other frames and show the front page
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame) and widget != front_page_frame:
            widget.pack_forget()

    # Pack the front page frame to make it visible
    front_page_frame.pack(fill="both", expand=True)


def login_page():
    global login_frame, login_username_entry 

    # Clear the front page frame when transitioning to the login page
    for widget in front_page_frame.winfo_children():
        widget.destroy()
    front_page_frame.pack_forget()

    # Create the login frame if it doesn't exist
    if not hasattr(root, 'login_frame'):

        # Login Frame
        login_frame = tk.Frame(root, bg="#333333")

        # Username Label and Entry
        login_username_label = tk.Label(login_frame, text="Username", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
        login_username_label.pack(pady=10)
        login_username_entry = tk.Entry(login_frame, font=("Arial", 14))
        login_username_entry.pack(pady=20)

        # Login Button
        login_button = tk.Button(login_frame, text="Login", bg="#9d00ff", font=("Arial", 14), fg="#FFFFFF", command=login)
        login_button.pack(pady=20)
         # Back Button: Goes back to the front page
        back_button = tk.Button(login_frame, text="Back", bg="#9d00ff", font=("Arial", 14), fg="#FFFFFF", command=front_page)
        back_button.pack(pady=10)

        # Pack the login frame to make it visible
        login_frame.pack(fill="both", expand=True)

    

def login():
    global login_username_entry  # Ensure it's the same variable as in the login_page

    username = login_username_entry.get()

    # Simulate password check (replace with actual password check if needed)
    if username in users:
        messagebox.showinfo(title="Login Success", message=f"Welcome, {username}!")
        show_role_menu(users[username])
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

    login_username_entry.delete(0, tk.END)

def show_role_menu(user):
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.pack_forget()
    
    if user.role == "Admin":
        admin_menu(user)
    elif user.role == "Seller":
        seller_menu(user)
    elif user.role == "Buyer":
        buyer_menu(user)

def admin_menu(user):
    # Hide or clear the create_account_frame
    for widget in create_account_frame.winfo_children():
        widget.destroy()  # Clear all widgets in the create_account_frame
    create_account_frame.pack_forget()  # Hide the frame

    # Show the admin menu
    admin_frame.pack(fill="both", expand=True)

    # Recreate admin menu buttons
    create_account_button = tk.Button(admin_frame, 
                              text="Create Account", 
                              width=20,
                              height=2,  
                              bg="#9d00ff",  
                              fg="white",  
                              font=("Arial", 14),
                              command=lambda: create_account(user))
    create_account_button.pack(pady=20)

    delete_account_button = tk.Button(admin_frame, 
                              text="Delete Account", 
                              width=20,
                              height=2,  
                              bg="#9d00ff",  
                              fg="white",  
                              font=("Arial", 14),
                              command=lambda: delete_account(user))
    delete_account_button.pack(pady=20)

    report_users_button = tk.Button(admin_frame, 
                              text="Report Users", 
                              width=20,
                              height=2,  
                              bg="#9d00ff",  
                              fg="white",  
                              font=("Arial", 14),
                              command=report_users)
    report_users_button.pack(pady=20)

    report_books_button = tk.Button(admin_frame, 
                              text="Report Books", 
                              width=20,
                              height=2,  
                              bg="#9d00ff",  
                              fg="white",  
                              font=("Arial", 14),
                              command=report_books)
    report_books_button.pack(pady=20)

    logout_button = tk.Button(admin_frame, 
                              text="Logout", 
                              width=20,
                              height=2,  
                              bg="#ff4d4d",  
                              fg="white",  
                              font=("Arial", 14),
                              command=logout)
    logout_button.pack(pady=20)
    
    

    
def seller_menu(user):
    seller_frame.pack(fill="both", expand=True)

    # List Books
    list_books_button = tk.Button(seller_frame, 
                              text="List Books", 
                              width=20,
                              height=2,  
                              bg="#9d00ff",  
                              fg="white",  
                              font=("Arial", 14),
                              command=lambda: list_books(user))
    list_books_button.pack(pady=20)

    # Delete Books
    delete_books_button = tk.Button(seller_frame, 
                              text="Delete Books", 
                              width=20,
                              height=2,  
                              bg="#9d00ff",  
                              fg="white",  
                              font=("Arial", 14),
                              command=lambda: delete_books(user))
    delete_books_button.pack(pady=20)

    # Report Books
    report_books_button = tk.Button(seller_frame, 
                              text="Report Books", 
                              width=20,
                              height=2,  
                              bg="#9d00ff",  
                              fg="white",  
                              font=("Arial", 14),
                              command=report_books)
    report_books_button.pack(pady=20)

    # Logout
    logout_button = tk.Button(seller_frame, 
                              text="Logout", 
                              width=20,
                              height=2,  
                              bg="#ff4d4d",  
                              fg="white",  
                              font=("Arial", 14),
                              command=logout)
    logout_button.pack(pady=20)

def buyer_menu(user):
    buyer_frame.pack(fill="both", expand=True)

    # Buy Books
    buy_books_button = tk.Button(buyer_frame, 
                              text="Buy Books", 
                              width=20,
                              height=2,  
                              bg="#9d00ff",  
                              fg="white",  
                              font=("Arial", 14),
                              command=lambda: buy_books(user))
    buy_books_button.pack(pady=20)

    # Report Books
    report_books_button = tk.Button(buyer_frame, 
                              text="Report Books", 
                              width=20,
                              height=2,  
                              bg="#9d00ff",  
                              fg="white",  
                              font=("Arial", 14),
                              command=lambda: (report_books()))
    report_books_button.pack(pady=20)

    # Logout
    # Logout button in buyer_menu
    logout_button = tk.Button(buyer_frame, 
                            text="Logout", 
                            width=20,
                            height=2,  
                            bg="#ff4d4d",  
                            fg="white",  
                            font=("Arial", 14), 
                            command=lambda: logout_from_menu(buyer_frame))
    logout_button.pack(pady=20)


# Admin functions
def create_account(current_user):
    # Unpack all frames to display only the create_account_frame
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.pack_forget()

    # Clear admin_frame widgets if needed
    for widget in admin_frame.winfo_children():
        widget.destroy()

       # Display the create account frame
    create_account_frame.pack(fill="both", expand=True)

    # Create Account Frame
    
    name_label = tk.Label(create_account_frame, text="Name", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
    name_label.pack(pady=5)
    name_entry = tk.Entry(create_account_frame, font=("Arial", 14))
    name_entry.pack(pady=5)
    email_label = tk.Label(create_account_frame, text="Email", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
    email_label.pack(pady=5)
    email_entry = tk.Entry(create_account_frame, font=("Arial", 14))
    email_entry.pack(pady=5)
    username_label = tk.Label(create_account_frame, text="Username", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
    username_label.pack(pady=5)
    username_entry = tk.Entry(create_account_frame, font=("Arial", 14))
    username_entry.pack(pady=5)
    role_label = tk.Label(create_account_frame, text="Role", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
    role_label.pack(pady=5)
    role_entry = tk.Entry(create_account_frame, font=("Arial", 14))
    role_entry.pack(pady=5)
    
    def add_account():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        username = username_entry.get().strip()
        role = role_entry.get().strip()

        # Input validation
        if not name or not email or not username or not role:
            messagebox.showerror("Error", "All fields are required.")
            return

        if username in users:
            messagebox.showerror("Error", f"Username '{username}' already exists.")
            return

        if role not in ["Admin", "Seller", "Buyer"]:
            messagebox.showerror("Error", "Role must be 'Admin', 'Seller', or 'Buyer'.")
            return

        # Add the new user to the dictionary
        users[username] = Account(name, email, username, role)
        messagebox.showinfo("Success", f"Account for '{username}' created successfully!")

        # Clear the entries after creation
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        role_entry.delete(0, tk.END)

    create_account_button = tk.Button(create_account_frame, text="Create Account", bg="#9d00ff", font=("Arial", 14), fg="#FFFFFF", command=add_account)
    create_account_button.pack(pady=30)

    back_button = tk.Button(
        create_account_frame,
        text="Back",
        bg="#9d00ff",
        font=("Arial", 14),
        fg="#FFFFFF",
        command=lambda: admin_menu(current_user)
    )
    back_button.pack(pady=30)

def delete_account(current_user):

    global delete_account_frame

    # Unpack all frames to display only the delete_account_frame
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.pack_forget()

    
    for widget in admin_frame.winfo_children():
        widget.destroy()

    # Display the delete account frame
    delete_account_frame = tk.Frame(root, bg="#333333")
    delete_account_frame.pack(fill="both", expand=True)

    # Username entry for deletion
    username_label = tk.Label(delete_account_frame, text="Enter Username to Delete", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
    username_label.pack(pady=5)
    username_entry = tk.Entry(delete_account_frame, font=("Arial", 14))
    username_entry.pack(pady=5)

    # Function to remove the account
    def remove_account():
        username = username_entry.get().strip()

        if not username:
            messagebox.showerror("Error", "Username is required.")
            return

        if username not in users:
            messagebox.showerror("Error", f"Username '{username}' does not exist.")
            return

        if username == "admin":
            messagebox.showerror("Error", "Cannot delete the default admin account.")
            return

        # Confirm deletion
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{username}'?")
        if confirm:
            del users[username]
            messagebox.showinfo("Success", f"Account for '{username}' has been deleted.")
            username_entry.delete(0, tk.END)

    # Delete Account button
    delete_account_button = tk.Button(
        delete_account_frame,
        text="Delete Account",
        bg="#ff4d4d",
        font=("Arial", 14),
        fg="#FFFFFF",
        command=remove_account
    )
    delete_account_button.pack(pady=20)

    # Back button to return to admin menu
    back_button = tk.Button(
        delete_account_frame,
        text="Back",
        bg="#9d00ff",
        font=("Arial", 14),
        fg="#FFFFFF",
        command=lambda: back_to_admin_menu(current_user)
    )
    back_button.pack(pady=30)

def back_to_admin_menu(current_user):
    # Clear the delete_account_frame and go back to the admin menu
    for widget in delete_account_frame.winfo_children():
        widget.destroy()  # Clear widgets from delete_account_frame

    # Hide the delete account frame
    delete_account_frame.pack_forget()

    # Show the admin menu again
    admin_menu(current_user)





def report_users():
    user_info = "\n".join([f"{user.name} ({user.username}) - {user.role}" for user in users.values()])
    messagebox.showinfo("User Report", user_info)

def report_books():
    book_info = "\n".join([f"Item # {book.item_num}: {book.title} by {book.author} - ${book.price} ({book.status})" for book in books.values()])
    messagebox.showinfo("Book Report", book_info)

def list_books(user):
    # Clear widgets in the list frame to prevent duplication
    for widget in list_frame.winfo_children():
        widget.destroy() 

    seller_frame.pack_forget()  # Hide the seller frame
    list_frame.pack(fill="both", expand=True)  # Show the List Books frame

    # Add labels and entry fields
    item_num_label = tk.Label(list_frame, text="Item Number", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
    item_num_label.pack(pady=5)
    item_num_entry = tk.Entry(list_frame, font=("Arial", 14))
    item_num_entry.pack(pady=5)
    title_label = tk.Label(list_frame, text="Book Title", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
    title_label.pack(pady=5)
    title_entry = tk.Entry(list_frame, font=("Arial", 14))
    title_entry.pack(pady=5)
    author_label = tk.Label(list_frame, text="Book Author", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
    author_label.pack(pady=5)
    author_entry = tk.Entry(list_frame, font=("Arial", 14))
    author_entry.pack(pady=5)
    price_label = tk.Label(list_frame, text="Book Price", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
    price_label.pack(pady=5)
    price_entry = tk.Entry(list_frame, font=("Arial", 14))
    price_entry.pack(pady=5)

    def submit_book():
        item_num = item_num_entry.get().strip()
        title = title_entry.get().strip()
        author = author_entry.get().strip()
        price = price_entry.get().strip()

        # Validate inputs
        if not item_num or not title or not author or not price:
            messagebox.showerror("Error", "All fields are required.")
            return
        if item_num in books:
            messagebox.showerror("Error", f"Book with Item Number '{item_num}' already exists.")
            return
        try:
            price = float(price)
            if price <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Price must be a valid number greater than 0.")
            return

        # Add the book
        books[item_num] = Book(item_num, title, author, price, user.username)
        messagebox.showinfo("Success", f"Book '{title}' has been listed successfully!")
        item_num_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)

    list_button = tk.Button(list_frame, text="Submit", bg="#9d00ff", font=("Arial", 14), fg="#FFFFFF", command=submit_book)
    list_button.pack(pady=10)

    back_button = tk.Button(
        list_frame,
        text="Back",
        bg="#9d00ff",
        font=("Arial", 14),
        fg="#FFFFFF",
        command=lambda: back_to_seller_from_list_books(user)
    )
    back_button.pack(pady=10)



def back_to_seller_from_list_books(user):
    # Hide the List Books frame
    for widget in seller_frame.winfo_children():
        widget.destroy()
    list_frame.pack_forget()

    # Redisplay seller menu
    seller_menu(user)



def delete_books(user):
    # Clear widgets in the delete frame to prevent duplication
    for widget in delete_frame.winfo_children():
        widget.destroy()

    # Hide the seller frame
    seller_frame.pack_forget()

    # Display the delete books interface
    delete_book_label = tk.Label(delete_frame, text="Enter the Item Number of the Book to Delete", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
    delete_book_label.pack(pady=5)

    delete_book_entry = tk.Entry(delete_frame, font=("Arial", 14))
    delete_book_entry.pack(pady=5)

    def confirm_delete():
        item_num = delete_book_entry.get().strip()

        # Input validation
        if not item_num:
            messagebox.showerror("Error", "Item number is required.")
            return

        if item_num not in books:
            messagebox.showerror("Error", f"No book found with Item Number '{item_num}'.")
            return

        book = books[item_num]

        # Check if the book is available
        if book.status == "Available":
            messagebox.showinfo("Info", f"The book '{book.title}' is still in stock.")
            return

        # Delete the book from the dictionary
        del books[item_num]
        messagebox.showinfo("Success", f"Book '{book.title}' has been deleted successfully!")

        # Clear the input field
        delete_book_entry.delete(0, tk.END)

    # Delete Button
    delete_button = tk.Button(delete_frame, text="Delete Book", bg="#9d00ff", font=("Arial", 14), fg="#FFFFFF", command=confirm_delete)
    delete_button.pack(pady=10)

    # Back Button
    back_button = tk.Button(delete_frame, text="Back", bg="#9d00ff", font=("Arial", 14), fg="#FFFFFF", command=lambda: back_to_seller_from_delete_books(user))
    back_button.pack(pady=10)

    # Show the delete frame
    delete_frame.pack(fill="both", expand=True)

def back_to_seller_from_delete_books(user):
    # Clear widgets in seller_frame to prevent duplication
    for widget in seller_frame.winfo_children():
        widget.destroy()

    # Hide the delete frame
    delete_frame.pack_forget()

    # Redisplay seller menu
    seller_menu(user)




def buy_books(user):
    # Clear the buyer frame
    for widget in buyer_frame.winfo_children():
        widget.destroy()

    # Ensure buy_book_frame exists and is managed
    global buy_book_frame
    buy_book_frame = tk.Frame(root, bg="#333333")
    buy_book_frame.place(relx=0.5, rely=0.5, anchor="center")

    def back_to_buyer_menu(user):
        # Clear the buy_book_frame and return to buyer menu
        for widget in buy_book_frame.winfo_children():
            widget.destroy()
        buy_book_frame.place_forget()  # This removes the frame and prevents the overlay

        # Redisplay the buyer menu
        buyer_menu(user)

    # Display widgets for the buy books interface
    buy_book_label = tk.Label(buy_book_frame, text="Enter the Item Number of the Book to Buy", bg="#333333", fg="#FFFFFF", font=("Arial", 14))
    buy_book_label.pack(pady=5)

    item_num_entry = tk.Entry(buy_book_frame, font=("Arial", 14))
    item_num_entry.pack(pady=5)

    def confirm_purchase():
        item_num = item_num_entry.get().strip()

        # Validation for input
        if not item_num:
            messagebox.showerror("Error", "Item number is required.")
            return

        # Check if the book exists in the inventory
        if item_num not in books:
            messagebox.showerror("Error", f"No book found with Item Number '{item_num}'.")
            return

        book = books[item_num]

        # Check if the book is already sold
        if book.status == "Sold":
            messagebox.showinfo("Info", f"The book '{book.title}' is already sold.")
            return

        # Mark the book as sold
        book.status = "Sold"

        # Display transaction summary
        messagebox.showinfo("Success", f"You have successfully bought '{book.title}' by {book.author} for ${book.price:.2f}!")

        # Clear the entry field
        item_num_entry.delete(0, tk.END)

    # Buy Button
    buy_button = tk.Button(buy_book_frame, text="Buy Book", bg="#9d00ff", font=("Arial", 14), fg="#FFFFFF", command=confirm_purchase)
    buy_button.pack(pady=10)

    # Back Button
    back_button = tk.Button(buy_book_frame, text="Back", bg="#9d00ff", font=("Arial", 14), fg="#FFFFFF", command=lambda: back_to_buyer_menu(user))
    back_button.pack(pady=10)

    # Pack the buy_book_frame to make it visible
    buy_book_frame.place(relx=0.5, rely=0.5, anchor="center")

# Logout function

def logout_from_menu(current_frame):
    # Clear the current frame
    for widget in current_frame.winfo_children():
        widget.destroy()
    current_frame.pack_forget()  # Hide the current frame

    for widget in login_frame.winfo_children():
        widget.destroy()

    # Show the front page again
    front_page() 

def logout():
    # Hide all frames by clearing them
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.pack_forget()

    # Clear any user-specific frames
    for widget in admin_frame.winfo_children():
        widget.destroy()

    for widget in seller_frame.winfo_children():
        widget.destroy()

    for widget in buyer_frame.winfo_children():
        widget.destroy()

    for widget in front_page_frame.winfo_children():
        widget.destroy()

    for widget in buy_book_frame.winfo_children():
        widget.destroy()

    # Show the front page again
    front_page()

# Front Page
root = tk.Tk()
root.title("Book System")
root.geometry("1200x800")
root.configure(bg="#333333")

# Front Page Frame
front_page_frame = tk.Frame(root, bg="#333333")
login_button = tk.Button(front_page_frame, 
                              text="Start", 
                              width=20,
                              height=2,  
                              bg="#9d00ff",  
                              fg="white",  
                              font=("Arial", 14),  
                              command=login_page)
login_button.place(relx=0.5, rely=0.4, anchor="center")

exit_button = tk.Button(front_page_frame, 
                              text="Exit", 
                              width=20,
                              height=2,  
                              bg="#9d00ff",  
                              fg="white",  
                              font=("Arial", 14),
                              command=root.quit)
exit_button.place(relx=0.5, rely=0.5, anchor="center")

create_account_frame = tk.Frame(root, bg="#333333")
# Admin Frame
admin_frame = tk.Frame(root, bg="#333333")

# Seller Frame
seller_frame = tk.Frame(root, bg="#333333")

# Buyer Frame
buyer_frame = tk.Frame(root, bg="#333333")

# Seller List Book Frame
list_frame = tk.Frame(root, bg="#333333")

# Delete Book Frame 
delete_frame = tk.Frame(root, bg="#333333")

buy_book_frame = tk.Frame(root, bg="#333333")

# Start with the front page
front_page()

root.mainloop()
