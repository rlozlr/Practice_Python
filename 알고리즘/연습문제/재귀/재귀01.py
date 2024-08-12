# 다음은 'A상사'의 2021년 월별 매출을 나타내는 표
'''
      월   |   1월   |  2월  |   3월   |  4월   |  5월   |  6월   |  7월   |  8월   |  9월   |  10월  |  11월   |  12월
매출(천원) | 12,000 | 13,000 | 12,500 | 11,000 | 10,500 | 98,000 | 91,000 | 91,500 | 10,500 | 11,500 | 12,000  |  12,500
'''
# 재귀 Algorithm을 이용해서 1월부터 12월까지 전월대비 매출 증감액을 나타내기

sales = [ 12000, 13000, 12500, 11000, 10500, 98000, 91000, 91500, 10500, 11500, 12000, 12500]

def salesUpAndDown(ss):

    if len(ss) == 1:
        return ss

    print(f'sales: {ss}')
    currentSales = ss.pop(0)  # [ 12000, 13000, 12500, 11000, 10500, 98000, 91000, 91500, 10500, 11500, 12000, 12500]
    nextSales = ss[0]
    increase = nextSales - currentSales
    if increase > 0:
        increase = '+' + str(increase)
    print(f'매출 증감액: {increase}')

    return salesUpAndDown(ss)


if __name__ == '__main__':
    salesUpAndDown(sales)