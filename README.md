# MyCounter App - Mobile Automation Test Suite

This repository contains an automated test suite for the **MyCounter** Flutter application, built with **Appium 2**, **pytest**

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-user/mycounter-appium-tests.git
cd mycounter-appium-tests
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Appium & Flutter driver

Make sure [Node.js](https://nodejs.org/) is installed.

```bash
npm install -g appium
appium driver install flutter
```

---

## How to Run the Tests

### 1. Start Appium Server

```bash
appium
```

### Launch Android emulator or connect real device

Make sure the app is built and the path to the `.apk` file is valid in your `capabilities.json`.

### 3. Run the tests

```bash
pytest -s
```

Or to run a specific test file:

```bash
pytest tests/test_login_screen.py
```

---

## Project Structure

```
.
── apps
│   └── app-debug.apk               # The compiled APK file of the app under test
├── capabilities
│   └── android_caps.json           # JSON file with Appium capabilities (platform, app path, device name, etc.)
├── conftest.py                     # Pytest configuration hooks (fixtures like driver setup, teardown, etc.)
├── pages
│   ├── base_page.py                # Base class with common actions (click, send_keys, wait, etc.)
│   ├── login_page.py               # Page Object for login screen
│   ├── main_page.py                # Page Object for main (counter) screen
│   ├── messages_page.py           # Page Object for messages screen
│   └── profile_page.py            # Page Object for profile screen
├── pytest.ini                      # Pytest configuration (markers, logging, etc.)
├── README.md                       # Project documentation (this file)
├── requirements.txt                # List of Python dependencies for the project
├── tests
│   ├── test_e2e.py                 # End-to-end flow tests (e.g. login → navigate → logout)
│   └── test_login_screen.py        # Focused tests for login scenarios
├── utils
│   └── driver_factory.py           # Utility to initialize the Appium driver from capabilities
```

---

## High-Level Design

* **Framework:** `pytest` + Page Object Model (POM)
* **Driver:** `UiAutomator2`
* **Logging:** Built-in `logging` module
* **Error handling:** All interactions are wrapped with logging and exception tracing
* **Reusable components:** All screen actions are encapsulated in `pages/`

---
