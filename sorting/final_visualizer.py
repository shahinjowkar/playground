#!/usr/bin/env python3
"""
Final Polished Sorting Visualizer
Beautiful, smooth animations with professional styling
"""

import matplotlib.pyplot as plt
import numpy as np
import time
from sorting_algorithms import ALGORITHMS


class FinalSortingVisualizer:
    def __init__(self, algorithm_name="bubble"):
        """Initialize the final visualizer."""
        self.algorithm_name = algorithm_name
        self.algorithm_func = ALGORITHMS.get(algorithm_name)
        if not self.algorithm_func:
            raise ValueError(f"Algorithm '{algorithm_name}' not found")
        
        # Setup the plot with professional styling
        plt.style.use('default')
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(14, 10), 
                                                       gridspec_kw={'height_ratios': [3, 1]})
        
        self.fig.suptitle(f'{algorithm_name.title()} Sort - Real-Time Visualization', 
                         fontsize=18, fontweight='bold', color='#2E86AB')
        
        # Professional color scheme
        self.colors = {
            'default': '#2E86AB',      # Blue
            'comparing': '#A23B72',    # Pink
            'swapping': '#F18F01',     # Orange
            'sorted': '#C73E1D',       # Red
            'current': '#7209B7',      # Purple
            'background': '#F8F9FA'    # Light gray
        }
        
        # Animation settings
        self.animation_speed = 0.3
        self.pause_between_steps = 0.1
        
        # Statistics
        self.comparisons = 0
        self.swaps = 0
        self.passes = 0
        
    def setup_plot(self, arr):
        """Setup the enhanced plot with professional styling."""
        # Main sorting visualization
        self.ax1.clear()
        self.ax1.set_facecolor(self.colors['background'])
        self.ax1.set_xlim(-0.5, len(arr) - 0.5)
        self.ax1.set_ylim(min(arr) - 1, max(arr) + 1)
        self.ax1.set_xlabel('Array Index', fontsize=12, fontweight='bold')
        self.ax1.set_ylabel('Value', fontsize=12, fontweight='bold')
        self.ax1.grid(True, alpha=0.3, linestyle='--')
        self.ax1.set_title('Sorting Process', fontsize=14, fontweight='bold', pad=20)
        
        # Progress bar
        self.ax2.clear()
        self.ax2.set_facecolor(self.colors['background'])
        self.ax2.set_xlim(0, 100)
        self.ax2.set_ylim(0, 1)
        self.ax2.set_xlabel('Progress (%)', fontsize=12, fontweight='bold')
        self.ax2.set_title('Sorting Progress', fontsize=14, fontweight='bold', pad=20)
        self.ax2.grid(True, alpha=0.3)
        
        # Create bars with enhanced styling
        x_positions = np.arange(len(arr))
        self.bars = self.ax1.bar(x_positions, arr, 
                                color=self.colors['default'],
                                edgecolor='black', 
                                linewidth=2, 
                                alpha=0.8,
                                width=0.8)
        
        # Add value labels with better styling
        self.value_labels = []
        for i, (bar, value) in enumerate(zip(self.bars, arr)):
            height = bar.get_height()
            label = self.ax1.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                                 f'{value}', ha='center', va='bottom', 
                                 fontweight='bold', fontsize=11,
                                 bbox=dict(boxstyle="round,pad=0.3", 
                                          facecolor='white', 
                                          edgecolor='black', 
                                          alpha=0.8))
            self.value_labels.append(label)
        
        # Progress bar
        self.progress_bar = self.ax2.bar(0, 0.8, width=0, 
                                       color=self.colors['comparing'], 
                                       alpha=0.8)
        
        # Statistics text
        self.stats_text = self.ax2.text(50, 0.5, 
                                       f'Comparisons: {self.comparisons} | Swaps: {self.swaps} | Passes: {self.passes}',
                                       ha='center', va='center', fontsize=12, fontweight='bold',
                                       bbox=dict(boxstyle="round,pad=0.5", 
                                                facecolor='white', 
                                                edgecolor='black', 
                                                alpha=0.9))
        
        plt.tight_layout()
        
    def update_bars(self, arr, comparing_indices=None, swapping_indices=None, 
                   sorted_indices=None, progress=0):
        """Update the visualization with smooth transitions."""
        # Update bar heights and colors
        for i, (bar, value) in enumerate(zip(self.bars, arr)):
            # Smooth height transition
            current_height = bar.get_height()
            target_height = value
            bar.set_height(target_height)
            
            # Update colors based on state
            if comparing_indices and i in comparing_indices:
                bar.set_color(self.colors['comparing'])
                bar.set_alpha(1.0)
            elif swapping_indices and i in swapping_indices:
                bar.set_color(self.colors['swapping'])
                bar.set_alpha(1.0)
            elif sorted_indices and i in sorted_indices:
                bar.set_color(self.colors['sorted'])
                bar.set_alpha(0.9)
            else:
                bar.set_color(self.colors['default'])
                bar.set_alpha(0.8)
            
            # Update value labels
            height = bar.get_height()
            self.value_labels[i].set_position((bar.get_x() + bar.get_width()/2., height + 0.1))
            self.value_labels[i].set_text(f'{value}')
        
        # Update progress bar
        self.progress_bar[0].set_width(progress)
        
        # Update statistics
        self.stats_text.set_text(f'Comparisons: {self.comparisons} | Swaps: {self.swaps} | Passes: {self.passes}')
        
        # Force redraw
        self.fig.canvas.draw()
        plt.pause(self.pause_between_steps)
        
    def visualize_bubble_sort(self, arr):
        """Enhanced bubble sort visualization with real-time statistics."""
        arr_copy = arr.copy()
        n = len(arr_copy)
        
        # Setup initial plot
        self.setup_plot(arr_copy)
        plt.show(block=False)
        
        # Reset statistics
        self.comparisons = 0
        self.swaps = 0
        self.passes = 0
        
        # Track sorted elements
        sorted_count = 0
        
        for pass_num in range(n - 1):
            self.passes += 1
            swapped = False
            
            for i in range(n - 1 - pass_num):
                self.comparisons += 1
                
                # Highlight comparing elements
                comparing = [i, i + 1]
                progress = ((pass_num * (n - 1) + i) / ((n - 1) * (n - 1))) * 100
                self.update_bars(arr_copy, comparing_indices=comparing, progress=progress)
                
                if arr_copy[i] > arr_copy[i + 1]:
                    self.swaps += 1
                    
                    # Highlight swapping elements
                    self.update_bars(arr_copy, swapping_indices=comparing, progress=progress)
                    
                    # Perform swap with animation
                    temp = arr_copy[i]
                    arr_copy[i] = arr_copy[i + 1]
                    arr_copy[i + 1] = temp
                    
                    # Update plot after swap
                    self.update_bars(arr_copy, swapping_indices=comparing, progress=progress)
                    swapped = True
                
                # Mark elements as sorted if they're in final position
                if i >= n - 1 - pass_num - sorted_count:
                    sorted_indices = list(range(n - sorted_count, n))
                    self.update_bars(arr_copy, sorted_indices=sorted_indices, progress=progress)
            
            # Mark the largest element as sorted
            sorted_count += 1
            sorted_indices = list(range(n - sorted_count, n))
            progress = ((pass_num + 1) * (n - 1) / ((n - 1) * (n - 1))) * 100
            self.update_bars(arr_copy, sorted_indices=sorted_indices, progress=progress)
            
            if not swapped:
                # Array is sorted, mark all as sorted
                sorted_indices = list(range(n))
                self.update_bars(arr_copy, sorted_indices=sorted_indices, progress=100)
                break
        
        # Final state - all sorted
        self.update_bars(arr_copy, sorted_indices=list(range(n)), progress=100)
        
        # Success message
        self.ax1.set_title('SORTING COMPLETE! Array is now sorted!', 
                          fontsize=16, color='green', fontweight='bold')
        
        # Final statistics
        self.stats_text.set_text(f'FINAL: Comparisons: {self.comparisons} | Swaps: {self.swaps} | Passes: {self.passes}')
        
        plt.show()
        
    def visualize_sort(self, arr):
        """Main method to visualize sorting."""
        if self.algorithm_name == "bubble":
            self.visualize_bubble_sort(arr)
        else:
            # Placeholder for other algorithms
            self.setup_plot(arr)
            self.ax1.set_title(f'{self.algorithm_name.title()} Sort (Coming Soon!)', 
                              fontsize=16, color='orange')
            plt.show()


