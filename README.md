# Snake AI — Deep Q-Learning

A reinforcement learning agent that learns to play Snake from scratch using a Deep Q-Network (DQN), built with PyTorch and Pygame.

## How it works

The agent observes an 11-value state vector (danger straight/right/left, current direction, food location relative to the head), and picks one of three actions: go straight, turn right, or turn left. It's trained online with a mix of short-term (per-step) and long-term (batched replay) memory updates.

- **`snake_game.py`** — the Snake game environment (Pygame), exposing `reset()`, `play_step(action)`, and `is_collision()` so the agent can drive it programmatically and receive rewards.
- **`model.py`** — the neural network (`Linear_QNet`, an 11→256→3 fully connected net) and the `Qtrainer` that runs the Bellman-equation update step.
- **`agent.py`** — the `Agent` class (state extraction, memory buffer, epsilon-greedy action selection) and the main training loop.
- **`helper.py`** — live matplotlib plotting of score and rolling mean score during training.

## Requirements

- Python 3.8+
- [PyTorch](https://pytorch.org/get-started/locally/)
- Pygame
- Matplotlib
- NumPy

Install with:
```bash
pip install torch pygame matplotlib numpy
```

## Running it

```bash
python agent.py
```

This launches the game window and a live plot window side by side. The agent starts by exploring randomly and gradually shifts to exploiting what it's learned. Progress prints to the console after every game:

```
Game 1 Score 0 Record: 0
Game 2 Score 1 Record: 1
...
```

The best-performing model is automatically saved to `./model/model.pth` whenever a new high score is reached.

## Notes

- Training runs indefinitely (`while True`) — stop it manually (Ctrl+C) once the average score plateaus or you're satisfied with performance.
- The game speed is controlled by the `SPEED` constant in `snake_game.py` — lower it to watch the agent play more slowly, raise it to train faster.
- Since exploration is epsilon-greedy and decays with `agent.n_games`, expect noisy scores early on, with the rolling mean score trending upward over time.

## Possible improvements

- Add a target network to stabilize Q-value targets.
- Tune the reward shaping (e.g., small reward for moving closer to food).
- Experiment with a deeper network or a convolutional input (raw pixels instead of the 11-value state).
- Add prioritized experience replay.

## License

Feel free to use, modify, and learn from this project.
