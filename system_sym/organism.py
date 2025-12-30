import math
import random
from system_sym import config

class Organism:
    def __init__(self, x, y, genome=None):
        self.x = x
        self.y = y
        self.name = "Organism"
        if genome is None:
            self.genome = {
                "color_r": random.randint(config.GENE_COLOR_MIN, config.GENE_COLOR_MAX),
                "color_g": random.randint(config.GENE_COLOR_MIN, config.GENE_COLOR_MAX),
                "color_b": random.randint(config.GENE_COLOR_MIN, config.GENE_COLOR_MAX),
                "speed": random.uniform(config.GENE_SPEED_MIN, config.GENE_SPEED_MAX),
                "size": random.randint(config.GENE_SIZE_MIN, config.GENE_SIZE_MAX),
                "photosynthesis": random.random(),
            }
        else:
            self.genome = genome

        self._express_genes()


        self.energy = config.STARTING_ENERGY  # Starting energy
        self.alive = True
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)

    def respond(self):
        return f"{self.name} is reporting for duty!"
    
    def update(self, width, height):
        if not self.alive:
            return
        #move
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off walls
        if self.x <= self.radius or self.x >= width - self.radius:
            self.vx *= -1
        if self.y <= self.radius or self.y >= height - self.radius:
            self.vy *= -1
        
        # Keep within bounds
        self.x = max(self.radius, min(width - self.radius, self.x))
        self.y = max(self.radius, min(height - self.radius, self.y))
        
        # Lose energy over time
        self.energy -= config.ENERGY_DECAY_RATE
        if self.energy <= 0:
            self.alive = False
    
    def draw(self, screen):
        """Draw the organism on a pygame surface"""
        if self.alive:
            import pygame
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        


    def _express_genes(self):        
        """Set organism traits based on its genome"""
        green = int(self.genome["color_g"])
        if self.can_photosynthesize() and int(self.genome["color_g"]) < 255/2:
            green +=  (config.GREEN_BOOST_PHOTO) # Boost green for photosynthetic organisms
        else:
            green -=  (config.GREEN_BOOST_PHOTO) # Reduce green for non-photosynthetic organisms
        green = max(0, min(255, green))  # Clamp between    0-255

        self.color = (
            int(self.genome["color_r"]),
            int(green),
            int(self.genome["color_b"])
            )

        self.max_speed = self.genome["speed"] * 5  # 0-5 
        self.radius = int(self.genome["size"] * 10) + 3  # 3-13 (ensures minimum size)
        
        # Initialize velocity based on speed gene
        angle = random.uniform(0, 2 * math.pi) 
        self.vx = self.max_speed * math.cos(angle)
        self.vy = self.max_speed * math.sin(angle)

    def reproduce(self):
        """Create a new organism based on the current organism's genome"""
        child_genome = {}
        for gene, value in self.genome.items():
            mutation = random.uniform(-0.1, 0.1)
            child_genome[gene] = value + mutation

        # deplete the parent's energy
        self.energy -= config.REPRODUCTION_ENERGY_COST
        return Organism(self.x, self.y, genome=child_genome)

    def can_reproduce(self):
        if self.alive and self.energy >= config.REPRODUCTION_ENERGY_THRESHOLD:
            print ( self.color," Reproducing! with energy:", self.energy)
        return self.energy >= config.REPRODUCTION_ENERGY_THRESHOLD and self.alive

    def can_photosynthesize(self):
        """Check if organism has photosynthesis capability"""
        return self.genome["photosynthesis"] > config.PHOTOSYNTHESIS_THRESHOLD  # Threshold

    def photosynthesize(self, sunlight_level):
        """Gain energy from sunlight"""
        if self.can_photosynthesize():
            efficiency = self.genome["photosynthesis"]
            energy_gain = sunlight_level * efficiency * config.PHOTOSYNTHESIS_EFFICIENCY  # Scale factor
            self.energy += energy_gain

    def eat(self, material):
        """Consume a material for energy"""
        if not material.consumed:
            self.energy += material.energy_value
            material.consumed = True