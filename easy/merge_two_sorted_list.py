def merge_two_sorted_list(ls1,ls2):
    sls=[]
    a=True
    while a:
        try:
            i=0
            j=0
            if ls1[j]>=ls2[i]:
                sls.append(ls2[i])
                ls2.remove(ls2[i])
                i+=1
            if ls1[j]<=ls2[i]:
                sls.append(ls2[j])
                ls1.remove(ls1[j])
                j+=1

            print(sls)
        except IndexError as e:
            print(e)
            a=False

    return sls
ls1=[1,1,2,2,3,4]
ls2=[1,1,2,2,3,4]

print(merge_two_sorted_list(ls1,ls2))
