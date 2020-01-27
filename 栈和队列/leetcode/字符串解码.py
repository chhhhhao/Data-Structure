class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack = []
        ch_stack = []
        tmp = ""
        number = ""
        i = 0
        while 0 <= i < len(s):
            if "0" <= s[i] <= "9":
                while "0" <= s[i] <= "9":
                    number += s[i]
                    i += 1
                num_stack.append(int(number))
                number = ""
            if s[i] != "]":
                ch_stack.append(s[i])
            else:
                num = num_stack.pop()
                e = ch_stack.pop()
                while e != "[":
                    tmp += e
                    e = ch_stack.pop()
                tmp *= num
                # 将解析括号的字符重新压入栈中
                for ch in tmp[::-1]:
                    ch_stack.append(ch)
                tmp = ""
            i += 1
        answer = "".join(ch_stack)
        return answer


if __name__ == "__main__":
    # s = input("INPUT: ")
    s = "2[b4[F]c]"
    print(Solution().decodeString(s))
