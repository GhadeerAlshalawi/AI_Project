
class Node():
    
    def __init__(self,name,H): 
        
        self.name=name
        self.H=H
        
        self.adjcent=[]
        self.cost=0
        self.parent=None
        

    
    def add_adjcent(self, adj):#add adjacent
        self.adjcent.append(adj)
    
    def my_adjcents(self): #return all node's adjacent
        return self.adjcent
       
    
    
    def leng(self):
        return len(self.adjcent)

    def F_funcation(self):
       
           return self.cost+self.H
    
    
    def print_adj(self):
        print('curent Node and the avaliable path from it  ')
        for x in self.adjcent:
            print('from ',x.parent,'to',x.name,'with cost:',x.cost)
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
       return self.name


class adj():
    
 def __init__(self,name,parent,cost,H):
     self.name=name
     self.parent=parent
     self.cost=cost
     self.H=H
    


 def F_funcation(self):
    
        return self.cost+self.H

 def my_adjcents(self): #return all node's adjacent
        return self.name.my_adjcents()
 def leng(self):
        return len(self.name.adjcent)
 def __repr__(self):
        return self.name
    
 def __str__(self):
       return self.name


class graph():
 verteces=[]
 start=None
 goal=None
 
 def add_ver(self,node):
     self.verteces.append(node)
    

 def print_ver(self):
     i=0
     for vertex in self.verteces:
         print(' ', vertex.name)
         print()
         if(i==9):
            print("the second graph with the second huristic")
         elif (i==19):
          print("the third graph with the third huristic")

         i=i+1

 def retVert(self):
    return self.verteces
    
 



#Define the first graph with H1=Which calculates the distance of each node from Goal as huristic
gra1=graph()


CVDC =  Node('CVDC',7) 
Home1 = Node('Home1',5)
Home2 = Node('Home2',6)
Home3 = Node('Home3',4)
Home4 = Node('Home4',7)
Home5 = Node('Home5',1)
Home6= Node('Home6',4)
Home7= Node('Home7',3)
Home8= Node('Home8',2)
Home9= Node('Home9',0)

gra1.add_ver(CVDC)
gra1.add_ver(Home1)
gra1.add_ver(Home2)
gra1.add_ver(Home3)
gra1.add_ver(Home4)
gra1.add_ver(Home5)
gra1.add_ver(Home6)
gra1.add_ver(Home7)
gra1.add_ver(Home8)
gra1.add_ver(Home9)


#Connecting each node with its adjacents and determine the cost between them

#it's add the node's adjacent ,and determain the node as it's adjacent's parent, the cost between them ,the adjacent huristic
CVDC.add_adjcent(adj(Home1,CVDC,1,5)) 
CVDC.add_adjcent(adj(Home2,CVDC, 1,6))



Home1.add_adjcent(adj(Home3,Home1,2,4))

Home2.add_adjcent(adj(Home3,Home2,2,4))
Home2.add_adjcent(adj(Home4,Home2,2,7))

Home3.add_adjcent(adj(Home2,Home3,2,6))
Home3.add_adjcent(adj(Home5,Home3,3,1))

Home4.add_adjcent(adj(Home6,Home4,3,4))

Home5.add_adjcent(adj(Home9,Home5,4,0))

Home6.add_adjcent(adj(Home7,Home6,4,3))


Home7.add_adjcent(adj(Home8,Home7,5,2))

Home8.add_adjcent(adj(Home9,Home8,6,0))

#detrmine the start state for the first graph
gra1.start= CVDC

#determine the goal state for the first graph
gra1.goal = Home9

gra2=graph()

#Define the second graph with H2=Which use the manhatan distance as hurstic
cVDC =  Node('cVDC',4) 
home1 = Node('home1',3)
home2 = Node('home2',3)
home3 = Node('home3',2)
home4 = Node('home4',4)
home5 = Node('home5',1)
home6= Node('home6',3)
home7= Node('home7',2)
home8= Node('home8',1)
home9= Node('home9',0)

