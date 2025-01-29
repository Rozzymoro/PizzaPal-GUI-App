import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For handling images

# Main Application Class
class PizzaPalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PizzaPal - Order Your Pizza")
        self.root.geometry("500x400")  # Set window size

        # Load and display the pizza image
        self.load_image()

        # Create labels
        self.create_labels()

        # Create buttons
        self.create_buttons()

    def load_image(self):
        # Load the pizza image
        try:
            self.pizza_image = Image.open("images/pizza_image.png")  # Ensure the image path is correct
            self.pizza_image = self.pizza_image.resize((200, 150), Image.ANTIALIAS)  # Resize the image
            self.pizza_photo = ImageTk.PhotoImage(self.pizza_image)

            # Display the image in a label
            self.image_label = tk.Label(self.root, image=self.pizza_photo)
            self.image_label.pack(pady=10)
        except FileNotFoundError:
            messagebox.showerror("Error", "Pizza image not found! Please check the file path.")

    def create_labels(self):
        # Welcome label
        self.welcome_label = tk.Label(self.root, text="Welcome to PizzaPal!", font=("Arial", 16))
        self.welcome_label.pack(pady=10)

        # Pizza size label
        self.size_label = tk.Label(self.root, text="Select Your Pizza Size:", font=("Arial", 12))
        self.size_label.pack()

        # Toppings label
        self.toppings_label = tk.Label(self.root, text="Choose Your Toppings:", font=("Arial", 12))
        self.toppings_label.pack()

    def create_buttons(self):
        # Add to Cart button
        self.add_to_cart_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack(pady=10)

        # View Cart button
        self.view_cart_button = tk.Button(self.root, text="View Cart", command=self.view_cart)
        self.view_cart_button.pack(pady=10)

        # Exit button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=10)

    def add_to_cart(self):
        # Placeholder function for adding items to the cart
        messagebox.showinfo("Add to Cart", "Your pizza has been added to the cart!")

    def view_cart(self):
        # Placeholder function for viewing the cart
        messagebox.showinfo("View Cart", "This will open the order summary window.")

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaPalApp(root)
    root.mainloop()
