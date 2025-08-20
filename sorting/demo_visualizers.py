#!/usr/bin/env python3
"""
Demo script showcasing all the sorting visualizers
"""

import subprocess
import sys
import time

def run_visualizer(script_name, description, args=""):
    """Run a visualizer with the given arguments."""
    print(f"\n{'='*60}")
    print(f"🎨 {description}")
    print(f"{'='*60}")
    print(f"Running: python {script_name} {args}")
    print("Close the plot window to continue to the next demo...")
    
    try:
        subprocess.run([sys.executable, script_name] + args.split(), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
    except KeyboardInterrupt:
        print("Demo interrupted by user")

def main():
    """Main demo function."""
    print("🚀 SORTING ALGORITHM VISUALIZER DEMO")
    print("=" * 60)
    print("This demo will showcase different visualization styles:")
    print("1. Basic text-based visualizer")
    print("2. Advanced graphical visualizer")
    print("3. Final polished visualizer")
    print("\nPress Enter to start the demo...")
    input()
    
    # Demo 1: Basic text visualizer
    run_visualizer("main.py", "Basic Text Visualizer (CLI)", "--algo bubble --visualize")
    
    # Demo 2: Simple graphical visualizer
    run_visualizer("sorting_visualizer.py", "Simple Graphical Visualizer", "--algo bubble --array 7,1,4,9,2")
    
    # Demo 3: Advanced visualizer
    run_visualizer("advanced_visualizer.py", "Advanced Real-Time Visualizer", "--algo bubble --array 7,1,4,9,2,8,3,6,5 --speed 0.4")
    
    # Demo 4: Final polished visualizer
    run_visualizer("final_visualizer.py", "Final Polished Visualizer", "--algo bubble --array 7,1,4,9,2,8,3,6,5 --speed 0.3")
    
    print(f"\n{'='*60}")
    print("🎉 DEMO COMPLETE!")
    print(f"{'='*60}")
    print("You've seen all the visualizers:")
    print("✅ Text-based CLI visualizer")
    print("✅ Simple graphical visualizer")
    print("✅ Advanced real-time visualizer")
    print("✅ Final polished visualizer")
    print("\nChoose your favorite and use it for your sorting needs!")

if __name__ == "__main__":
    main() 