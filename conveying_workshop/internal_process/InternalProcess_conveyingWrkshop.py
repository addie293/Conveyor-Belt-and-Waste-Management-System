import random
num=random.randint(0,1)
initiate_the_process=input("please type in START to initialise:")
case_sensitive_input1=initiate_the_process.lower()
if case_sensitive_input1=='start':
    print("checking the availability of green jack")
    if num==1:
        print("jack status is okay")
        print("now checking power button status")
        if num==1:
            print("the power button is ON")
            print("checking the tray status now")
            if num==1:
                print("pots are available, please choose the pot type")
                pot_size=int(input("please choose 0 for small pots and 1 for large pots:"))
                if pot_size==0:
                    pot_number=int(input("enter the number of small pots required:"))
                elif pot_size==1:
                    pot_number=int(input("enter the number of large pots required:"))
                speed=int(input("please set the speed of the conveyer between 1 and 10:"))
                if speed in range(1,11):
                    print("starting belt")
                    print("starting arm")
                    print("checking error")
                    print("checking air fault status")
                    if num==1:
                        print("air fault doesn't exist, all well")
                        print("checking axis controller fault")
                        if num==1:
                            print("no fault found in axis controller")
                            print("checking critical conveyer motor fault")
                        else:
                            print("fault exists, stopping now, cannot proceed forward")
                        if num==1:
                                print("no fault found in critical conveyer motor")
                                print("checking critical fault emergency stop")
                        else:
                            print("fault exists, stopping now, cannot proceed forward") 
                        if num==1:
                            print("no fault found in critical fault emergency")
                            print("everything is fine, no errors found")
                            print("initiating grab arm and sending")
                            print(pot_number,"is required")
                            pot_number=pot_number+1  
                            for i in range(1,pot_number):
                                print(i,"has arrived at the end of conveyer belt")
                            print("end of arm and belt")
                            print("checking information from filling, if it's finished or not")
                            print("status:filling is completed")
                        else:
                            print("fault exists, stopping now, cannot proceed forward")                                
                else:
                    print("invalid speed range has been selected")
            elif num==0:
                print("no pot stock availabel right now")
            else:
                print("fault exists, stopping now, cannot proceed forward")
        elif num==0:
            print("power button is off, right now")
    elif num==0:
        print("no jack available")
else:
    print("wrong initialisation method attempted")
                    