
#  File: Bottles.py 

#  Description:  hw 24

#  Student Name:  Melanie Sifen

#  Student UT EID:  ms69768

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created:4/4

#  Date Last Modified: 4/7

# this function takes as input a list v of positive integers
# it returns two lists s_v and b_v, containing the contents of
# the columns S(v) and B(v) as shown
def bottles_dp(v):
    n = len(v)
    sv = [v[0]]
    bv = [0]
    # add max of first or second bottle
    sv.append(max(v[0], v[1]))
    if v[1] > v[0]:
        bv.append(1)
    else:
        bv.append(-1)
    for j in range(2, n):
        a = v[j] + sv[j - 2]
        b = sv[j - 1]
        new_vol = max(a, b)
        sv.append(new_vol)
        if a > b:
            bv.append(j)
        else:
            bv.append(-1)


    return sv, bv

# gets contributor bottles
def get_contributors(v):
    contributor_lst = []
    for i in range(0, len(v) - 1, 2):
        contributor_lst.append(max(v[i], v[i + 1]))

    if v[-1] > contributor_lst[-1]:
        del contributor_lst[-1]
        contributor_lst.append(v[-1])

    return contributor_lst
        
                            
    
def main():

    inf = open("bottles.txt", "r")

    v = []
    num_bottles = int(inf.readline().strip())
    for i in range(num_bottles):
        line = int(inf.readline().strip())
        v.append(line)

    inf.close()
   
    s_v, b_v = bottles_dp(v)
    contributors = get_contributors(v)
    s_s_v = " ".join(str(num) for num in s_v)
    s_b_v = " ".join(str(num) for num in b_v)
    s_contributors = " ".join(str(num) for num in contributors)

    

    print(s_s_v)
    print(s_b_v)
    print(str(s_v[-1]))
    print(s_contributors)
    

    

main()

        
    
