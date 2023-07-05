# LFI_PID_Fuzzer

A script for fuzzing process IDs (PIDs) to retrieve command line information from a target website using multithreads.

## Introduction

This script utilizes multithreading to send requests to a target website and retrieve command line information of various process IDs (PIDs). It performs a GET request by appending the PID to the URL and the /proc/{}/cmdline payload. The script checks if the response contains the phrase "not found" and if the response is not empty, then it prints the command line information.
Prerequisites

``Python 3.x
requests library (can be installed via pip install requests)``

## Usage

``Make sure you have Python 3.x installed.``
Install the requests library by running the following command:

    pip install requests

Save the script as PID_Fuzzer.py.
Run the script using the following command:

    python3 PID_Fuzzer.py

## Important Note

Please ensure that you have the necessary permissions and legal rights to perform this type of activity on the target website. Unauthorized access or misuse of this script may violate applicable laws and regulations.

## Disclaimer

This script is provided for educational purposes only. The author and the organization behind this script disclaim any responsibility or liability for any misuse or damage caused by the script.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This script is licensed under the MIT License.
