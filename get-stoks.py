import requests
import os
import pandas as pd
from openpyxl.workbook import Workbook
from datetime import date
from string import Template
from dateutil.relativedelta import relativedelta

## pip install openpyxl
## pip install xlrd
URL_API = Template('https://www.bvc.com.co/mercados/DescargaXlsServlet?archivo=acciones_detalle&nemo=$nemo&tipoMercado=1&fechaIni=$start_date&fechaFin=$end_date')
ROOT_PATH = os.path.abspath('')

def mergeXlsFiles(activo_name):
    cwd = os.path.abspath('')
    files = os.listdir(cwd)

    df = pd.DataFrame()
    for file in files:
        if file.endswith('.xls'):
            df = df.append(pd.read_excel(file, skiprows=1), ignore_index=True)
    detail_file = 'detalle_'+activo_name+'.xlsx'

    print('activo {0} df shape {1}'.format(activo_name, df.shape))
    df.to_excel(detail_file)

    os.rename(cwd + '/'+ detail_file, ROOT_PATH +'/'+ detail_file)
    # going back to parent directory
    os.chdir('..')



with open('stock-list.txt', 'r') as activos:
    #iterates the list of activos.
    for activo in activos:
        #date range to dowload
        starts = date(2020, 1, 1)
        ends = starts.replace(month=6, day=30)

        dir_folder = activo.strip()
        if not dir_folder.startswith('#'):
            os.makedirs(dir_folder)
            os.chdir(dir_folder)

            # will dowload all data starting from 2020-01-01
            for i in range(4):
                url = URL_API.substitute(nemo=dir_folder, start_date=starts, end_date=ends)
                print(url)
                response = requests.get(url)
                if response.status_code == 200:
                    file_name = Template("detalle-$year-$month-$monthEnd.xls")
                    file = open(
                        file_name.substitute(year=starts.year, month=starts.month, monthEnd=ends.month), 
                        "wb")
                    file.write(response.content)
                    file.close()

                    delta_start = relativedelta(months=6)
                    delta_ends = relativedelta(months=6)
                    starts = starts + delta_start
                    ends = ends + delta_ends
        # Merging and copy to root parent. 
        mergeXlsFiles(dir_folder)
