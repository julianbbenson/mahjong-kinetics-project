# The Kinetics of Riichi Mahjong: A Stochastic Biochemical Analysis

**Project Lead:** Julian Benson

**Dataset:** $N = 1,087,446$ Tenhou Phoenix Room Logs (2025)

## Overview

This project investigates the non-linear probability curves of Riichi Mahjong through the lens of **Michaelis-Menten enzyme kinetics**. By treating a "Tenpai" (ready) hand as a catalytic enzyme and the depleting tile wall as a substrate pool, we derived a **Michaelis Constant ($K_m$) of ~64 tiles**.

![Experimental Saturation Curve](https://files.catbox.moe/kh0a0c.png)

The results mathematically demonstrate that Mahjong is a **substrate-limited system**, providing a rigorous kinetic explanation for strategic "failure points" in the late game.

---

## Core Findings

* **Conformational Locking:** We model the *Riichi* declaration as a conformational lock, where a player sacrifices structural flexibility for an exponential increase in potential energy (payout).
* **The Starvation Threshold:** Because a standard game starts with only 70 substrate units (tiles) and has a $K_m$ of 64, the "reaction" operates in a state of starvation from Turn 1.
* **Kinetic Failure:** Win rates collapse non-linearly. We identify Turn 8 as the critical kinetic threshold after which the board state can no longer support high-efficiency product formation.

---

## Repository Contents

* **`Mahjong_Kinetics_Paper.md`**: The full documentary-style deep dive, covering the evolutionary history of the game, the protein dynamics of the hand, and the thermodynamic implications of the "Rule of 64."
* **`harvest_data.py`**: High-performance parser for Tenhou JSON logs.
* **`analyze_kinetics.py`**: Regression script using `scipy.optimize` to calculate $V_{max}$ and $K_m$ from experimental data.
* **`kinetics_data.csv`**: The processed dataset ($>1M$ records).

---

## Quick Start

```bash
pip install -r requirements.txt
python analyze_kinetics.py

```

## [Read the Full Paper Here](https://github.com/julianbbenson/mahjong-kinetics-project/blob/main/Mahjong_Kinetics_Paper.md)
