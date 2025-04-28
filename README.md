Here is the updated `README.md` file with all content in English and styled for a more professional look. It also includes the required instructions for using the terminal commands and file management in Command Prompt (CMD).

# JuanDevID Terminal Portfolio

## Description

JuanDevID Terminal Portfolio is an interactive terminal-based application that showcases my work as a developer. It uses various terminal techniques to present information in an elegant manner, including animations and text-based design.

## Key Features
- **Loading Animation**: Displays a loading animation when the application starts.
- **Interactive Commands**: Supports interactive commands such as `help`, `about`, `projects`, and `contact`.
- **Terminal Portfolio**: Presents portfolio information in an attractive way through the terminal.
- **Clear Screen**: Function to clear the screen and display the logo and header again.

## Requirements
- Python 3.x
- Python Module: `prettytable` (Installation can be done via the following command: `pip install prettytable`)

## Installation

1. **Clone the Repository**:
   Clone this repository to your local directory using the following command:

   ```bash
   git clone https://github.com/JuanDevID/juan-devid-terminal-portfolio.git
   ```

2. **Install Dependencies**:
   Install the required dependencies with the following command:

   ```bash
   pip install prettytable
   ```

3. **Run the Application**:
   Start the application with the command:

   ```bash
   python portfolio.py
   ```

## Available Commands

### Available Commands:
- **`help`**: Displays the list of available commands.
- **`about`**: Shows information about JuanDevID.
- **`projects`**: Displays a list of projects I've worked on.
- **`contact`**: Shows my contact information.
- **`clear`**: Clears the screen and re-displays the logo and header.
- **`exit`**: Exits the application.

### Deleting Files Using CMD
If you want to delete a file using **Command Prompt (CMD)**, follow these steps:

#### Step 1: Open Command Prompt
- Press **Windows + R**, type `cmd`, and press **Enter**.

#### Step 2: Navigate to the Directory of the File
Use the `cd` command to navigate to the directory where the file you want to delete is located. For example:

```bash
cd C:\Users\Username\Documents
```

#### Step 3: Delete the File
To delete a specific file, use the `del` command followed by the file name. For example, to delete the file `fileku.txt`:

```bash
del fileku.txt
```

If the file is located in a folder that requires administrator permission, make sure to run CMD as **Administrator**.

#### Delete All Files of a Specific Type
If you want to delete all files of a certain type within the directory, use a wildcard (`*`). For example, to delete all `.txt` files:

```bash
del *.txt
```

#### Delete a Folder (Directory)
To delete a folder and its contents, use the `rmdir` or `rd` command. For example, to delete the `folderku` directory:

```bash
rmdir /s /q folderku
```

The `/s` flag deletes the folder and all its contents, and `/q` forces deletion without asking for confirmation.

## Notes
- **Deleting files in CMD is permanent** and they are not moved to the Recycle Bin.
- **Be cautious when deleting files** to avoid losing important data.

## Contact
- **GitHub**: [JuanDevID](https://github.com/JuanDevID)
- **X (Twitter)**: [@EOSD_Sakuya](https://x.com/EOSD_Sakuya)

---

Thank you for visiting my portfolio!

### Key Enhancements:
1. **English Translation**: All content is now in English, making it suitable for a wider audience.
2. **Styling**: 
   - Sections are clearly marked with headers (`#` for main title, `##` for sub-sections).
   - Code blocks (for commands) are wrapped in triple backticks for clarity and better readability.
3. **Command Prompt Instructions**: I’ve included step-by-step instructions for deleting files and folders via the command line.
4. **Clear Formatting**: The document is well-structured with clear instructions on setting up and using the portfolio.
