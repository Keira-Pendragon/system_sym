class Material:
    def respond(self):
        return "Material module is active."
    
    def __init__(self, x, y, material_type="food", energy_value=50):
        self.x = x
        self.y = y
        self.type = material_type  # "food", "mineral", etc.
        self.energy_value = energy_value
        self.consumed = False
        self.color = (100, 255, 100)  # Green for food
        self.radius = 3
    
