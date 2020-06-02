"""피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다.
1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?"""

f_list = [1,2]
i=0
new_list=list()
while True:
    a=f_list[i]+f_list[i+1]
    i=i+1
    f_list.append(a)
    if(a %2==0):
        new_list.append(a)
    if(a>4000000):
        break

t_sum=sum(new_list[:])
print(t_sum+2)
