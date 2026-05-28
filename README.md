<div align="center">

  ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
  ![License](https://img.shields.io/badge/License-MIT-green?logo=opensourceinitiative&logoColor=white)
  ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

  # TempMail CLI

  **A command-line temporary email tool powered by Guerrilla Mail API**

  [Website](https://nicram-code.github.io/) • [Profile](https://doxbean.cc/@nicram)

</div>

---

## Features

- 📧 Create temporary email addresses instantly
- 📥 Check inbox for received emails
- 🔒 No registration required
- ⚡ Fast and lightweight CLI interface
- 🌍 Cross-platform support (Windows, Linux, macOS)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Quick Setup

#### Linux / macOS

```bash
# Clone the repository
git clone https://github.com/nicram-code/tempmail-cli.git
cd tempmail-cli

# Run the setup script
chmod +x setup.sh
./setup.sh

# Activate virtual environment
source .venv/bin/activate

# Run the tool
python main.py
```

#### Windows

```powershell
# Clone the repository
git clone https://github.com/nicram-code/tempmail-cli.git
cd tempmail-cli

# Run the setup script
.\setup.sh

# Activate virtual environment
.venv\Scripts\activate

# Run the tool
python main.py
```

### Manual Installation

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the tool
python main.py
```

## Usage

1. Run the tool: `python main.py`
2. Choose an option from the menu:
   - **1** - Create a new temporary email address
   - **2** - View existing email addresses / check inbox
   - **3** - Help
   - **99** - Exit

## Dependencies

- `typer` - CLI framework
- `rich` - Terminal formatting
- `requests` - HTTP library
- `python-dotenv` - Environment variables
- `colorama` - Cross-platform colored terminal text

## Author

**nicram**

- [Website](https://nicram-code.github.io/)
- [Profile](https://doxbean.cc/@nicram)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Powered by [Guerrilla Mail API](https://www.guerrillamail.com/)
- Emails expire after ~1-2 hours
- CLI template available at [nicram-code/tempmail-cli](https://github.com/nicram-code/tempmail-cli)

---

<div align="center">

  Made with ❤️ by [nicram](https://doxbean.cc/@nicram)

</div>