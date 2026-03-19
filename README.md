# 🌤 Weather & Sun Tracker
A Python desktop GUI application using Tkinter and REST APIs to fetch real-time weather data and sunrise/sunset times for any city; featuring OOP design, JSON parsing, and exception handling.

**Real-time weather intelligence and solar timing — for any city on Earth.**

![Python](https://img.shields.io/badge/python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![REST API](https://img.shields.io/badge/REST-API-orange)
![OOP](https://img.shields.io/badge/OOP-Architecture-yellow)
![MIT](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Table of Contents
<ul>
  <li><a href="#what-is-this">What Is This</a></li>
  <li><a href="#apis-used">APIs Used</a></li>
  <li><a href="#why-3-apis">Why 3 APIs</a></li>
  <li><a href="#tools--technologies">Tools & Technologies</a></li>
  <li><a href="#project-architecture">Project Architecture</a></li>
  <li><a href="#application-workflow">Application Workflow</a></li>
  <li><a href="#sample-output">Sample Output</a></li>
  <li><a href="#exception-handling-strategy">Exception Handling Strategy</a></li>
  <li><a href="#key-concepts-demonstrated">Key Concepts Demonstrated</a></li>
  <li><a href="#how-to-run">How to Run</a></li>
  <li><a href="#future-roadmap">Future Roadmap</a></li>
  <li><a href="#author--contact">Author & Contact</a></li>
  <li><a href="#license">License</a></li>
</ul>

---

## What Is This?

**Weather & Sun Tracker** is a fully functional desktop application that retrieves and displays **live weather data** and **precise solar timing** for any city worldwide — all from a single text input.

Built entirely in Python using object-oriented design, this project demonstrates the complete lifecycle of a software application: from **API integration** and **JSON parsing**, to **error handling**, **modular architecture**, and a **polished graphical interface**.

> _"Type a city. Get the world."_

---

## APIs Used

| API | Endpoint | Purpose |
|-----|----------|---------|
| OpenWeatherMap Geocoding | `/geo/1.0/direct` | Converts city name → latitude & longitude |
| OpenWeatherMap Current Weather | `/data/2.5/weather` | Fetches live temperature, humidity, pressure |
| SunriseSunset.io | `/json` | Retrieves sunrise, sunset, dawn, dusk, day length |

---

## Why 3 APIs?
The Geocoding API acts as a **bridge** — it resolves the city name into coordinates, which are passed to both APIs simultaneously. This eliminates the need for the user to input coordinates manually.

---

## Tools & Technologies

| Tool | Role |
|------|------|
| **Python 3** | Core programming language |
| **Tkinter** | Native GUI framework |
| **Requests** | HTTP client for REST API communication |
| **OOP** | Modular, maintainable architecture |
| **JSON** | Data format returned by all APIs |
| **Exception Handling** | Robust error management |

---

## Project Architecture
```
weather-sun-tracker/
│
├── weather_sun_tracker.py   # Core application class (OOP)
│   ├── __init__()           # Window & screen configuration
│   ├── window()             # App title widget
│   ├── entry_label()        # City input label
│   ├── text_entry()         # City input field
│   ├── button_creation()    # Trigger button
│   ├── button_click()       # API chain + data rendering
│   └── sunrisesunset()      # App launcher
│
├── main.py                  # Entry point
├── weather_sun_tracker.py   # 🔒 API key (excluded from GitHub)
└── README.md                # Documentation
```

---

## Application Workflow
```
User enters city name
        │
        ▼
[ Empty Input Check ]
        │
        ▼
[ Geocoding API ] ──► city name → lat, lon
        │
        ▼
[ City Not Found Check ]
        │
        ├──────────────────────────┐
        ▼                          ▼
[ Weather API ]          [ Sunrise Sunset API ]
lat, lon → weather       lat, lon → solar schedule
        │                          │
        ▼                          ▼
[ Weather Panel ]        [ Sun Timing Panel ]
        │                          │
        └──────────┬───────────────┘
                   ▼
         [ Dual Panel GUI Display ]
```

---

## Sample Output

**Weather Panel** (`Lahore, Pakistan`):

| Attribute | Value |
|-----------|-------|
| Temperature | 16.98 °C |
| Feels Like | 17.03 °C |
| Temp Min | 16.98 °C |
| Temp Max | 16.98 °C |
| Pressure | 1013 hPa |
| Humidity | 88% |
| Sea Level | 1013 hPa |
| Ground Level | 988 hPa |

**Sunrise & Sunset Panel** (`Lahore, Pakistan`):

| Attribute | Value |
|-----------|-------|
| Date | 2026-03-19 |
| Sunrise | 6:09:45 AM |
| Sunset | 6:14:09 PM |
| First_Light | 4:48:43 AM |
| Last_Light | 7:35:11 PM |
| Dawn | 5:45:29 AM |
| Dusk | 6:38:25 PM |
| Solar Noon | 12:11:57 PM |
| Day Length | 12:04:23 |
| Timezone | Asia/Karachi |

---

## Exception Handling Strategy

| Scenario | Handling |
|----------|----------|
| Empty city input | Error dialog before any API call |
| City not found | Detects empty JSON list |
| No internet | `ConnectionError` → user guidance |
| Server timeout | `Timeout` → retry suggestion |
| Unexpected failure | `RequestException` → error dialog |

---

## Key Concepts Demonstrated

1. REST API Integration — chaining 3 APIs sequentially
2. JSON Parsing — navigating nested dictionaries and lists
3. Object-Oriented Programming — class-based architecture
4. GUI Development — Tkinter grid layout, frames, widgets
5. Exception Handling — multi-level error managementre`
---

## How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/weather-sun-tracker.git
cd weather-sun-tracker
```

**2. Install required library:**
```bash
pip install requests
```

**3. Create `main.py`:**
```python
API_KEY = 'your_openweathermap_api_key_here'
```

**4. Run:**
```bash
python main.py
```

---

## Future Roadmap

| Feature | Description |
|---------|-------------|
| 📅 5-Day Forecast | Weekly weather prediction |
| 🌙 Dark / Light Mode | Theme switching |
| 🕓 Search History | Cache previously searched cities |

---

## Author & Contact

**Sana Aziz Sial**  
Biotechnologist and Bioinformatician
- 🎓 [Your University](https://www.uvas.edu.pk/)
- 📧 [Email](sanaazizsial@gmail.com)
- 🐙 [GitHub URL](https://github.com/genome-miner)
- 🔗 [LinkedIn](in/sana-aziz-sial-73b189265)

---

## License

[MIT License](https://github.com/genome-miner/weather-sun-tracker/blob/main/LICENSE) is free to use, modify, and distribute with attribution.

---

<div align="center">
⭐ If you found this useful, consider giving it a star!

*Built with Python • Powered by OpenWeatherMap & SunriseSunset.io*
</div>
