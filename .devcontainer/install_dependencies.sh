#!/bin/bash

# Check if the path to the requirements file was provided
if [ -z "$1" ]; then
    echo "Please provide the path to the requirements file"
    exit 1
fi

# Installing prerequisites
apt-get update && \
    apt-get install -y \
    build-essential \
    python3-launchpadlib \
    python3-dev \
    python3-pip \
    python3-venv \
    gcc \
    && apt-get update

# Initialize the virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Set the path of the requirements.txt file
REQUIREMENTS_FILE=$1

# Upgrade pip
python -m pip install --upgrade pip

# Install the Python packages
python -m pip install -r $REQUIREMENTS_FILE
