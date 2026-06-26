"""
End-to-End Pandas ETL Pipeline
This script generates a mock dataset, processes it by handling missing values, 
optimizes memory usage, and performs data aggregation.
"""

import pandas as pd
import numpy as np
import os

def generate_mock_data(file_path="raw_dataset.csv", num_rows=1000):
    """
    Generates a realistic mock dataset with missing values for pipeline testing.
    """
    print(f"⚙️ Generating raw mock data with {num_rows} rows...")
    np.random.seed(42)
    
    # Base columns
    data = {
        'Employee_ID': range(1001, 1001 + num_rows),
        'Department': np.random.choice(['IT', 'HR', 'Sales', 'Marketing', 'Finance'], num_rows),
        'City': np.random.choice(['Delhi', 'Mumbai', 'Bangalore', 'Pune', 'Chennai'], num_rows),
        'Experience_Years': np.random.randint(1, 25, num_rows),
        'Salary': np.random.randint(30000, 150000, num_rows),
    }
    
    # Generate 95 continuous features with ~10% intentional missing values (NaN)
    for i in range(1, 96):
        values = np.random.randn(num_rows) * 100
        missing_mask = np.random.rand(num_rows) < 0.1
        values[missing_mask] = np.nan
        data[f'Feature_{i}'] = values
        
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"✅ Raw data generated and saved to '{file_path}'.\n")


class DataProcessor:
    """
    A reusable ETL pipeline class to clean, optimize, and transform tabular data.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Loads data from the specified CSV file."""
        print(f"📂 Loading data from {self.file_path}...")
        self.df = pd.read_csv(self.file_path)
        
        # Display initial memory usage for benchmark
        initial_mem = self.df.memory_usage(deep=True).sum() / 1024
        print(f"   -> Initial Memory Usage: {initial_mem:.2f} KB")
        return self
    
    def clean_missing_values(self):
        """Imputes missing numeric values with the column mean."""
        numeric_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
        self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].mean())
        print("🧹 Step 1: Missing values imputed successfully.")
        return self
        
    def optimize_memory(self):
        """Converts object dtypes to category for memory efficiency."""
        object_cols = self.df.select_dtypes(include=['object']).columns
        for col in object_cols:
            self.df[col] = self.df[col].astype('category')
            
        final_mem = self.df.memory_usage(deep=True).sum() / 1024
        print(f"⚡ Step 2: Memory optimized. Current Usage: {final_mem:.2f} KB")
        return self
        
    def generate_insights(self, target_dept='IT', min_exp=5):
        """Filters specific demographics and calculates aggregate metrics."""
        filtered_df = self.df[(self.df['Department'] == target_dept) & (self.df['Experience_Years'] > min_exp)]
        avg_salary = self.df.groupby('Department', observed=True)['Salary'].mean()
        
        print(f"📊 Step 3: Insights Extracted.")
        print(f"   -> Found {len(filtered_df)} employees in {target_dept} with > {min_exp} years of experience.")
        print(f"   -> Average {target_dept} Salary: ₹{avg_salary.get(target_dept, 0):,.2f}")
        return self
        
    def save_output(self, output_path="clean_pipeline_output.csv"):
        """Exports the processed DataFrame to a new CSV."""
        self.df.to_csv(output_path, index=False)
        print(f"🚀 Pipeline Complete! Transformed data saved to: {output_path}\n")


if __name__ == "__main__":
    # Define file names
    RAW_DATA_FILE = "raw_dataset.csv"
    CLEAN_DATA_FILE = "clean_dataset.csv"
    
    # 1. Generate the mock data automatically
    generate_mock_data(RAW_DATA_FILE, num_rows=1000)
    
    # 2. Initialize and run the ETL pipeline using method chaining
    pipeline = DataProcessor(RAW_DATA_FILE)
    
    (pipeline.load_data()
             .clean_missing_values()
             .optimize_memory()
             .generate_insights(target_dept='IT', min_exp=5)
             .save_output(CLEAN_DATA_FILE))
             
    # Clean up the raw mock file (Optional: keeps the workspace clean)
    # if os.path.exists(RAW_DATA_FILE):
    #     os.remove(RAW_DATA_FILE)