class Solution:
    def intToRoman(self, num: int) -> str:
        valuesymbols=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
        (100,'C'),(90,'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        res=[]

        for val,symbol in valuesymbols :
            if num==0 :
                break 
            count =num//val
            res.append(symbol*count)
            num-=count*val

        return ''.join(res)
        