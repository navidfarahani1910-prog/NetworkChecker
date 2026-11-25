

\# NetworkChecker



A beginner-friendly network connectivity checker built with Python.



This is my first cybersecurity project, developed while learning networking fundamentals and Python programming.



\## Features



\- DNS lookup for a configured domain

\- IPv4 address resolution

\- TCP connectivity testing for a user-specified host and port

\- Port number validation (1–65535)

\- Basic error handling

\- Timestamped text reports



\## Technologies



\- Python 3.12

\- Python Socket Library

\- Python Datetime

\- Python Pathlib



\## Installation



1\. Install Python 3.12 or newer.

2\. Clone or download this repository.

3\. Open a terminal in the project directory.

4\. Run the application:



&#x20;   py checker.py



No third-party Python packages are required.



\## How It Works



1\. The program resolves the configured domain to an IPv4 address.

2\. The user enters a target host and TCP port.

3\. The program attempts to establish a TCP connection.

4\. Results are saved to `network\_report.txt`.



The report is overwritten on each execution and is excluded from Git.



\## Example Output



&#x20;   === NetworkChecker ===

&#x20;   DNS lookup successful

&#x20;   Domain: example.com

&#x20;   IPv4: 192.0.2.10



&#x20;   Enter host: 1.1.1.1

&#x20;   Enter port: 443

&#x20;   TCP Connection Successful!



The IPv4 address above is an illustrative example.



\## Limitations



\- DNS lookup currently resolves one IPv4 address.

\- The DNS domain is configured in the source code.

\- TCP testing checks connectivity, not application security.

\- The tool does not scan multiple ports automatically.



\## Security Notice



Use this tool only on systems you own or have permission to test.



\## Project Status



Version 1.0 — Initial learning project.



\## Future Improvements



\- Interactive DNS lookup

\- IPv6 support

\- Multiple connectivity checks

\- Structured JSON reports

\- Automated tests