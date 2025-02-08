from datasets import load_dataset
import pandas as pd
import numpy as np
from collections import defaultdict

def analyze_dataset():
    # Load the dataset
    print("Loading dataset...")
    dataset = load_dataset("DigitalLearningGmbH/MATH-lighteval")
    
    # Print basic info
    print("\n=== Dataset Structure ===")
    print(f"Dataset splits: {dataset.keys()}")
    for split in dataset.keys():
        print(f"\nSplit '{split}' size: {len(dataset[split])}")
        print(f"Columns: {dataset[split].column_names}")
    
    # Convert first few examples to DataFrame for better viewing
    print("\n=== First 5 Examples ===")
    df = pd.DataFrame(dataset['train'][:5])
    print(df)
    
    # Analyze lengths
    print("\n=== Length Analysis ===")
    stats = defaultdict(dict)
    for column in dataset['train'].column_names:
        if isinstance(dataset['train'][0][column], str):
            lengths = [len(x[column]) for x in dataset['train']]
            stats[column] = {
                'mean_length': np.mean(lengths),
                'median_length': np.median(lengths),
                'max_length': max(lengths),
                'min_length': min(lengths)
            }
    
    for column, metrics in stats.items():
        print(f"\nColumn: {column}")
        for metric, value in metrics.items():
            print(f"{metric}: {value:.2f}")
    
    # Sample a full example
    print("\n=== Detailed Example ===")
    example = dataset['train'][0]
    print("Problem:")
    print(example['problem'])
    print("\nSolution:")
    print(example['solution'])

if __name__ == "__main__":
    analyze_dataset()