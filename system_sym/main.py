import sys


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
    
    print("\n🎉 All systems go!")
    print("\nModes available:")
    print("  - God Mode: Tune the cosmos, watch populations evolve")
    print("  - Creature Mode: Be an organism, survive the ecosystem")
    print("\nReady to build your biosphere! 🌱")

if __name__ == "__main__":
    main()