class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford: having a temp array of price, check video for setting up 2 arrays
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1): # nth of layer
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if p + prices[s] < tmpPrices[d]:
                    tmpPrices[d] = p + prices[s]
            prices = tmpPrices
                    
        return -1 if prices[dst] == float("inf") else prices[dst]
                    
