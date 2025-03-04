#!/bin/bash

if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3 first."
    exit 1
fi


if [ -d ".venv" ]; then
    echo "Virtual environment '.venv' already exists."
    echo "To remove it: rm -rf .venv"
    exit 1
fi


echo "Creating virtual environment..."
python3 -m venv .venv

# Upgrade pip
echo "Upgrading pip..."
.venv/bin/pip install --upgrade pip

echo "Starting venv and insalling requirements"
source .venv/bin/activate
pip install -r requirements.txt

echo "Setting up django"
python manage.py makemigrations

python manage.py migrate

python manage.py loaddata fixture/db.json

echo "Setting up completed"