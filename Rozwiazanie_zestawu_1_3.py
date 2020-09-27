import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

survey_results_schema_file_path = 'survey_results_schema.csv'
survey_results_schema_data = pd.read_csv(survey_results_schema_file_path)
#print (survey_results_schema_data)

survey_results_public_file_path = 'survey_results_public.csv'
survey_results_public_data = pd.read_csv(survey_results_public_file_path,
                            usecols=['Respondent','Age','WorkWeekHrs','Gender'],
                            index_col='Respondent')
survey_results_public_data.to_csv(survey_results_public_file_path)                           
#print (survey_results_public_data['Gender'])
survey_results_public_data.dropna(inplace=True)
survey_results_public_data = survey_results_public_data.astype({ 'Age': 'int64', 'WorkWeekHrs': 'int64' },copy=False)
#print (survey_results_public_data)
survey_results_public_data = survey_results_public_data[(survey_results_public_data['Age'].between(16,70,inclusive = True)) & (survey_results_public_data['WorkWeekHrs'] <=84)]

plt.plot(survey_results_public_data['Age'], survey_results_public_data['WorkWeekHrs'], 'ro', markersize=0.1)
plt.title('Working hours in accorance to the age')
plt.xlabel('Age')
plt.ylabel('WorkWeekHrs')
plt.show()

survey_men = survey_results_public_data[(survey_results_public_data['Gender'] == 'Man')]
plt.plot(survey_men['Age'], survey_men['WorkWeekHrs'], 'ro', markersize=0.1)
plt.title("Working hours in accordance to the age - MEN")
plt.xlabel('Age')
plt.ylabel('WorkWeekHrs')
plt.show()

survey_women = survey_results_public_data[(survey_results_public_data['Gender'] == 'Woman')]
plt.plot(survey_women['Age'], survey_women['WorkWeekHrs'], 'ro', markersize=0.1)
plt.title("Working hours in accordance to the age - WOMEN")
plt.xlabel('Age')
plt.ylabel('WorkWeekHrs')
plt.show()