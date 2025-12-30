import pygame
import random
from system_sym.organism import Organism
from system_sym.material import Material
from system_sym import config

class Environment:
    def __init__(self, width=config.WINDOW_WIDTH, height=config.WINDOW_HEIGHT):
        self.width = width
        self.height = height
        self.organisms = [] # List to hold organisms
        self.materials = [] # Placeholder for environmental materials
        self.sunlight_level = config.DEFAULT_SUNLIGHT_LEVEL # Simulated sunlight level (0.0 to 1.0)
        self.background_color = config.BACKGROUND_COLOR
        self.name = "Environment"
        self.cycle_count = 0
        self.spawn_food()
    
    def respond(self):
        return f"{self.name} is ready to sustain life!"
    
    def add_organism(self, organism):
        """Add an organism to the environment"""
        self.organisms.append(organism)
    
    def spawn_random_organisms(self, count=3):
        """Spawn organisms at random positions"""
        
        for i in range(count):
            x = random.randint(100, self.width - 100)
            y = random.randint(100, self.height - 100)
            
            org = Organism(x, y, genome=None)
            self.add_organism(org)
    
    def update(self):
        """Update all organisms"""
        new_organisms = [] # To hold newly reproduced organisms

        for org in self.organisms:
            org.update(self.width, self.height)
            org.photosynthesize(self.sunlight_level) 
               # Check for nearby food
            for material in self.materials:
                if not material.consumed:
                    distance = ((org.x - material.x)**2 + (org.y - material.y)**2)**0.5
                    if distance < org.radius + material.radius:
                        org.eat(material)

            # Check if the organism can reproduce
            if len(self.organisms) < 5 and org.can_reproduce():
                child = org.reproduce()
                if child is not None:
                    new_organisms.append(child)
        
        self.organisms.extend(new_organisms)

        # Remove dead organisms
        self.organisms = [org for org in self.organisms if org.alive]

        if self.cycle_count % config.FOOD_SPAWN_INTERVAL == 0:
            self.spawn_food(count=config.FOOD_SPAWN_AMOUNT)
            self.cycle_count = 0
        else:
            self.cycle_count += 1

    
    def draw(self, screen):
        """Draw the environment and all organisms"""
        screen.fill(self.background_color)
    
        # Draw materials first (background layer)
        for material in self.materials:
            pygame.draw.circle(screen, material.color, 
                            (int(material.x), int(material.y)), material.radius)
        for org in self.organisms:
            org.draw(screen)

    def spawn_food(self, count=10):
        """Spawn food particles randomly"""
        for _ in range(count):
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 50)
            food = Material(x, y, material_type="food", energy_value=30)
            self.materials.append(food)