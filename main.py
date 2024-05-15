# This program is Calories Burnt Program which let the user to choose the activity and calculate the energy expenditure based on weight and activity
# Owner: May Thu Htun (T0333024)

import time
import os


# create a file to store work out history
def createFile():
    try:
        if (os.path.isfile("workout history.txt")):
            print("Let's GO!")
        else:
            print("Let's G0!")
            file = open("workout history.txt", "x")
            file.close()
    except:
        print("File cannot be written in your device.")


# checking unit and convert to kg if necessary
def checkUnit():
    loop = True
    while loop == True:
        unit = input("Is your weight in lbs or kg? ").lower()
        if unit == "lbs":
            # code modified from https://www.geeksforgeeks.org/precision-handling-python/
            # date accessed 30 October 2022
            weight = round(weight0 / 2.2, 3)  # converting weight from lbs to kg
            print("Your weight is", weight, "kg", "\n")
            loop = False
        elif unit == "kg":
            weight = weight0
            print("Your weight is", weight, "kg", "\n")
            loop = False
        else:
            loop = True

    # storing the weight
    file = open("workout history.txt", "a")
    file.write("\nYour weight: ")
    file.write(str(weight))
    file.write("kg")
    file.close()
    return weight


# providing the list of exercise and let the user choose
def exercise():
    print("Here is a list of exercises! ")
    activity = ["sitting", "bicycling", "cycling", "calisthenics", "dancing", "inactivity", "running", "rowing machine",
                "skiing", "stairmaster", "stairmaster stepmill", "swimming", "walking"]
    for x in activity:
        print(x, "")
        # code modified from https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/ (dhimanthakuria97, 2022)
        # date accessed 27 October 2022
        time.sleep(0.3)

    choice = input("Pick one of the activities you want to do: ").lower()
    while choice not in activity:
        choice = input("Pick one of the activities mentioned above ").lower()
    if choice == "sitting":
        met = sitting()
    elif choice == "bicycling":
        met = bicycling()
    elif choice == "cycling":
        met = cycling()
    elif choice == "calisthenics":
        met = calisthenics()
    elif choice == "dancing":
        met = dancing()
    elif choice == "inactivity":
        met = inactivity()
    elif choice == "running":
        met = running()
    elif choice == "rowing machine":
        met = rowing()
    elif choice == "skiing":
        print("\nThere are two types of skiing...")
        typeski = ["cross country", "downhill"]
        for x in typeski:
            print(x, "")
            time.sleep(0.2)
        typeskiC = input("Choose your preference type of skiing: ").lower()
        while typeskiC not in typeski:
            typeskiC = input("Your preference skiing type must be from the list above ").lower()
        if typeskiC == "cross country":
            met = crossCountry()

        elif typeskiC == "downhill":
            met = downHill()
    elif choice == "stairmaster":
        print("\nThere are two levels of PT...")
        pt = ["4000", "4400"]
        for x in pt:
            print(x, "")
            time.sleep(0.2)
        ptC = input("Choose your preference level of PT: ").lower()
        while ptC not in pt:
            ptC = input("Your preference skiing type must be from the list above ").lower()
        if ptC == "4000":
            met = pt4()
        elif ptC == "4400":
            met = pt44()
    elif choice == "stairmaster stepmill":
        met = pt7()
    elif choice == "swimming":
        met = swimming()
    elif choice == "walking":
        met = walking()

    # storing the met of the activity
    file = open("workout history.txt", "a")
    file.write(choice)
    file.write("\nIts met: ")
    file.write(str(met))
    file.close()
    calculation(met)


