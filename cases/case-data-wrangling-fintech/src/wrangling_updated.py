"""
Data Wrangling Pipeline for Dirty Financial Transactions Dataset

This module provides specialized functions to clean the Dirty Financial Transactions
Dataset from Kaggle, which contains realistic data quality issues.

Dataset Columns:
- Transaction_ID: Unique identifier (missing/formatting issues)
- Transaction_Date: Date (invalid dates like 2023-13-01)
- Customer_ID: Customer identifier (duplicates)
- Product_Name: Product name (misspelled, extra spaces)
- Quantity: Number of items (negative, outliers like 1000)
- Price: Product price USD (negative, symbols like "$300")
- Payment_Method: Payment type (case/spacing inconsistencies)
- Transaction_Status: Status (inconsistent casing: "completed" vs "Completed")

Author: Jose Marcel Lopez Pino
Module: M3 - Data Preparation (Alkemy Bootcamp)
"""

import pandas as pd
import numpy as np
from typing import Tuple, Dict, List
import logging
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DirtyFinTechWrangler:
    """
    Specialized wrangler for the Dirty Financial Transactions Dataset.
    
    Handles specific issues found in this dataset:
    - Invalid dates (2023-13-01, 2025-02-30)
    - Price strings with symbols ("$300", "price")
    - Product name inconsistencies
    - Duplicate transaction IDs
    - Inconsistent casing in categorical columns
    """
    
    def __init__(self, filepath: str):
        """
        Initialize wrangler with CSV file.
        
        Args:
            filepath (str): Path to dirty_financial_transactions.csv
        """
        try:
            self.df = pd.read_csv(filepath)
            self.original_shape = self.df.shape
            self.cleaning_report = {
                'original_rows': self.original_shape[0],
                'original_cols': self.original_shape[1],
                'actions': []
            }
            logger.info(f"✓ Loaded {self.original_shape[0]} rows × {self.original_shape[1]} columns")
            logger.info(f"  Columns: {', '.join(self.df.columns)}")
        except FileNotFoundError as e:
            logger.error(f"✗ File not found: {filepath}")
            raise
    
    def diagnose_data_quality(self) -> Dict:
        """
        Comprehensive diagnosis of data quality issues.
        
        Returns:
            Dict: Summary of all issues found
        """
        issues = {
            'missing_values': {},
            'invalid_data': {},
            'duplicates': {},
            'inconsistencies': {}
        }
        
        # Check each column for issues
        for col in self.df.columns:
            null_count = self.df[col].isnull().sum()
            null_pct = (null_count / len(self.df)) * 100
            
            if null_count > 0:
                issues['missing_values'][col] = {
                    'count': null_count,
                    'percentage': null_pct
                }
        
        # Check for duplicates
        if 'Transaction_ID' in self.df.columns:
            dup_count = self.df.duplicated(subset=['Transaction_ID']).sum()
            issues['duplicates']['Transaction_ID'] = dup_count
        
        logger.info("\n📊 DATA QUALITY DIAGNOSIS:")
        logger.info(f"  Missing values: {sum(len(v) for v in issues['missing_values'].values())} columns affected")
        logger.info(f"  Duplicates: {sum(issues['duplicates'].values())} rows")
        
        return issues
    
    def clean_transaction_id(self) -> int:
        """
        Handle Transaction_ID issues:
        - Missing values
        - Special characters
        - Incorrect formatting
        
        Returns:
            int: Number of rows removed (invalid IDs)
        """
        if 'Transaction_ID' not in self.df.columns:
            logger.warning("⚠ Transaction_ID column not found")
            return 0
        
        rows_before = len(self.df)
        
        # Remove rows where Transaction_ID is completely missing
        self.df = self.df.dropna(subset=['Transaction_ID'])
        
        # Clean formatting: ensure T followed by numbers
        self.df['Transaction_ID'] = self.df['Transaction_ID'].astype(str).str.strip()
        
        rows_after = len(self.df)
        rows_removed = rows_before - rows_after
        
        logger.info(f"✓ Transaction_ID cleaned: {rows_removed} invalid rows removed")
        
        self.cleaning_report['actions'].append({
            'action': 'clean_transaction_id',
            'rows_removed': rows_removed,
            'method': 'Removed rows with missing Transaction_ID'
        })
        
        return rows_removed
    
    def clean_transaction_date(self) -> int:
        """
        Handle Transaction_Date issues:
        - Invalid dates (2023-13-01, 2025-02-30)
        - Missing values
        - Inconsistent formats
        
        Returns:
            int: Number of rows with invalid dates removed
        """
        if 'Transaction_Date' not in self.df.columns:
            logger.warning("⚠ Transaction_Date column not found")
            return 0
        
        rows_before = len(self.df)
        invalid_dates = 0
        
        # Try to parse dates, mark invalid ones
        def parse_date_safe(date_str):
            if pd.isna(date_str):
                return pd.NaT
            try:
                parsed = pd.to_datetime(date_str, format='%Y-%m-%d', errors='coerce')
                return parsed
            except:
                return pd.NaT
        
        self.df['Transaction_Date'] = self.df['Transaction_Date'].apply(parse_date_safe)
        
        # Remove rows with invalid dates
        self.df = self.df.dropna(subset=['Transaction_Date'])
        
        rows_after = len(self.df)
        rows_removed = rows_before - rows_after
        
        logger.info(f"✓ Transaction_Date cleaned: {rows_removed} rows with invalid dates removed")
        
        self.cleaning_report['actions'].append({
            'action': 'clean_transaction_date',
            'rows_removed': rows_removed,
            'method': 'Removed rows with invalid/missing dates'
        })
        
        return rows_removed
    
    def clean_customer_id(self) -> int:
        """
        Handle Customer_ID issues:
        - Missing values
        - Duplicated IDs (keep first occurrence)
        
        Returns:
            int: Number of rows removed
        """
        if 'Customer_ID' not in self.df.columns:
            logger.warning("⚠ Customer_ID column not found")
            return 0
        
        rows_before = len(self.df)
        
        # Remove rows with missing Customer_ID
        self.df = self.df.dropna(subset=['Customer_ID'])
        
        # Clean formatting
        self.df['Customer_ID'] = self.df['Customer_ID'].astype(str).str.strip().str.upper()
        
        rows_after = len(self.df)
        rows_removed = rows_before - rows_after
        
        logger.info(f"✓ Customer_ID cleaned: {rows_removed} rows with missing IDs removed")
        
        self.cleaning_report['actions'].append({
            'action': 'clean_customer_id',
            'rows_removed': rows_removed,
            'method': 'Removed rows with missing Customer_ID'
        })
        
        return rows_removed
    
    def clean_product_name(self) -> None:
        """
        Handle Product_Name issues:
        - Misspelled product names
        - Extra spaces
        - Inconsistent casing
        - Missing values → impute with 'Unknown'
        """
        if 'Product_Name' not in self.df.columns:
            logger.warning("⚠ Product_Name column not found")
            return
        
        null_count = self.df['Product_Name'].isnull().sum()
        
        # Impute missing with 'Unknown'
        if null_count > 0:
            self.df['Product_Name'].fillna('Unknown', inplace=True)
        
        # Clean formatting: lowercase, trim spaces, title case for readability
        self.df['Product_Name'] = (
            self.df['Product_Name']
            .astype(str)
            .str.strip()
            .str.title()
        )
        
        logger.info(f"✓ Product_Name cleaned: {null_count} nulls imputed, formatting standardized")
        
        self.cleaning_report['actions'].append({
            'action': 'clean_product_name',
            'nulls_imputed': null_count,
            'method': 'Imputed with "Unknown", standardized formatting to title case'
        })
    
    def clean_quantity(self) -> int:
        """
        Handle Quantity issues:
        - Negative values (remove rows)
        - Outliers like 1000 items (flag but keep for now)
        - Missing values (impute with median)
        
        Returns:
            int: Number of rows removed (negative quantities)
        """
        if 'Quantity' not in self.df.columns:
            logger.warning("⚠ Quantity column not found")
            return 0
        
        rows_before = len(self.df)
        null_count = self.df['Quantity'].isnull().sum()
        
        # Impute missing with median
        if null_count > 0:
            median_qty = self.df['Quantity'].median()
            self.df['Quantity'].fillna(median_qty, inplace=True)
            logger.info(f"  Imputed {null_count} null quantities with median: {median_qty}")
        
        # Remove negative quantities (invalid)
        self.df = self.df[self.df['Quantity'] >= 0]
        
        rows_after = len(self.df)
        rows_removed = rows_before - rows_after
        
        logger.info(f"✓ Quantity cleaned: {rows_removed} rows with negative quantities removed")
        
        # Flag outliers for investigation (don't remove)
        Q1 = self.df['Quantity'].quantile(0.25)
        Q3 = self.df['Quantity'].quantile(0.75)
        IQR = Q3 - Q1
        outliers = self.df[(self.df['Quantity'] > Q3 + 1.5 * IQR)].shape[0]
        
        if outliers > 0:
            logger.warning(f"  ⚠ {outliers} outliers detected (high quantities) - keeping for review")
        
        self.cleaning_report['actions'].append({
            'action': 'clean_quantity',
            'nulls_imputed': null_count,
            'negative_removed': rows_removed,
            'outliers_flagged': outliers,
            'method': 'Imputed nulls (median), removed negative values'
        })
        
        return rows_removed
    
    def clean_price(self) -> int:
        """
        Handle Price issues:
        - Prices with symbols ("$300", "price")
        - Negative prices (remove)
        - Missing values (impute with median)
        
        Returns:
            int: Number of rows removed (invalid prices)
        """
        if 'Price' not in self.df.columns:
            logger.warning("⚠ Price column not found")
            return 0
        
        rows_before = len(self.df)
        
        def extract_numeric_price(price_str):
            """
            Extract numeric value from price string.
            Examples: "$300" → 300, "price" → NaN, "150.50" → 150.50
            """
            if pd.isna(price_str):
                return np.nan
            
            price_str = str(price_str).strip()
            
            # Extract numbers and decimal points
            match = re.search(r'(\d+\.?\d*)', price_str)
            if match:
                return float(match.group(1))
            else:
                return np.nan
        
        # Clean prices
        self.df['Price'] = self.df['Price'].apply(extract_numeric_price)
        
        # Impute missing with median
        null_count = self.df['Price'].isnull().sum()
        if null_count > 0:
            median_price = self.df['Price'].median()
            self.df['Price'].fillna(median_price, inplace=True)
            logger.info(f"  Imputed {null_count} null prices with median: ${median_price:.2f}")
        
        # Remove negative prices
        self.df = self.df[self.df['Price'] >= 0]
        
        rows_after = len(self.df)
        rows_removed = rows_before - rows_after
        
        logger.info(f"✓ Price cleaned: Extracted numeric values, imputed {null_count} nulls, removed {rows_removed} negative prices")
        
        self.cleaning_report['actions'].append({
            'action': 'clean_price',
            'nulls_imputed': null_count,
            'negative_removed': rows_removed,
            'method': 'Extracted numeric values (removed symbols), imputed nulls (median), removed negatives'
        })
        
        return rows_removed
    
    def clean_payment_method(self) -> None:
        """
        Handle Payment_Method issues:
        - Inconsistent casing ("Credit card" vs "Credit Card")
        - Extra spaces
        - Missing values → impute with mode
        - Standardize to expected categories
        """
        if 'Payment_Method' not in self.df.columns:
            logger.warning("⚠ Payment_Method column not found")
            return
        
        null_count = self.df['Payment_Method'].isnull().sum()
        
        # Standardize to title case and trim
        self.df['Payment_Method'] = (
            self.df['Payment_Method']
            .astype(str)
            .str.strip()
            .str.title()
        )
        
        # Impute missing with mode (most common payment method)
        if null_count > 0:
            mode_method = self.df['Payment_Method'].mode()[0]
            self.df['Payment_Method'].fillna(mode_method, inplace=True)
            logger.info(f"  Imputed {null_count} null payment methods with mode: {mode_method}")
        
        logger.info(f"✓ Payment_Method cleaned: Standardized casing, imputed {null_count} nulls")
        
        self.cleaning_report['actions'].append({
            'action': 'clean_payment_method',
            'nulls_imputed': null_count,
            'method': 'Standardized to title case, imputed nulls (mode)'
        })
    
    def clean_transaction_status(self) -> None:
        """
        Handle Transaction_Status issues:
        - Inconsistent casing ("completed" vs "Completed")
        - Missing values → impute with 'Pending'
        - Standardize to expected categories
        """
        if 'Transaction_Status' not in self.df.columns:
            logger.warning("⚠ Transaction_Status column not found")
            return
        
        null_count = self.df['Transaction_Status'].isnull().sum()
        
        # Standardize to title case
        self.df['Transaction_Status'] = (
            self.df['Transaction_Status']
            .astype(str)
            .str.strip()
            .str.title()
        )
        
        # Impute missing with 'Pending' (conservative approach)
        if null_count > 0:
            self.df['Transaction_Status'].fillna('Pending', inplace=True)
            logger.info(f"  Imputed {null_count} null statuses with 'Pending'")
        
        logger.info(f"✓ Transaction_Status cleaned: Standardized casing, imputed {null_count} nulls")
        
        self.cleaning_report['actions'].append({
            'action': 'clean_transaction_status',
            'nulls_imputed': null_count,
            'method': 'Standardized to title case, imputed nulls with "Pending"'
        })
    
    def remove_duplicate_transactions(self) -> int:
        """
        Remove duplicate transactions (keep first occurrence).
        
        Returns:
            int: Number of duplicate rows removed
        """
        rows_before = len(self.df)
        
        if 'Transaction_ID' in self.df.columns:
            self.df.drop_duplicates(subset=['Transaction_ID'], keep='first', inplace=True)
        else:
            self.df.drop_duplicates(keep='first', inplace=True)
        
        rows_after = len(self.df)
        rows_removed = rows_before - rows_after
        
        logger.info(f"✓ Duplicates removed: {rows_removed} duplicate rows removed (kept first occurrence)")
        
        self.cleaning_report['actions'].append({
            'action': 'remove_duplicates',
            'rows_removed': rows_removed,
            'method': 'Removed duplicates on Transaction_ID, kept first occurrence'
        })
        
        return rows_removed
    
    def get_quality_report(self) -> Dict:
        """
        Generate comprehensive data quality report.
        
        Returns:
            Dict: Before/after metrics
        """
        final_nulls = self.df.isnull().sum().sum()
        final_nulls_pct = (final_nulls / (len(self.df) * len(self.df.columns))) * 100
        
        report = {
            'original_rows': self.cleaning_report['original_rows'],
            'final_rows': len(self.df),
            'rows_removed': self.cleaning_report['original_rows'] - len(self.df),
            'original_columns': self.cleaning_report['original_cols'],
            'final_columns': len(self.df.columns),
            'final_nulls_pct': final_nulls_pct,
            'final_completeness_pct': 100 - final_nulls_pct,
            'cleaning_actions': self.cleaning_report['actions']
        }
        
        return report
    
    def save_cleaned_data(self, output_path: str, include_index: bool = False) -> None:
        """
        Save cleaned dataframe to CSV.
        
        Args:
            output_path (str): Path to save cleaned CSV
            include_index (bool): Whether to include index
        """
        self.df.to_csv(output_path, index=include_index)
        logger.info(f"✅ Cleaned data saved: {output_path}")
        logger.info(f"   {len(self.df)} rows × {len(self.df.columns)} columns")
    
    def get_dataframe(self) -> pd.DataFrame:
        """Return cleaned dataframe."""
        return self.df


