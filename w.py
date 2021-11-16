name1 =  input("請輸入你的名字:")
name2 =  input("請輸入你的座號:")
print("hello!", name1 ,"你好")
score1 = int(input("請輸入作業成績:"))
score2 = int(input("請輸入測驗成績:"))
score3 = int(input("請輸入平時成績:"))
score4 = score1*0.4 + score2*0.4 + score3*0.2
print("學期成績是" + str(score4))
if score4 <60:
    print("不及格")
    name3 = "不及格"
else:
    print("及格")
    name3 = "及格"
print("姓名","座號","作業成績","測驗成績","平時成績","學期成績","學期成績評定")
print("{:<5} {:<6} {:<7} {:<8} {:<9} {:<10} {:<11}".format(name1 , name2 , score1 , score2 , score3 , score4 , name3))












# scores =  "{:<5} {:<6} {:<7} {:<8} {:<9} {:<10} {:<11}".format(name1 , name2 , score1 , score2 , score3 , grade , name3)
     # print (scores)


#???
"""
name1 =  input("請輸入你的名字:")
name2 =  input("請輸入你的座號:")
print("hello!", name1 ,"你好")
score1 = int(input("請輸入作業成績:"))
score2 = int(input("請輸入測驗成績:"))
score3 = int(input("請輸入平時成績:"))
grade = score1*0.4 + score2*0.4 + score3*0.2
print("學期成績是" + str(grade))
if grade <60:
    print("不及格")
    name3 = "不及格"
else:
    print("及格")
    name3 = "及格"
scores1 =  "{:<5} {:<6} {:<7} {:<8} {:<9} {:<10} {:<11}".format(name1 , name2 , score1 , score2 , score3 , grade , name3)

name1 =  input("請輸入你的名字:")
name2 =  input("請輸入你的座號:")
print("hello!", name1 ,"你好")
score1 = int(input("請輸入作業成績:"))
score2 = int(input("請輸入測驗成績:"))
score3 = int(input("請輸入平時成績:"))
grade = score1*0.4 + score2*0.4 + score3*0.2
print("學期成績是" + str(grade))
if grade <60:
    print("不及格")
    name3 = "不及格"
else:
    print("及格")
    name3 = "及格"

scores2 =  "{:<5} {:<6} {:<7} {:<8} {:<9} {:<10} {:<11}".format(name1 , name2 , score1 , score2 , score3 , grade , name3)
print (scores1) 
print (scores2) 
"""
#int強制整數-變數字
