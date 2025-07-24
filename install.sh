#!/bin/bash

echo "🔧 Installing HackerDose..."

# Check for Python3
if ! command -v python3 &>/dev/null; then
    echo "❌ Python3 is not installed. Please install it and try again."
    exit 1
fi

# Install required Python packages
pip3 install -r requirements.txt

# Make script executable
chmod +x hackerdose.py

# Move to /usr/local/bin for global access
sudo cp hackerdose.py /usr/local/bin/hackerdose

echo "✅ Installation complete!"
echo "➡️  You can now run HackerDose using: hackerdose"
