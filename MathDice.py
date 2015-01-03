import random
"""
This function takes the target value, the largest face value of the scoring die, a copy of the rolled values,
and a list of answers as input. This function is then recursively called while numbers are added to the answer_list.
First, it checks the length of the scoring_values list. If the length = 0 then it returns the list. Next it
checks if the sum is greater than or less than the max of the scoring values. If the sum is greater, it
subtracts the max number. If it is less than it adds the max number. The used number is then removed from the
scoring values list and the funtion is called again with the updated scoring values and answer list.
"""
def build_toward_target(target, scoring_values_copy, answer_list):
    #base case
    if len(scoring_values_copy) <= 0:
        return answer_list
    else:
        if sum(answer_list) >= max(scoring_values_copy):
            answer_list.append(-max(scoring_values_copy))
            scoring_values_copy.remove(max(scoring_values_copy))
            return build_toward_target(target, scoring_values_copy, answer_list)
        if sum(answer_list) < max(scoring_values_copy):
            answer_list.append(max(scoring_values_copy))
            scoring_values_copy.remove(max(scoring_values_copy))
            return build_toward_target(target, scoring_values_copy, answer_list)
            
        

#Checks that input is valid. Loops until it is
error = True
while error == True:
    print('Enter Target die in the form of 1dx, where x is the number of faces')
    target_die_raw = input()
    print('Enter the Scoring dice in the form ndx, where n is the number of die and x is the number of faces.')
    scoring_die_raw = input()


    try:
        target_die_num = 1
        target_die_faces = int(target_die_raw.split('d')[1])
        scoring_die_num = int(scoring_die_raw.split('d')[0])
        scoring_die_faces = int(scoring_die_raw.split('d')[1])
        error = False
    except ValueError:
        print('ERROR: Please enter die in the form, ndx\n')
        error = True
    
#Rolls the target dice    
target = random.randrange(1,target_die_faces+1)

#Rolls scoring_dice and stores their value in a list
scoring_values = []
for i in range(scoring_die_num):
    scoring_values.append(random.randrange(1, scoring_die_faces+1))

#Caluculate max possible score
max_score = sum(scoring_values)

#Checks if it is possible to reach the target
if max_score < target:
    print(str(target) + ', ' + " ".join(str(i) for i in scoring_values))
    print('There is no way to reach the rolled target.\n')
#Checks if adding them all is equal to the target
if max_score == target:
    print(str(target) + ', ' + " ".join(str(i) for i in scoring_values))
    print(' + '.join(str(i) for i in scoring_values) + ' = ' + str(target))
#Normal execution of script
if max_score > target:
    
    #Make another copy of this list. scoring_values_cp will have elements removed from it and added to the answer_list in build_toward_target.
    scoring_values_cp = list(scoring_values)
    answer_list = []
    answer_list = build_toward_target(target, scoring_values_cp, answer_list)
    
    #An answer cannot be found
    if sum(answer_list) != target:
        print(str(target) + ', ' + " ".join(str(i) for i in scoring_values))
        print('An answer cannot be found with these rolls.')
        

    #The answer was found
    if sum(answer_list) == target:
        answer_list_str = ''
        for i in answer_list:
            if answer_list_str == '':
                answer_list_str = str(i)
            else:    
                if i < 0:
                    answer_list_str = answer_list_str + ' - ' + str(abs(i))
                else:
                    answer_list_str = answer_list_str + ' + ' + str(i)
        print(str(target) + ', ' + " ".join(str(i) for i in scoring_values))
        print(answer_list_str + ' = ' + str(target))
    
    
    