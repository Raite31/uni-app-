class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        # words一个大循环
        # words每串字符一个小循环
        # 小循环负责一个个对比allowed有无出现该字符
        # 卡在了双重循环里的if那，一开始忘记了加else，于是得不到想要的结果
        # 若不加else这个把flag改回0的条件，那么当flag=1时，就会一直都是1，从而影响结果
        # 并且if中的中断条件必须用break，若用continue，效果可想而知
        flag = 0
        num = 0
        n = list(allowed)
        for i in words:
            for j in i:
                if j not in n:
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 0:
                num += 1
        return num