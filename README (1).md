# Personal Notes + AI Assistant CLI

A command-line app for saving your own notes, fetching random facts from the internet, and asking an AI to reflect on or explain any saved note. Built as a learning project covering Python fundamentals, API requests, and authenticated LLM calls — all in one program.

## Features

- Add and save your own notes (persisted to disk)
- View all saved notes
- Fetch a random fact from a public API
- Save a fetched fact as a note
- Ask an AI to explain or reflect on any saved note
- Handles errors gracefully (no internet, bad API key, invalid input)

## Requirements

- Python 3.x
- `requests`
- `python-dotenv`
- An OpenAI API key with available billing credits

Install dependencies:

```bash
pip install requests python-dotenv
```

## Setup

1. Clone this repo
2. Create a `.env` file in the project folder (not included — you create it yourself):
   ```
   OPENAI_API_KEY=your_real_api_key_here
   ```
3. Make sure your OpenAI account has billing credits added
4. Run the app:
   ```bash
   python notes_assistant.py
   ```

## Usage

```
========================================
1. Add a note
2. View all notes
3. Get a random fact from the internet
4. Fetch a fact and save it as a note
5. Ask AI about a saved note
6. Exit
========================================
Choose an option:
```

## How it works

| Step | What happens |
|------|----------------|
| Notes storage | Notes are stored as a list of dictionaries and saved to `notes.json` |
| Fetching facts | A GET request is sent to a public facts API; the result can be saved as a note |
| Asking AI | A saved note's text is sent to the OpenAI API in a POST request, with your API key attached via the `Authorization` header |
| Parsing responses | The AI's reply is extracted from a nested JSON response and optionally saved back into that note |
| Error handling | All API calls are wrapped in `try/except` to handle no internet, bad status codes, or missing files |

## Project structure

```
notes_assistant.py   # main script
.env                  # your real API key (not committed to GitHub)
.env.example          # template showing required variable name
.gitignore            # excludes .env and notes.json from version control
notes.json             # saved notes (created automatically)
README.md              # this file
```

## Topics covered

- Functions, loops, dictionaries, file I/O
- Reading and writing JSON to disk
- GET requests to a public API
- Environment variables for secret keys
- Authentication headers (`Authorization: Bearer <key>`)
- POST requests with a JSON body
- Parsing nested JSON responses
- Error handling with `try/except` and HTTP status codes

## Security note

The `.env` file is excluded via `.gitignore` and should never be pushed to GitHub. If an API key is ever accidentally exposed, regenerate it immediately from the OpenAI dashboard.

## Status

Complete — covers Python fundamentals through authenticated API calls in one project.
