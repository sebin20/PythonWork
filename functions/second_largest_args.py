def second_largest(*args):
    # leng=len(args)
    # minimun=min(args)
    # maximum=max(args)
    # second_lar=0
    # for i in range(len(args)):
    #     if args[i]>minimun and args[i]< maximum:
    #         second_lar=args[i]
    #         minimun=args[i]
    # print(second_lar)
    sorted_numb=sorted(args,reverse=True)
    print(sorted_numb[1])
    
    
second_largest(10,200,30,40,34)