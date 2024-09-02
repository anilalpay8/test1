akp_votes = 510532
mhp_votes = 180000
chp_votes = 428734
iyi_votes = 249587
hdp_votes = 106087

dhont_list = [akp_votes, mhp_votes, chp_votes, iyi_votes, hdp_votes]
den_list = [1, 1, 1, 1, 1]
x = 0
print_list = [akp_votes, mhp_votes, chp_votes, iyi_votes, hdp_votes]
while x < 16:
    x = x + 1
    print(print_list) 
    largest_number = max(print_list)
    for i in range(len(print_list)):
        if print_list[i] == largest_number:
            den_list[i] = den_list[i] + 1
            print_list[i] = int(dhont_list[i] / den_list[i])
        else :
            pass
