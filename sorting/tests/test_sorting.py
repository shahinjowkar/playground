"""
Unit tests for sorting algorithms.
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sorting_algorithms import ALGORITHMS

# Fixed datasets as specified in SPEC.md
DATASETS = {
    "sorted": [1, 2, 3, 4, 5],
    "reverse": [5, 4, 3, 2, 1],
    "duplicates": [2, 3, 2, 1, 3, 1],
    "empty": [],
    "random": [7, 1, 4, 9, 2],
    "single": [42],
    "negatives": [0, -1, 5, -3, 2],
    "all_equal": [7, 7, 7, 7, 7],
    "near_sorted": [1, 2, 3, 5, 4, 6, 7],
    "mixed_small": [-10, 0, 7, -1, 7, 3, -10],
    "alternating": [1, 100, 2, 99, 3, 98, 4, 97],
    "zeros_negs": [0, 0, 0, -1, -1, -2, 0, -3],
    "gapped": [1000, -1000, 500, -500, 0, 250, -250],
    "random10_fixed": [12, -3, 7, 7, 0, -11, 25, 4, 4, -3]

    # Trivial / tiny
    "empty": [],
    "single_zero": [0],
    "single_positive": [42],
    "pair_sorted": [1, 2],
    "pair_reverse": [2, 1],
    "trio_one_inversion": [1, 3, 2],

    # Already sorted / reversed / nearly sorted
    "sorted_small": [1, 2, 3, 4, 5],
    "reverse_small": [5, 4, 3, 2, 1],
    "near_sorted_one_swap": [1, 2, 4, 3, 5, 6],

    # Duplicates / degenerate distributions
    "all_equal": [7, 7, 7, 7, 7],
    "duplicates_small": [2, 3, 2, 1, 3, 1],         # expect [1,1,2,2,3,3]
    "two_values_alt": [1, 0, 1, 0, 1, 0, 1, 0],
    "duplicates_at_ends": [5, 5, 1, 2, 3, 3],
    "min_max_repeat": [-10, -10, 0, 10, 10],

    # Signs / zeros / magnitude extremes
    "negatives_mixed": [0, -1, 5, -3, 2],
    "zero_heavy": [0, 0, 0, 0, 1, 0, 0, -1, 0],
    "large_magnitudes": [2_147_483_647, -2_147_483_648, 0, 999_999_999, -999_999_999],

    # Patterns that trip naive pivots/loops
    "alternating_high_low": [1, 100, 2, 99, 3, 98, 4, 97],
    "sawtooth": [3, 1, 2, 3, 1, 2, 3, 1, 2],
    "gapped_values": [1000, -1000, 500, -500, 0, 250, -250],

    # Fixed “random” (deterministic)
    "random5_fixed": [7, 1, 4, 9, 2],
    "random10_fixed": [12, -3, 7, 7, 0, -11, 25, 4, 4, -3],

    # Length variety (odd/even/prime-ish)
    "odd_length": [9, -1, 8, 0, -2],
    "even_length": [10, -1, 8, 0, 2, -3],
    "primeish_length": [13, 2, 5, 11, 7, 3],

}


class TestSortingAlgorithms:
    """Test class for all sorting algorithms."""
    
    @pytest.mark.parametrize("algorithm_name,algorithm", ALGORITHMS.items())
    @pytest.mark.parametrize("dataset_name,arr", DATASETS.items())
    def test_algorithm_correctness(self, algorithm_name, algorithm, dataset_name, arr):
        """Test algorithm correctness against sorted() for each dataset."""
        expected = sorted(arr)
        result = algorithm(arr.copy())  # Use copy to avoid modifying original
        assert result == expected, f"{algorithm_name} failed on {dataset_name} dataset" 