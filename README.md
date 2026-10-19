# ReconAgent — AI-Powered Financial Reconciliation

ReconAgent is a Python-based financial reconciliation application that compares bank statements with Razorpay settlement records. It identifies exact transaction matches, highlights unmatched records, and demonstrates how AI-assisted exception resolution could help investigate discrepancies.

## Features

- **CSV Upload:** Upload bank statements and Razorpay settlement data.
- **Sample Dataset:** Test the application using the included synthetic CSV files.
- **Exact Matching:** Match transactions using transaction reference IDs and exact amounts.
- **Exception Detection:** Identify unmatched bank and Razorpay records.
- **AI Resolution Demo:** Display an example of how unmatched transactions could be investigated using confidence scores and explanations.
- **Interactive Dashboard:** Preview transaction data and reconciliation results through a Streamlit interface.

## Tech Stack

- Python
- Streamlit
- Pandas
- Google Generative AI SDK (included for potential future integration)
- python-dotenv

## Project Structure

```text
ReconAgent/
├── app.py
├── matcher.py
├── agent.py
├── requirements.txt
├── .env.example
└── data/
    ├── bank_statement.csv
    └── razorpay_settlements.csv
```

## Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ReconAgent
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`, where you can access the application.

## How to Use

1. Launch the application.
2. Select **Use sample synthetic data included in the project**, or upload your own bank statement and Razorpay settlement CSV files.
3. Review the uploaded transaction data.
4. Click **Run AI Reconciliation**.
5. Review exact matches, unmatched transactions, and the exception-resolution demonstration.

## CSV Data Format

**Bank statement — `bank_statement.csv`**

| Column | Description |
|---|---|
| `txn_id` | Bank transaction reference |
| `date` | Transaction date |
| `amount` | Transaction amount |
| `description` | Transaction description |

**Razorpay settlements — `razorpay_settlements.csv`**

| Column | Description |
|---|---|
| `rzp_id` | Razorpay settlement identifier |
| `rzp_date` | Settlement date |
| `rzp_amount` | Settlement amount |
| `bank_ref_id` | Corresponding bank reference |
| `status` | Settlement status |

The exact matcher compares the bank transaction ID with `bank_ref_id` and the bank amount with `rzp_amount`.

## AI Integration Status

The current `agent.py` contains a demonstration stub that returns a predefined example resolution for unmatched records. It does **not** call a live AI model or independently verify the suggested match.

The Google Generative AI SDK and `.env.example` are included for a possible future integration. A live API key and actual model integration are not currently required to run the demonstration.

## Future Enhancements

- Integrate a live AI model for exception analysis.
- Implement fuzzy matching and configurable fee tolerance.
- Add duplicate transaction detection.
- Provide downloadable reconciliation reports.
- Improve validation and error handling for uploaded CSV files.
- Add audit logs and secure handling of financial data.

## Limitations

- The included datasets contain synthetic sample transactions.
- Exact matching does not automatically account for gateway fees, timing differences, or partial settlements.
- Demonstration AI resolutions must not be treated as verified financial matches.
- The application is a prototype and should not be used for production financial decisions without additional validation, security, and testing.

## Disclaimer

ReconAgent is an educational project developed to demonstrate financial transaction reconciliation and potential AI-assisted exception handling. It is not an official Razorpay product and is not intended for production financial processing.

## Author

**Subhanil Mitra**  
Computer Science Engineering Student  
SRM Institute of Science and Technology