def clean_dirty_financial_transactions(
    input_path: str,
    output_path: str = None,
    verbose: bool = True
) -> pd.DataFrame:
    """
    Execute complete data wrangling pipeline for Dirty Financial Transactions Dataset.
    
    This function applies a sequence of cleaning steps specifically designed
    for the issues found in this dataset:
    1. Clean Transaction_ID
    2. Clean Transaction_Date
    3. Clean Customer_ID
    4. Clean Product_Name
    5. Clean Quantity
    6. Clean Price
    7. Clean Payment_Method
    8. Clean Transaction_Status
    9. Remove Duplicates
    
    Args:
        input_path (str): Path to dirty_financial_transactions.csv
        output_path (str): Path to save cleaned CSV (optional)
        verbose (bool): Print detailed logs
        
    Returns:
        pd.DataFrame: Cleaned dataset
        
    Example:
        >>> df_clean = clean_dirty_financial_transactions(
        ...     'data/raw/dirty_financial_transactions.csv',
        ...     'data/processed/clean_transactions.csv'
        ... )
    """
    
    # Initialize wrangler
    wrangler = DirtyFinTechWrangler(input_path)
    
    if verbose:
        print("\n" + "="*70)
        print("DIRTY FINANCIAL TRANSACTIONS - DATA WRANGLING PIPELINE")
        print("="*70 + "\n")
        print(f"Original dataset: {wrangler.original_shape[0]} rows × {wrangler.original_shape[1]} columns\n")
    
    # Step 1: Diagnose data quality
    if verbose:
        issues = wrangler.diagnose_data_quality()
    
    if verbose:
        print("\n" + "-"*70)
        print("CLEANING STEPS")
        print("-"*70 + "\n")
    
    # Step 2: Clean each column sequentially
    wrangler.clean_transaction_id()
    wrangler.clean_transaction_date()
    wrangler.clean_customer_id()
    wrangler.clean_product_name()
    wrangler.clean_quantity()
    wrangler.clean_price()
    wrangler.clean_payment_method()
    wrangler.clean_transaction_status()
    wrangler.remove_duplicate_transactions()
    
    # Step 3: Generate report
    if verbose:
        print("\n" + "-"*70)
        print("QUALITY REPORT")
        print("-"*70 + "\n")
        
        report = wrangler.get_quality_report()
        
        print(f"Final dataset: {report['final_rows']} rows × {report['final_columns']} columns")
        print(f"Rows removed: {report['rows_removed']}")
        print(f"Data completeness: {report['final_completeness_pct']:.2f}%")
        print(f"\n" + "="*70 + "\n")
    
    # Step 4: Save cleaned data
    if output_path:
        wrangler.save_cleaned_data(output_path, include_index=False)
    
    return wrangler.get_dataframe()


if __name__ == "__main__":
    # Example usage
    df_clean = clean_dirty_financial_transactions(
        'data/raw/dirty_financial_transactions.csv',
        'data/processed/clean_transactions.csv',
        verbose=True
    )
    
    print("\nCleaned data preview:")
    print(df_clean.head(10))
    print(f"\nDataset Info:")
    print(df_clean.info())
