# Bio Grow Simulation

Bio Grow is a generative simulation project developed with Python and Pygame. The simulation visualizes a biological growth system, where organisms replicate based on probabilistic factors, producing an intricate network of life-like entities. This simulation is ideal for users interested in observing natural patterns, biological decay, and growth dynamics in a visualized environment.

![image](https://github.com/user-attachments/assets/968372cc-ab8a-489c-96c4-63d912faf352)

![image](https://github.com/user-attachments/assets/530952d2-4582-4216-83b5-6081d60f5127)

![image](https://github.com/user-attachments/assets/4bb1daed-77ed-4bf5-8791-50fcb4125444)


## Features

- **Organism Growth**: Organisms grow, decay, and reproduce, creating a network of interconnected entities over time.
- **Probabilistic Reproduction**: Each organism has a unique probability of reproducing, allowing for diverse growth patterns.
- **Life Decay and Regeneration**: Organisms gradually lose vitality, adding a realistic decay factor to the system.
- **Zoom and Pan**: Control the view by zooming in and out or panning across the environment to explore various growth areas.
- **Dynamic Color Changes**: Organisms change colors over their life cycle, enhancing visual feedback on growth stages.

## Requirements

- **Python 3.x**
- **Pygame**: Install via pip with `pip install pygame`

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/LoanTB/Bio-grow.git
   cd Bio-grow
   ```

2. Install Pygame if not already installed:
   ```bash
   pip install pygame
   ```

3. Run the simulation:
   ```bash
   python main.py
   ```

## Controls

- **Left Mouse Button**: Click and drag to pan the view.
- **Mouse Scroll Up/Down**: Zoom in or out.
- **R Key**: Reset the simulation to its initial state.

## Project Structure

- **`Organism` Class**: Represents each organism's properties, including position, size, life decay, and reproduction probability.
- **`BioSystem` Class**: Manages the collection of organisms, handling updates and interactions.
- **`Main Loop`**: Processes user input, updates organism states, and renders the simulation on the screen.

## Simulation Details

- **Growth Patterns**: Organisms replicate based on a probabilistic algorithm, generating children organisms with varying sizes, rotation, and decay rates.
- **Life Decay**: Organisms lose life over time, impacting color and visual appearance, creating a realistic aging effect.
- **Zoom and Pan**: Adjust the view to explore different areas of the simulation, especially useful for observing complex growth networks.

## HUD and Visualization

The simulation visualizes organism life cycles with dynamic color changes:
- **Color Gradients**: Indicate organism vitality, transitioning from vibrant hues to dull tones as they age.
- **Position Tracking**: Organisms appear in clusters, growing in proximity to their parent organisms.

## Customization

You can modify various parameters in the `Organism` and `BioSystem` classes to alter simulation dynamics:
- **Initial Reproduction Probability**
- **Life Decay Rate**
- **Zoom Sensitivity**

These parameters allow for a range of growth styles and can be adjusted to create unique visual effects.

## License

This project is licensed under the Mozilla Public License 2.0 (MPL-2.0).

### Additional Note on Commercial Use
**Commercial use of this software or any derived works is prohibited without prior written permission from the original author.** For commercial licensing inquiries, please contact loan.tremoulet.breton@gmail.com.
