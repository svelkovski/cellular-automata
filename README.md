# Cellular Automata Simulator

A simple interactive cellular automata simulation in Python using Pygame.  
Draw your own patterns and watch them evolve using Conway’s Game of Life rules.

## Rules (Conway's Game of Life)

1. **Live cell survives** if it has **2 or 3 neighbors**  
2. **Dead cell becomes alive** if it has **exactly 3 neighbors**  
3. **All other cells** die or remain dead

## Requirements

- Python 3.x  
- Pygame

## Installation

1. Clone the repository:
```bash
git clone https://github.com/svelkovski/cellular-automata.git
cd cellular-automata
```

2. Install dependencies:
```bash
pip install pygame
```

3. Run the program:
```bash
python main.py
```

## Controls

| Action                 | Key / Mouse              |
|------------------------|-------------------------|
| Draw cells             | Left Click (hold & drag)|
| Erase cells            | Right Click             |
| Start / Stop simulation| SPACE                   |
| Clear grid             | C                       |
