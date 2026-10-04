 Automated Warehouse Inventory & Reporting Tool (My first Python Automated!)

A Python script designed to automate daily inventory evaluation, dynamic cost calculations, and visual conditional formatting for warehouse logistics.

# Business Problem
Manual data entry and inventory reviews are prone to human errors, slow down restocking workflows, and consume valuable labor hours.

# The Automated Solution
This script processes unformatted operational spreadsheets and automatically:
- Calculates total stock value dynamically (`Stock * Unit Price`).
- Formats monetary values with standard financial notation (`$#,##0.00`).
- Evaluates stock thresholds against minimum required levels.
- Flags critical restock alerts with conditional red highlighting.
- Styles headers and adjusts column widths automatically for immediate executive review.

# Tech Stack
- Python 3
- OpenPyXL 

# How to Run Locally :)
1. Clone the repository:
   ```bash
   git clone [https://github.com/USER/warehouse-excel-automation.git](https://github.com/USER/warehouse-excel-automation.git)
   cd warehouse-excel-automation

1.- Setup your virtual environment and install dependences:

python -m ven venv (or py -m venv venv)
On Windows:
.\venv\Scripts\activate
On Linux/macOS:
source venv/bin/activate
pip install openpyxl

2.- Generate sample data and run the automated pipeline: 
py generar_invetario.py
py procesar_bodega.py
