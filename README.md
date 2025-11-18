# find-insta-profile

Find and check Instagram profiles by name. This tool searches for Instagram profiles that match a given name by checking various username variations.

## Features

- Search for Instagram profiles by name
- Check multiple username variations (no spaces, underscores, dots)
- Display profile information (username, full name, bio, followers, etc.)
- Identify private vs public profiles

## Installation

1. Clone this repository:
```bash
git clone https://github.com/satyavenik/find-insta-profile.git
cd find-insta-profile
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Default search (searches for "subrahmanyam kommireddy"):
```bash
python find_insta_profile.py
```

### Search for a specific name:
```bash
python find_insta_profile.py "john doe"
```

### Search for any name:
```bash
python find_insta_profile.py "your name here"
```

## Example Output

```
============================================================
Instagram Profile Checker
============================================================

Searching for Instagram profiles for: subrahmanyam kommireddy
Checking username variations: ['subrahmanyamkommireddy', 'subrahmanyam_kommireddy', 'subrahmanyam.kommireddy', 'subrahmanyamkommireddy']

✓ Found profile: @username
  Full Name: Subrahmanyam Kommireddy
  Bio: Sample bio text...
  Followers: 1000
  Following: 500
  Posts: 50
  Private: False
  URL: https://www.instagram.com/username/

============================================================
Summary: Found 1 profile(s)
  - @username (Subrahmanyam Kommireddy)
============================================================
```

## How it Works

The script:
1. Takes a name as input (defaults to "subrahmanyam kommireddy")
2. Generates potential username variations by:
   - Removing spaces and converting to lowercase
   - Replacing spaces with underscores
   - Replacing spaces with dots
   - Preserving original case without spaces
3. Checks each username variation on Instagram
4. Returns found profiles with detailed information

## Requirements

- Python 3.6+
- instaloader
- requests

## Notes

- Instagram may rate-limit requests if too many searches are performed quickly
- Some profiles may be private and will show limited information
- The script checks common username patterns but may not find all variations

## License

MIT License