# to calculate the calories burnt
def calculation(met):
    cpm = 0.0175 * met * weight  # calculating the energy expenditure
    print("Your energy expenditure(calories burned per minute) is", cpm)

    loop = True
    # exception handling when the user input is not a positive number
    while loop == True:
        try:
            duration = float(input("\nEnter the duration of the activity in MINUTE: "))
            if duration > 0:
                loop = False
            else:
                print("Your duration must be a positive number!")
                loop = True
        except ValueError as e:
            print(e)
            print("Enter only numbers!!!! Your duration must be in MINUTE!!")
            loop = True

    tcpm = cpm * duration
    print("You have burned", tcpm, "calories in", duration, "minutes")
    totalcpm.append(tcpm)
    totalDuration.append(duration)
    total.append(cpm)
    # code modified from https://www.geeksforgeeks.org/sum-function-python/#:~:text=Python%20provides%20an%20inbuilt%20function,of%20numbers%20in%20the%20iterable.
    # Date accessed 3 November 2022
    print("\nYour total energy expenditure for your chosen activites:", sum(total), "calories per minute")
    print("You have burned a total of", sum(totalcpm), "calories in", sum(totalDuration), "minutes")

    # storing the energy expenditure
    file = open("workout history.txt", "a")
    file.write("\nEnergy expenditure: ")
    file.write(str(cpm))
    file.write("\nYour workout duration: ")
    file.write(str(duration))
    file.write("\nYour total energy expenditure: ")
    file.write(str(tcpm))
    file.close()


def sitting():
    met = 1.0
    print("There is no specific warm down guidance for this activity.")
    # storing the workout
    file = open("workout history.txt", "a")
    file.write("\nYour workout: ")
    file.close()
    return met


def bicycling():
    print("\nThis activity has 6 levels...")
    # code modified from https://youtu.be/wa1XcMSBWdA (Bro Code, 2020)
    # date accessed 5 November 2022
    bicycling = {"general": "4.0",
                 "light": "6.0",
                 "moderate": "8.0",
                 "vigorous": "10.0",
                 "very fast": "12.0",
                 "racing": "16.0"}
    for keys in bicycling:
        print(keys, "")
        time.sleep(0.2)
    bicycleC = input("Which one of the levels matches with yours___").lower()
    while bicycleC not in bicycling:
        bicycleC = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(bicycling[bicycleC])
        print("To warm down after bicycling, you could do 4 or 5 minutes of easy pedalling after your ride.")
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(bicycleC)
        file.close()
        return met


def cycling():
    print("\nThis activity has 5 levels...")
    cycling = {"very light": "3.0",
               "light": "5.5",
               "moderate": "7.0",
               "vigorous": "10.5",
               "very vigorous": "12.5"}
    for keys in cycling:
        print(keys, "")
        time.sleep(0.2)
    cyclingC = input("Which one of the levels matches with yours___").lower()
    while cyclingC not in cycling:
        cyclingC = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(cycling[cyclingC])
        print("To warm down after cycling, you could do 4 or 5 minutes of easy pedalling after your ride.")
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(cyclingC)
        file.close()
        return met


def calisthenics():
    print("\nThis activity has 2 levels...")
    calisthenics = {"moderate": "4.5",
                    "vigorous": "8.0"}
    for keys in calisthenics:
        print(keys, "")
        time.sleep(0.2)
    calisthenicsC = input("Which one of the levels matches with yours___").lower()
    while calisthenicsC not in calisthenics:
        calisthenicsC = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(calisthenics[calisthenicsC])
        print(
            "To warm down after calisthenics, it is the best to end with light jogging or walking to release tension and promote relaxation.")
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(calisthenicsC)
        file.close()
        return met


def dancing():
    print("\nThis activity has 3 levels...")
    dancing = {"aerobic": "6.0",
               "low impact aerobic": "5.0",
               "high impact aerobic": "7.0"}
    for keys in dancing:
        print(keys, "")
        time.sleep(0.2)
    dancingC = input("Which one of the levels matches with yours___").lower()
    while dancingC not in dancing:
        dancingC = input("Your level must be form the list mentioned above ").lower()
    else:
        met = float(dancing[dancingC])
        # code modified from https://www.w3schools.com/python/gloss_python_multi_line_strings.asp (w3schools, n.d.)
        # date accessed 29 October 2022
        print("""
To warm down after dancing, it is the best to end with some stretches.
Here are a few simple stretches that you could follow.
1. Kneeling Reach - kneel down on the floor and then put your chest to your knees with your arms outstretched in front of you.
2. Spinal Stretch - lay on your back and pull your knees to your chest by pulling your hands and arms behind your knees.
3. Seated Hamstring Stretch - put one leg out in front of you and bend the other so that the bottom of your foot is touching your leg flat 
                            and lean into the hamstring stretch.
4. Standing Quad Stretch - stand on one leg. Pick up the other and hold your foot behind you.
Hold these stretch positions for 30 seconds and repeat on the right side.
                """)
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(dancingC)
        file.close()
        return met


