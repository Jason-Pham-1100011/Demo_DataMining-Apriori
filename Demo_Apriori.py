## Demo Apriori
import math as m

data = [[3287.0, 0.0, 0.0], [385.0, 0.0, 0.0], [3528.0, 9.0, 4.9], [1411.0, 0.0, 0.0], [67586.0, 819.0, 4.3], [4548.0, 17.0, 5.0], [1193.0, 14.0, 4.7], [659.0, 0.0, 0.0], [6461.0, 405.0, 4.2], [36069.0, 358.0, 4.3], [11949.0, 73.0, 4.0], [4761.0, 16.0, 3.4], [12196.0, 49.0, 3.9], [10256.0, 48.0, 4.5], [21769.0, 105.0, 3.5], [4158.0, 20.0, 4.7], [4220.0, 24.0, 3.9], [2.0, 66.0, 4.7], [18880.0, 744.0, 4.0], [8111.0, 85.0, 4.1], [3091.0, 0.0, 0.0], [2239.0, 2.0, 5.0], [11050.0, 69.0, 4.9], [3068.0, 4.0, 2.5], [13476.0, 47.0, 4.0], [11260.0, 13.0, 4.0], [5020.0, 1.0, 1.5], [2994.0, 2.0, 4.2], [5378.0, 1.0, 5.0], [2581.0, 0.0, 0.0], [20146.0, 161.0, 4.3], [14487.0, 57.0, 4.1], [2016.0, 26.0, 4.0], [63229.0, 976.0, 4.4], [15215.0, 56.0, 3.3], [62492.0, 713.0, 4.3], [8078.0, 22.0, 4.7], [9758.0, 14.0, 3.5], [6672.0, 22.0, 4.8], [3404.0, 12.0, 4.8], [13426.0, 33.0, 4.0], [7470.0, 13.0, 5.0], [37142.0, 888.0, 4.1], [6907.0, 64.0, 4.0], [24244.0, 100.0, 4.3], [2920.0, 0.0, 0.0], [157218.0, 3.0, 4.4], [96980.0, 790.0, 4.3], [6508.0, 0.0, 0.0], [3983.0, 0.0, 0.0], [6705.0, 0.0, 0.0], [3809.0, 9.0, 5.0], [6435.0, 13.0, 4.2], [65666.0, 488.0, 4.3], [1705.0, 1.0, 4.0], [6406.0, 8.0, 5.0], [1642.0, 6.0, 4.6], [17373.0, 567.0, 4.1], [8240.0, 327.0, 4.3], [16297.0, 81.0, 3.9], [57522.0, 476.0, 4.4], [66897.0, 366.0, 4.3], [11733.0, 5.0, 3.3], [11648.0, 0.0, 0.0], [3555.0, 39.0, 4.5], [16720.0, 157.0, 3.8], [61529.0, 457.0, 4.4], [98545.0, 819.0, 4.2], [4871.0, 364.0, 4.3], [18323.0, 463.0, 4.4], [13892.0, 149.0, 3.3], [27627.0, 51.0, 4.4], [898.0, 0.0, 0.0], [1443.0, 7.0, 4.6], [90522.0, 4.0, 4.5], [1235.0, 0.0, 0.0], [1427.0, 0.0, 0.0], [1335.0, 0.0, 0.0], [1567.0, 0.0, 0.0], [1519.0, 0.0, 0.0], [1172.0, 0.0, 0.0], [109279.0, 1.0, 4.2], [73549.0, 1.0, 4.3], [67078.0, 670.0, 4.2], [74233.0, 499.0, 4.3], [131720.0, 2.0, 4.3], [8917.0, 37.0, 4.0], [15198.0, 9.0, 3.0], [2374.0, 0.0, 0.0], [13115.0, 40.0, 4.1], [3850.0, 25.0, 4.9], [34315.0, 745.0, 4.5], [23744.0, 99.0, 4.2], [21231.0, 121.0, 3.8], [58913.0, 631.0, 3.9], [4470.0, 0.0, 0.0], [18401.0, 59.0, 3.7], [51432.0, 1.0, 4.2], [6833.0, 10.0, 4.2], [13303.0, 368.0, 4.2], [2773.0, 4.0, 5.0], [14926.0, 75.0, 4.1], [7310.0, 4.0, 5.0], [51932.0, 284.0, 4.4], [48118.0, 389.0, 4.3], [59150.0, 210.0, 4.1], [53103.0, 157.0, 4.4], [65399.0, 676.0, 4.3], [17480.0, 137.0, 4.1], [20244.0, 466.0, 4.1], [2975.0, 82.0, 4.2], [54200.0, 560.0, 4.4], [14830.0, 43.0, 3.5], [30713.0, 97.0, 4.2], [3514.0, 9.0, 4.0], [9289.0, 27.0, 3.5], [9548.0, 107.0, 4.3], [9454.0, 32.0, 4.4], [75598.0, 2.0, 4.4], [12939.0, 851.0, 4.1], [103878.0, 1.0, 4.2], [11008.0, 28.0, 3.8], [112118.0, 3.0, 4.3], [7286.0, 11.0, 4.1], [11568.0, 484.0, 4.3], [28767.0, 817.0, 4.5], [15412.0, 217.0, 4.1], [10780.0, 600.0, 4.3], [6740.0, 18.0, 5.0], [36547.0, 2.0, 4.0], [3442.0, 75.0, 4.3], [2988.0, 6.0, 4.5], [13162.0, 627.0, 4.3], [17585.0, 113.0, 4.2], [5022.0, 4.0, 5.0], [4250.0, 4.0, 5.0], [7936.0, 29.0, 4.4], [11353.0, 32.0, 4.1], [19786.0, 45.0, 4.4], [6944.0, 48.0, 4.6], [8553.0, 22.0, 3.9], [21034.0, 112.0, 4.3], [24529.0, 314.0, 4.3], [34354.0, 172.0, 4.1], [3254.0, 100.0, 4.5], [58322.0, 506.0, 3.9], [4272.0, 57.0, 3.5], [509.0, 0.0, 0.0], [35678.0, 208.0, 4.2], [115520.0, 2.0, 4.1], [53841.0, 2.0, 4.4], [10162.0, 11.0, 4.6], [7967.0, 25.0, 4.0], [30754.0, 156.0, 4.4], [11488.0, 20.0, 4.6], [10578.0, 56.0, 4.2], [1886.0, 20.0, 4.1], [27304.0, 91.0, 4.3], [63250.0, 860.0, 3.8], [25560.0, 251.0, 3.7]]

