# JuanDevID Terminal Portfolio

This is an interactive terminal application showcasing the professional portfolio of JuanDevID. It includes information about my projects, contact details, and more. This application is designed to run on multiple operating systems.

## Prerequisites

Before installing and running the application, make sure that Python is installed on your system.

### Installing Python

1. **Windows**:
   - Download and install Python from the official website: https://www.python.org/downloads/
   - Ensure that Python is added to the PATH during installation.

2. **macOS**:
   - Python is usually pre-installed on macOS. To check, open the terminal and run:
     ```bash
     python3 --version
     ```
   - If Python is not installed, you can install it using [Homebrew](https://brew.sh/):
     ```bash
     brew install python
     ```

3. **Linux (Ubuntu/Debian)**:
   - To install Python, run the following commands:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

## Installation Instructions

### 1. Clone the Repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/JuanDevID/Terminal.git
cd JuanDevID-Terminal-Portfolio
```

### 2. Install Dependencies

After cloning the repository, you need to install the required dependencies. Run the following command:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is not available, you can manually install the required libraries:

```bash
pip install prettytable
```

### 3. Running the Application

After installing the dependencies, you can run the application in the terminal with the following command:

```bash
python3 portfolio.py
```

### 4. (Optional) Run the Application on Startup

If you want the application to run automatically when your system boots up (especially on Linux), you can add the script to your startup applications.

- **Windows**: Add a shortcut to the startup folder.
- **Linux (Ubuntu)**: Use `crontab` to add it to the startup:

```bash
crontab -e
```

Then add the following line to run the application at system boot:

```bash
@reboot python3 /path/to/python.py
```

## Usage

Once the application is running, you can use the following commands in the terminal:

- `help` ➔ Display a list of available commands.
- `about` ➔ Show information about JuanDevID.
- `projects` ➔ Display a list of my projects.
- `contact` ➔ Display contact information.
- `clear` ➔ Clear the screen.
- `exit` ➔ Exit the application.

## Rules

To ensure a smooth experience, please follow these simple rules when using the JuanDevID Terminal Portfolio:

1. **Respect**: Treat the application and its contents with respect. No inappropriate commands or actions should be executed.
2. **No Spamming**: Avoid typing repetitive or irrelevant commands that can disrupt the user experience.
3. **Use for Intended Purposes**: The application is intended to display my professional portfolio. Do not misuse it for any purpose that violates this intent.
4. **Report Issues**: If you encounter any bugs or issues, please report them via the issue tracker on GitHub.

## Contributing

If you would like to contribute to the development of this project, you can fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

### Explanation of Sections:
1. **Prerequisites**: Information on installing Python on different operating systems.
2. **Installation Instructions**: Steps for cloning the repository, installing dependencies, and running the application.
3. **Usage**: List of commands that can be used in the application.
4. **Rules**: A set of simple guidelines for users to follow when using the application to ensure proper behavior.
5. **Contributing**: Information for users who want to contribute to the project.
6. **License**: Information about the licensing under the MIT License.

### How to Use:
- Save the above content in a `README.md` file in the root directory of your project.
- This file will serve as the primary documentation for users, guiding them on how to set up and use the project on various systems.
