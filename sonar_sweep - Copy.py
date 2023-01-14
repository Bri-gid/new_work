data=[199,200,208,210,200,207,240,269,260,263]
count=0
larger_than_previous_measurement=0
previous_measurement=data[0]
sonar_sweep_report=data[1:]
for sea_floor_depth in sonar_sweep_report:
    if sea_floor_depth>previous_measurement:
        count+=1
    previous_measurement=sea_floor_depth
        
print(count)
        
    
        
