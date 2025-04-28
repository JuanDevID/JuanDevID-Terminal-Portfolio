# JuanDevID Terminal Portfolio 🌐💻

Welcome to the **interactive terminal application** showcasing the professional portfolio of **JuanDevID**. Explore my projects, contact details, and more through this terminal-based interface.

---

## 🔧 Prerequisites

Before installing and running the application, ensure that **Python** is installed on your system.

### 💻 Installing Python

1. **Windows**:
   - Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/)
   - Ensure that Python is added to your PATH during installation.

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

---

## ⚙️ Installation Instructions

### 1. Clone the Repository

Clone the repository to your local machine using **Git**:

```bash
git clone https://github.com/JuanDevID/JuanDevID-Terminal-Portfolio.git
cd JuanDevID-Terminal-Portfolio
```

### 2. Install Dependencies

After cloning the repository, install the required dependencies. Run the following command:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is not available, you can manually install the required libraries:

```bash
pip install prettytable
```

### 3. Running the Application

Once the dependencies are installed, you can run the application by executing the following command in the terminal:

```bash
python3 portfolio.py
```

### 4. (Optional) Run the Application on Startup

If you want the application to run automatically when your system boots up (especially on Linux), you can add the script to your startup applications.

- **Windows**: Add a shortcut to the startup folder.
- **Linux (Ubuntu)**: Use `crontab` to add it to startup:
  ```bash
  crontab -e
  ```
  Then add the following line to run the application at system boot:
  ```bash
  @reboot python3 /path/to/portfolio.py
  ```

---

## 🖥️ Usage

Once the application is running, you can use the following commands:

- `help` ➔ Display a list of available commands.
- `about` ➔ Show information about **JuanDevID**.
- `projects` ➔ Display a list of my **projects**.
- `contact` ➔ Display my **contact information**.
- `clear` ➔ **Clear** the terminal screen.
- `exit` ➔ **Exit** the application.

---

## 📜 Rules

To ensure a smooth experience, please follow these simple rules when using the **JuanDevID Terminal Portfolio**:

1. **Respect**: Treat the application and its contents with respect. Do not run inappropriate or harmful commands.
2. **No Spamming**: Avoid entering repetitive or irrelevant commands that can disrupt the user experience.
3. **Use for Intended Purposes**: The application is designed to showcase my professional portfolio. Please refrain from misusing it.
4. **Report Issues**: If you encounter any bugs or issues, please report them via the issue tracker on [GitHub Issues](https://github.com/JuanDevID/JuanDevID-Terminal-Portfolio/issues).

---

## 🤝 Contributing

If you want to contribute to this project, feel free to fork the repository, make changes, and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

### 🙏 Thanks for checking out my portfolio! If you have any questions or feedback, feel free to reach out. 😊

### Key Enhancements:
- **Emojis**: Emojis have been added to sections like **Prerequisites**, **Usage**, **Rules**, and **License** to make it more visually engaging.
- **Headings & Sections**: The file is structured with different heading levels and clear section breaks for better readability.
- **Italicized and Bold Text**: Emphasis is added where necessary (e.g., project name, commands, etc.).
- **Links**: Hyperlinks to the GitHub repository and issues page for easier access.
