import pygame
from system_sym.environment import Environment
from system_sym import config

class Simulation:
    def __init__(self, width=config.WINDOW_WIDTH, height=config.WINDOW_HEIGHT, fullscreen=False):
        pygame.init()
        
        self.name = "Simulation"
        if fullscreen:
            self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
            # Windowed mode - slightly smaller for easier testing
            self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        
        pygame.display.set_caption("SystemSym - Biosphere Simulator")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.environment = Environment(width=self.screen.get_width(), 
                                       height=self.screen.get_height())
        
        # Spawn initial organisms
        self.environment.spawn_random_organisms(count=3)

    def respond(self):
        return f"{self.name} is up and running!"
    
    def handle_events(self):
        """Handle keyboard and window events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    # Spawn more organisms on spacebar
                    self.environment.spawn_random_organisms(count=1)
    
    def update(self):
        """Update simulation state"""
        self.environment.update()
    
    def draw(self):
        """Draw everything"""
        self.environment.draw(self.screen)
        
        # Draw info text
        font = pygame.font.Font(None, config.FONT_SIZE) 
        text = font.render(f"Organisms: {len(self.environment.organisms)}", 
                          True, (config.FONT_COLOR))
        self.screen.blit(text, (10, 10))
         # DEBUG: Show material count
        materials_text = font.render(f"Materials: {len(self.environment.materials)}", 
                                True, (config.FONT_COLOR))
        self.screen.blit(materials_text, (10, 50))
        
        pygame.display.flip()
    
    def run(self):
        """Main simulation loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(config.FPS)  # 60 FPS
        
        pygame.quit()