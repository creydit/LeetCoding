class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        if x==0 or y < 4:
            return "Bob"
        turns = min(x,y//4)
        if turns%2==0:
            return "Bob"
        return "Alice"
