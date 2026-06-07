#!/bin/bash
source venv/Scripts/activate || source venv/bin/activate
PYTHONPATH=. pytest tests/
