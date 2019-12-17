import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# VARIABLES
featureRange = 100      # Amount of features
timeForFeature = 60     # Amount of time for a feature to be developed
testScriptTime = 30     # Amount of time for a test script for that feature to be develope
manualTestTime = 2      # Amoutn of time for a manual test to take

# WITH TESTS
# Once the feature test has been developed a manual test is done to verify correct funtionality
# After that a test script is written to automate manual test.
withTests = []
totalTimeWithTests = 0
withTests.append(totalTimeWithTests)

x = 0
while x < featureRange:
    total = timeForFeature + testScriptTime + manualTestTime
    totalTimeWithTests += total
    withTests.append(totalTimeWithTests)
    x += 1
    
# WITHOUT TESTS
# Once the feature test has been developed a manual test is done to verify correct funtionality
# Then every time a new feature is added that feature is tested and all previous features should be tested
# to ensure they still function correctly after the changes.
withoutTests = []
witoutTestsTime = 0
withoutTests.append(witoutTestsTime)

i = 0
while i < featureRange:
    test = manualTestTime * i
    total = timeForFeature + test
    witoutTestsTime += total
    withoutTests.append(witoutTestsTime)
    i += 1
    
# PLOTTING
fig, ax = plt.subplots()
ax.plot(withTests,range(0, featureRange + 1), withoutTests, range(0, featureRange + 1))

# LEGEND
ax.set(xlabel='Time in mintures', ylabel='Feature amount', title='Comparison with and without testing based on Feature amount')
ax.legend()
ax.legend(['With Tests', 'Without tests'])
ax.grid()

# SAVING PNG AND RENDERING
fig.savefig("test.png")
plt.show()