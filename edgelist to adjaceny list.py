def traverse(edge):
    keys=[]
    ad_list={}
    values=[]
    for i in edge:
        if i[0] not in keys:
            keys.append(i[0])
        if i[1] not in keys:
            keys.append(i[1])
    keys.sort()
    for j in keys:
        
        for k in edge:
            if j==k[0]:
                if j in ad_list:
                    ad_list[j]=ad_list[j]+[k[1]]
                elif j not in ad_list:
                    ad_list.update({j:[]})
                    ad_list[j]=ad_list[j]+[k[1]]
                
                if k[1] not in ad_list:
                  
                  ad_list.update({k[1]:[]})
                  ad_list[k[1]]=ad_list[k[1]]+[j]
                else:
                    
                    ad_list[k[1]]=ad_list[k[1]]+[j]
    return ad_list
            
                
    
   
     
            
    
    
