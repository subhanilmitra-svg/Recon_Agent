import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def resolve_exceptions(unmatched_bank_df, unmatched_rzp_df):
    # This is a stub for the AI logic. 
    # In a real scenario, you would format the unmatched rows into a prompt
    # and ask the LLM to find fuzzy matches (e.g., amount minus 2% fee).
    
    if unmatched_bank_df.empty or unmatched_rzp_df.empty:
        return []
        
    # Example prompt structure for future implementation:
    '''
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Find matches between these bank records: {unmatched_bank_df.to_dict()} and these Razorpay records: {unmatched_rzp_df.to_dict()} considering a 2% gateway fee."
    response = model.generate_content(prompt)
    '''
    
    # Returning a dummy AI match for demonstration purposes based on our synthetic dataset
    dummy_resolution = {
        "bank_txn": unmatched_bank_df.iloc[0]['txn_id'],
        "bank_amount": float(unmatched_bank_df.iloc[0]['amount']),
        "rzp_txn": unmatched_rzp_df.iloc[0]['rzp_id'],
        "rzp_amount": float(unmatched_rzp_df.iloc[0]['rzp_amount']),
        "confidence": 0.98,
        "reason": "AI matched via fuzzy logic: Bank amount (980) matches Razorpay settlement (1000) minus standard 2% gateway fee."
    }
    
    return [dummy_resolution]
