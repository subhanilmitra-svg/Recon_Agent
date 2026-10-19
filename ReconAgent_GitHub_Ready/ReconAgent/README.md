# ReconAgent — AI-Powered Reconciliation Demo

A small Streamlit demo that compares bank statement transactions with Razorpay settlement records, displays exact matches, and demonstrates exception-resolution output on synthetic sample data.

## Requirements
- Python 3.10+ recommended

## Run locally
1. Extract this folder.
2. Open a terminal in the `ReconAgent` directory.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   streamlit run app.py
   ```
5. Select **Use sample synthetic data included in the project**, then click **Run AI Reconciliation**.

## Files
- `app.py` — Streamlit interface
- `matcher.py` — exact transaction matching
- `agent.py` — illustrative exception-resolution stub
- `data/` — synthetic CSV examples
- `.env.example` — example environment variable name

## Important note
The exception resolver currently returns a demonstration result; it does not call a live AI model. Use synthetic data only and do not commit API keys, credentials, or real financial data.
