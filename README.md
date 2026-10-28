# Green Cloud Optimizer

A beginner-friendly academic prototype for sustainable cloud computing. The app displays simulated server CPU and memory utilization, provides rule-based optimization recommendations, and calculates illustrative energy estimates.

## Features

- Dashboard showing average CPU and memory utilization
- Simulated server readings
- Rule-based recommendations for lightly used or highly utilized servers
- Simplified illustrative energy estimate
- Responsive HTML/CSS interface

## Tech stack

- Python
- Flask
- HTML
- CSS

## Run locally

1. Install Python 3.10 or later.
2. Open a terminal in this project folder.
3. (Optional but recommended) create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate it on Windows:

   ```bash
   .venv\Scripts\activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the app:

   ```bash
   python app.py
   ```

7. Open `http://127.0.0.1:5000` in your browser.

## Important limitations

This is a classroom demonstration. Server metrics are simulated in `app.py`. The energy calculation is a simplified illustrative estimate, not a measurement, carbon accounting method, or guaranteed saving. The app does not connect to a real cloud provider.

## Future enhancements

- Connect to authorized cloud monitoring APIs
- Store historical readings in a database
- Add charts and time-series reports
- Estimate carbon emissions using a documented regional emissions factor
- Add authentication and automated tests
