#!/usr/bin/env python3
"""
Selection Sort Visualizer - Following the documentation specifications
"""

import matplotlib.pyplot as plt
import numpy as np
import time
from sorting_algorithms.selection_sort import selection_sort


class SelectionSortVisualizer:
    def __init__(self, algorithm_name="selection"):
        """Initialize the selection sort visualizer."""
        self.algorithm_name = algorithm_name
        
        # Setup the plot with professional styling
        plt.style.use('default')
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(14, 10), 
                                                       gridspec_kw={'height_ratios': [3, 1]})
        
        self.fig.suptitle(f'{algorithm_name.title()} Sort - Real-Time Visualization', 
                         fontsize=18, fontweight='bold', color='#2E86AB')
        
        # Professional color scheme as per documentation
        self.colors = {
            'default': '#2E86AB',      # Blue
            'comparing': '#A23B72',    # Pink
            'swapping': '#F18F01',     # Orange
            'sorted': '#C73E1D',       # Red
            'current': '#7209B7',      # Purple
            'minimum_tracked': '#28A745',  # Green - for minimum being tracked
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
        self.ax1.set_title('Selection Sort Process', fontsize=14, fontweight='bold', pad=20)
        
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
                                       f'Passes: {self.passes} | Comparisons: {self.comparisons} | Swaps: {self.swaps}',
                                       ha='center', va='center', fontsize=12, fontweight='bold',
                                       bbox=dict(boxstyle="round,pad=0.5", 
                                                facecolor='white', 
                                                edgecolor='black', 
                                                alpha=0.9))
        
        plt.tight_layout()
        
    def update_bars(self, arr, comparing_indices=None, swapping_indices=None, 
                   sorted_indices=None, current_index=None, minimum_tracked=None, progress=0):
        """Update the visualization with smooth transitions."""
        # Update bar heights and colors
        for i, (bar, value) in enumerate(zip(self.bars, arr)):
            # Smooth height transition
            current_height = bar.get_height()
            target_height = value
            bar.set_height(target_height)
            
            # Update colors based on state
            if current_index and i == current_index:
                bar.set_color(self.colors['current'])
                bar.set_alpha(1.0)
            elif minimum_tracked and i == minimum_tracked:
                bar.set_color(self.colors['minimum_tracked'])
                bar.set_alpha(1.0)
            elif comparing_indices and i in comparing_indices:
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
        if hasattr(self, 'progress_bar') and self.progress_bar:
            self.progress_bar[0].set_width(progress)
        
        # Update statistics
        self.stats_text.set_text(f'Passes: {self.passes} | Comparisons: {self.comparisons} | Swaps: {self.swaps}')
        
        # Force redraw
        self.fig.canvas.draw()
        plt.pause(self.pause_between_steps)
        
    def visualize_selection_sort(self, arr):
        """Selection sort visualization with real-time statistics showing each step clearly."""
        arr_copy = arr.copy()
        n = len(arr_copy)
        
        # Setup initial plot
        self.setup_plot(arr_copy)
        plt.show(block=False)
        
        # Reset statistics
        self.comparisons = 0
        self.swaps = 0
        self.passes = 0
        
        print(f"Starting selection sort on array: {arr_copy}")
        
        # Selection sort algorithm visualization
        for i in range(n):
            self.passes = i
            minIndex = i
            
            print(f"\n--- Pass {i}: Looking for minimum element to place at position {i} ---")
            print(f"Current array: {arr_copy}")
            
            # Highlight current position where we'll place the minimum
            progress = (i / n) * 100
            self.update_bars(arr_copy, current_index=i, progress=progress)
            plt.pause(0.5)  # Pause to show current position
            
            # Find the minimum element in the unsorted portion
            for j in range(i + 1, n):
                self.comparisons += 1
                print(f"  Comparing {arr_copy[j]} with current minimum {arr_copy[minIndex]}")
                
                # Highlight comparing elements
                comparing = [j]
                self.update_bars(arr_copy, comparing_indices=comparing, current_index=i, 
                               minimum_tracked=minIndex, progress=progress)
                plt.pause(0.3)  # Pause to show comparison
                
                # Update minimum if we found a smaller element
                if arr_copy[j] < arr_copy[minIndex]:
                    print(f"  New minimum found: {arr_copy[j]} at position {j}")
                    minIndex = j
                    # Highlight new minimum
                    self.update_bars(arr_copy, comparing_indices=comparing, current_index=i, 
                                   minimum_tracked=minIndex, progress=progress)
                    plt.pause(0.3)  # Pause to show new minimum
            
            # Swap if minimum is not already at position i
            if minIndex != i:
                print(f"  Swapping {arr_copy[i]} (position {i}) with {arr_copy[minIndex]} (position {minIndex})")
                arr_copy[i], arr_copy[minIndex] = arr_copy[minIndex], arr_copy[i]
                self.swaps += 1
                
                # Highlight swapping
                swapping = [i, minIndex]
                self.update_bars(arr_copy, swapping_indices=swapping, progress=progress)
                plt.pause(0.5)  # Pause to show swap
            else:
                print(f"  No swap needed - {arr_copy[i]} is already at the correct position")
            
            # Mark current position as sorted
            sorted_indices = list(range(i + 1))
            self.update_bars(arr_copy, sorted_indices=sorted_indices, progress=progress)
            print(f"  After pass {i}: {arr_copy}")
            plt.pause(0.5)  # Pause to show result
        
        # Final state - all sorted
        self.update_bars(arr_copy, sorted_indices=list(range(n)), progress=100)
        
        # Success message
        self.ax1.set_title('SORTING COMPLETE! Array is now sorted!', 
                          fontsize=16, color='green', fontweight='bold')
        
        # Final statistics
        self.stats_text.set_text(f'FINAL: Passes: {self.passes} | Comparisons: {self.comparisons} | Swaps: {self.swaps}')
        
        print(f"\n=== SORTING COMPLETE ===")
        print(f"Final sorted array: {arr_copy}")
        print(f"Total passes: {self.passes}")
        print(f"Total comparisons: {self.comparisons}")
        print(f"Total swaps: {self.swaps}")
        
        plt.show()
        
    def visualize_sort(self, arr):
        """Main method to visualize sorting."""
        if self.algorithm_name == "selection":
            self.visualize_selection_sort(arr)
        else:
            # Placeholder for other algorithms
            self.setup_plot(arr)
            self.ax1.set_title(f'{self.algorithm_name.title()} Sort (Coming Soon!)', 
                              fontsize=16, color='orange')
            plt.show()


def main():
    """Main function to run the selection sort visualizer."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Selection Sort Visualizer")
    parser.add_argument("--algo", choices=["selection"], default="selection",
                       help="Algorithm to visualize")
    parser.add_argument("--array", type=str, default="7,3,5,2,8,1,9,4,6",
                       help="Comma-separated array to sort")
    parser.add_argument("--speed", type=float, default=0.3,
                       help="Animation speed (lower = faster)")
    
    args = parser.parse_args()
    
    # Parse the array
    try:
        arr = [int(x.strip()) for x in args.array.split(",")]
    except ValueError:
        print("Invalid array format. Using default: [7, 3, 5, 2, 8, 1, 9, 4, 6]")
        arr = [7, 3, 5, 2, 8, 1, 9, 4, 6]
    
    print(f"Visualizing {args.algo} sort on array: {arr}")
    print(f"Animation speed: {args.speed}s per step")
    print("Close the plot window when done!")
    
    # Create and run visualizer
    try:
        visualizer = SelectionSortVisualizer(args.algo)
        visualizer.animation_speed = args.speed
        visualizer.pause_between_steps = args.speed
        visualizer.visualize_sort(arr)
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have matplotlib installed: pip install matplotlib")


if __name__ == "__main__":
    main() 