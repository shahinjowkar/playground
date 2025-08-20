#!/usr/bin/env python3
"""
Entry point to run tests and select algorithm.
"""

import argparse
import json
import sys
from sorting_algorithms import ALGORITHMS

# Fixed datasets as specified in SPEC.md (exact values; not to be printed by CLI)
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
    "random10_fixed": [12, -3, 7, 7, 0, -11, 25, 4, 4, -3],
    
    # Duplicates / degenerate distributions
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



def run_algorithm_on_datasets(algorithm_name, algorithm_func, report_type="text", visualize=False):
    """Run algorithm on all datasets and return results."""
    results = []
    
    for dataset_name in DATASETS.keys():
        dataset = DATASETS[dataset_name]
        
        if visualize:
            print(f"\n{'='*50}")
            print(f"Testing {algorithm_name} on {dataset_name} dataset")
            print(f"{'='*50}")
            algo_output = algorithm_func(dataset.copy(), visualize=True)
        else:
            algo_output = algorithm_func(dataset.copy())
            
        expected = sorted(dataset)
        passed = algo_output == expected
        
        if report_type == "text":
            print(f"ALGO={algorithm_name} RESULT={'PASS' if passed else 'FAIL'}")
        
        results.append({
            "dataset": dataset_name,
            "passed": passed
        })
    
    return results


def print_text_summary(algorithm_name, results):
    """Print text summary for an algorithm."""
    passed_count = sum(1 for r in results if r["passed"])
    total_count = len(results)
    print(f"SUMMARY ALGO={algorithm_name} PASSED={passed_count} TOTAL={total_count}")


def print_json_report(algorithms_results):
    """Print JSON report."""
    algorithms_data = []
    overall_status = "OK"
    
    for algo_name, results in algorithms_results.items():
        passed_count = sum(1 for r in results if r["passed"])
        total_count = len(results)
        
        if passed_count < total_count:
            overall_status = "FAIL"
        
        algorithms_data.append({
            "name": algo_name,
            "results": results,
            "summary": {
                "passed": passed_count,
                "total": total_count
            }
        })
    
    json_report = {
        "algorithms": algorithms_data,
        "status": overall_status
    }
    
    print(json.dumps(json_report))


def main():
    """Main function implementing the exact CLI contract from SPEC.md."""
    parser = argparse.ArgumentParser(description="Sorting Algorithms Testing Project")
    parser.add_argument("--algo", choices=["bubble", "merge", "quick"], required=True,
                       help="Algorithm to use")
    parser.add_argument("--report", choices=["text", "json"], default="text",
                       help="Report format (default: text)")
    parser.add_argument("--failfast", action="store_true",
                       help="Stop on first failure")
    parser.add_argument("--visualize", action="store_true",
                       help="Show sorting process step by step")
    
    args = parser.parse_args()
    
    # Resolve selected algorithm(s)
    if args.algo == "all":
        selected_algorithms = ALGORITHMS
    else:
        selected_algorithms = {args.algo: ALGORITHMS[args.algo]}
    
    # Execute harness
    algorithms_results = {}
    exit_code = 0
    
    for algo_name, algo_func in selected_algorithms.items():
        results = run_algorithm_on_datasets(algo_name, algo_func, args.report, args.visualize)
        algorithms_results[algo_name] = results
        
        # Check for failures
        if any(not r["passed"] for r in results):
            exit_code = 1
            if args.failfast:
                # Print summary for current algorithm before exiting
                if args.report == "text":
                    print_text_summary(algo_name, results)
                sys.exit(exit_code)
    
    # Print summaries
    if args.report == "text":
        for algo_name, results in algorithms_results.items():
            print_text_summary(algo_name, results)
    else:  # JSON
        print_json_report(algorithms_results)
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main() 