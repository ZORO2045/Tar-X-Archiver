# Tar-X Archiver

![banner](https://raw.githubusercontent.com/ZORO2045/Tar-X-Archiver/main/banner.jpg)

[![Python](https://img.shields.io/badge/Python-3.6+-blue?style=flat-square&logo=python)](https://www.python.org/)

## Description 📝

This tool is designed to simplify the creation of non-compressed `.tar` archives from your files. It's particularly useful when you need to create archives without file compression, making the archiving process very fast.

## Features

*   **Non-Compressed .tar Archives:** Utilizes the standard `tar` command to create archives quickly and without compression.
*   **Easy-to-Use Command-Line Interface:** Provides a clear and straightforward user experience.
*   **Self-Updating:** You can update the tool automatically by using `git clone` to pull the latest changes from the repository.

## Requirements

*   Python 3.6 or higher.
*   Python Libraries:
    *   `requests`
    *   `art`
    *   `colorama`
*   Git (for automatic updates).
*   `tar` command (usually present by default on Unix-like systems).

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ZORO2045/Tar-X-Archiver.git
    ```
2.  **Navigate to the tool's directory:**
    ```bash
    cd Tar-X-Archiver
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the tool:**
    ```bash
    python main.py
    ```
2.  **Choose an option:**
   *   **1: Create Archive:** The tool will prompt you for the input path and the output path.
   *   **Example Input File:** `/storage/emulated/0/Download/boot.img`
   *   **Example Output Archive:** `/storage/emulated/0/Download/boot.tar`
   *   **2: Check for Updates:** The tool will check for updates and clone them if available.
   *   **3: Exit:** To exit the tool.

## Created By ✍️

This project was created by: [ፚ Ꭷ Ꮢ Ꭷ ❥](https://t.me/ZORO2045).
