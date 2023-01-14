measurements=[199,200,208,210,200,207,240,269,260,263]
first_window_A = sum(measurements[0:3])
second_window_B = sum(measurements[1:4])
third_window_C = sum(measurements[2:5])
forth_window_D = sum(measurements[3:6])
fifth_window_E = sum(measurements[4:7])
sixth_window_F = sum(measurements[5:8])
seventh_window_G = sum(measurements[6:9])
eigth_window_H = sum(measurements[7:10])
previous_measurement=first_window_A
count=0
windows_sum=[first_window_A,second_window_B,third_window_C,forth_window_D,fifth_window_E,sixth_window_F,seventh_window_G,eigth_window_H]
for current_measurement in windows_sum:
	if current_measurement>previous_measurement:
		count+=1
	previous_measurement=current_measurement
print(count)
			




