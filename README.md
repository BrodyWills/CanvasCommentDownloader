# Canvas Submission Comments Exporter

This program allows you to export all comments on your Canvas assignments into a `.txt` file. It will prompt you to enter your **Canvas API URL**, **API Key**, **Course ID**, and the **file path** where the results will be exported.

## Features

- Retrieve submission comments from all assignments in your Canvas course.
- Export the assignment names and comments into a `.txt` file at the location you specify.
- Simple to use: just provide your Canvas **API URL**, **API Key**, **Course ID**, and the location where you'd like to save the output.

## Requirements

- **Windows 10/11** or similar OS for the executable.
- **Canvas API Key**: You can generate this from your Canvas account settings.
- **Canvas Course ID**: This is the ID of the Canvas course you wish to fetch submission comments from.

## How to Use

1. **Download the Executable:**

   Download the latest version of the executable from the [releases page](https://github.com/BrodyWills/CanvasCommentDownloader/releases/tag/release).

2. **Run the Executable:**

   After downloading the `.exe` file, simply double-click it to run the program. It will prompt you to enter the following details:

   - **Canvas API URL**: This is the base URL for your Canvas instance (e.g., `https://your-school.instructure.com`).
   - **Canvas API Key**: Your personal API key from Canvas. You can generate it in the Canvas API settings under **Account > Settings > New Access Token**.
   - **Canvas Course ID**: This is the ID of the course you're working with (e.g., `12345`). You can find it in the URL when you are viewing the course in Canvas.
   - **Export File Path**: Enter the path and filename where you want the `.txt` file to be saved (e.g., `C:\Users\YourName\Documents\submission_comments.txt`). If no path is provided, the file will be saved in the same directory as the executable.

3. **Export the Comments:**

   After entering the required details, the program will automatically fetch all submission comments for each assignment and save them in the `.txt` file at the location you specified.

