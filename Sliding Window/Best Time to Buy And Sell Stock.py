class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):            
            if prices[left] < prices[right]:
                currentProfit = prices[right] - prices[left] #current Profit
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit   