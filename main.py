from mean_var_std import calculate

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = calculate([0,1,2,3,4,5,6,7,8])
    print("{\n" + "mean: " + str(result['mean']).replace('array','').replace('(','').replace(')',''))
    print("variance: " + str(result['variance']).replace('array', '').replace('(', '').replace(')', ''))
    print("standard deviation: " + str(result['standard deviation']).replace('array', '').replace('(', '').replace(')', ''))
    print("max: " + str(result['max']).replace('array', '').replace('(', '').replace(')', ''))
    print("min: " + str(result['min']).replace('array', '').replace('(', '').replace(')', ''))
    print("sum: " + str(result['sum']).replace('array', '').replace('(', '').replace(')', ''))
    print("}")
