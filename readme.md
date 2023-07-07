# Domain Expiration Checker

This project is a simple script written in Python that checks the expiration status of domain names. It utilizes the `whois` library to retrieve domain information and sends notifications to a Telegram chat if any domain is expiring soon.

## Prerequisites

- Python 3.x
- `whois` library
- `requests` library
- Docker (optional)

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/alfiyansys/dex-check.git
    ```

2. Navigate to the project directory:

    ```shell
    cd dex-check
    ```

3. Set up a virtual environment (optional but recommended):
    
    ```shell
    python -m venv .venv
    ```

4. Activate the virtual environment:

    On Windows:
    ```shell
    .venv\Scripts\activate
    ```
    
    On macOS/Linux:
    ```shell
    source .venv/bin/activate
    ```

5. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

## Configuration

Before running the script, make sure to configure the `config.ini` file with your desired settings:

- **Telegram API credentials and chat ID**: Provide your Telegram bot token and chat ID in the `[TELEGRAM]` section.
- **List of TLD domains to monitor**: Add the TLD domains you want to monitor in the `[DOMAINS]` section, separated by commas.

## Usage

To run the script locally:

```shell
python main.py
```

The script will check the expiration status of the specified domains and send a notification to the configured Telegram chat if any domain is expiring within the specified threshold.

## Docker Support

Alternatively, you can run the Domain Expiration Checker using Docker. Docker provides an isolated environment, ensuring consistent execution across different systems.

1. Build the Docker image:

    ```shell
    docker build -t dex-check .
    ```

2. Run the Docker container:

    ```shell
    docker run -it --rm -v /path/to/config.ini:/app/config.ini dex-check
    ```

The container will execute the script and display the output.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, or submit pull requests.