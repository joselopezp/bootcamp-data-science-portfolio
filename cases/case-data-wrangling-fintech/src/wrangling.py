"""
Data Wrangling Pipeline for Fintech Transactions

This module provides reusable functions to clean and transform
dirty financial transaction data.

Author: Jose Marcel Lopez Pino
Module: M3 - Data Preparation (Alkemy Bootcamp)
"""

import pandas as pd
import numpy as np
from typing import Tuple, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FinTechWrangler:
    """
    A class to handle data wrangling for fintech transactions.
    
    Attributes:
        df (pd.DataFrame): The working dataframe
        original_shape (Tuple): Original data shape before cleaning
        cleaning_report (Dict): Dictionary to track cleaning actions
    """
    
    def __init__(self, filepath: str):
        """
        Initialize the wrangler with a CSV file.
        
        Args:
            filepath (str): Path to the CSV file
            
        Raises:
            FileNotFoundError: If the file doesn't exist
        """
        try:
            self.df = pd.read_csv(filepath)
            self.original_shape = self.df.shape
            self.cleaning_report = {
                'original_rows': self.original_shape[0],
                'original_cols': self.original_shape[1],
                'actions': []
            }
            logger.info(f"Loaded {self.original_shape[0]} rows, {self.original_shape[1]} columns")
        except FileNotFoundError:
            logger.error(f"File not found: {filepath}")
            raise
    
    def analyze_nulls(self) -> pd.Series:
        """
        Analyze missing values in the dataset.
        
        Returns:
            pd.Series: Null count and percentage by column
        """
        null_count = self.df.isnull().sum()
        null_pct = (null_count / len(self.df)) * 100
        
        result = pd.DataFrame({
            'null_count': null_count,
            'null_percentage': null_pct
        })
        
        logger.info(f"\nNull Values Analysis:\n{result[result['null_count'] > 0]}")
        return result
    
    def analyze_duplicates(self, subset: list = None) -> int:
        """
        Analyze duplicate records.
        
        Args:
            subset (list): Columns to check for duplicates. 
                          If None, check all columns.
        
        Returns:
            int: Number of duplicate rows found
        """
        if subset:
            dup_count = self.df.duplicated(subset=subset).sum()
            logger.info(f"Duplicates found on {subset}: {dup_count}")
        else:
            dup_count = self.df.duplicated().sum()
            logger.info(f"Total duplicate rows: {dup_count}")
        
        return dup_count
    
    def impute_missing_numeric(self, column: str, strategy: str = 'median') -> None:
        """
        Impute missing values in numeric columns.
        
        Args:
            column (str): Column name to impute
            strategy (str): 'mean', 'median', or a specific value
            
        Raises:
            ValueError: If strategy is invalid or column doesn't exist
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found")
        
        null_before = self.df[column].isnull().sum()
        
        if null_before == 0:
            logger.info(f"No nulls in '{column}'")
            return
        
        if strategy == 'median':
            fill_value = self.df[column].median()
        elif strategy == 'mean':
            fill_value = self.df[column].mean()
        elif isinstance(strategy, (int, float)):
            fill_value = strategy
        else:
            raise ValueError(f"Invalid strategy: {strategy}")
        
        self.df[column].fillna(fill_value, inplace=True)
        
        null_after = self.df[column].isnull().sum()
        logger.info(f"Imputed {null_before} nulls in '{column}' with {strategy}: {fill_value:.2f}")
        
        self.cleaning_report['actions'].append({
            'action': 'impute_numeric',
            'column': column,
            'strategy': strategy,
            'value_used': fill_value,
            'rows_affected': null_before
        })
    
    def impute_missing_categorical(self, column: str, strategy: str = 'mode') -> None:
        """
        Impute missing values in categorical columns.
        
        Args:
            column (str): Column name to impute
            strategy (str): 'mode' or a specific category value
            
        Raises:
            ValueError: If column doesn't exist
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found")
        
        null_before = self.df[column].isnull().sum()
        
        if null_before == 0:
            logger.info(f"No nulls in '{column}'")
            return
        
        if strategy == 'mode':
            fill_value = self.df[column].mode()[0]
        else:
            fill_value = strategy
        
        self.df[column].fillna(fill_value, inplace=True)
        
        logger.info(f"Imputed {null_before} nulls in '{column}' with '{fill_value}'")
        
        self.cleaning_report['actions'].append({
            'action': 'impute_categorical',
            'column': column,
            'strategy': strategy,
            'value_used': fill_value,
            'rows_affected': null_before
        })
    
    def standardize_dates(self, column: str, format_str: str = None) -> None:
        """
        Standardize date column to ISO 8601 format (YYYY-MM-DD).
        
        Args:
            column (str): Column name with dates
            format_str (str): Explicit format (e.g., '%d/%m/%Y'). 
                             If None, infer format.
            
        Raises:
            ValueError: If column doesn't exist
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found")
        
        try:
            if format_str:
                self.df[column] = pd.to_datetime(self.df[column], format=format_str)
            else:
                self.df[column] = pd.to_datetime(self.df[column], infer_datetime_format=True)
            
            logger.info(f"Standardized dates in '{column}' to ISO 8601")
            
            self.cleaning_report['actions'].append({
                'action': 'standardize_dates',
                'column': column,
                'format': 'ISO 8601 (YYYY-MM-DD)'
            })
        except Exception as e:
            logger.error(f"Failed to standardize dates in '{column}': {e}")
            raise
    
    def remove_duplicates(self, subset: list = None, keep: str = 'first') -> int:
        """
        Remove duplicate records.
        
        Args:
            subset (list): Columns to consider for identifying duplicates.
                          If None, consider all columns.
            keep (str): 'first', 'last', or False (remove all duplicates)
        
        Returns:
            int: Number of rows removed
        """
        rows_before = len(self.df)
        
        self.df.drop_duplicates(subset=subset, keep=keep, inplace=True)
        
        rows_after = len(self.df)
        removed = rows_before - rows_after
        
        logger.info(f"Removed {removed} duplicate rows (keep='{keep}')")
        
        self.cleaning_report['actions'].append({
            'action': 'remove_duplicates',
            'subset': subset,
            'keep': keep,
            'rows_removed': removed
        })
        
        return removed
    
    def standardize_categories(self, column: str, method: str = 'lower') -> None:
        """
        Standardize categorical values (casing, trimming whitespace).
        
        Args:
            column (str): Column name to standardize
            method (str): 'lower', 'upper', or 'title'
            
        Raises:
            ValueError: If column doesn't exist or method is invalid
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found")
        
        if method == 'lower':
            self.df[column] = self.df[column].str.lower().str.strip()
        elif method == 'upper':
            self.df[column] = self.df[column].str.upper().str.strip()
        elif method == 'title':
            self.df[column] = self.df[column].str.title().str.strip()
        else:
            raise ValueError(f"Invalid method: {method}")
        
        logger.info(f"Standardized '{column}' to {method} case and trimmed whitespace")
        
        self.cleaning_report['actions'].append({
            'action': 'standardize_categories',
            'column': column,
            'method': method
        })
    
    def remove_outliers_iqr(self, column: str, multiplier: float = 1.5) -> int:
        """
        Remove outliers using Interquartile Range (IQR) method.
        
        Args:
            column (str): Numeric column to check for outliers
            multiplier (float): IQR multiplier (default 1.5 for standard outlier detection)
        
        Returns:
            int: Number of rows removed
            
        Raises:
            ValueError: If column doesn't exist
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found")
        
        rows_before = len(self.df)
        
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - multiplier * IQR
        upper_bound = Q3 + multiplier * IQR
        
        self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
        
        rows_after = len(self.df)
        removed = rows_before - rows_after
        
        logger.info(f"Removed {removed} outliers from '{column}' (bounds: {lower_bound:.2f} - {upper_bound:.2f})")
        
        self.cleaning_report['actions'].append({
            'action': 'remove_outliers_iqr',
            'column': column,
            'lower_bound': lower_bound,
            'upper_bound': upper_bound,
            'rows_removed': removed
        })
        
        return removed
    
    def get_quality_report(self) -> Dict:
        """
        Generate a data quality report comparing before and after.
        
        Returns:
            Dict: Quality metrics
        """
        final_nulls = self.df.isnull().sum().sum()
        final_nulls_pct = (final_nulls / (len(self.df) * len(self.df.columns))) * 100
        
        report = {
            'original_rows': self.original_shape[0],
            'final_rows': len(self.df),
            'rows_removed': self.original_shape[0] - len(self.df),
            'original_columns': self.original_shape[1],
            'final_columns': len(self.df.columns),
            'original_nulls_pct': (self.df.isnull().sum().sum() / (self.original_shape[0] * self.original_shape[1])) * 100,
            'final_nulls_pct': final_nulls_pct,
            'final_completeness_pct': 100 - final_nulls_pct,
            'cleaning_actions': self.cleaning_report['actions']
        }
        
        return report
    
    def save_cleaned_data(self, output_path: str, include_index: bool = False) -> None:
        """
        Save the cleaned dataframe to CSV.
        
        Args:
            output_path (str): Path where to save the CSV file
            include_index (bool): Whether to include the dataframe index
        """
        self.df.to_csv(output_path, index=include_index)
        logger.info(f"Cleaned data saved to {output_path}")
    
    def get_dataframe(self) -> pd.DataFrame:
        """
        Return the cleaned dataframe.
        
        Returns:
            pd.DataFrame: The cleaned dataset
        """
        return self.df


# Convenience function for quick pipeline execution
def clean_fintech_transactions(
    input_path: str,
    output_path: str = None,
    verbose: bool = True
) -> pd.DataFrame:
    """
    Execute a complete data wrangling pipeline for fintech transactions.
    
    This is a convenience function that applies standard cleaning steps
    appropriate for fintech transaction data.
    
    Args:
        input_path (str): Path to dirty CSV file
        output_path (str): Path to save cleaned CSV (optional)
        verbose (bool): Whether to print detailed logs
        
    Returns:
        pd.DataFrame: Cleaned dataframe
        
    Example:
        >>> df_clean = clean_fintech_transactions(
        ...     'data/raw/dirty_financial_transactions.csv',
        ...     'data/processed/clean_transactions.csv'
        ... )
    """
    
    # Initialize wrangler
    wrangler = FinTechWrangler(input_path)
    
    if verbose:
        print("\n" + "="*60)
        print("FINTECH TRANSACTION DATA WRANGLING PIPELINE")
        print("="*60 + "\n")
        print(f"Original dataset: {wrangler.original_shape[0]} rows × {wrangler.original_shape[1]} columns\n")
    
    # Step 1: Analyze initial quality
    wrangler.analyze_nulls()
    wrangler.analyze_duplicates(subset=['transaction_id'])
    
    if verbose:
        print("\n" + "-"*60)
        print("CLEANING STEPS")
        print("-"*60 + "\n")
    
    # Step 2: Remove duplicates (on transaction_id, keep first)
    wrangler.remove_duplicates(subset=['transaction_id'], keep='first')
    
    # Step 3: Impute missing numeric values
    numeric_columns = wrangler.df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
        if wrangler.df[col].isnull().sum() > 0:
            wrangler.impute_missing_numeric(col, strategy='median')
    
    # Step 4: Impute missing categorical values
    categorical_columns = wrangler.df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        if wrangler.df[col].isnull().sum() > 0:
            wrangler.impute_missing_categorical(col, strategy='mode')
    
    # Step 5: Standardize date columns (if 'date' column exists)
    if 'date' in wrangler.df.columns:
        wrangler.standardize_dates('date')
    
    # Step 6: Standardize categorical columns
    for col in categorical_columns:
        wrangler.standardize_categories(col, method='lower')
    
    # Step 7: Generate final report
    if verbose:
        print("\n" + "-"*60)
        print("QUALITY REPORT")
        print("-"*60 + "\n")
        
        report = wrangler.get_quality_report()
        
        print(f"Final dataset: {report['final_rows']} rows × {report['final_columns']} columns")
        print(f"Rows removed: {report['rows_removed']}")
        print(f"Data completeness: {report['final_completeness_pct']:.2f}%")
        print(f"Improvement: {report['final_completeness_pct'] - (100 - report['original_nulls_pct']):.2f}%")
        
        print("\n" + "="*60 + "\n")
    
    # Step 8: Save cleaned data if output path provided
    if output_path:
        wrangler.save_cleaned_data(output_path, include_index=False)
    
    return wrangler.get_dataframe()


if __name__ == "__main__":
    # Example usage
    df_clean = clean_fintech_transactions(
        'data/raw/dirty_financial_transactions.csv',
        'data/processed/clean_transactions.csv'
    )
    
    print("\nCleaned data preview:")
    print(df_clean.head())
    print(f"\nDataframe info:")
    print(df_clean.info())
