import tkinter as tk
from searchDB import *


# Function to paste from clipboard
def paste_from_clipboard(input_box, root):
    try:
        clipboard_content = root.clipboard_get()
        input_box.delete(0, tk.END)  # Clear any existing text
        input_box.insert(0, clipboard_content)  # Paste clipboard content
    except tk.TclError:
        show_result("אין טקסט להדבקה.", root)


# Function to handle search
def handle_search(search_type, input_box, lords_name, online_search, root):
    user_input = input_box.get()
    include_lords_name = lords_name.get() if lords_name else False  # Get the Checkbutton state if available
    enable_online_search = online_search.get() if online_search else False

    if search_type == 'פסוק':  # חיפוש לפי פסוק

        result = search_sefaria_export(user_input, include_lords_name, enable_online_search)
        if result is None:
            result = " סתם"
    elif search_type == 'מראה מקום':  # חיפוש לפי מראה מקום
        result = find_by_loc(user_input, enable_online_search)
        if result is None:
            result = " סתם"
    else:
        result = "לא הוגדר"

    show_result(result, root)


# Function to show result
def show_result(result, root):
    for widget in root.winfo_children():
        widget.pack_forget()  # Hide all widgets

    # Add a label for context
    result_label = tk.Label(root, text="תוצאות החיפוש:", font=("Open Sans", 16))
    result_label.pack(pady=10)

    # Create a frame to hold the text widget and scrollbar
    frame = tk.Frame(root)
    frame.pack(pady=10, fill="both", expand=True)

    # Create a Text widget for displaying results
    result_box = tk.Text(frame, font=("Open Sans", 14), wrap="word", height=3, width=30)
    result_box.insert("1.0", result)  # Insert the result text
    result_box.config(state="normal")  # Allow interaction for copying
    result_box.pack(side="left", fill="both", expand=True)

    # Add a vertical scrollbar
    scrollbar = tk.Scrollbar(frame, command=result_box.yview)
    scrollbar.pack(side="right", fill="y")
    result_box.config(yscrollcommand=scrollbar.set)

    # Function to copy the result text to clipboard
    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(result)
        root.update()  # Now the clipboard is updated
        copied_label.config(text="הטקסט הועתק בהצלחה", fg="green")

    # Add a "Copy to Clipboard" button
    copy_button = tk.Button(root, text="העתק", font=("Open Sans", 14), bg="#e6ebe9", fg="black", command=copy_to_clipboard)
    copy_button.pack(pady=10)

    # Label to confirm copy action
    copied_label = tk.Label(root, text="", font=("Open Sans", 12), fg="red")
    copied_label.pack(pady=5)

    # Back button to return to the main menu
    back_button = tk.Button(root, text="חזרה", font=("Open Sans", 14), bg="#e6ebe9", fg="black", command=lambda: show_main_menu(root))
    back_button.pack(pady=10)


# Function to show text input
def show_text_input(search_type, root):
    for widget in root.winfo_children():
        widget.pack_forget()  # Hide all widgets

    # Display the appropriate label and text box
    label = tk.Label(root, text=f"הכנס {search_type}:", font=("Open Sans", 16))
    label.pack(pady=10)

    input_box = tk.Entry(root, width=40, font=("Open Sans", 14))
    input_box.pack(pady=10)

    # Add a "Paste from Clipboard" button
    paste_button = tk.Button(root, text="הדבק טקסט", font=("Open Sans", 14), bg="#e6ebe9", fg="black",
                             command=lambda: paste_from_clipboard(input_box, root))
    paste_button.pack(pady=5)

    lords_name = None
    online_search = None

    if search_type == 'פסוק':
        # Checkbutton tied to `lords_name`
        lords_name = tk.BooleanVar(value=False)  # Variable to track the state
        check_button = tk.Checkbutton(root, text="שם השם חסר", font=("Open Sans", 14),
                                      variable=lords_name, onvalue=True, offvalue=False)
        check_button.pack(pady=5)

    # Checkbutton for online search
    online_search = tk.BooleanVar(value=False)
    online_check_button = tk.Checkbutton(root, text="חיפוש אונליין", font=("Open Sans", 14),
                                         variable=online_search, onvalue=True, offvalue=False)
    online_check_button.pack(pady=5)

    search_button = tk.Button(root, text="חיפוש", font=("Open Sans", 14), bg="#e6ebe9", fg="black",
                              command=lambda: handle_search(search_type, input_box, lords_name, online_search, root))
    search_button.pack(pady=10)

    # Back button to return to the main menu
    back_button = tk.Button(root, text="חזרה", font=("Open Sans", 14), bg="#e6ebe9", fg="black", command=lambda: show_main_menu(root))
    back_button.pack(pady=10)


# Function to show the main menu
def show_main_menu(root):
    for widget in root.winfo_children():
        widget.pack_forget()  # Hide all widgets

    title = tk.Label(root, text="חיפוש במקורות", font=("Open Sans", 24, "bold"), bg="#dff2f2", fg="black")
    title.pack(pady=10, fill="y")

    verse_button = tk.Button(root, text='חיפוש לפי פסוק', font=("Open Sans", 14), bg="#e6ebe9", fg="black",
                             command=lambda: show_text_input("פסוק", root))
    verse_button.pack(pady=10)

    reference_button = tk.Button(root, text='חיפוש לפי מראה מקום', font=("Open Sans", 14), bg="#e6ebe9", fg="black",
                                 command=lambda: show_text_input("מראה מקום", root))
    reference_button.pack(pady=10)


# Initialize the app
def main():
    root = tk.Tk()
    root.configure(bg="#dff2f2")
    root.title("חיפוש במקורות")

    root.geometry("500x300")
    show_main_menu(root)
    root.mainloop()


if __name__ == "__main__":
    main()
