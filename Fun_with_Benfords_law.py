populationNums = ['82.9', '67.2', '60.4', '46.7', '38', '19.5', '17.2', '11.4', '10.7', '10.6', '10.3', '10.1', '9.8', '8.8', '7.1', '5.8', '5.5', '5.4', '4.8', '4.1', '2.8', '2', '1.9', '1.3', '0.9', '0.6', '0.5']
first1 = []
first2 = []
first3 = []
first4 = []
first5 = []
first6 = []
first7 = []
first8 = []
first9 = []
first0 = []
for num in populationNums:
    if num[0] == '1':
        first1.append(num)
    elif num[0] == '2':
        first2.append(num)
    elif num[0] == '3':
        first3.append(num)
    elif num[0] == '4':
        first4.append(num)
    elif num[0] == '5':
        first5.append(num)
    elif num[0] == '6':
        first6.append(num)
    elif num[0] == '7':
        first7.append(num)
    elif num[0] == '8':
        first8.append(num)
    elif num[0] == '9':
        first9.append(num)
    else:
        first0.append(num)

print(len(first1), len(first2), len(first3), len(first4), len(first5), len(first6), len(first7), len(first8), len(first9), len(first0))