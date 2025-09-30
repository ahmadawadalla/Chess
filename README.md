# ♟️ Chess Game (Pygame)

A fully playable **Chess game** built in Python using **Pygame**.  
Supports all standard chess rules including **castling, en passant, pawn promotion**, and features an **undo/redo system** for move history navigation.

---
# Features
- All standard chess pieces with correct movement rules:
  - Pawn (**en passant**, promotion)
  - Rook
  - Knight
  - Bishop
  - Queen
  - King (**castling with check validation**)
- Turn-based play (white vs black)
- **Move highlighting** (possible moves shown on the board as well as the last move the user made)
- **Pawn promotion menu** (choose queen, rook, bishop, knight)
- **Undo / Redo** support with arrow keys
- Piece images for white/black
- Coordinate labels (ranks & files)

---

## 🖥️ Requirements
- Python 3.8+
- [Pygame](https://www.pygame.org/)

Install dependencies:
```bash
pip install pygame
```

---

## ▶️ How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/ahmadawadalla/Chess.git
   cd Chess
   ```
2. Run the game:
   ```bash
   python Game.py
   ```

---

## 🎮 Controls
- **Left-click** a piece to select it.
- **Left-click** a square to move.
- **Undo/Redo**:
  - Press `←` (Left Arrow) → Undo last move
  - Press `→` (Right Arrow) → Redo undone move
- Close the window or press `ESC` to quit.

---

## 📂 Project Structure
These are the main files in the **Chess** directory:

```
Chess/
│── Bishop.py       # Bishop movement logic
│── Board.py        # Board logic, drawing, move handling
│── Chess.iml       # IntelliJ/PyCharm project config
│── Game.py         # Main game loop
│── King.py         # King movement logic (inc. castling rules)
│── Knight.py       # Knight movement logic
│── Pawn.py         # Pawn movement logic (inc. en passant, promotion)
│── Piece.py        # Initializes all pieces in starting position
│── Queen.py        # Queen movement logic
│── Rook.py         # Rook movement logic
│── README.md       # Project documentation
```

> Other directories (e.g., `Images/`, `Sounds/`) contain assets like piece graphics and sound effects.

---

## 🛠️ To-Do / Possible Improvements
- Optimize move generation (currently recalculates all enemy moves).
- Add AI opponent (minimax or Stockfish integration).
- Add multiplayer (local or online).
- Add timers for blitz mode.

---

## 📜 License
MIT License. Free to use, modify, and distribute.
