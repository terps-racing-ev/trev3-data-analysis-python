import os

first_line = True
state_index = 0
apps_index = 0
bse_index = 0
torque_index = 0

f = os.listdir()

for file in f:
    if "csv" in file:
        first_line = True
        for line in open(file):
            if first_line:
                line_arr = line.split(",")
                i = 0

                for item in line_arr:
                    if "\"APPS\"|" in item:
                        apps_index = i
                    elif "\"Front_BP\"|" in item:
                        bse_index = i
                    elif "\"VCU_State\"|" in item:
                        state_index = i
                    elif "\"TorqueCmd\"|" in item:
                        torque_index = i
                    i += 1

                

                first_line = False
                
            else:
                line_arr = line.split(",")

                state = line_arr[state_index]
                bse = line_arr[bse_index]
                apps = line_arr[apps_index]
                torque = line_arr[torque_index]

                if state != "" and bse != "" and apps != "" and torque != "":
                    state = float(state)
                    bse = float(bse)
                    apps = float(apps)
                    torque = float(torque)

                    if state == 3.0:
                        print(file)
                        print("State " + str(state))
                        print("APPS " + str(apps))
                        print("BSE " + str(bse))
                        print("torque " + str(torque))
                        print("\n")
                        break



  
