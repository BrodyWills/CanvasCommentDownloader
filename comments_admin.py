import tkinter as tk
from tkinter import messagebox
from canvasapi import Canvas

def fetch_comments(api_url, api_key, course_id, user_id, output_file):
    """Fetch comments for a specific user's submissions in the course and save to a text file."""
    try:
        # Initialize Canvas API
        canvas = Canvas(api_url, api_key)
        course = canvas.get_course(course_id)

        # Open the file in write mode with UTF-8 encoding
        with open(output_file, 'w', encoding='utf-8') as file:
            # Fetch all assignments and their comments
            comments_output = ""
            for assignment in course.get_assignments():
                try:
                    submission = assignment.get_submission(user_id, include=['submission_comments'])
                    if submission and submission.submission_comments:
                        comments_output += f"\nAssignment: {assignment.name}\n"
                        comments_output += "=" * len(f"Assignment: {assignment.name}") + "\n"
                        for comment in submission.submission_comments:
                            # Extract the comment content
                            content = comment.get('comment', 'No content available')

                            # Replace non-breaking spaces with regular spaces only
                            content = content.replace('\u00A0', ' ')

                            # Add comment to output without modifying other spacing
                            comments_output += f"{content}\n"
                            comments_output += "-" * 40 + "\n"

                except Exception as e:
                    # Skip assignments that the user didn't submit or other issues
                    comments_output += f"\nAssignment: {assignment.name} - No submission or error occurred.\n"

            # If comments are found, write them to the file
            if comments_output.strip():
                file.write(comments_output)
                messagebox.showinfo("Success", f"Comments saved to {output_file}")
            else:
                file.write("No comments found for the specified user.")
                messagebox.showinfo("No Comments", "No comments found for the specified user.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def submit_form():
    """Handle the form submission from the GUI."""
    api_url = api_url_entry.get()
    api_key = api_key_entry.get()
    try:
        course_id = int(course_id_entry.get())  # Ensure course_id is an integer
    except ValueError:
        messagebox.showerror("Invalid Input", "Course ID must be an integer.")
        return

    try:
        user_id = int(user_id_entry.get())  # Ensure user_id is an integer
    except ValueError:
        messagebox.showerror("Invalid Input", "User ID must be an integer.")
        return

    output_file = output_file_entry.get()  # Get output file path

    # Call fetch_comments function
    fetch_comments(api_url, api_key, course_id, user_id, output_file)

def create_gui():
    """Create the Tkinter GUI."""
    # Create the main window
    root = tk.Tk()
    root.title("Canvas Comment Fetcher")

    # Create and place the labels and input fields
    tk.Label(root, text="Canvas API URL:").grid(row=0, column=0, padx=10, pady=5)
    global api_url_entry
    api_url_entry = tk.Entry(root, width=40)
    api_url_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="API Key:").grid(row=1, column=0, padx=10, pady=5)
    global api_key_entry
    api_key_entry = tk.Entry(root, width=40, show='*')  # Mask API key for security
    api_key_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Course ID:").grid(row=2, column=0, padx=10, pady=5)
    global course_id_entry
    course_id_entry = tk.Entry(root, width=40)
    course_id_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="User ID:").grid(row=3, column=0, padx=10, pady=5)
    global user_id_entry
    user_id_entry = tk.Entry(root, width=40)
    user_id_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Output File Path:").grid(row=4, column=0, padx=10, pady=5)
    global output_file_entry
    output_file_entry = tk.Entry(root, width=40)
    output_file_entry.grid(row=4, column=1, padx=10, pady=5)

    # Submit button
    submit_button = tk.Button(root, text="Fetch Comments", command=submit_form)
    submit_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Run the main GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
