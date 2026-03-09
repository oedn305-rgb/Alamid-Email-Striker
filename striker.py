name: Alamid System

on:
  workflow_dispatch:

jobs:
  run-system:
    runs-on: ubuntu-latest

    steps:

      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install libraries
        run: pip install python-dotenv

      - name: Clean Emails
        run: python radar.py

      - name: Send Emails
        env:
          GMAIL_USER: ${{ secrets.GMAIL_USER }}
          GMAIL_PASS: ${{ secrets.GMAIL_PASS }}
        run: python striker.py
