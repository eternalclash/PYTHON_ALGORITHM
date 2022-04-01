#문제 보자마자 Maximum-subarray문제랑 거의 비슷하다고 생각했다
#배열을 순회하면서 그 전의 요소들보다 작을 경우에는 result에 현재 요소를 넣고
#전의 요소보다 현재요소가 클 경우에는 answer에 최댓값을 판단하여 넣는다
#이건 좀 잘 푼듯? 이제 해결책이 떠올라도 시간복잡도를 조금씩 생각하는 것 같다,, 시간 초과가 제일 두렵다,,

class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        result =-1
        answer=0
        for i in range(n):
            if result == -1:
                result = prices[i]
            else:
                if prices[i] <= result:
                    result=prices[i]
                else :
                    answer=max(answer,prices[i]-result)
        return answer