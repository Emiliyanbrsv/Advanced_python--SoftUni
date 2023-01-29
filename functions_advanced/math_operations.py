def math_operations(*args,**kwargs):
    
    result = []
    for i in range(len(args)):
        operation = list(kwargs.keys())[i%4]
        if operation=='a':
            kwargs[operation] +=args[i]
        elif operation=='s':
            kwargs[operation] -=args[i]
        elif operation=='d':
            if args[i] !=0:
                kwargs[operation] /=args[i]
        elif operation=='m':
            kwargs[operation] *=args[i]
            
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    for pair,value in sorted_dict:
        result.append(f'{pair}: {value:.1f}')
    
    return '\n'.join(result)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
