"""
main.py - Entry point for Projectile Motion Sandbox
Handles CLI arguments, user prompts, and runs the simulation and visualisation.
"""
import argparse
from simulation import ProjectileSimulation
from visualiser import run_visualisation

def get_args():
    parser = argparse.ArgumentParser(description="2D Projectile Motion Simulator")
    parser.add_argument('--velocity', type=float, help='Initial velocity (metres/second)')
    parser.add_argument('--angle', type=float, help='Launch angle (degrees)')
    parser.add_argument('--gravity', type=float, default=9.81, help='Gravity (metres/second²)')
    parser.add_argument('--air', action='store_true', help='Enable air resistance')
    parser.add_argument('--csv', type=str, help='Optional: Save trajectory to CSV file')
    args = parser.parse_args()
    # Interactive prompts if not provided
    if args.velocity is None:
        args.velocity = float(input('Initial velocity (metres/second): '))
    if args.angle is None:
        args.angle = float(input('Launch angle (degrees): '))
    return args

def main():
    args = get_args()
    sim = ProjectileSimulation(
        velocity=args.velocity,
        angle_deg=args.angle,
        gravity=args.gravity,
        air_resistance=args.air
    )
    run_visualisation(sim, save_csv=args.csv)

if __name__ == "__main__":
    main() 