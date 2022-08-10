#!/bin/bash
python3 run_scraper.py && uvicorn server:app --host 0.0.0.0 --port 8080