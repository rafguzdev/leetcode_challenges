class Solution:

    @staticmethod
    def encode(words):
        temp = ''
        for word in words:
            temp += f'{len(word)}#{word}'
        return temp

    @staticmethod
    def decode(word):
        temp = []
        while word != '':
            idx = word.find('#')
            snum = word[:idx]
            prefix = len(snum) + 1
            num = int(snum)
            temp.append(word[prefix:prefix + num])
            word = word[prefix + num:]
        return temp


s = Solution()
print(s.decode(s.encode(words=['acvasdsdad', 'aasdasdsd', 'a'])))


