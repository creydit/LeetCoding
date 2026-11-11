class UndergroundSystem:

    def __init__(self):
        # (s,e)->[sum,#?]
        self.dic = {}
        self.startS = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startS[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # ...
        enter, et = self.startS[id]
        # t - et -> sum += (t  - et)
        # len -> len += 1

        ss, ll = self.dic.get((enter, stationName), [0,0])
        self.dic[(enter, stationName)] = [ss + (t - et), ll + 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ssum, llen = self.dic[(startStation, endStation)]
        return ssum/llen


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)