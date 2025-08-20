#!/usr/bin/env python3
"""
Beautiful Graphical Sorting Visualizer
Uses matplotlib to create animated bar charts showing the sorting process
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
from sorting_algorithms import ALGORITHMS


class SortingVisualizer:
    def __init__(self, algorithm_name="bubble"):
        """Initialize the visualizer with the specified algorithm."""
        self.algorithm_name = algorithm_name
        self.algorithm_func = ALGORITHMS.get(algorithm_name)
        if not self.algorithm_func:
            raise ValueError(f"Algorithm '{algorithm_name}' not found")
        
        # Setup the plot
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.fig.suptitle(f'{algorithm_name.title()} Sort Visualization', fontsize=16, fontweight='bold')
        
        # Colors for different states
        self.colors = {
            'default': '#2E86AB',      # Blue
            'comparing': '#A23B72',    # Pink
            'swapping': '#F18F01',     # Orange
            'sorted': '#C73E1D',       # Red
            'current': '#7209B7'       # Purple
        }
        
        # Animation settings
        self.animation_speed = 0.5  # seconds between frames
        
    def setup_plot(self, arr):
        """Setup the initial plot with the array."""
        self.ax.clear()
        self.ax.set_xlim(0, len(arr))
        self.ax.set_ylim(min(arr) - 1, max(arr) + 1)
        self.ax.set_xlabel('Array Index', fontsize=12)
        self.ax.set_ylabel('Value', fontsize=12)
        self.ax.grid(True, alpha=0.3)
        
        # Create bars
        x_positions = np.arange(len(arr))
        self.bars = self.ax.bar(x_positions, arr, color=self.colors['default'], 
                               edgecolor='black', linewidth=1, alpha=0.8)
        
        # Add value labels on top of bars
        for i, (bar, value) in enumerate(zip(self.bars, arr)):
            height = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{value}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        
    def update_bars(self, arr, comparing_indices=None, swapping_indices=None, sorted_indices=None):
        """Update the bar colors and heights based on current state."""
        for i, (bar, value) in enumerate(zip(self.bars, arr)):
            # Update bar height
            bar.set_height(value)
            
            # Update bar color based on state
            if comparing_indices and i in comparing_indices:
                bar.set_color(self.colors['comparing'])
            elif swapping_indices and i in swapping_indices:
                bar.set_color(self.colors['swapping'])
            elif sorted_indices and i in sorted_indices:
                bar.set_color(self.colors['sorted'])
            else:
                bar.set_color(self.colors['default'])
            
            # Update value label
            height = bar.get_height()
            self.ax.texts[i].set_position((bar.get_x() + bar.get_width()/2., height + 0.1))
            self.ax.texts[i].set_text(f'{value}')
        
        plt.pause(self.animation_speed)
        
    def visualize_bubble_sort(self, arr):
        """Visualize bubble sort with beautiful animations."""
        arr_copy = arr.copy()
        n = len(arr_copy)
        
        # Setup initial plot
        self.setup_plot(arr_copy)
        plt.show(block=False)
        
        # Track sorted elements
        sorted_count = 0
        
        for pass_num in range(n - 1):
            swapped = False
            
            for i in range(n - 1 - pass_num):
                # Highlight comparing elements
                comparing = [i, i + 1]
                self.update_bars(arr_copy, comparing_indices=comparing)
                
                if arr_copy[i] > arr_copy[i + 1]:
                    # Highlight swapping elements
                    self.update_bars(arr_copy, swapping_indices=comparing)
                    
                    # Perform swap
                    arr_copy[i], arr_copy[i + 1] = arr_copy[i + 1], arr_copy[i]
                    swapped = True
                    
                    # Update plot after swap
                    self.update_bars(arr_copy, swapping_indices=comparing)
                
                # Mark elements as sorted if they're in final position
                if i >= n - 1 - pass_num - sorted_count:
                    sorted_indices = list(range(n - sorted_count, n))
                    self.update_bars(arr_copy, sorted_indices=sorted_indices)
            
            # Mark the largest element as sorted
            sorted_count += 1
            sorted_indices = list(range(n - sorted_count, n))
            self.update_bars(arr_copy, sorted_indices=sorted_indices)
            
            if not swapped:
                # Array is sorted, mark all as sorted
                sorted_indices = list(range(n))
                self.update_bars(arr_copy, sorted_indices=sorted_indices)
                break
        
        # Final state - all sorted
        self.update_bars(arr_copy, sorted_indices=list(range(n)))
        plt.title(f'{self.algorithm_name.title()} Sort Complete!', fontsize=14, color='green')
        plt.show()
        
    def visualize_sort(self, arr):
        """Main method to visualize sorting based on algorithm type."""
        if self.algorithm_name == "bubble":
            self.visualize_bubble_sort(arr)
        else:
            # For now, just show the array
            self.setup_plot(arr)
            plt.title(f'{self.algorithm_name.title()} Sort (Not yet implemented)', fontsize=14)
            plt.show()


def main():
    """Main function to run the visualizer."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Beautiful Sorting Visualizer")
    parser.add_argument("--algo", choices=["bubble", "merge", "quick"], default="bubble",
                       help="Algorithm to visualize")
    parser.add_argument("--array", type=str, default="7,1,4,9,2",
                       help="Comma-separated array to sort")
    
    args = parser.parse_args()
    
    # Parse the array
    try:
        arr = [int(x.strip()) for x in args.array.split(",")]
    except ValueError:
        print("Invalid array format. Using default: [7, 1, 4, 9, 2]")
        arr = [7, 1, 4, 9, 2]
    
    print(f"Visualizing {args.algo} sort on array: {arr}")
    
    # Create and run visualizer
    try:
        visualizer = SortingVisualizer(args.algo)
        visualizer.visualize_sort(arr)
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have matplotlib installed: pip install matplotlib")


if __name__ == "__main__":
    main() 