# Financial Calculator

## Description
This project is a **Financial Calculator** built using **Streamlit** that helps users understand the breakdown of their loans and identify potential interest-related scams by banks and loan lenders. The application provides a detailed monthly breakdown of interest payments, principal returns, and the remaining principal amount, helping users calculate their actual EMI and compare it with the offered monthly installment.

---

## Features
- User-friendly interface to input loan details.
- Detailed monthly breakdown of interest and principal.
- Calculates total interest, actual EMI, and potential losses or gains.
- Interactive visualizations using Plotly:
  - Line chart showing the Remaining Principal and Interest over time.
  - Pie chart comparing Total Interest vs Principal.
- Customizable inputs via the Streamlit sidebar.

---

## Technologies Used
- **Python**
- **Streamlit**: For the web interface.
- **Pandas**: For data manipulation.
- **Plotly**: For creating interactive visualizations.

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/financial-calculator.git
   cd financial-calculator
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

5. Open the URL provided by Streamlit in your browser (usually `http://localhost:8501`).

---

## How to Use

1. Input the loan parameters in the sidebar:
   - **Amount**: Enter the initial principal amount.
   - **Monthly Return**: Enter the amount returned monthly.
   - **Rate of Interest**: Enter the interest rate as a percentage.
   - **Number of Months**: Specify the loan duration in months.

2. Click the **Calculate** button.

3. View the results:
   - A detailed **Monthly Breakdown** in a table.
   - A **Summary** of total interest, actual EMI, and loss/gain.
   - Interactive visualizations for a clear understanding of interest and principal dynamics.

4. Analyze the results to detect any discrepancies or potential scams.

---

## File Structure
```
financial-calculator/
├── app.py                 # Main application script
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation (this file)
```

---

## Sample Outputs
- **Monthly Breakdown**:
  | Month | Interest | Principal Return | Remaining Principal |
  |-------|----------|------------------|---------------------|
  | 1     | 500.00   | 500.00          | 9500.00             |

- **Summary**:
  - Total Interest: 1200.00
  - Actual EMI: 1040.00
  - Loss/Gain: Loss of 60.00
  - Total Loss: 720.00

- **Visualizations**:
  - Line chart showing Remaining Principal and Interest over time.
  - Pie chart comparing Total Interest vs Principal.

---

## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements
- [Streamlit](https://streamlit.io/) for providing an easy-to-use framework for data apps.
- [Plotly](https://plotly.com/) for the interactive visualizations.
- Inspired by the need to promote financial transparency and awareness.

---

## Disclaimer
This tool is for informational purposes only and should not be considered as financial advice. Always consult with a financial advisor for accurate financial planning.

