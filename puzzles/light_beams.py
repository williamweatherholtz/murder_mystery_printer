'''
Information from IP address A and information from IP address B both move from opposite ends on a transmission line at 1,000 miles per second.  There is a quicker subnet made of a modulated encoding signal that moves information at 4,400 miles per second, and starts simultaneously with information A and B, all on the same transmission line.  Upon reaching information B, the modulated (quicker) information signal will fully reflect (retaining its speed) and bounce back to information A, where it reflects back towards information B.  It keeps reflecting until both information A and information B meet, at which time the modulated signal is attenuated and eradicated.  

How far does the modulated information travel in total before it is eradicated, if information A and B are 2020 miles apart?
'''

dist_A_B = 200 #miles
speed_A_B = 50 #miles per hour
speed_C = 75

time_for_a_b = dist_A_B / (2*speed_A_B)
#print (time_for_a_b)
dist_C = time_for_a_b * speed_C

print (dist_C)



dist_A_B = 2020. #miles
speed_A_B = 1000 #miles per hour
speed_C = 4400

time_for_a_b = dist_A_B / (2*speed_A_B)
#print (time_for_a_b)
dist_C = time_for_a_b * speed_C


#4444 = (1/2 * dist_A_B / speed_A_B) * speed_C
print (4444*2*speed_A_B / speed_C)
print (dist_C)