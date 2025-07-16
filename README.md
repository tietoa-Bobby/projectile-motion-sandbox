# Projectile Motion Sandbox

A 2D physics simulator for projectile motion, featuring real-time visualisation using Pygame and flexible CLI input. Perfect for learning, teaching, or analysing projectile motion in physics.

## Features
- Simulate projectile motion with adjustable parameters:
  - Initial velocity (metres/second)
  - Launch angle (degrees)
  - Gravity (metres/second²)
  - (Optional) Air resistance toggle
- Animated trajectory visualisation in a Pygame window
- Real-time display of time, position, and velocity
- Restart or exit simulation with keyboard input
- Input parameters via command-line arguments or interactive prompts
- Modular codebase for easy extension
- (Optional) Export trajectory data to CSV for analysis

## Physics Background
The simulation uses the standard equations of motion for projectiles:

- **Horizontal motion:**
  - $x(t) = v_0 \cos(\theta) t$
- **Vertical motion:**
  - $y(t) = v_0 \sin(\theta) t - \frac{1}{2} g t^2$
- **With air resistance (optional):**
  - Linear drag model (see code for details)

## Usage
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the simulator:
   ```bash
   python main.py
   ```
   Or provide arguments:
   ```bash
   python main.py --velocity 20 --angle 45 --gravity 9.81
   ```
3. Follow on-screen instructions to restart or exit.

## File Structure
- `main.py` - Entry point, CLI handling
- `simulation.py` - Physics calculations
- `visualiser.py` - Pygame visualisation
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## Licence
MIT Licence 