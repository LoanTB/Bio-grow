import pygame
import random
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
INITIAL_ZOOM = 1.0
ZOOM_STEP = 0.01
FPS = 100
INITIAL_POSITION = (400, 400)
INITIAL_RADIUS = 5
INITIAL_PROBABILITY = 0.5
LIFE_DECAY_RATE = 0.01
ROTATION_VARIATION_RANGE = 0.5
RADIUS_VARIATION_RANGE = 0.25
PROBABILITY_DECAY_RATE = 0.005
BACKGROUND_COLOR = (0, 0, 0)
RESET_KEY = pygame.K_r
MOUSE_LEFT_BUTTON = 1
MOUSE_SCROLL_UP = 4
MOUSE_SCROLL_DOWN = 5


# Global Variables
zoom_level = INITIAL_ZOOM
view_offset = [0, 0]


class Organism:
    """
    Represents an organism in the biological system.
    """

    def __init__(self, x, y, radius, reproduction_probability, rotation_angle):
        """
        Initializes an organism with position, size, reproduction probability, and rotation.

        Args:
            x (float): X-coordinate of the organism.
            y (float): Y-coordinate of the organism.
            radius (float): Radius of the organism.
            reproduction_probability (float): Probability of reproducing.
            rotation_angle (float): Rotation angle in radians.
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.reproduction_probability = reproduction_probability
        self.rotation_angle = rotation_angle
        self.life = 1.0
        self.is_locked = False
        self.last_view_state = view_offset.copy() + [zoom_level]

    def update(self):
        """
        Updates the life of the organism by decreasing it over time.
        """
        if self.life > 0:
            self.life -= LIFE_DECAY_RATE
            self.life = max(self.life, 0)

    def reproduce(self):
        """
        Attempts to create a child organism based on reproduction probability.

        Returns:
            Organism or None: A new Organism instance if reproduction is successful, otherwise None.
        """
        if self.life <= 0:
            return None
        if random.random() < self.reproduction_probability and not self.is_locked:
            if random.random() >= self.reproduction_probability * 0.1:
                self.is_locked = True
            new_rotation = self.rotation_angle + ROTATION_VARIATION_RANGE * (random.random() * 2 - 1)
            new_radius = self.radius + RADIUS_VARIATION_RANGE * (random.random() * 2 - 1)
            new_probability = self.reproduction_probability - PROBABILITY_DECAY_RATE * random.random()
            child_x = self.x + (self.radius + new_radius) * math.sin(new_rotation) / 2
            child_y = self.y + (self.radius + new_radius) * math.cos(new_rotation) / 2
            return Organism(child_x, child_y, new_radius, new_probability, new_rotation)
        return None

    def render(self, screen):
        """
        Renders the organism on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the organism on.
        """
        view_changed = (
            self.last_view_state[0] != view_offset[0] or
            self.last_view_state[1] != view_offset[1] or
            self.last_view_state[2] != zoom_level
        )
        if self.life > 0 or view_changed:
            self.last_view_state = view_offset.copy() + [zoom_level]
            color = (
                int(41 * (1 - self.life) + 100 * self.life),
                int(150 * self.life),
                int(255 * self.life + 86 * (1 - self.life))
            )
            screen_position = (
                int((self.x + view_offset[0]) * zoom_level),
                int((self.y + view_offset[1]) * zoom_level)
            )
            screen_radius = max(1, int(self.radius * zoom_level))
            pygame.draw.circle(screen, color, screen_position, screen_radius)


class BioSystem:
    """
    Manages the collection of organisms and their interactions.
    """

    def __init__(self):
        """
        Initializes the biological system with a single organism.
        """
        initial_organism = Organism(
            x=INITIAL_POSITION[0],
            y=INITIAL_POSITION[1],
            radius=INITIAL_RADIUS,
            reproduction_probability=INITIAL_PROBABILITY,
            rotation_angle=random.uniform(0, 2 * math.pi)
        )
        self.organisms = [initial_organism]

    def update(self):
        """
        Updates all organisms in the system and handles reproduction.
        """
        new_organisms = []
        for organism in self.organisms:
            child = organism.reproduce()
            if child:
                new_organisms.append(child)
            organism.update()
        self.organisms.extend(new_organisms)

    def render(self, screen):
        """
        Renders all organisms in the system.

        Args:
            screen (pygame.Surface): The surface to draw organisms on.
        """
        for organism in self.organisms:
            organism.render(screen)


def main():
    """
    The main function to run the biological system simulation.
    """
    global zoom_level, view_offset

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological System Simulation")
    clock = pygame.time.Clock()
    bio_system = BioSystem()
    running = True
    mouse_last_position = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == RESET_KEY:
                    bio_system = BioSystem()
                    screen.fill(BACKGROUND_COLOR)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == MOUSE_LEFT_BUTTON:
                    mouse_last_position = list(pygame.mouse.get_pos())
                elif event.button == MOUSE_SCROLL_UP:
                    zoom_level += ZOOM_STEP
                    screen.fill(BACKGROUND_COLOR)
                elif event.button == MOUSE_SCROLL_DOWN:
                    zoom_level = max(zoom_level - ZOOM_STEP, ZOOM_STEP)
                    screen.fill(BACKGROUND_COLOR)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == MOUSE_LEFT_BUTTON and mouse_last_position:
                    current_position = pygame.mouse.get_pos()
                    delta_x = current_position[0] - mouse_last_position[0]
                    delta_y = current_position[1] - mouse_last_position[1]
                    view_offset[0] += delta_x / zoom_level
                    view_offset[1] += delta_y / zoom_level
                    if delta_x != 0 or delta_y != 0:
                        screen.fill(BACKGROUND_COLOR)
                    mouse_last_position = None

        bio_system.update()
        clock.tick(FPS)
        bio_system.render(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
