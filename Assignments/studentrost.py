roslistfname = []
roslistlname = []
roslistgrade = []
onestep = input("Do you want to add a student?[yes/no]: ")
while onestep == "yes":
    studfname = input("Enter the student first name: ")
    studlname = input("Enter the student last name: ")
    studgrade = input("Enter the student grade:")
    roslistfname.append(studfname)
    roslistlname.append(studlname)
    roslistgrade.append(studgrade)
    onestep = input("Do you want to add another student? [yes/no]: ")
    if onestep == "no":
        for i in range(len(roslistfname)):
            print(roslistfname[i] +" "+ roslistlname[i] +" in grade "+ roslistgrade[i])
            
    
    