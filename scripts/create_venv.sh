#!/bin/bash
python -m venv venv
source venv/Scripts/activate || source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
