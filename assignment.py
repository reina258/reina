import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

filename = "Sun_rise_set_2024.csv"

df = pd.read_csv(filename)

print(df.head())

df['YYYY-MM-DD'] = pd.to_datetime(df['YYYY-MM-DD'])

df['RISE'] = pd.to_datetime(df['RISE'], format='%H:%M').dt.hour + pd.to_datetime(df['RISE'], format='%H:%M').dt.minute / 60
df['TRAN.'] = pd.to_datetime(df['TRAN.'], format='%H:%M').dt.hour + pd.to_datetime(df['TRAN.'], format='%H:%M').dt.minute / 60
df['SET'] = pd.to_datetime(df['SET'], format='%H:%M').dt.hour + pd.to_datetime(df['SET'], format='%H:%M').dt.minute / 60

fig, ax = plt.subplots(figsize=(10, 6))

fig.patch.set_facecolor('white')
ax.set_facecolor('white')

line_rise, = ax.plot([], [], color='gray', alpha=0.2, label='Sunrise Time (Line)')
line_noon, = ax.plot([], [], color='gray', alpha=0.2, label='Solar Noon Time (Line)')
line_set, = ax.plot([], [], color='gray', alpha=0.2, label='Sunset Time (Line)')

point_rise, = ax.plot([], [], 'o', color='lightpink', label='Sunrise Time', markersize=15)  
point_noon, = ax.plot([], [], 'o', color='lightgreen', label='Solar Noon Time', markersize=15) 
point_set, = ax.plot([], [], 'o', color='lightblue', label='Sunset Time', markersize=15)

ax.set_title('Sunrise, Solar Noon, and Sunset Times in 2024')
ax.set_xlabel('Date')
ax.set_ylabel('Time (hours)')
ax.grid(True)


ax.legend(loc='lower left', bbox_to_anchor=(0.02, 0.02), frameon=True, facecolor='white', fontsize='medium', handlelength=2, markerscale=0.8)

ax.set_xlim(df['YYYY-MM-DD'].min(), df['YYYY-MM-DD'].max())
ax.set_ylim(0, 20) 

def init():
    point_rise.set_data([], [])
    point_noon.set_data([], [])
    point_set.set_data([], [])
    line_rise.set_data([], [])
    line_noon.set_data([], [])
    line_set.set_data([], [])
    return point_rise, point_noon, point_set, line_rise, line_noon, line_set

def update(frame):
    x = df['YYYY-MM-DD'][:frame+1]
    y_rise = df['RISE'][:frame+1]
    y_noon = df['TRAN.'][:frame+1]
    y_set = df['SET'][:frame+1]

    point_rise.set_data(x.iloc[frame], y_rise.iloc[frame])
    point_noon.set_data(x.iloc[frame], y_noon.iloc[frame])
    point_set.set_data(x.iloc[frame], y_set.iloc[frame])
    
    line_rise.set_data(x, y_rise)
    line_noon.set_data(x, y_noon)
    line_set.set_data(x, y_set)
    
    return point_rise, point_noon, point_set, line_rise, line_noon, line_set

n_frames = len(df)
interval = 5000 / n_frames  

ani = animation.FuncAnimation(fig, update, frames=n_frames, init_func=init, blit=True, interval=interval)

plt.show()
