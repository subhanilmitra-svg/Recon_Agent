import pandas as pd

def exact_match(bank_df, rzp_df):
    # Merge on bank_ref_id (from razorpay) matching txn_id (from bank) and exact amount
    merged = pd.merge(
        bank_df, 
        rzp_df, 
        left_on=['txn_id', 'amount'], 
        right_on=['bank_ref_id', 'rzp_amount'], 
        how='inner'
    )
    
    # Identify unmatched records
    matched_bank_ids = merged['txn_id'].tolist()
    unmatched_bank = bank_df[~bank_df['txn_id'].isin(matched_bank_ids)]
    
    matched_rzp_ids = merged['rzp_id'].tolist()
    unmatched_rzp = rzp_df[~rzp_df['rzp_id'].isin(matched_rzp_ids)]
    
    return merged, unmatched_bank, unmatched_rzp