gra2.add_ver(cVDC)
gra2.add_ver(home1)
gra2.add_ver(home2)
gra2.add_ver(home3)
gra2.add_ver(home4)
gra2.add_ver(home5)
gra2.add_ver(home6)
gra2.add_ver(home7)
gra2.add_ver(home8)
gra2.add_ver(home9)





#Connecting each node with its adjacent and determine the cost between them


#it's add the node's adjacent ,and determain the node as it's adjacent's parent, the cost between them ,the adjacent huristic
cVDC.add_adjcent(adj(home1,cVDC,1,3)) 
cVDC.add_adjcent(adj(home2,cVDC, 1,3))



home1.add_adjcent(adj(home3,home1,2,2))

home2.add_adjcent(adj(home3,home2,2,2))
home2.add_adjcent(adj(home4,home2,2,4))

home3.add_adjcent(adj(home2,home3,2,3))
home3.add_adjcent(adj(home5,home3,3,1))

home4.add_adjcent(adj(home6,home4,3,3))

home5.add_adjcent(adj(home9,home5,4,0))

home6.add_adjcent(adj(home7,home6,4,2))


home7.add_adjcent(adj(home8,home7,5,1))

home8.add_adjcent(adj(home9,home8,6,0))

#detrmine the start state 
gra2.start= cVDC

#determine the goal state
gra2.goal = home9

#Define the third graph with H3=Which use The house temperature as a huristic

gra3=graph()

CvDC =  Node('CvDC',50-40) 
HomE1 = Node('HomE1',50-41)
HomE2 = Node('HomE2',50-42)
HomE3 = Node('HomE3',50-30)
HomE4 = Node('HomE4',50-45)
HomE5 = Node('HomE5',50-30)
HomE6= Node('HomE6',50-46)
HomE7= Node('HomE7',50-47)
HomE8= Node('HomE8',50-49)
HomE9= Node('HomE9',50-50)

gra3.add_ver(CvDC)
gra3.add_ver(HomE1)
gra3.add_ver(HomE2)
gra3.add_ver(HomE3)
gra3.add_ver(HomE4)
gra3.add_ver(HomE5)
gra3.add_ver(HomE6)
gra3.add_ver(HomE7)
gra3.add_ver(HomE8)
gra3.add_ver(HomE9)




#Connecting each node with its adjacent and determine the cost between them


#it's add the node's adjacent ,and determain the node as it's adjacent's parent, the cost between them ,the adjacent huristic
CvDC.add_adjcent(adj(HomE1,CvDC,1,50-41)) 
CvDC.add_adjcent(adj(HomE2,CvDC, 1,50-42))

HomE1.add_adjcent(adj(HomE3,HomE1,2,50-30))

HomE2.add_adjcent(adj(HomE3,HomE2,2,50-30))
HomE2.add_adjcent(adj(HomE4,HomE2,2,50-45))

HomE3.add_adjcent(adj(HomE2,HomE3,2,50-42))
HomE3.add_adjcent(adj(HomE5,HomE3,3,50-30))

HomE4.add_adjcent(adj(HomE6,HomE4,3,50-46))

HomE5.add_adjcent(adj(HomE9,HomE5,4,50-50))

HomE6.add_adjcent(adj(HomE7,HomE6,4,50-47))

HomE7.add_adjcent(adj(HomE8,HomE7,5,50-49))

HomE8.add_adjcent(adj(HomE9,HomE8,6,50-50))

#detrmine the start state for the third graph
gra3.start= CvDC

#determine the goal state for the third graph
gra3.goal = HomE9


print("the state space for the three graphs :")

gra3.print_ver()


def inOpenList(node): #check if the state in open list
        
        for x in openlist:
            if x.name==node.name:
                return True
        else:
            False
        
def inCloseList(node): #check if the state in closelist
        
        for x in closelist:
            if x.name==node.name:
                return True
        else:
            False


    


openlist=[] #list for the 
closelist=[] #list for the expanded node 

 
def minm(): #to determain the lowest f(x) in openlist
    mine=[]
    for x in openlist:
       
        mine.append(x.F_funcation())
    
    return min(mine)


