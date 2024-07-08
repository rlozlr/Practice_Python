import unitConversion as uc

if __name__ == '__main__':
    userInput = int(input('길이(cm) 입력: '))

    result = uc.cmToMm(userInput)
    print(f'결과: {result}mm')

    result = uc.cmToInch(userInput)
    print(f'결과: {result}inch')

    result = uc.cmToM(userInput)
    print(f'결과: {result}m')

    result = uc.cmToFt(userInput)
    print(f'결과: {result}ft')