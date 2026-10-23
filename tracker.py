#!/usr/bin/env python3
import json
import os
import random
from datetime import datetime, timedelta

DATA_FILE = "tracker_data.json"

#A list of motivational sentences
MOTIVATION = [
    "Great job! Your brain is healing and regaining focus.",
    "One day at a time. You are more than an algorithm!",
    "The real world looks better than a 9:16 screen.",
    "Your attention is your most valuable asset. Thanks for protecting it today.",
    "Consistency is the path to freedom, keep going!",
    "Your brain is enjoying the silence. Keep going it space to breathe.",
    "Real life doesn't have 'scroll' button. Enjoy the stillness of today.",
    "You aren't missing out on anything; you are finally tuning into yourself.",
    "Your dopamine levels are resetting. Your future self will thank you for this discomfort.",
    "The world is wide, and your focus is sharp. Keep it that way.",
    "You are the master of the machine, not the other way around.",
    "An algorithm was designed to break your will. Today, you broke the algorithm.",
    "Success is built in the moments you choose 'boring' reality over 'exciting' pixels.",
    "You just reclaimed hours of your life. What will you build with them?",
    "Don't trade your long-term goals for a 15-second distraction.",
    "Comparison is the thief of joy. By closing the app, you kept your joy safe.",
    "Nobody ever looked back on their life and wished they had watched more shorts.",
    "You are a creator, not just a consumer. Go write your own story.",
    "Reels are a filtered version of reality. Today, you lived the unfiltered truth.",
    "Your attention is the currency of the 21st century. Today, you stayed rich.",
    "Your energy is a finite resource. Don't let an algorithm bait you into wasting it on a screen.",
    "Truly physical strength is the ability to acknowledge an urge and choose not to act on it. You are the boss of your body today.",
    "Redirect that physical energy into your growth. Your muscles and your mind have better things to build than a temporary hit of dopamine.",
    "Provocative pixels are a shadow of reality. Choose the health of your real-world self over the exhaustion of a digital fantasy.",
    "Every time you look away, you are rewiring your brain for real connection and lasting discipline. Stand tall today.",
]

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"streak": 0, "last_date": None}

def save_data(streak, last_date):
    with open(DATA_FILE, "w") as f:
        json.dump({"streak": streak, "last_date": last_date}, f)

def update_tracker():
    data = load_data()
    today = datetime.now().date()

    if data["last_date"]:
        last_date = datetime.strptime(data["last_date"], "%Y-%m-%d").date()
    else:
        last_date = None

    # Check if user already logged today
    if last_date == today:
        print(f"You've already checked in today! Current streak: {data['streak']} days.")
        return
    
    print("--- Digital Detox Tracker ---")
    status = input("Did you stay away from Reels/Shorts/Porn/Chatbots today? (y/n): \n").lower()

    if status == 'y':
        # Check if it's a consecutive day
        if last_date == today - timedelta(days=1) or last_date is None:
            new_streak = data["streak"] + 1
        else:
            print("⚠️ You missed a day! Streak reset to 1.")
            new_streak = 1

        save_data(new_streak, str(today))

        # --- RANDOM SELECTION HAPPENS HERE ---
        random_sentence = random.choice(MOTIVATION)

        print(f"\n🔥 Streak: {new_streak} Days!")
        print(f"💡 {random_sentence}")
        # ---------------------------------------

    else:
        print("❌ Streak reset to 0. Tomorrow is a new opportunity to start fresh.")
        print("Take a deep breathe. Tomorrow is a fresh start to reclaim your health.")
        save_data(0, str(today))

if __name__ == "__main__":
    update_tracker()
