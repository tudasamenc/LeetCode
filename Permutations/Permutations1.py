def per(numss,n):
    p=[]
    a=[]
    if len(numss)>1:
        for i in range(len(numss)):
            if i<len(numss):
                a=numss.copy()
                a.pop(i)
                a2=[]
                a2=per(a,n)
                for j in range(len(a2)):
                    q=[numss[i]]
                    if isinstance(a2[j], int):
                        q.extend([a2[j]])
                    else:
                        q.extend(a2[j])
                    p.append(q)
    else:
        p.append(numss[0])
    return p
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if(len(nums)==1):
            P=[nums.copy()]
        else:
            P=per(nums,len(nums))
        return P