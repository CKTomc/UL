global data
global output_ind # output index
global path
<initialize data>
<initialize the output index>
<initialize path>

def kmedoids(k):
    
    nochange=False
    
    #init medoids
    medoids={}
    meds={}
    for i in range(k):
       m=randrange(len(data))
       while medoids.get((m,0))!=None:
           m=randrange(len(data))
       medoids[(m,0)]=[]
       meds[m]=0      
       
    while nochange==False: 
            #assigning points                                 
            for i,elm in enumerate(data):
                if meds.get(i)!=None:
                   continue 
                else:
                    best=100000
                    for m in medoids.keys():
                        dist=distance(elm,m)          
                        if dist<best:
                            best=dist
                            medoid=m                            
                    
                    medoids[medoid].append(i)
                    medoids[(medoid[0],medoid[1]+best)]=medoids.pop(medoid)

            #check for a new config
            changes=[]
            for m in medoids.keys():
                cost=m[1]
                change=()
                x=()
                for o in medoids[m]: 
                    cost2=0
                    for q in medoids[m]:
                        if q!=o:                
                           cost2+=distance(data[o],data[q])
                    cost2+=distance(data[o],data[m[0]])                    
                    if cost2<cost:
                       cost=cost2
                       x=(o,cost2)
                if x!=():
                    change=(m,x)
                    changes.append(change)           
            if changes!=[]:
               for c in changes:
                   medoids[c[1]]=medoids.pop(c[0])
                   del(meds[c[0][0]])
                   meds[c[1][0]]=0
               cop=copy.deepcopy(medoids)
               for m in cop.keys():
                   medoids[m]=[]  
                   medoids[(m[0],0)]=medoids.pop(m)              
            else:
                nochange=True
                  
        
    clusters={}
    for m, objects in medoids:
        cluster=[data[o] for o in objects]
        clusters[data[m[0]]]=cluster   
    
    return clusters
