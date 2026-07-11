class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bst_price=prices[0]
        profit=0
        for price in prices:
            bst_price =min(bst_price,price)
            profit=max(profit,price-bst_price)
        return profit