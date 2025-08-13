import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
# --- 1. Synthetic Data Generation ---
# Generate synthetic data for delivery routes, including coordinates, congestion levels, and distances.
np.random.seed(42)  # for reproducibility
num_deliveries = 100
data = {
    'delivery_id': range(1, num_deliveries + 1),
    'origin_latitude': np.random.uniform(34, 35, num_deliveries),
    'origin_longitude': np.random.uniform(-118, -117, num_deliveries),
    'destination_latitude': np.random.uniform(34, 35, num_deliveries),
    'destination_longitude': np.random.uniform(-118, -117, num_deliveries),
    'congestion_level': np.random.randint(1, 11, num_deliveries), # 1-10 scale
    'distance_km': np.random.uniform(5, 20, num_deliveries)
}
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Preprocessing ---
# Create Point geometries for origin and destination
df['origin'] = df.apply(lambda row: Point(row['origin_longitude'], row['origin_latitude']), axis=1)
df['destination'] = df.apply(lambda row: Point(row['destination_longitude'], row['destination_latitude']), axis=1)
# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='origin', crs="EPSG:4326") #WGS84
# --- 3. Analysis ---
# Calculate weighted average congestion based on distance
df['weighted_congestion'] = df['congestion_level'] * df['distance_km']
average_weighted_congestion = df['weighted_congestion'].mean()
print(f"Average weighted congestion: {average_weighted_congestion}")
# --- 4. Visualization ---
# Create a scatter plot of delivery routes, colored by congestion level.
plt.figure(figsize=(10, 6))
plt.scatter(df['origin_longitude'], df['origin_latitude'], c=df['congestion_level'], cmap='viridis', s=50)
plt.colorbar(label='Congestion Level')
plt.title('Delivery Routes and Congestion Levels')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
#Save the plot
output_filename = 'delivery_routes.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
# --- 5. Route Optimization (Illustrative Example) ---
# This section is a simplified example and would require more sophisticated algorithms for real-world application.
#  For instance, a real-world solution would use a routing library like OSMnx or a graph-based approach.
# Identify high-congestion routes
high_congestion_routes = df[df['congestion_level'] > 7]
print("\nHigh Congestion Routes:")
print(high_congestion_routes[['delivery_id', 'origin_latitude', 'origin_longitude', 'destination_latitude', 'destination_longitude', 'congestion_level']])
# Recommendation: Explore alternative routes for high-congestion deliveries (Requires external routing API or algorithm)
print("\nRecommendation: Investigate alternative routes for deliveries with high congestion levels.")