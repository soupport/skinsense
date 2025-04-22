import pandas as pd
import re
import csv

def load_products():
    csv_file_path = r"C:/Users/lf220/Desktop/SKINSENSE/boots_skincare_products.csv"
    
    # Read CSV with flexible column handling
    try:
        # First try standard pandas read
        df = pd.read_csv(csv_file_path, quotechar='"', on_bad_lines='skip')
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None
    
    # Clean column names
    df.columns = df.columns.str.strip()
    
    # Verify required columns exist
    required = ['Name', 'Brand', 'Price', 'Link', 'Ingredients', 'Skin_Concerns']
    missing = [col for col in required if col not in df.columns]
    if missing:
        print(f"Missing columns: {missing}")
        return None
        
    return df

def clean_concerns(concerns_str):
    """Clean and extract skin concerns from messy string"""
    if pd.isna(concerns_str):
        return []
    
    concerns_str = str(concerns_str).strip()
    
    # Remove surrounding brackets and quotes
    concerns_str = re.sub(r'^\[|\]$', '', concerns_str)  # Remove [ and ]
    concerns_str = re.sub(r'^"|"$', '', concerns_str)    # Remove surrounding quotes
    
    # Split by comma, but ignore commas inside parentheses
    concerns = []
    current = []
    paren_level = 0
    
    for char in concerns_str:
        if char == '(':
            paren_level += 1
            current.append(char)
        elif char == ')':
            paren_level -= 1
            current.append(char)
        elif char == ',' and paren_level == 0:
            concerns.append(''.join(current).strip(' "\''))
            current = []
        else:
            current.append(char)
    
    if current:
        concerns.append(''.join(current).strip(' "\''))
    
    # Clean each concern and filter empty
    clean_concerns = []
    for concern in concerns:
        concern = concern.strip(' "\'')
        if concern:
            clean_concerns.append(concern.lower())
    
    return clean_concerns

def prepare_data(df):
    # Clean the skin concerns
    df['Clean_Concerns'] = df['Skin_Concerns'].apply(clean_concerns)
    
    # Get all unique concerns (cleaned version)
    all_concerns = set()
    for concerns in df['Clean_Concerns']:
        all_concerns.update(concerns)
    all_concerns = sorted(all_concerns)
    
    return df, all_concerns

def main():
    print("Loading data...")
    df = load_products()
    if df is None:
        print("Failed to load data")
        return
    
    print("Preparing data...")
    df, all_concerns = prepare_data(df)
    
    print("\nAvailable skin concerns:")
    print(', '.join(all_concerns))
    
    while True:
        user_input = input("\nEnter skin concern (or 'quit'): ").strip().lower()
        if user_input == 'quit':
            break
        
        # Find matching concerns (case insensitive and ignores punctuation)
        matches = []
        for concern in all_concerns:
            # Compare cleaned versions
            clean_user = re.sub(r'[^a-z]', '', user_input)
            clean_concern = re.sub(r'[^a-z]', '', concern)
            if clean_user == clean_concern:
                matches.append(concern)
        
        if not matches:
            print(f"No matching concern found for '{user_input}'")
            print("Available concerns:", ', '.join(all_concerns))
            continue
        
        # Use first match (should only be one if we cleaned properly)
        matched_concern = matches[0]
        
        # Find products containing this concern
        products = df[df['Clean_Concerns'].apply(lambda x: matched_concern in x)]
        
        if products.empty:
            print(f"No products found for '{matched_concern}'")
        else:
            print(f"\nFound {len(products)} products for '{matched_concern}':")
            for _, row in products.iterrows():
                print("\n" + "="*50)
                print(f"Product: {row['Name']}")
                print(f"Brand: {row['Brand']}")
                print(f"Price: {row['Price']}")
                print(f"Link: {row['Link']}")
                print("Concerns:", ', '.join(row['Clean_Concerns']))

if __name__ == "__main__":
    main()