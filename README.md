# Daily Assistant Agent

This is a Python-based agent that automates daily tasks related to your email, calendar, and blog.

## Features

*   Fetches and summarizes unread emails (Gmail).
*   Lists today's events (Google Calendar).
*   *Placeholder for blog tasks (requires specific blog platform integration).*

## Requirements

*   Python 3.7+
*   Google Cloud Platform project with Gmail API and Calendar API enabled.
*   OAuth 2.0 Client ID and Client Secret from Google Cloud Console.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [Your GitHub Repository URL]
    cd daily-assistant-agent
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure:**

    *   Rename `config.py.template` to `config.py`.
    *   Download your `client_secret.json` from the Google Cloud Console (Credentials section).
    *   Fill in the `GOOGLE_CLIENT_SECRET_FILE`, `GMAIL_SCOPES`, and `CALENDAR_SCOPES` in `config.py`.  Keep this file secret!

## Usage
1.  **First Run (Authentication):**
     The script will open a browser window to authenticate with Google. Grant the necessary permissions. The authentication token will be saved to `token.pickle`.
2. **Run daily tasks**:
    ```bash
    python main.py
    ```
3. **Schedule (Optional):**
    Use a scheduler like `cron` (Linux/macOS) or Task Scheduler (Windows) to run `main.py` daily.  Alternatively, you can use the included (commented-out) scheduling example with the `schedule` library.

## Contributing
Contributions are welcome! Please create a pull request.
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.