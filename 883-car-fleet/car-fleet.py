class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        n = len(position)
        arr = []

        for i in range(n):
            arr.append((position[i], speed[i]))
            
        arr.sort(reverse = True)

        st = []
        for i in range(n):
            time = (target - arr[i][0] ) / arr[i][1]
            if not st or st[-1] < time:
                st.append(time)
        return len(st)