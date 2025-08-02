# 🧩 Rubik’s Cube Solver

This project is a Python-based **Rubik's Cube Solver** that uses the **CFOP (Cross, F2L, OLL, PLL)** algorithm. It features a move engine, solving logic, and a 2D visualizer built with Pygame to simulate each solving step.

---

## 👨‍💻 Submitted By

**Rithish H R**  
Sahyadri College of Engineering and Management  
GitHub: https://github.com/rithishhr 
Email: rithish20047@gmail.com  

---

## 📌 Project Highlights

- ✅ Full 3x3 Rubik’s Cube Solver using CFOP method
- 🔁 Simulates face turns, edge rotations, and whole cube rotations
- 📊 Efficient modular architecture with solver and move engine
- 🎨 Visual 2D UI built using Pygame
- ♻️ Move optimization logic (e.g., `R R → R2`)
- 🚀 Solves scrambles in under 1 second

---

## 🛠️ Tools & Technologies

| Tool       | Purpose                             |
|------------|-------------------------------------|
| Python     | Core logic, data structures         |
| Pygame     | 2D visualization of the cube        |
| Git/GitHub | Version control and project hosting |

---

## 📁 Folder Structure

RubiksCubeSolver/
│
├── Cube.py # Cube engine and move simulation
├── Solver.py # CFOP solver logic
├── helper.py # Utilities (move parser, optimizer)
├── solver_data.py # Lookup tables for F2L, OLL, PLL
├── visualizer.py # Pygame-based UI

---

## ▶️ How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
python demo.py
