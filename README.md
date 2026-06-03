# 🎭 VTuber Toolkit

> *A streaming assistant with chat overlay, OBS integration, and alerts*

![Flask](https://img.shields.io/badge/Flask-3.0-black)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Socket.io](https://img.shields.io/badge/Socket.io-4.5-green)

## ✨ Features

- 💬 **Chat Overlay** - Display chat in OBS with custom styling
- 🔔 **Alert System** - Show notifications for follows, subs, donations
- 🎬 **OBS Integration** - Control scenes and sources via WebSocket
- 🎨 **Customizable** - Easy to theme and modify
- 🔧 **Dashboard** - Control everything from one place

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
python app.py
```

### 3. Open Dashboard
Go to http://localhost:5000/dashboard

### 4. Add Overlays to OBS
- Add Browser Source → URL: `http://localhost:5000/overlay` (for chat)
- Add Browser Source → URL: `http://localhost:5000/alerts` (for alerts)

## 🎬 OBS Setup

### Enable WebSocket
1. In OBS: Tools → WebSocket Server Settings
2. Enable WebSocket Server
3. Set port (default: 4455)
4. Set password (optional but recommended)

### Configure in Dashboard
1. Go to Dashboard → OBS Configuration
2. Enter host (usually `localhost`)
3. Enter port (default `4455`)
4. Enter password if set
5. Click Connect

## 🎨 Customization

### Chat Overlay
Edit `templates/overlay.html` to change:
- Colors and fonts
- Animation styles
- Message display format

### Alert Styles
Edit `templates/alerts.html` to change:
- Alert animations
- Colors and gradients
- Duration

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/chat` | GET/POST | Get/send chat messages |
| `/api/alerts` | GET/POST | Get/send alerts |
| `/api/obs/config` | GET/POST | OBS connection settings |

## 🔌 WebSocket Events

| Event | Description |
|-------|-------------|
| `new_message` | New chat message received |
| `new_alert` | New alert triggered |
| `connected` | Client connected |

## 🛠️ Tech Stack

- **Backend:** Flask + Flask-SocketIO
- **Frontend:** HTML5, CSS3, Vanilla JS
- **Real-time:** Socket.IO
- **OBS:** obs-websocket-py

## 📁 Project Structure

```
vtuber-toolkit/
├── app.py                 # Flask application
├── requirements.txt       # Dependencies
├── README.md             # This file
└── templates/
    ├── index.html        # Landing page
    ├── dashboard.html    # Control dashboard
    ├── overlay.html      # Chat overlay (for OBS)
    └── alerts.html       # Alert overlay (for OBS)
```

## 🚀 Future Features

- [ ] YouTube Live Chat integration
- [ ] Twitch Chat integration
- [ ] Custom alert sounds
- [ ] Avatar/lip sync
- [ ] Scene transitions
- [ ] Recording controls

## 🦐 Credits

Made with 🎭 by **theetee** ([@theeteeshrimp](https://github.com/theeteeshrimp))

For **T** - happy streaming!

---

*Go live and have fun!* 🎬✨