def Astar(graph):
    
    intail_state=graph.start #defind the problem initial state
    goal_state=graph.goal     #defind the problrm goal state
    
    openlist.append(intail_state) #add the initial state to the open list to expand it

    while(len(openlist)!=0): #start the search
        
        for x in openlist: #search for the lowest node in the openlist
             min=minm()    
             if( x.F_funcation()==min):
                
                i=openlist.index(x)
                
        current=openlist.pop(i) #pick the lowset as the current node
        
        
        if(str(current.name) == str(goal_state)): #goal test 
            break
        
        else:
        
            for suc in current.my_adjcents(): #check the node adjacents
                
                suc.cost=suc.cost+current.cost #update the adjacent's cost with the cost from the inital state to it
                
                if (inCloseList(suc)): #if the adjacent in close list ignore it
                   continue
                elif(inOpenList(suc)): #if the adjacent in open list ignore it
                    continue 
  
                else: #otherwise add it to the open list
                    openlist.append(suc)
                   
        closelist.append(current) # add the current to the close list the node after expaned it
    print("the expanded nodes is ")
    for v in closelist:
        print(v.name)

    print("----------------")
     #after find the goal find the path 
    find_The_path(closelist,current)
   
    

def find_The_path(closelist,current): #to find the path that the agent took it to find the goal
    path=[] 
    closelist.reverse()
    goal_path=current.cost 
    while(current.parent!=None):
        
        for x in closelist:
            
            if(str(x.name)==str(current.parent.name)):
             
             path.append(x)
             
             current=x
    path.reverse()
    print("this is the paht: ")
    for x in path:
        print(x.name)
    print("the path cost a = ",goal_path)
    
   



Astar(gra1) #graph1 with first huristic

closelist.clear()
openlist.clear()

Astar(gra2) #graph2 with second huristic

closelist.clear()
openlist.clear()




Astar(gra3) #graph3 with third huristic


#test another example
gra4=graph()
gra5=graph()
gra6=graph()

closelist.clear()
openlist.clear()

c=Node("c",5)
h1=Node("h1",2)
h2=Node("h2",1)
h3=Node("h3",3)
h4=Node("h4",0)

gra4.add_ver(c)
gra4.add_ver(h1)
gra4.add_ver(h2)
gra4.add_ver(h3)
gra4.add_ver(h4)

c.add_adjcent(adj(h1,c,3,2))

c.add_adjcent(adj(h3,c,6,3))

h1.add_adjcent(adj(h2,h1,2,1))

h2.add_adjcent(adj(h4,h2,1,0))

h3.add_adjcent(adj(h4,h3,4,0))

gra4.start=c
gra4.goal=h4

Astar(gra4)



closelist.clear()
openlist.clear()

C=Node("C",50-40)
H1=Node("H1",50-45)
H2=Node("H2",50-46)
H3=Node("H3",50-47)
H4=Node("H4",50-50)

gra5.add_ver(C)
gra5.add_ver(H1)
gra5.add_ver(H2)
gra5.add_ver(H3)
gra5.add_ver(H4)

C.add_adjcent(adj(H1,C,3,50-45))

C.add_adjcent(adj(H3,C,9,50-47))

H1.add_adjcent(adj(H2,H1,6,50-46))

H2.add_adjcent(adj(H4,H2,3,50-50))

H3.add_adjcent(adj(H4,H3,5,50-50))

gra5.start=C
gra5.goal=H4

Astar(gra5)


closelist.clear()
openlist.clear()

Cc=Node("Cc",2)
Hh1=Node("Hh1",1)
Hh2=Node("Hh2",2)
Hh3=Node("Hh3",1)
Hh4=Node("Hh4",0)

gra6.add_ver(Cc)
gra6.add_ver(Hh1)
gra6.add_ver(Hh2)
gra6.add_ver(Hh3)
gra6.add_ver(Hh4)

Cc.add_adjcent(adj(Hh1,Cc,1,1))

Cc.add_adjcent(adj(Hh3,Cc,1,1))

Hh1.add_adjcent(adj(Hh2,Hh1,2,2))

Hh3.add_adjcent(adj(Hh4,Hh3,2,0))


gra6.start=Cc
gra6.goal=Hh4

Astar(gra6)

