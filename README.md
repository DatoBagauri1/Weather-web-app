🌍 Weather-Time Heatmap with Live Webcams & Fun Facts
An interactive Flask web application that combines real-time weather, time zone data, heatmaps, and live webcams from around the world — all in a sleek, modern UI.
Just pick a country, and the app will show you:

🗺️ Live Weather Heatmap — visualizes temperatures across the country using Leaflet + heatmap.js.

⏰ Local Time — instantly fetches and displays the current local time.

💡 Fun Facts — retrieves interesting trivia about the country via the Wikipedia API.

🎥 Live Webcam (if available near capital) — streams webcams near the country's capital using Windy API (primary) and WorldCam API (fallback). If no webcam is found, a message is displayed.

✨ Features
Modern Bootstrap-based UI

Interactive heatmap with zoom and pan

Real-time weather from OpenWeatherMap API

Fun facts via Wikipedia API

Live webcams via Windy API + WorldCam API (fallback)

Displays “No webcam available near the capital” if none are found

Fully responsive design for desktop and mobile

🔧 Tech Stack
Backend: Flask (Python)

Frontend: HTML5, CSS3, Bootstrap, JavaScript, Leaflet.js, heatmap.js

APIs Used:

OpenWeatherMap (Weather Data)

Wikipedia API (Fun Facts)

Windy API (Primary Webcams)

WorldCam API (Fallback Webcams)

🚀 How It Works
User selects a country from the dropdown.

The app fetches coordinates for the capital city.

Weather data is pulled from OpenWeatherMap to generate a temperature heatmap.

Local time is calculated based on time zone API data.

Fun facts are fetched from Wikipedia.

The app tries to find a live webcam near the capital:

First via Windy API (within ~50km radius)

If none found, via WorldCam API

If still none found, a message is displayed instead of an empty embed

