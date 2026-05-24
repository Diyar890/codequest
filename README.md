# ⚔️ CodeQuest: Algorithm Roguelike

> A browser-based RPG where you defeat monsters by solving real algorithmic tasks — powered by Flask + Judge0 API.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![Judge0](https://img.shields.io/badge/Judge0-Code%20Execution-green)
![Status](https://img.shields.io/badge/Phase-2%20OOP-orange)

---

## 📖 About

**CodeQuest** is a fullstack educational game inspired by Hades. Instead of swinging a sword, you write code. Your solution is sent to a real sandbox (Judge0), tested against real test cases, and the result determines how much damage you deal to the enemy.

Built as a university pair project for a Python course.

---

## 🎮 How It Works

```
You enter the dungeon...
👾 TREE_SUM MONSTER (Medium) appears!

⏱️  TIME LIMIT Attack: 60s
💾 MEMORY LIMIT Attack: 256MB

[ Code Editor — Python ]
1  def two_sum(nums, target):
2      ...

> Submit

Judge0: TESTING... (4/5 test cases passed)
✅ Accepted!  → You deal 30 damage to the monster!
❌ TLE!       → Monster deals 20 damage to you!
💥 CE!        → Compilation Shield blocks the attack!
```

---

## ✨ Features

- ⚔️ **Code battles** — defeat enemies by solving algorithmic tasks in real time
- 🧠 **Judge0 integration** — code runs in a real sandbox with test cases
- 🐍 **Language inventory** — start with Python, unlock C (lvl 5) and C++ (lvl 10)
- ⏱️ **Time & Memory limits** — TLE and MLE deal damage to your character
- 🧪 **Artifact system** — Clean Code Potion restores HP, Compilation Shield blocks CE
- 💾 **Save system** — game state saved to JSON
- 📊 **Task bank** — algorithmic problems by difficulty (Easy → Hard)

---

## 🗂️ Project Structure

```
codequest/
├── main.py                  # Entry point + OOP tests
├── game/
│   ├── __init__.py          # Module exports
│   ├── player.py            # Player class
│   ├── enemy.py             # Enemy + Boss classes
│   ├── task.py              # Task class + task bank
│   ├── battle.py            # Battle class (Core)
│   ├── judge0_result.py     # Judge0Result class
│   ├── inventory.py         # Item + Inventory classes
│   └── game_save.py         # GameSave class (JSON)
├── api/
│   ├── judge0.py            # Judge0 API client (Phase 3)
│   └── checker.py           # Verdict → damage calculator (Phase 3)
├── static/
│   ├── game.js              # Map + UI (Phase 4)
│   └── editor.js            # CodeMirror editor (Phase 4)
├── templates/
│   ├── game.html            # Main game screen (Phase 4)
│   └── battle.html          # Battle screen (Phase 4)
└── saves/
    └── save.json            # Player save file
```

---

## 🧬 UML Class Diagram

| Class | Role |
|-------|------|
| `PLAYER` | Hero — hp, level, gold, language inventory |
| `BATTLE` | ⭐ Core — connects player, enemy, task, result |
| `ENEMY` | Monster — hp, attack, difficulty |
| `BOSS` | Inherits Enemy — adds TLE/MLE special attacks |
| `TASK` | Algorithmic problem — description, test cases, limits |
| `JUDGE0_RESULT` | Code execution result — verdict, tests passed, exec time |
| `ITEM` | Artifact — potion, shield, language gem |
| `INVENTORY` | Player's item storage |
| `GAME_SAVE` | Save/load game state via JSON |

---

## 🎮 Language Inventory

| Language | Unlock Level | Status |
|----------|-------------|--------|
| 🐍 Python | Level 1 | ✅ Default |
| 🔵 C | Level 5 | 🔒 Locked |
| 🔷 C++ | Level 10 | 🔒 Locked |
| 🟡 JavaScript | Bonus | ✅ Always |

---

## ⚙️ Getting Started

```bash
# Clone the repo
git clone https://github.com/Diyar890/codequest.git
cd codequest

# Run OOP tests (Phase 2)
python3 main.py
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10+, Flask |
| Code execution | Judge0 API |
| Frontend | HTML, CSS, JavaScript |
| Code editor | CodeMirror |
| Save system | JSON |
| Tasks source | LeetCode / Codeforces |

---

## 📅 Development Phases

| Phase | Status | Description |
|-------|--------|-------------|
| Phase 1 | ✅ Done | UML Class Diagram |
| Phase 2 | ✅ Done | OOP — 8 classes implemented |
| Phase 3 | 🔄 Next | Flask backend + Judge0 API |
| Phase 4 | ⏳ | Frontend — game map + code editor |
| Phase 5 | ⏳ | Full integration |
| Phase 6 | ⏳ | Polish + final presentation |

---

## 👥 Authors

- **Diyar** — Backend, game logic
- **[Partner]** — Frontend, API integration

University Python Course — 2026

---

## 📄 License

MIT License — free to use and modify.

---

*Built with ❤️, Python, and way too many algorithm problems*
