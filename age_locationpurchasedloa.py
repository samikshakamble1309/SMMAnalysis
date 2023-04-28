import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('AI_Datasetcsv.csv')

# Filter the data to include only rows where the purchase decision was 1
df_purchased = df[df['purchase_decision'] == 1]

# Create a new column for age ranges
bins = [21, 25, 30, 35, 40, 45, 50, 55]
labels = ['21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55']
df_purchased['age_range'] = pd.cut(df_purchased['customer_age'], bins=bins, labels=labels, include_lowest=True)

# Iterate over each age range
for age_range in labels:
    # Filter the data to include only rows where the customer is in the current age range
    df_age_range = df_purchased[df_purchased['age_range'] == age_range]

    # Group the data by customer service location
    df_service_location = df_age_range.groupby('customer_service_location').size().reset_index(name='count')

    # Create a pie chart
    plt.pie(df_service_location['count'], labels=df_service_location['customer_service_location'])
    plt.title(f'Customers Who Purchased the Loan in the {age_range} Age Range by Service Location')

    plt.show()
