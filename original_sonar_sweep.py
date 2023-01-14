with open("./puzzle_inputs.txt", "r") as file:
	puzzle_input=[int(line.strip()) for line in file.readlines()]
count=0
larger_than_previous_measurement=0
previous_measurement=puzzle_input[0]
sonar_sweep_report=puzzle_input[1:]
for sea_floor_depth in sonar_sweep_report:
    if sea_floor_depth>previous_measurement:
        count+=1
    previous_measurement=sea_floor_depth
        
print(count)
   
    
   

	
