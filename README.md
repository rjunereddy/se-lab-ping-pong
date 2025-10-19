Ping Pong Game 🏓
A real-time Ping Pong game built with Python and Pygame featuring smooth gameplay, AI opponent, sound effects, and replay system.

Features ✨
🎮 Gameplay
Smooth Controls: Responsive paddle movement with W/S keys

Smart AI: Competitive but beatable AI opponent

Realistic Physics: Ball collision with angle variation based on hit position

Visual Feedback: Clean UI with score display and center line

🎵 Sound System
Built-in Sound Effects: Programmatically generated sounds (no external files needed)

Three Distinct Sounds:

🎯 Paddle Hit: High-pitched beep (660Hz)

🧱 Wall Bounce: Medium-pitched beep (440Hz)

⚽ Score: Long high-pitched beep (880Hz)

🏆 Game Modes
Best of Series: Choose between Best of 3, 5, or 7 games

Replay System: Play multiple sessions without restarting

Game Over Screen: Clear winner announcement with final score

Installation 🚀
Prerequisites
Python 3.6 or higher

pip (Python package manager)

Step-by-Step Setup
Create Project Structure

text
pingpong-game/
├── main.py
├── requirements.txt
└── game/
    ├── game_engine.py
    ├── paddle.py
    └── ball.py
Install Dependencies

bash
pip install pygame numpy
Run the Game

bash
python main.py
How to Play 🎯
Controls
W Key: Move paddle UP

S Key: Move paddle DOWN

ESC Key: Quit game (anytime)

3/5/7 Keys: Choose replay series after game over

Game Rules
Score points by getting the ball past your opponent's paddle

First player to reach the winning score wins the match

Ball speed and angle vary based on where it hits the paddle

Replay System
After each game, you can choose:

Best of 3 (first to 2 wins)

Best of 5 (first to 3 wins)

Best of 7 (first to 4 wins)

ESC to quit

Project Structure 📁
text
pingpong-game/
├── main.py                 # Entry point and sound initialization
├── requirements.txt        # Project dependencies
└── game/                  # Game logic package
    ├── game_engine.py     # Main game controller and rendering
    ├── paddle.py          # Paddle class with movement logic
    └── ball.py            # Ball class with physics and collision
Code Files
