import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For handling images
import os

# Main Application Class
class PizzaPalApp:
    def __init__(self, root):
        """Initialize the PizzaPal GUI application."""
        self.root = root
        self.root.title("PizzaPal - Order Your Pizza")
        self.root.geometry("500x400")  # Set window size

        # Load and display the pizza image
        self.load_image()

        # Create labels
        self.create_labels()

        # Create selection menu
        self.create_selection_menu()

        # Create buttons
        self.create_buttons()

    def load_image(self):
        """Loads the pizza image from the images folder and displays it in the GUI."""
        # Get absolute path of the image
        image_path = os.path.abspath("images/pizza_image.png")
        print(f"Looking for image at: {image_path}")  # Debugging print

        # Load the pizza image
        try:
            self.pizza_image = Image.open(image_path)  # Use absolute path
            self.pizza_image = self.pizza_image.resize((200, 150), Image.LANCZOS)  # Resize the image
            self.pizza_photo = ImageTk.PhotoImage(self.pizza_image)

            # Display the image in a label
            self.image_label = tk.Label(self.root, image=self.pizza_photo)
            self.image_label.pack(pady=10)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Pizza image not found at: {image_path}\nPlease check the file path.")
        except Exception as e:
            messagebox.showerror("Image Error", f"Could not load image: {e}")

    def create_labels(self):
        """Creates labels for the application, including the welcome message."""
        self.welcome_label = tk.Label(self.root, text="Welcome to PizzaPal!", font=("Arial", 16))
        self.welcome_label.pack(pady=10)

        # Pizza size label
        self.size_label = tk.Label(self.root, text="Select Your Pizza Size:", font=("Arial", 12))
        self.size_label.pack()

    def create_selection_menu(self):
        """Creates dropdown menus for selecting pizza type and size."""
        self.pizza_options = ["Margherita", "Pepperoni", "BBQ Chicken", "Veggie"]
        self.pizza_var = tk.StringVar()
        self.pizza_var.set("Select Pizza")
        self.pizza_menu = tk.OptionMenu(self.root, self.pizza_var, *self.pizza_options)
        self.pizza_menu.pack(pady=5)

        # Toppings label
        self.toppings_label = tk.Label(self.root, text="Choose Your Toppings:", font=("Arial", 12))
        self.toppings_label.pack()

        # Size selection
        self.size_options = ["Small", "Medium", "Large"]
        self.size_var = tk.StringVar()
        self.size_var.set("Select Size")
        self.size_menu = tk.OptionMenu(self.root, self.size_var, *self.size_options)
        self.size_menu.pack(pady=5)

    def create_buttons(self):
        """Creates all buttons for user interaction, including Add to Cart and Exit."""
        self.add_to_cart_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack(pady=10)

        self.order_button = tk.Button(self.root, text="Submit Order", command=self.submit_order)
        self.order_button.pack(pady=10)

        self.view_cart_button = tk.Button(self.root, text="View Cart", command=self.view_cart)
        self.view_cart_button.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Reset Selections", command=self.reset_selections)
        self.reset_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.confirm_exit)
        self.exit_button.pack(pady=10)

    def add_to_cart(self):
        """Displays a message indicating that the pizza has been added to the cart."""
        messagebox.showinfo("Add to Cart", "Your pizza has been added to the cart!")

    def submit_order(self):
        """Handles the pizza order submission and displays a summary of the order."""
        pizza_choice = self.pizza_var.get()
        size_choice = self.size_var.get()
        if pizza_choice == "Select Pizza" or size_choice == "Select Size":
            messagebox.showerror("Input Error", "Please select a pizza and size before ordering.")
            return
        order_summary = f"You ordered a {size_choice} {pizza_choice} pizza."
        messagebox.showinfo("Order Summary", order_summary)

    def reset_selections(self):
        """Resets the pizza and size selection menus to their default values."""
        self.pizza_var.set("Select Pizza")
        self.size_var.set("Select Size")

    def view_cart(self):
        """Opens a new window displaying the user's current order summary."""
        messagebox.showinfo("View Cart", "This will open the order summary window.")

    def confirm_exit(self):
        """Asks the user for confirmation before closing the application."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaPalApp(root)
    root.mainloop()
