import pandas as pd
import matplotlib.pyplot as plt
quiz=pd.read_csv('Quiz.csv')
homework=pd.read_csv('Homework.csv')
exam=pd.read_csv('Exam.csv')
final_data=pd.merge(quiz,homework,on=['Rollno','Name'],how='outer')
final_data=pd.merge(final_data,exam,on=['Rollno','Name'],how='outer')
final_data=final_data.fillna(0)
quiz_wt=0.3
homework_wt=0.3
exam_wt=0.4
final_data['Quiz Score']=(final_data['Quiz1']+final_data['Quiz2'])/(final_data['Max Score1']+final_data['Max Score2'])*quiz_wt
final_data['Homework Score']=(final_data['HW1']+final_data['HW2'])/(final_data['MaxScoreHW1']+final_data['MaxScoreHW2'])*homework_wt
final_data['Exam Score']=(final_data['Test1']+final_data['Test2'])/50*exam_wt
final_data['Final Score']=final_data['Quiz Score']+final_data['Homework Score']+final_data['Exam Score']
final_data.to_csv('Final_Grade.csv',index=False)
df=pd.read_csv('Final_Grade.csv')
kind='bar'
df.plot(kind=kind)
plt.show()