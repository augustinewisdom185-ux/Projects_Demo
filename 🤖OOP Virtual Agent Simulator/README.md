# 🤖 OOP Virtual Agent Simulator

A lightweight, object-oriented state-machine simulator built in Python that models physical lifecycle parameters (Energy, Happiness, Temporal Rest Durations) for specialized virtual sub-agents. 

This project demonstrates clean implementations of **Inheritance**, **Encapsulation**, and **Dynamic State Calculations** based on real-time execution pauses.

---

## 🚀 Key Features

- **Object-Oriented Design (OOP):** Utilizes a robust base class (`VirtualSimulator`) to govern universal properties, cleanly extended by specialized modules (`ChatBotPet`, `VisionBotPet`).
- **State Machine Management:** Dynamically modifies internal state pools (capped safely between 0% and 100%) depending on the operations requested.
- **Dynamic Rest Profiler:** Implements real-time system clock analysis (`datetime`) to accurately record, calculate, and log exact rest cycles down to the second.

---

## 🛠️ Architecture & Class Structure

### 1. `VirtualSimulator` (Base Class)
The architectural foundation. It sets up foundational properties (`name`, `energy`, `happiness`) and handles the complex math behind the resource recovery algorithm (`sleep`).

### 2. `ChatBotPet` (Child Class)
A specialized NLP-agent mockup that increases user engagement metrics (Happiness) at the expense of computational reserves (Energy).

### 3. `VisionBotPet` (Child Class)
A specialized spatial-recognition simulation block that consumes massive computational overhead (Energy) to execute high-value sensor sweeps.

---

## 💻 Test Execution Pipeline

The included `__main__` test runtime demonstrates the state machine mechanics under compounding stress and recovery cycles:
1. **Multi-Turn Stress Testing:** `Byte` (`ChatBotPet`) executes back-to-back chat loops to show sequential stat drains.
2. **Critical Exhaustion Testing:** `Aero` (`VisionBotPet`) executes rapid room scans to drop its energy reserves significantly.
3. **Targeted Delta Recovery:** `Aero` goes to sleep for a controlled 3-second window to run clock duration math and recover energy metrics.
4. **Final Lifecycle Audit:** Prints the concluding decoupled system metrics for both independent agents side-by-side.

---

## 📦 How to Run

1. Clone this repository to your local directory:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the directory:
   ```bash
   cd virtual-agent-simulator
   ```
3. Run the simulation platform:
   ```bash
   python simulator.py
   ```

---

## 📈 Future Architecture Roadmap
- [ ] **Data Persistence:** Integrate a local JSON database system to cache agent configurations and structural states between sessions.
- [ ] **Interactive CLI Console:** Build a full interactive command loop interface (`while` loop input engine) allowing real-time runtime control.
- [ ] **Asynchronous Decay:** Convert stat deterioration routines into live background processes using `threading` or `asyncio`.
