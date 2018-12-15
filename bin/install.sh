
#!/bin/bash

echo Installing environment

echo 1 - creating virtual env
python3 -m venv .env

echo 2 - activating env
source .env/bin/activate

echo 3 - upgrade pip
pip install --upgrade pip

echo 4 - update dependencies
pip install -r requirements.txt
