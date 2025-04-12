# One Finger Salute 🫡

<img src="./assets/one-finger-salute.gif" alt="One Finger Salute (AI Generated)"/>

> ⚠️ **NSFW Warning:** This project involves explicit gestures, words etc. Use responsibly and for fun only.

Shut down your PC with a **middle finger**.  
Just type `fuckyou`, flip the bird, and your machine goes *bye bye*.  
No dialogs. No prompts. Just pure **rage quit** energy. 👍👍👍

## Demo Video

[Demo.mp4](assets/one-finger-salute.mp4)

---

## 🤔 Why?

Because... why not?  
A power-off command with feeling.

---

## 💡 How useful is it?

🛑 **Not at all.**  
But it sure is fun
to flip the bird at your computer and watch it shut down.
---

## ⚙️ How does it work?

This is a simple python script that uses mediapipe and opencv along with
the [hand gesture model](https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task)
to detect the middle finger gesture.

- 🤖 `mediapipe`
- 🎥 `opencv`
- 👉
  A [hand gesture model](https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task)

When the middle finger gesture is detected, it sends a shutdown command to the operating system. Should work on Windows,
Linux, and MacOS. Its calls the shutdown command, so it might require admin privileges.

> 💡 **Tech Note:** It checks the relative position of other fingers to the middle finger to determine if it's raised.
> May not be super accurate, but it worked in my testing :)

---

## 🚀 Installation

Install it directly via `pip`:

```bash
pip install git+https://github.com/fbn776/OneFingerSalute.git
```

---

## 🛠️ Dev Setup

### 1️⃣ Create a virtual environment

```bash
python -m venv .venv

# For Linux/Mac users:
python3 -m venv .venv
```

### 2️⃣ Activate the virtual environment

```bash
# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\Activate
```

### 3️⃣ Install the dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Launch the finger-powered fury

```bash
python src/main.py
```

---

## 🎉 Final Thoughts

This is **completely pointless** project. It exists, simple beacause it can

Pro tip:
If installation doesn't work, use a alias to run the script;
`fuckyou="python src/main.py"` 😆

- The image <img src="./assets/one-finger-salute.gif" alt="One Finger Salute (AI Generated)" width="24px"/> is generated
by chatGPT.
