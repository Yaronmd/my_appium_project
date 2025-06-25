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
├── apps
│   └── app-debug.apk
├── capabilities
│   └── android_caps.json
├── conftest.py
├── pages
│   ├── base_page.py
│   ├── login_page.py
│   ├── main_page.py
│   ├── messages_page.py
│   └── profile_page.py
├── pytest.ini
├── README.md
├── requirements.txt
├── tests
│   ├── test_e2e.py
│   └── test_login_screen.py
├── utils
│   └── driver_factory.py
```

---

## 🧠 High-Level Design

* **Framework:** `pytest` + Page Object Model (POM)
* **Driver:** `appium-flutter-driver@2.0.0`
* **Logging:** Built-in `logging` module
* **Error handling:** All interactions are wrapped with logging and exception tracing
* **Reusable components:** All screen actions are encapsulated in `pages/`
* **Logout method:** Available globally via `BasePage`
* **Future extensions:** Easy to add screenshots, video recording, and reporting (Allure, HTML, etc.)

---

## 💬 Questions or Issues?

Feel free to open an issue or contact the maintainer.

---

Made with ❤️ using Python & Appium
