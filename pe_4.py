"""앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?"""

ne_list = list()
for i in range(100,1000):
    for j in range(100,1000):
        result = i*j
        s_len=str(result)
        if len(s_len) == 6:
            a = s_len[0]
            b = s_len[1]
            c = s_len[2]
            d = s_len[3]
            e = s_len[4]
            f = s_len[5]
            if a==f and b==e and c==d:
                ne_list.append(result)

print(max(ne_list))
