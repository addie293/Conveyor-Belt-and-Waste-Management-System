import random
num=random.randint(0,1)
initiate_the_process=input("please type in START to initialise:")
case_sensitive_input=initiate_the_process.lower()
while case_sensitive_input!='start':
    try_again=int(input("enter 0 to skip and 1 to try again:"))
    if try_again==1:
        initiate_the_process=input("please type in START to initialise:")
        case_sensitive_input=initiate_the_process.lower()
    else:
        print("goodbye")
        break
if case_sensitive_input=='start':
    print("checking the availability of green jack")
    while num==0:
        print("no jack available")
        try_again=int(input("enter 0 to skip and 1 to try again:"))
        if try_again==1:
            print("checking the availability of green jack")
            num=1
        else:
            print("goodbye")
    if num==1:
        print("jack status is okay")
        print("now checking power button status")
        while num==0:
            print("power button is off, right now")
            try_again=int(input("enter 0 to skip and 1 to try again:"))
            if try_again==1:
                print("now checking power button status")
            else:
                print("goodbye")
                break
        if num==1:
            print("the power button is ON")
            print("checking the tray status now")
            while num==0:
                print("no pot stock available right now")
                try_again=int(input("enter 0 to skip and 1 to try again:"))
                if try_again==1:
                    print("checking the tray status now")
                else:
                    print("goodbye")
                    break
            if num==1:
                print("pots are available, please choose the pot type")
                pot_size=int(input("please choose 0 for small pots and 1 for large pots:"))
                if pot_size==0:
                    pot_number=int(input("enter the number of small pots required:"))
                else:
                    pot_number=int(input("enter the number of large pots required:"))
                speed=int(input("please set the speed of the conveyer between 1 and 10:"))
                if speed in range(1,11):
                    
                    print("starting belt")
                    print("starting arm")
                    print("checking error")
                    print("checking air fault status")
                    print("air fault doesn't exist, all well")
                    print("checking axis controller fault")
                    while num==0:
                        print("fault exists in axis controller, stopping now, cannot proceed forward")
                        try_again=int(input("enter 0 to skip and 1 to try again:"))
                        if try_again==1:
                            print("checking axis controller fault")
                        else:
                            print("goodbye")
                            break
                    if num==1:
                            print("no fault found in axis controller")
                            print("checking critical conveyer motor fault")
                            while num==0:
                                print("fault exists in critical conveyer motor fault,stopping now")
                                try_again=int(input("enter 0 to skip and 1 to try again:"))
                                if try_again==1:
                                    print("checking critical conveyer motor fault")
                                else:
                                    print("goodbye")
                                    break
                            if num==1:
                                print("no fault found in critical conveyer motor")
                                print("checking critical fault emergency stop")
                                while num==0:
                                    print("fault exists in critical fault emergency stop, stopping now, cannot proceed forward")
                                    try_again=int(input("enter 0 to skip and 1 to try again:"))
                                    if try_again==1:
                                        print("checking critical conveyer motor fault")
                                    else:
                                        print("goodbye")
                                        break
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
                    print("invalid speed range has been selected")
