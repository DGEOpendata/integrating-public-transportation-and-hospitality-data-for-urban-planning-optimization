python
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
transportation_data = pd.read_csv('Abu_Dhabi_Public_Transportation_Usage_Statistics.csv')
hotel_data = pd.read_excel('Abu_Dhabi_Hotels_Open_Datasets1.xlsx')

# Merge datasets on a common key, e.g., date
merged_data = pd.merge(transportation_data, hotel_data, on='date')

# Analyze peak ridership against hotel occupancy
plt.figure(figsize=(12, 6))
plt.plot(merged_data['date'], merged_data['peak_ridership'], label='Peak Ridership')
plt.plot(merged_data['date'], merged_data['occupancy_rate'], label='Hotel Occupancy Rate')
plt.title('Comparison of Public Transport Peak Ridership and Hotel Occupancy')
plt.xlabel('Date')
plt.ylabel('Count/Percentage')
plt.legend()
plt.show()

# Identify correlation
correlation = merged_data['peak_ridership'].corr(merged_data['occupancy_rate'])
print(f'Correlation between peak ridership and hotel occupancy: {correlation}')
