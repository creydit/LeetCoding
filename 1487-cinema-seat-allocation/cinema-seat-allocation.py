class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        reservedSeats.sort()
        reserved = defaultdict(list)
        extrarows = n

        for row, seat in reservedSeats:
            reserved[row].append(seat)
        #print(reserved)

        ans = 0 

        for row in reserved.keys():
            extrarows -= 1
            g1 = [2,3,4,5]
            g2 = [4,5,6,7]
            g3 = [6,7,8,9]
            op1 = True
            op2 = True
            op3 = True
            for i in g1:
                if i in reserved[row]:
                    op1 = False
                    break
            for i in g2:
                if i in reserved[row]:
                    op2 = False
                    break
            for i in g3:
                if i in reserved[row]:
                    op3 = False
                    break
            if op1:
                ans += 1
                op2 = False
            if op3:
                ans += 1
                op2 = False
            if op2:
                ans += 1

        ans += extrarows*2

        return ans