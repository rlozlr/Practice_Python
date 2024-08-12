import 근삿값01 as nearMod01
import 근삿값02 as nearMod02

def run01():

    depth = int(float(input('input depth: ')))
    print(f'depth: {depth}m')

    na = nearMod01.NearAlgorithm(depth)
    temp = na.getNearNumbers()
    print(f'master temperature: {temp}도')

uWeight = float(input('input weight(Kg): '))
uHeight = float(input('input height(m): '))
na = nearMod02.BmiAlgorithm(uWeight, uHeight)
na.calculatorBMI()
na.printUserCondition()