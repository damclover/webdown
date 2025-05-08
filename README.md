
# WebDown

**WebDown** is a Python script that allows you to download raw files or web pages directly from the internet and save them locally.

## Requirements

* Python 3.x
* `requests` library
* `argparse` library

You can install the necessary libraries by running the `install.sh` script.

## Installation

1. Clone the repository or download the files.

2. Run the `install.sh` script to install the required dependencies and set up the script globally:

   ```bash
   ./install.sh
   ```

   The `install.sh` script will:

   * Install the necessary Python libraries (`requests` and `argparse`)
   * Make `webdown.py` executable
   * Copy `webdown.py` to `/usr/local/bin` for global usage

3. Ensure that you have the necessary permissions to execute the script:

   ```bash
   sudo chmod +x webdown.py
   sudo cp webdown.py /usr/local/bin/webdown
   ```

## Usage

After installing, you can run the script from any directory by calling `webdown`. Here’s how to use the script:

### Basic Command:

```bash
webdown -u <URL> -o <output_filename>
```

### Example 1: Download a raw file (e.g., shell script):

```bash
webdown -u https://raw.githubusercontent.com/someuser/somerepo/main/script.sh -o myscript.sh
```

### Example 2: Download a webpage:

```bash
webdown -u https://example.com/page.html -o saved_page.html
```

### Arguments:

* `-u`, `--url`: **(Required)** The URL of the raw file or webpage you want to download.
* `-o`, `--output`: **(Required)** The name of the file to save the content.

### Important Note:

It is EXTREMELY IMPORTANT that the URL provided is the **raw content** of the file. If there is any other information besides the content itself, the file may become corrupted when executed. You can also use this script to download web pages.

## Error Handling

* If the URL is invalid or the file can't be downloaded, the script will print an error message with the details.
* If the file is successfully downloaded, the script will display a message confirming the file name.

## Example of Usage

```bash
webdown -u https://raw.githubusercontent.com/username/repository/branch/file.sh -o downloaded_file.sh
```

---

### `install.sh` Script Content:

```bash
# Install dependencies
pip install requests --break-system-packages
pip install argparse --break-system-packages

# Make the script executable and move to the local bin directory
sudo chmod +x webdown.py
sudo cp webdown.py /usr/local/bin/webdown
```

---

## Troubleshooting

* **Permission Denied**: If you face a "Permission Denied" error, ensure that the script has execute permissions (`chmod +x webdown.py`).
* **Missing Dependencies**: If you encounter missing dependencies, ensure that the Python packages are installed via `install.sh`.

---
