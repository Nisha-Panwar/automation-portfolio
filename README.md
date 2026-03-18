# Automation Portfolio 🤖

A login and cart automation project using Playwright and Python.

## What it tests
- ✅ Valid login on saucedemo.com
- ✅ Invalid login shows error message
- ✅ Add to cart functionality
- ✅ Logout functionality

## Tools Used
- Python
- Playwright
- Pytest
- Pytest-HTML (test reporting)

## How to run
pip3 install pytest-playwright
pip3 install pytest-html
playwright install chromium
pytest test_login.py -v --html=report.html

## Test Report
After running, open report.html in your browser to see a full test report with pass/fail results.
