#  >>>>>>>>>>  1. Draw the line chart for the total number of steps on daily basis.
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('F:\ThirdSemesterMaterials\DSA-LAB\Lab-4\Archive\dailySteps_merged.csv' )
# print(df.dtypes)
# list1 = df['ActivityDay'].values.tolist()
# fig, ax = plt.subplots()
# list2 = df['StepTotal'].values.tolist()
# ax.plot(list1, list2 )
#
# plt.show()

# >>>>>  Draw the scatter chart for the total time in the bed
#
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('F:\ThirdSemesterMaterials\DSA-LAB\Lab-4\Archive\dailySteps_merged.csv' )
print(df.dtypes)
list1 = df['ActivityDay'].values.tolist()
fig, ax = plt.subplots()
list2 = df['StepTotal'].values.tolist()
ax.plot(list1, list2 )

plt.show()


#  >>>>>>>>>>>>>>>>>>>>>>>>Draw the bar chart for the daily distance covered
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('F:\ThirdSemesterMaterials\DSA-LAB\Lab-4\import matplotlib.pyplot as plt
# # import pandas as pd
# # df = pd.read_csv('F:\ThirdSemesterMaterials\DSA-LAB\Lab-4\Archive\sleepDay_merged.csv' )
# # print(df.dtypes)
# # list1 = df['TotalTimeInBed'].values.tolist()
# # fig, ax = plt.subplots()
# # # list2 = df['StepTotal'].values.tolist()
+# # # ax.scatter(list1, list2)
# # ax.scatter(list1)
# # plt.show()Archive\dailyActivity_merged.csv' )
# print(df.dtypes)
# list1 = df['ActivityDate'].values.tolist()
# fig, ax = plt.subplots()
# list2 = df['TotalDistance'].values.tolist()
# ax.bar(list1, list2)
#
# plt.show()
