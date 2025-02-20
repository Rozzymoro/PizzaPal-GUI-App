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

        # Create selection menu
        self.create_selection_menu()

        # Create buttons
        self.create_buttons()

    def load_image(self):
        # Load the pizza image
        try:
            self.pizza_image = Image.open("pizza_image.png")  # Ensure the image path is correct
            self.pizza_image = self.pizza_image.resize((200, 150), Image.ANTIALIAS)  # Resize the image
            self.pizza_photo = ImageTk.PhotoImage(self.pizza_image)

            # Display the image in a label
            self.image_label = tk.Label(self.root, image=self.pizza_photo)
            self.image_label.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Image Error", f"Could not load image: {e}")

    def create_labels(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Select Your Pizza", font=("Arial", 14))
        self.title_label.pack()

    def create_selection_menu(self):
        # Pizza selection
        self.pizza_options = ["Margherita", "Pepperoni", "BBQ Chicken", "Veggie"]
        self.pizza_var = tk.StringVar()
        self.pizza_var.set("Select Pizza")
        self.pizza_menu = tk.OptionMenu(self.root, self.pizza_var, *self.pizza_options)
        self.pizza_menu.pack(pady=5)

        # Size selection
        self.size_options = ["Small", "Medium", "Large"]
        self.size_var = tk.StringVar()
        self.size_var.set("Select Size")
        self.size_menu = tk.OptionMenu(self.root, self.size_var, *self.size_options)
        self.size_menu.pack(pady=5)

    def create_buttons(self):
        # Order button
        self.order_button = tk.Button(self.root, text="Submit Order", command=self.submit_order)
        self.order_button.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Selections", command=self.reset_selections)
        self.reset_button.pack()

        # Exit button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.confirm_exit)
        self.exit_button.pack(pady=10)

    def submit_order(self):
        pizza_choice = self.pizza_var.get()
        size_choice = self.size_var.get()

        if pizza_choice == "Select Pizza" or size_choice == "Select Size":
            messagebox.showerror("Input Error", "Please select a pizza and size before ordering.")
            return

        order_summary = f"You ordered a {size_choice} {pizza_choice} pizza."
        messagebox.showinfo("Order Summary", order_summary)

    def reset_selections(self):
        self.pizza_var.set("Select Pizza")
        self.size_var.set("Select Size")

    def confirm_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaPalApp(root)
    root.mainloop()
