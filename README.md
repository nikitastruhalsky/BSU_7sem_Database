# BSU_7sem_Database
## Exchanges reference
1. Exchange Id (integer)
2. Exchange Name (text)
3. Formation Date (date)
4. Location (text)
5. Revenue (float)
## Companies reference:
1. Company Id (integer)
2. Company Name (text)
3. Formation Date (date)
4. Exchange Traded (reference to Exchanges)
5. Employees Number (integer)

Steps to run (python3 should be installed (help link: https://docs.python.org/3/tutorial/venv.html)):

Install packages by using the following commands (run one by one):
"pip install streamlit";
"pip install pandas";
"pip install psycopg2";
"pip install sqlalchemy".
Run the calculator.py script in cmd (for Windows) by typing: streamlit run lab2.py
