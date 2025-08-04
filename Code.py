import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

df = pd.read_csv(r"C:/Users/ANUGYA GUPTA/OneDrive/Desktop/Skillcraft internship tasks/US_Accidents_March23.csv")  

df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df = df.dropna(subset=['Start_Time'])  

df['Hour'] = df['Start_Time'].dt.hour

plt.figure(figsize=(10, 5))
sns.countplot(x='Hour', data=df, hue='Hour', palette='coolwarm', legend=False)
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.show()

top_weather = df['Weather_Condition'].value_counts().head(10).index
weather_df = df[df['Weather_Condition'].isin(top_weather)]

plt.figure(figsize=(12, 6))
sns.countplot(y='Weather_Condition', data=weather_df, order=top_weather, palette='viridis')
plt.title('Top 10 Weather Conditions in Accidents')
plt.xlabel('Count')
plt.ylabel('Weather Condition')
plt.tight_layout()
plt.show()

road_features = ['Bump', 'Junction', 'Traffic_Signal', 'Stop', 'Crossing']
for feature in road_features:
    if feature in df.columns:
        plt.figure(figsize=(6, 3))
        sns.countplot(x=feature, data=df, palette='pastel')
        plt.title(f'Accidents with {feature}')
        plt.tight_layout()
        plt.show()
        
heat_df = df[['Start_Lat', 'Start_Lng']].dropna().sample(10000)
m = folium.Map(location=[37, -95], zoom_start=5)
HeatMap(data=heat_df.values, radius=8).add_to(m)
m.save("accident_hotspots_map.html")
print("Analysis complete")