def inactivity():
    print("\nThis activity has 2 levels...")
    inactivity = {"sitting": "1.0",
                  "standing": "1.2"}
    for keys in inactivity:
        print(keys, "")
        time.sleep(0.2)
    inactivityC = input("Which one of the levels matches with your level___").lower()
    while inactivityC not in inactivity:
        inactivityC = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(inactivity[inactivityC])
        print("There is no specific warm down guidane for this activity.")
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(inactivityC)
        file.close()
        return met


def running():
    print("\nThis activity has 12 levels...")
    running = {"5mph": "8.0",
               "5.2mph": "9.0",
               "6mph": "10.0",
               "6.7mph": "11.0",
               "7mph": "11.5",
               "7.5mph": "12.5",
               "8mph": "13.5",
               "8.6mph": "14.0",
               "9mph": "15.0",
               "10mph": "16.0",
               "10.9mph": "18.0",
               "running stairs": "15.0"}
    for keys in running:
        print(keys, "")
        time.sleep(0.2)
    runningC = input("Which one of the levels matches with your level___").lower()
    while runningC not in running:
        runningC = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(running[runningC])
        print(
            "To warm down after running, decrease your pace to a very slow jog for 1-2 minutes, followed by light to brisk walking for 3-5 minutes.")
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(runningC)
        file.close()
        return met


def rowing():
    print("\nThis activity has 2 levels...")
    rowing = {"vigorous": "8.5",
              "very vigorous": "12.0"}
    for keys in rowing:
        print(keys, "")
        time.sleep(0.2)
    rowingC = input("Which one of the levels matches with your level___").lower()
    while rowingC not in rowing:
        rowingC = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(rowing[rowingC])
        print("""
To warm down after rowing, it is best to end with some stretches.
Here are a few stretches that you could follow.
1. Hip Flexor - left knee on the ground and right foot in front of you. Reach your left arm up as high as you can and
            both hips should be pointed forwards as you lean slightly forward into the stretch.
2. Piriformis - lay on your back with your knees bent, feet flat on the floor, head resting on the ground.
            Cross your right ankle over your left knee and pull your left leg toward you chest with both hands.
3. Hamstring - stand with your right foot two feet in front of your left foot, both hips pointing forward.
            Sit back into left leg and glute and let your right foot tip back onto right heel.
4. Lion - start with all fours. Reach your hands straight out in front of you on the floor while you push your hips back and up,
        resting your forehead on the floor.
5. Doorway - stand in a doorway with both forearms resting on either side of the opeing, arms at a 90-degree angle, 
            shoulder blades gently squeezing down and back.
6. Low Back Twist - start by laying on your back on the ground. Bring your right knee to your cheest. With your left hand, 
                bring your knee across your body, all the way to the ground if possible. Stretch your right arm out to the other side
                and turn your head to look at your right hand.
Hold these stretch positions for 30 seconds and repeat on the right side.
        """)
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(rowingC)
        file.close()
        return met


def crossCountry():
    print("This activity has 5 levels...")
    skiC = {"slow": "7.0",
            "moderate": "8.0",
            "vigorous": "9.0",
            "racing": "14.0",
            "uphill": "16.5"}
    for keys in skiC:
        print(keys)
        time.sleep(0.2)
    print("")
    skiCC = input("Which one of the levels matches with your level___").lower()
    while skiCC not in skiC:
        skiCC = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(skiC[skiCC])
        print("""
To warm down after skiing, hold your chest high, and raise your left hand into the air to open your chest, then reach down
and through your planted arm to twist your torso and stretch your back. Pause for a few seconds, then reverse the movement.
Continue until you feel the muscles release, then repeat on the other side. 
        """)
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(skiCC)
        file.close()
        return met


def downHill():
    print("\nThis activity has 3 levels...")
    skiD = {"light": "5.0",
            "moderate": "6.0",
            "vigorous": "8.0"}
    for keys in skiD:
        print(keys, "")
        time.sleep(0.2)
    skiDC = input("Which one of the levels matches with your level___").lower()
    while skiDC not in skiD:
        skiDC = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(skiD[skiDC])
        print("""
To warm down after skiing, hold your chest high, and raise your left hand into the air to open your chest, then reach down
and through your planted arm to twist your torso and stretch your back. Pause for a few seconds, then reverse the movement.
Continue until you feel the muscles release, then repeat on the other side. 
        """)
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(skiDC)
        file.close()
        return met


