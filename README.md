# Port Scanner Tool

## Description
This Python-based port scanner leverages the `nmap` library to scan target IP addresses and identify open ports within a specified range. Designed for network security analysis, it provides color-coded output for better readability and quick insights.

## Features
- Scans a target IP for open ports in a specified range.
- Color-coded output for clear and organized results.
- Error handling for seamless user experience.

## Prerequisites
- Python 3.x installed.
- `nmap` module: Install it using `pip install python-nmap`.
- `nmap` application: Ensure it is installed and added to your system's PATH.

## Usage
1. Clone this repository or download the script.
2. Run the script with the following format:
   ```
   python3 portscanner.py <target_ip> <port_range>
   ```
3. Example:
   ```
   python3 portscanner.py 192.168.1.1 1-100
   ```

## Output
- Displays open ports in the specified range.
- Errors and warnings are displayed in red for easy identification.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer
This tool is intended for educational purposes only. Ensure you have permission before scanning any network. Misuse of this tool is strictly prohibited.
