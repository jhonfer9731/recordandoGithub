def get_hour_min_seg(time_str,time_str_2):

    from datetime import datetime
    from datetime import timedelta
    import pandas as pd
    list_hour = []
    list_min = []
    list_second = []
    date_format_str = '%d/%m/%Y %H:%M:%S'

    time_1 = datetime.strptime(time_str, date_format_str)
    time_2 = datetime.strptime(time_str_2, date_format_str)
    n = 1
    while time_1 <= time_2:
        list_hour.append(str(time_1.hour) if time_1.hour >= 10 else '0'+ str(time_1.hour))
        list_min.append(str(time_1.minute) if time_1.minute >= 10 else '0'+ str(time_1.minute))
        list_second.append(str(time_1.second) if time_1.second >= 10 else '0'+ str(time_1.second))
        time_1 = time_1 + timedelta(seconds=n)

    df = pd.DataFrame(
    list(
        zip(list_hour,list_min,list_second)
    ),
    columns = ['Hora','Min','Sec'])

    return df




def get_date(time_str,time_str_2):
    
    from datetime import datetime
    from datetime import timedelta
    import pandas as pd
    
    list_date = []
    list_day = []
    list_month = []
    list_year = []

    date_format_str = r'%d/%m/%Y'

    # create datetime object from timestamp string
    time_1 = datetime.strptime(time_str, date_format_str).date()
    time_2 = datetime.strptime(time_str_2, date_format_str).date()
    n = 1

    while time_1 <= time_2:
        list_date.append(time_1)
        list_day.append(int(time_1.day))
        list_month.append(int(time_1.month))
        list_year.append(int(time_1.year))
        time_1 = time_1 + timedelta(days=n)
    
    df = pd.DataFrame(
        list(
            zip(list_date,list_year,list_month,list_day)
        ),
        columns = ['Fecha','Año','Mes','Dia'])
    
    return df
#print(list)


import time


# df = get_hour_min_seg('01/01/2026 00:00:00','01/01/2026 23:59:59')
# df['idTiempo'] =  df.Hora + df.Min + df.Sec
# df['FechaString'] = df.Hora + ":" + df.Min + ":" + df.Sec







# f = open('./DimHoraMinSec.txt', 'w')
# for index, row in df.iterrows():    
    
#     f.write(
#         f"INSERT [dim].[Tiempo] ([idTiempo],[FechaString] ,[Hour], [Min], [Sec]) VALUES ( '{row['idTiempo']}','{row['FechaString']}' ,'{row['Hora']}', '{row['Min']}','{row['Sec']}') \n")

# f.close()

# end = time.time()


start = time.time()
print("Año 2000")
df = get_date('01/01/2010','31/12/2060')
df['idFecha'] = str(df.Año) + str(df.Mes).zfill(2) + str(df.Dia).zfill(2)
end = time.time()

f = open('./DimFecha.txt', 'w')
for index, row in df.iterrows():    
    
    f.write(
        f"INSERT [cmmd_datamodel].[dim_Fecha] ([id], [Ano],[Mes],[Dia], [FechaDate]) VALUES ( '{row['idFecha']}', '{row['Año']}', '{row['Mes']}',{row['Dia']},'{row['Fecha']}' ) \n"
        )

f.close()

print(f"Duración de la ejecución {end-start} segundos")