def pt4():
    print("This activity has 7 levels...")
    pt4 = {"2": "4.2",
           "4": "5.8",
           "6": "7.3",
           "8": "8.9",
           "10": "10.4",
           "12": "12.1",
           "14": "13.6"}
    for keys in pt4:
        print(keys, "")
        time.sleep(0.2)
    pt4C = input("Which one of the levels matches with your level___").lower()
    while pt4C not in pt4:
        pt4C = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(pt4[pt4C])
        print(
            "To warm down after stairmaster, reduce the intensity level and take another5-10 minutes of slow stair climbing.")
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(pt4C)
        file.close()
        return met


def pt44():
    print("\nThis activity has 7 levels...")
    pt44 = {"2": "4.4",
            "4": "6.5",
            "6": "8.6",
            "8": "10.7",
            "10": "12.7",
            "12": "14.8",
            "14": "16.9"}
    for keys in pt44:
        print(keys, "")
        time.sleep(0.2)
    pt44C = input("Which one of the levels matches with your level___").lower()
    while pt44C not in pt44:
        pt44C = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(pt44[pt44C])
        print(
            "To warm down after stairmaster, reduce the intensity level and take another5-10 minutes of slow stair climbing.")
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(pt44C)
        file.close()
        return met


def pt7():
    print("\nThis activity has 7 levels...")
    pt7 = {"2": "5.0",
           "4": "7.0",
           "6": "9.0",
           "8": "11.0",
           "10": "13.0",
           "12": "15.0",
           "14": "17.0"}
    for keys in pt7:
        print(keys, "")
        time.sleep(0.2)
    pt7C = input("Which one of the levels matches with your level___").lower()
    while pt7C not in pt7:
        pt7C = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(pt7[pt7C])
        print(
            "To warm down after stairmaster, reduce the intensity level and take another5-10 minutes of slow stair climbing.")
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(pt7C)
        file.close()
        return met


def swimming():
    print("\nThis activity has 4 levels...")
    swimming = {"leisurely": "6.0",
                "backstroke": "8.0",
                "breaststroke": "10.0",
                "butterfly": "11.0"}
    for keys in swimming:
        print(keys, "")
        time.sleep(0.2)
    swimmingC = input("Which one of the levels matches with yours___").lower()
    while swimmingC not in swimming:
        swimmingC = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(swimming[swimmingC])
        print(
            "To warm down after swimming, start of by gradually slowing down. After that, stretch your calf, foot muscles, arms and back.")
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(swimmingC)
        file.close()
        return met


def walking():
    print("\nThis activity has 6 levels...")
    walking = {"2mph": "2.5",
               "2.5mph": "3.0",
               "3mph": "3.5",
               "3.5-4mph": "4.0",
               "4.5mph": "4.5",
               "racewalking": "6.5"}
    for keys in walking:
        print(keys, "")
        time.sleep(0.2)
    walkingC = input("Which one of the levels matches with yours___").lower()
    while walkingC not in walking:
        walkingC = input("Your level must be from the list mentioned above ").lower()
    else:
        met = float(walking[walkingC])
        print("To warm down after walking, walk slowly for 5-10 minutes.")
        # storing the workout
        file = open("workout history.txt", "a")
        file.write("\nYour workout: ")
        file.write(walkingC)
        file.close()
        return met


# asking if the user want to do another activity and combine energy expenditure
def another():
    again = True
    while again == True:
        ex2 = input(
            "Do you want to combine with another activities to calculate total calories burned? yes/no: ").lower()
        if ex2 == "yes":
            exercise()
            again = True
        elif ex2 == "no":
            again = False
        else:
            again = True


# main
total = []
totalDuration = []
totalcpm = []
createFile()

# asking user weight and convert it to kg if the user input is lbs
# error handling if the user input is not number
loop = True
while loop == True:
    try:
        weight0 = float(input("Enter your weight: "))
        if weight0 > 0:
            weight = checkUnit()
            exercise()  # showing list for users to help them choose the activity
            another()
            loop = False
        else:
            print("Your entered weight is invalid!")
    except ValueError as e:
        print(e)
        print("Enter only numbers!!!")
        loop = True
