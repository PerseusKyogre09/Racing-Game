# Python Racing Game

An arcade-style lane racer built with Python and Pygame. Drift past traffic, chase high scores, and enjoy a retro-inspired presentation with animated overlays and a fully interactive front end.

---

## 📺 Game Overview

- **Intro screen** with Play, Instructions, and About sections
- **Countdown launch** sequence to build excitement before each race
- **Analog speedometer** with a rotating needle tied to in-game speed
- **Persistent high-score** tracking saved between sessions
- **Random soundtrack** – every race loads one of several background tracks

### Controls

- `←` / `→` – Steer between lanes (car tilts slightly while turning)
- `↑` – Accelerate
- `↓` – Brake
- `Esc` – Exit from game over screen
- `Space` – Restart after a crash

### Objective

Stay on the road, weave around other cars, and build the highest score you can. Collisions stop the run, but your best result is recorded in `Assets/highscore.txt`.

---

## 🛠️ Requirements

- Python 3.9 or newer
- Pygame 2.0+

Install dependencies (from the project root):

```bash
pip install -r requirements.txt  # optional convenience
pip install pygame               # minimal dependency
```

> **Tip:** A virtual environment keeps your global Python install tidy.

---

## 🚀 Quick Start

```bash
git clone https://github.com/PerseusKyogre09/Racing-Game.git
cd Racing-Game
python main.py
```

If you prefer using a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
pip install pygame
python main.py
```

---

## 🎧 Audio & 🎨 Art Credits

- All visual assets: see `Assets/` directory (custom and royalty-free resources)
- Music sourced from Pixabay:
    - SPmusic
    - Mykola Sosin
    - Melody Ayres-Griffiths

Please respect the usage terms of each asset provider when redistributing or modifying the project.

---

## 🧰 Project Structure

```text
Assets/
├── Audio/
├── Sprite/
├── speedometer_carbon.png
├── indicator.png
└── ...
main.py
Readme.md
```

`main.py` contains the entire game loop, UI logic, and asset loading. All images, fonts, and audio files live under `Assets/`.

---

Contributions are welcome! Feel free to open an issue or pull request with improvements or bug fixes.
