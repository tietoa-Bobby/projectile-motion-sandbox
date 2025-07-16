"""
visualiser.py - Pygame visualisation for projectile motion
"""
import pygame
import sys
import csv

def run_visualisation(sim, save_csv=None):
    """
    Animates the projectile motion using Pygame.
    Args:
        sim: ProjectileSimulation instance
        save_csv: Optional path to save trajectory data as CSV
    """
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Projectile Motion Sandbox")
    font = pygame.font.SysFont(None, 28)
    clock = pygame.time.Clock()

    # Scaling factors for visualisation
    scale = 8  # pixels per metre
    ground_y = HEIGHT - 50
    origin = (50, ground_y)

    running = True
    while running:
        sim.reset()
        trajectory_points = []
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        done = True  # Restart
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            t, x, y, vx, vy = sim.step()
            trajectory_points.append((x, y))
            screen.fill((255, 255, 255))
            # Draw ground
            pygame.draw.line(screen, (0, 0, 0), (0, ground_y), (WIDTH, ground_y), 2)
            # Draw trajectory
            for i in range(1, len(trajectory_points)):
                x1, y1 = trajectory_points[i-1]
                x2, y2 = trajectory_points[i]
                p1 = (origin[0] + int(x1 * scale), ground_y - int(y1 * scale))
                p2 = (origin[0] + int(x2 * scale), ground_y - int(y2 * scale))
                pygame.draw.line(screen, (0, 100, 255), p1, p2, 2)
            # Draw projectile
            proj_pos = (origin[0] + int(x * scale), ground_y - int(y * scale))
            pygame.draw.circle(screen, (255, 0, 0), proj_pos, 8)
            # Display info
            info = f"t={t:.2f}s  x={x:.2f}m  y={y:.2f}m  v=({vx:.2f},{vy:.2f}) m/s"
            text = font.render(info, True, (0, 0, 0))
            screen.blit(text, (20, 20))
            hint = font.render("[R]estart  [ESC] Exit", True, (100, 100, 100))
            screen.blit(hint, (20, 55))
            pygame.display.flip()
            clock.tick(60)
            if not sim.is_active():
                done = True
        # Save CSV if requested
        if save_csv:
            with open(save_csv, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['time', 'x', 'y', 'vx', 'vy'])
                for row in sim.get_trajectory():
                    writer.writerow(row)
        # Wait for user to restart or exit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False  # Restart
                        running = True
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            clock.tick(10) 