for row in data:
    n_stu = row[0]
    n_rat = row[1]
    n_sta = row[2]
    if n_stu > 999:
        row[0] = 1
    else:
        row[0] = 0
    if n_rat >99:
        row[1] = 1
    else:
        row[1] = 0
    if n_sta > 4:
        row[2] = 1
    else:
        row[2] = 0
##print (data)

def get_C1(data):
    C1 = {}
    
    for line in data:
        for i_col in range(len(line)):
            if line[i_col] != 0:
                if i_col not in C1:
                    C1[i_col] = [1]
                else:
                    C1[i_col].append(1)                    

    for key in sorted(C1):
        C1[key] = len(C1[key])
        
    C1 = {k: v for k, v in sorted(C1.items(), key=lambda item: item[0])}
##    print("C1: ",C1)
    return C1
    
def get_C2(L1,data):
    C2 = {}    

    for i in range(len(L1)):
        for j in range(i+1,len(L1)):
            item_list = [L1[i],L1[j]]
            supp = get_supp(item_list,data)
            key = get_key(item_list)
            C2[key] = supp
##    print("C2: ",C2)
    return C2

def get_L1(C1,minsupp):
    L1 = []
    for key in C1:
        if C1[key]>= minsupp:
            L1.append(key)
            L1 = sorted(L1)
##    print("L1: ",L1)
    return L1

def get_L_gen(C,minsupp):
    L_gen = []
    for key in C:
        if C[key]>= minsupp:
            key = key.split(",")
            items = [int(item) for item in key]
            L_gen.append(items)
##    print("L gen: ",L_gen)
    return L_gen



def get_key(item_list):
    str_list = [str(item) for item in item_list]
    key = ",".join(str_list)
    return key

def get_supp(item_list,data):
    supp = 0
    for line in data:
        flag = True
        for item in item_list:
            if line[item] == 0:
                flag = False
                break
        if flag:
            supp += 1
    return supp

def apriori_gen(L,data):
    C = {}
    for i_line in range(len(L)):
        for i_nline in range(i_line+1,len(L)):
            flag = True
            for i_col in range (len(L[i_line])-1):
                if L[i_line][i_col] != L[i_nline][i_col]:
                    flag = False
                    break
                
            if (flag and (L[i_line][len(L[i_line])-1]!=L[i_nline][len(L[i_line])-1])):
                l1 = list(L[i_line])
                l2 = list(L[i_nline])
                l1.extend(l2)
                c = sorted(list(set(l1)))
                if not has_infrequent_subset(c,L):
                    key = get_key(c)
                    supp = get_supp(c,data)
                    C[key] = supp
