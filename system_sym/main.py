import sys

from pathlib import Path

def main():
    print("Hello, ocean of code! 🌊")
    print("SystemSym biosphere simulator initializing...")
    print("Checking dependencies...")
    try:
        import numpy as np
        print(f"✓ NumPy {np.__version__} loaded successfully")
    except ImportError:
        print("✗ NumPy not found - run: pip install numpy")
        return
    try:
        import matplotlib
        print(f"✓ Matplotlib {matplotlib.__version__} loaded successfully")
    except ImportError:
        print("✗ Matplotlib not found - run: pip install matplotlib")
        return
    
    try:
        import pygame
        print(f"✓ Pygame {pygame.__version__} - Graphics engine ready")
    except ImportError:
        print("✗ Pygame not found")
        return
    
    print("\nModule Roll Call:")
    try:
        from system_sym.organism import Organism
        org = Organism(1,1)
        print(f"✓ {org.respond()}")
    except ImportError as e:
        print("✗ Organism module not found")
        print(e)
        return
    try:        
        from system_sym.environment import Environment
        env = Environment()
        print(f"✓ {env.respond()}")
    except ImportError as e:
        print("✗ Environment module not found")
        print(e)
        return
    try:
        from system_sym.simulation import Simulation
        sim = Simulation()
        print(f"✓ {sim.respond()}")
    except ImportError as e:
        print("✗ Simulation module not found")
        print(e)
        return

    try:
        from system_sym.utils import respond as utils_respond
        print(f"✓ {utils_respond()}")
    except ImportError as e:
        print("✗ Utils module not found")
        print(e)
        return
        
    print("\n🎉 All systems go!")
    print("\nModes available:")
    print("  - God Mode: Tune the cosmos, watch populations evolve")
    print("  - Creature Mode: Be an organism, survive the ecosystem")
    print("\nReady to build your biosphere! 🌱")
    
    print("\n🎉 All systems go! Starting simulation...")
    print("\nControls:")
    print("  ESC - Quit")
    print("  SPACE - Spawn new organism")
    print("\nLaunching window...\n")
    
    from system_sym.simulation import Simulation
    
    sim = Simulation()
    sim.run()
    
    print("\nSimulation ended. Goodbye! 🌊")

if __name__ == "__main__"and __package__ is None:
    sys.path.insert(0, str(Path(__file__).parent.parent))
    __package__ = "system_sym"
    main()