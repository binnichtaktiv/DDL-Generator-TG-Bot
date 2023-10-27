# DirectDownloadLinkBot

## Description
This bot converts Userscloud, SharePoint, personal OneDrive and Starfiles links into direct download links.

## Requirements
- Python (tested with version 3.8+)

Install the necessary libraries:
```pip3 install pyTelegramBotAPI requests```

## Installation
1. Clone the repository.
2. Navigate to the directory containing the `DDL Generator.py` file.

## Usage
1. Replace the TOKEN in the file with your own, substituting the provided TOKEN placeholder.
2. Start the bot using:
```python3 DDL Generator.py```

After launching, the bot awaits incoming messages. Upon receiving a supported link, it returns the direct download link.

## Supported Link Types
- Userscloud
- SharePoint
- Personal OneDrive links (Note the specific instructions in the bot for OneDrive links.)

