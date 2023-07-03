
all_rounds_list = []
for i in range(0,26):
    for j in range(0,21):
        for k in range(0,13):
            all_rounds_list.append([i,j,k])

in_range_rounds = []
for round in all_rounds_list:
    if (((round[0]*3)+(round[1]*5)+(round[2]*8)) <= 100):
        in_range_rounds.append(round)


outputs = []
for output in in_range_rounds:
    output_1 = [output[0] * 8, output[0] * 4]
    output_2 = [output[1] * 6, output[1] * 9]
    output_3 = [output[2] * 7, output[2] * 5]
    outputs.append([output_1,output_2,output_3])


productions_list = []
for production in outputs:
    production_A = production[0][0]+production[1][0]+production[2][0]
    production_B = production[0][1]+production[1][1]+production[2][1]
    productions_list.append([production_A,production_B])


final_productions = []
for final_production in productions_list:
    final = int(min((final_production[0]/4),final_production[1]/3))
    final_productions.append(final)


max_output_round = in_range_rounds[final_productions.index(max(final_productions))]
print(max_output_round)
print(f"The factory Maximum output is: {max(final_productions)}, which is related to the"
      f" {max_output_round[2]} rounds of section 1, {max_output_round[1]} rounds of section2 and"
      f" {max_output_round[0]} rounds of section3. :) ")





