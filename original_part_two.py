with open(".puzzle_input.txt","r")as file:
	puzzle_input=[int(line.strip()) for line in file.readlines()]
previous_measurement=first_window_A
count=0
windows_sum=[first_window_A,second_window_B,third_window_C,forth_window_D,fifth_window_E,sixth_window_F,seventh_window_G,eigth_window_H]
for current_measurement in windows_sum:
	if current_measurement>previous_measurement:
		count+=1
	previous_measurement=current_measurement
print(count)
			

