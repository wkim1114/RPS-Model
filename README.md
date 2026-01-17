# Adaptive RPS Agent

### Python-Based Behavioral Modeling for Rock-Paper-Scissors

**Author:** Woojung (Will) Kim
**Status:** Prototype / Educational
**Language:** Python 3.x

---

## Overview
This project implements an adaptive Artificial Intelligence agent designed to play Rock-Paper-Scissors against human or randomized opponents. Unlike simple random-choice bots, this agent utilizes **frequency-based prediction** and **heuristic point evaluation** to analyze opponent patterns in real-time and exploit behavioral biases.

This project serves as a study in **Game Systems Design** and **Algorithmic Decision Making**, demonstrating how statistical inference can be applied to game theory.

---

## The Models
The repository contains two distinct algorithmic approaches to solving the RPS meta:

### 1. Probability-Based Model (model_prob_based)
* **Logic:** Maintains a rolling window of the opponent's historical moves (e.g., last 50, 100, or 250 turns).
* **Mechanism:** Calculates the conditional probability of the opponent's next move based on the frequency distribution of their recent history.
* **Decision:** Selects the rigid counter-strategy to the opponent's most statistically likely move.
* **Use Case:** Highly effective against players who have subconscious patterns or "favorite" moves.

### 2. Point-Based Heuristic Model (model_point_based)
* **Logic:** Assigns dynamic "values" to each move based on recent win/loss outcomes.
* **Mechanism:** Tracks a live score of which move (Rock, Paper, or Scissors) is currently generating the highest return on investment (ROI).
* **Decision:** Greedily selects the move with the highest current point yield.
* **Use Case:** Simulates a "reactive" player that adapts to the current meta of the match.

---

## Logic & Code Structure

The core predictive logic relies on analyzing the opponent's distribution within a `list_size` window.

```python
# Core Probability Logic Snippet
rock_prob = opp_count.count("Rock") / list_size
paper_prob = opp_count.count("Paper") / list_size
scissor_prob = opp_count.count("Scissor") / list_size

# Determine optimal counter
if max(rock_prob, paper_prob, scissor_prob) == rock_prob:
    computer_choice = "Paper"  # Counter high-frequency Rock
