############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

diagnosis = 1
yes = 'yes'
no = 'no'
while(diagnosis == 1):
    print 'what is your temp?'
    temp = int(raw_input())
    print 'have you been sick in the last 24 house?'
    sickLast = raw_input()
    print 'have you recently traveled to west africa?'
    travel = raw_input()
    if temp < 100:
        diagnosis = 0
    if temp < 106:
        if temp > 99:
            if sickLast == no:
                diagnosis = 0
    if travel == yes:
        if temp > 99:
            diagnosis = 1
        if sickLast == yes:
            diagnosis = 1    
    if diagnosis == 1:
        print 'You have Ebola!'
print 'You\'re Ebola free!'
