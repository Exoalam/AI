def getMembershipService(service):
    degree = {}
    if service < 0 or service > 1:
        degree["p"] = 0
        degree["g"] = 0
        degree["e"] = 0
    
    elif service <=.2:
        degree["p"] = 1
        degree["g"] = 0
        degree["e"] = 0

    
    elif service >.2 and service <=.4:
        degree["p"] = float((.4-service)*(1/(.4-.2)))
        degree["g"] = float((service-.20)*1.0/(.40-.20))
        degree["e"] = 0
    elif service >.4 and service <=.6:
        degree["p"] = 0
        degree["g"] = 1
        degree["e"] = 0
    elif service >.6 and service <=.8:
        degree["g"] = float((.8-service)*(1/(.8-.6)))
        degree["e"] = float((service-.6)*1.0/(.80-.60))
        degree["p"] = 0    
    elif service >= .80 and service <= 1:
        degree["p"] = 0
        degree["g"] = 0
        degree["e"] = 1
    
        
    return degree

def getMembershipFood(food):
    degree = {}
    
    if food < 0 or food > 1:
        degree["b"] = 0
        degree["d"] = 0
    
    elif food <=.4:
        degree["b"] = 1
        degree["d"] = 0
    
    elif food>.4 and food<.8:
        degree["b"] = float((.8-food)*(1/(.8-.4)))
        degree["d"] = float((food-.40)*1.0/(.80-.40))
      
    elif food >= .80 and food <= 1:
        
        degree["b"] = 0
        degree["d"] = 1
        
    return degree

def crispInput(val,base):
    return val* 1.0/base
   
def ruleEvalationAssessment(fuzzyservice,fuzzyfood):
    cheap=max(fuzzyservice["p"],fuzzyfood["b"])
    average=(fuzzyservice["g"])
    generous=max(fuzzyservice["e"],fuzzyfood["d"])
    
    return cheap,average,generous
   
        
def defuzzificationAssessment(cheap,average,generous ):
    cog=0 
    i=0
    s=0
    while(i<=(cheap+average+generous)*1.0):
        an=0
        if(i<=cheap):
            an=cheap
        elif(i>cheap and i<=cheap+average):
            an=average
            
        else:
            an=generous
        cog+=an*i
        s+=an
        i+=.20
    #print(cog)    
    return cog*1.0//s

#input
ser, foodd = 6, 3

s=crispInput(ser,10)
f=crispInput(foodd,10)

fuzzyservice=getMembershipService(s)
fuzzyfood=getMembershipFood(f)


cheap,average,generous = ruleEvalationAssessment(fuzzyservice,fuzzyfood)
#print(cheap)


conAssessment = defuzzificationAssessment(cheap,average,generous )
print("Fuzzified Continuous Assessment: ",conAssessment)