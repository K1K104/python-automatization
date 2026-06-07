#!/bin/bash
source venv/Scripts/activate || source venv/Scripts/activate
black --check app/ tests/
