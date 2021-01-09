max_rain = 0
is_first_line = True

for row in open("climate_data_2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    max_temp = float(values[2])
    if max_temp > 35:
      if float(values[3]) >= max_rain:
        max_rain = float(values[3]) 
  

print("Maximum amount of rainfall on hot days: {} mm".format(max_rain))