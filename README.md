# ARCNET

**Automated Recognition and Cleansing Network for Engagement Threats**

Local tool for automated detection and removal of spam comments on YouTube using heuristic and pattern-based analysis.

---

## Features

  - Detects and removes spam comments on your YouTube videos
  - Uses keyword, pattern, and similarity matching
  - Runs locally on your computer – no server required
  - Simple command-line interface for easy use

---

## Requirements

  - Python 3.8 or higher
  - Google account
  - Google Cloud Project with YouTube Data API enabled

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/arcnet.git
cd arcnet
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up Google API credentials**

  - Go to Google Cloud Console
  - Create a new project
  - Enable the YouTube Data API v3
  - Create an OAuth Client ID (type: Desktop App)
  - Download the JSON file
  - Rename it to client_secret.json and place it in the project folder

## Usage

1. Run the Programm

```bash
python main.py
```

2. Follow the prompts:
- Login: Your default browser will open for Google OAuth login
- Enter Video ID: Input the ID of the video you want to clean
- Scan: The tool fetches comments and detects spam
- eview: It shows how many spam comments were detected
- confirm Deletion: You can delete all detected spam comments

## Notes

- Only works for videos you own
- Uses official YouTube API (no password storage)
- Detection is heuristic: some false positives may occur
- Recommended to review detected spam before deletion

## Optional: Convert to executable (.exe)
If you want to share the tool with non-technical users:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```
- The .exe will appear in the dist/ folder
- Users can run it by double-clickin

## Recommended Workflow

1. Keep your client_secret.json safe
2. Regularly update the BLACKLIST in filter.py for new spam patterns
3. Run ARCNET periodically for new comments

## Contributing

- Fork the repo
- Make your changes
- Submit a pull request
- Keep detection rules clear and modular

## Note on Code Quality

This project is an **initial draft generated with AI assistance**.  

- The code works, but it **might not be the most elegant or professional**.  
- Some parts may be messy, redundant, or could be optimized

## License

MIT License
