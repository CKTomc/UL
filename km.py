global data
<init data>

def kmeans(k):
    
    nochange=False
    
    #init means
    means={}
    for i in range(k):
       m=randrange(len(data))
       while means.get(m)!=None:
           m=randrange(len(data))
       means[data[m]]=[]    
   
    while nochange==False: 

      #assigning points  
      for i in range (len(data)):
            best=100000
            for m in means.keys():
                dist=distance(data[i],m)          
                if dist<best:
                    best=dist
                    mean=m                            
            means[mean].append(i)

      #calculate means
      newmeans={}
      for m,objects in means:
          mean=calc_mean(objects)            
          newmeans[mean]=[]
      if newmeans.keys()!=means.keys():
         means=newmeans
      else:
          nochange=True
               
    clusters={}
    for m,objects in means:
        cluster=[data[o] for o in objects]
        clusters[m]=cluster   
    
    return clusters 
