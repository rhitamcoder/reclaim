# 🛡️ Reclaim

**A command-line streak tracker for breaking free from short-form content and other high-dopamine digital habits.**

Reclaim is a simple daily check-in tool. Once a day, it asks whether you stayed away from the habits you're trying to break, tracks your consecutive-day streak, and rewards a successful check-in with a randomly selected motivational message. Miss a day, and the streak resets, giving you a clear, honest signal of your progress over time.

---

## ✨ Features

- ✅ **Daily check-in system** — a simple yes/no prompt determines whether your streak continues
- 🔥 **Streak tracking** — counts consecutive successful days, and resets automatically if a day is missed
- 🔁 **Once-per-day enforcement** — running the script again on the same day shows your current streak instead of letting you check in twice
- 💬 **25 randomly selected motivational messages**, shown after each successful check-in to reinforce the habit
- 💾 **Persistent storage** — your streak and last check-in date are saved locally in a JSON file, so progress survives between runs

---

## 🛠️ Tech Stack

- **Python 3** — built entirely on the standard library (`json`, `os`, `random`, `datetime`)

---

## 📁 Project Structure

```
reclaim/
├── tracker.py             # Full tracker logic
├── tracker_data.json      # Auto-created file storing your streak and last check-in date
└── README.md
```

> **Note:** `tracker_data.json` is created automatically the first time you check in, so it doesn't need to exist in the repo beforehand.

---

## ▶️ Getting Started

### Prerequisites
- Python 3 (pure standard library, nothing else needed)

### Running It

```
git clone https://github.com/rhitamcoder/reclaim.git
```
```
cd reclaim
```
```
python tracker.py
```

You'll be asked once per day whether you stayed on track. Answer `y` to extend your streak, or `n` to reset it and start fresh tomorrow.

---

## 🧠 How It Works

- **`load_data()` / `save_data()`** read and write your streak and last check-in date to and from `tracker_data.json`
- **`update_tracker()`** is the core loop:
  - If you've already checked in today, it just reports your current streak
  - If you answer `y` and yesterday was your last check-in (or this is your very first check-in), your streak increases by 1
  - If you answer `y` but a day was missed in between, your streak resets to 1 with a warning
  - If you answer `n`, your streak resets to 0
- **`random.choice(MOTIVATION)`** picks one of 25 pre-written motivational messages to display after a successful check-in

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
