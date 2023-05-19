
import pandas as pd
import os
from tabulate import tabulate
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=8080)
    app.run(debug=True)


table_data = [['Ime', 'datum', 'obaveza']
              ['Lara', '11.05.2023.', 'Sastanak s klijentom u 15h']
              ['Sandro', '12.03.2020.', 'Razgovor s agentom']
              ['Enea', '14.04.2021.', 'Fotografiranje za novu kampanju']]


print(table_data)


a = pd.read_csv("users.csv")

a.to_html("base.html")
