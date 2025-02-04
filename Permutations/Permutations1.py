def per(numss,n):

    p=[]
    a=[]
    if len(numss)>1:
        for i in range(len(numss)):
            if i<len(numss):
                a=numss.copy()
                a.pop(i)
                a2=per(a,n)
                print(len(a2))
                for j in range(len(a2)):
                    q=[numss[i]]
                    q.extend([a2[j]])
                    print(q)
                    p.append(q)



    else:
        p.append(numss[0])

    return p
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        P=per(nums,len(nums))

        return P