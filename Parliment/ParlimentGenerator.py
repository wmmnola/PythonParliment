__author__ = 'Wade'
import random
ParlimentMembers = []
GreenParty = []
LiberalDemocrats = []
ToryParty = []
ConservativeParty = []
SocialistParty = []
RadicalSocialists = []
LabourParty = []
UnionOfFacists = []
RepublicanFront = []
LibertarianParty = []
Independents = []
def election(seats):
    for x in range(seats):

        #         Social Policy        Economic Policy          Democracy
        views = [random.randint(0,100),random.randint(0,100),random.randint(0,100)]
        #       0 full traditionlist     0 Anarcho Capitalist   0 All power to one person
        #       100 Committed to overhaul Communistic ideas     Direct Democracy
        ParlimentMembers.append(views)
    return ParlimentMembers
def partyCalc(x,s1,s2,e1,e2,p1,p2):
    if ParlimentMembers[x][0] in range(s1,s2):
        if ParlimentMembers[x][1] in range(e1,e2):
            if ParlimentMembers[x][2] in range(p1,p2):
                return True

    else:
        return False
def partyPlacement():
    for x in range(len(ParlimentMembers)):
        if partyCalc(x,70,100,50,90,75,100): GreenParty.append(ParlimentMembers[x])
        elif partyCalc(x,40,60,30,60,75,90): LiberalDemocrats.append(ParlimentMembers[x])
        elif partyCalc(x,0,40,50,75,10,40): ToryParty.append(ParlimentMembers[x])
        elif partyCalc(x,20,80,10,60,20,80): ConservativeParty.append(ParlimentMembers[x])
        elif partyCalc(x,75,100,60,90,60,90): SocialistParty.append(ParlimentMembers[x])
        elif partyCalc(x,60,100,80,100,0,100): RadicalSocialists.append(ParlimentMembers[x])
        elif partyCalc(x,20,90,40,80,30,80): LabourParty.append(ParlimentMembers[x])
        elif partyCalc(x,0,100,50,100,0,15): UnionOfFacists.append(ParlimentMembers[x])
        elif partyCalc(x,0,100,0,100,60,100): RepublicanFront.append(ParlimentMembers[x])
        elif partyCalc (x,40,80,0,30,60,100): LibertarianParty.append(ParlimentMembers[x])
        else: Independents.append(ParlimentMembers[x])
election(100)
partyPlacement()

print("Green Party has "+str(len(GreenParty))+" Seats")
print("The Liberal Democrats have "+str(len(LiberalDemocrats))+" Seats")
print("The Tory Party has "+str(len(ToryParty))+ " Seats")
print("The Conservative party has "+ str(len(ConservativeParty))+" Seats")
print("The Socialist party has "+str(len(SocialistParty))+ " seats")
print("The Radical Socialists have "+str(len(RadicalSocialists))+ " seats")
print("The Labour Party has "+str(len(LabourParty))+" seats")
print("The Union of Facists has "+str(len(UnionOfFacists))+" seats")
print("The Republican Front have "+ str(len(RepublicanFront))+ " seats")
print("The Liberatarian Party has "+str(len(LibertarianParty)) + " seats")
print("There are "+str(len(Independents))+" Independent members")