def main():
    """Main function to run the final visualizer."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Beautiful Sorting Visualizer")
    parser.add_argument("--algo", choices=["bubble", "merge", "quick"], default="bubble",
                       help="Algorithm to visualize")
    parser.add_argument("--array", type=str, default="7,1,4,9,2,8,3,6,5",
                       help="Comma-separated array to sort")
    parser.add_argument("--speed", type=float, default=0.3,
                       help="Animation speed (lower = faster)")
    
    args = parser.parse_args()
    
    # Parse the array
    try:
        arr = [int(x.strip()) for x in args.array.split(",")]
    except ValueError:
        print("Invalid array format. Using default: [7, 1, 4, 9, 2, 8, 3, 6, 5]")
        arr = [7, 1, 4, 9, 2, 8, 3, 6, 5]
    
    print(f"Visualizing {args.algo} sort on array: {arr}")
    print(f"Animation speed: {args.speed}s per step")
    print("Close the plot window when done!")
    
    # Create and run visualizer
    try:
        visualizer = FinalSortingVisualizer(args.algo)
        visualizer.animation_speed = args.speed
        visualizer.pause_between_steps = args.speed
        visualizer.visualize_sort(arr)
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have matplotlib installed: pip install matplotlib")


if __name__ == "__main__":
    main() 