##    print("C gen: ",C)
    return C

def has_infrequent_subset(c,L):
    
    for i in c:
        temp = list(c)
        temp.remove(i)
        subset = temp
        if subset not in L:
            return True
    return False

def is_sub(el,items_list):
    if type (el)== int:
            return el in items_list
    else:
            return True if(all(x in items_list for x in el)) else False
    

def get_clauses(items_list,L_list):
    k = len(items_list)
    k = int(k/2)
    clauses = []
    for i in range(k):
        for el in L_list[i]:
            if is_sub(el,items_list):
##                print(el, items_list)
                if type(el) == int:
                    el = [el]
                    temp = list(item for item in items_list if item not in el)
                else:
                    temp = list(item for item in items_list if item not in el)

                clauses.append([el,temp,items_list])
                if len(items_list)>2:
                    clauses.append([temp,el,items_list])
    return clauses

def get_conf_by_clauses(clauses_list,C,n):
    conf_dict = {}
    
    for line in clauses_list:
        for clause in line:
            left = clause[0]
            right = clause[1]
            parent = clause[2]
            k_left = len(left)
            k_right = len(right)
            k_parent = len(parent)
            
            left = get_key(left)
            right = get_key(right)
            parent = get_key(parent)
            
            supp_left = C["C"+str(k_left)][left]
            supp_right = C["C"+str(k_right)][right]
            supp_parent = C["C"+str(k_parent)][parent]
##            print("left: ",left,"\t","rigth: ",right,"parent",parent)
##            print("supp left",supp_left,"supp right",supp_right,"supp parent",supp_parent)
            conf = (supp_parent/n) / (supp_right/n)
            print(left+" -> "+right+" = ",(supp_parent/n) / (supp_left/n))
            conf_dict[left+" -> "+right] = (supp_parent/n) / (supp_left/n)
    return conf_dict
        
def get_conf(L,C,n): 
    L_list = [L[key] for key in L]
    items_to_check = list(L_list)
    items_to_check.pop(0)
    clauses_list = []
    print("items_to_check",items_to_check)
    for l in reversed(items_to_check):
        for el in l:
           clauses_list.append(get_clauses(el,L_list))
    conf_dict = get_conf_by_clauses(clauses_list,C,n)
    return conf_dict

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r
    
def apriori(data,minsupp,minconf):

    minsupp = m.ceil(len(data) * minsupp)
    print("minsupp: ",minsupp)
    C1 = get_C1(data)
    L1 = get_L1(C1,minsupp)
    C2 = get_C2(L1,data)
    L2 = get_L_gen(C2,minsupp)

    n_C1 = {}
    for key in C1:
        n_C1[str(key)] = C1[key]
        
    C = {"C1":n_C1,"C2":C2}
    L = {"L1":L1,"L2":L2}
    k = 2
    L_gen=L2
    
    while (1): 
        k+=1
        print("k: ",k)
        C_gen = apriori_gen(L_gen,data)
        L_gen = get_L_gen(C_gen,minsupp)
        
        L["L"+ str(k)] = L_gen
        C["C"+ str(k)] = C_gen
        if(len(L_gen)<2):
            break
        
        
        
    for key in C:
        print(key,C[key])
    for key in L:
        print(key,L[key])

    conf_dict = get_conf(L,C,len(data))
    
    print("conf_dict: ")
    print("min conf: ",minconf)
    key_list = [key for key in conf_dict]
    for key in key_list:
        print(key+" = ", conf_dict[key])
        if conf_dict[key]< minconf:
            del conf_dict[key]

    print("Out put:")
    for key in conf_dict:
        print(key+" = ", conf_dict[key])
##data = [[1,0,1,1,0],[0,1,1,0,1],[1,1,1,0,1],[0,1,0,0,1]]
##data = [[1,1,0,0,1],
##        [0,1,0,1,0],
##        [0,1,1,0,0],
##        [1,1,0,1,0],
##        [1,0,1,0,0],
##        [0,1,1,0,0],
##        [1,0,1,0,0],
##        [1,1,1,0,1],
##        [1,1,1,0,0]]
apriori(data,0.2,0.5)
##apriori(data,0.7)
##C1 = get_C1(data)
##L1 = get_L1(C1,2)
##C2 = get_C2(L1,data)
##L2 = get_L2(C2,2)
##data = [[0,0,0] for i in range(5)]
##L = [[1,2,3],[1,2,4],[1,3,4],[1,3,5],[2,3,4]]


##L = [[0,2],[1,2],[1,4],[2,4]]

##C = apriori_gen(L2,data)

