# Adaptive RPS Agent

> Adaptive game AI exploring opponent modeling, probability-based prediction, and heuristic decision-making in Python.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Complete-success)

---

## Overview

Adaptive RPS Agent is a Python project that explores how simple AI strategies can learn and adapt to an opponent's behavior in repeated games.

Rather than relying on random play, the agent continuously analyzes observed actions and adjusts its strategy using statistical inference and heuristic evaluation. The project demonstrates how lightweight learning algorithms can improve decision-making without requiring complex machine learning models.

Although implemented for Rock–Paper–Scissors, the underlying ideas extend to broader topics such as:

- Game AI
- Opponent modeling
- Behavioral prediction
- Adaptive decision-making
- Game systems

---

## Algorithms

The repository implements two independent adaptive strategies.

### Probability-Based Agent

The probability model estimates an opponent's future actions using a rolling history window.

**Approach**

- Maintains a configurable history window (50, 100, or 250 turns)
- Estimates empirical probabilities for each action
- Predicts the opponent's most likely next move
- Selects the optimal counter-strategy

This approach performs well against opponents with consistent behavioral tendencies.

---

### Point-Based Heuristic Agent

The heuristic model adapts by rewarding strategies that have recently been successful.

**Approach**

- Tracks cumulative performance for each move
- Continuously updates heuristic scores after every round
- Chooses the move with the highest current expected value
- Falls back to random exploration when appropriate

This strategy behaves similarly to a reactive player adapting to changing match dynamics.

---

## Project Structure

```text
.
├── rps_prob.py      # Probability-based adaptive agent
├── rps_point.py     # Point-based heuristic agent
└── README.md
```

---

## Example

The probability-based agent predicts an opponent's behavior from recent history.

```python
rock_prob = opp_count.count("Rock") / list_size
paper_prob = opp_count.count("Paper") / list_size
scissor_prob = opp_count.count("Scissor") / list_size

if max(rock_prob, paper_prob, scissor_prob) == rock_prob:
    computer_choice = "Paper"
```

The probability distribution is updated after every round, allowing the agent to continuously adapt as the opponent's behavior changes.

---

## Skills Demonstrated

- Python
- Algorithm Design
- Probability Estimation
- Behavioral Modeling
- Game AI
- Simulation
- Software Documentation

---

## Recognition

🏆 Awarded **Best Application of Course Concepts** at the UNC COMP110 Hackathon.

---

## Future Improvements

Potential future extensions include:

- Markov-chain opponent modeling
- Bayesian prediction
- Reinforcement learning
- Monte Carlo simulation
- Visualization of learning behavior
