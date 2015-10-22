__author__ = 'Wade'
import random
ParlimentMembers = []

def election(seats):
    for x in range(seats):
        #         Social Policy        Economic Policy          Democracy
        views = [random.randint(0,100),random.randint(0,100),random.randint(0,100)]
        #       0 full traditionlist     0 Anarcho Capitalist   0 All power to one person
        #       100 Committed to overhaul Communistic ideas     Direct Democracy
        ParlimentMembers[x] = views
        return ParlimentMembers

def partyGenerating():
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
    for x in range(len(ParlimentMembers)):
        if ParlimentMembers[x] == {range(0,20),range(55,75), range(0,30)}: ToryParty.append(ParlimentMembers[x])
        if ParlimentMembers[x] == {range(60,100),range(65,90), range(60,100)}: GreenParty.append(ParlimentMembers[x])
        if ParlimentMembers[x] == {range(25,75),range(40,60), range(70,85)}: LiberalDemocrats.append(ParlimentMembers[x])
        if ParlimentMembers[x] == {range(0,20),range(55,25), range(0,40)}: ConservativeParty.append(ParlimentMembers[x])
        if ParlimentMembers[x] == {range(0,20),range(55,25), range(0,40)}: SocialistParty.append(ParlimentMembers[x])
        if ParlimentMembers[x] == {range(0,20),range(55,25), range(0,40)}: RadicalSocialists.append(ParlimentMembers[x])
        if ParlimentMembers[x] == {range(0,20),range(55,25), range(0,40)}: LabourParty.append(ParlimentMembers[x])
        if ParlimentMembers[x] == {range(0,20),range(55,25), range(0,40)}: UnionOfFacists.append(ParlimentMembers[x])
        if ParlimentMembers[x] == {range(0,20),range(55,25), range(0,40)}: RepublicanFront.append(ParlimentMembers[x])
        if ParlimentMembers[x] == {range(0,20),range(55,25), range(0,40)}: LibertarianParty.append(ParlimentMembers[x])
        else: Independents.append(ParlimentMembers)

election(1)
print(ParlimentMembers[0])