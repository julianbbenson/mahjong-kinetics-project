import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

INPUT_FILE = 'kinetics_data.csv'


def michaelis_menten(S, Vmax, Km):
    return (Vmax * S) / (Km + S)


def analyze():
    print("Loading data...")
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print("CSV not found. Run harvest_data.py first.")
        return

    # Filter for valid game states
    df = df[(df['tiles_left_at_riichi'] > 0) & (df['tiles_left_at_riichi'] <= 70)]

    # Group by [S] (Substrate)
    stats = df.groupby('tiles_left_at_riichi')['outcome'].agg(['mean', 'count'])
    stats = stats[stats['count'] > 100]  # Filter noise

    S_data = stats.index.values
    V_data = stats['mean'].values

    # Fit Curve
    popt, pcov = curve_fit(michaelis_menten, S_data, V_data, p0=[0.6, 20])
    Vmax_fit, Km_fit = popt

    # Calculate R-squared
    residuals = V_data - michaelis_menten(S_data, *popt)
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((V_data - np.mean(V_data)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    print("-" * 30)
    print(f"RESULTS:")
    print(f"Vmax: {Vmax_fit:.4f}")
    print(f"Km:   {Km_fit:.4f} tiles")
    print(f"R^2:  {r_squared:.4f}")
    print("-" * 30)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(S_data, V_data, color='black', s=15, label='Experimental Data')

    S_range = np.linspace(min(S_data), max(S_data), 100)
    plt.plot(S_range, michaelis_menten(S_range, *popt), color='crimson', linewidth=2.5,
             label=f'Michaelis-Menten Fit (Km={Km_fit:.1f})')

    plt.title('Kinetics of Riichi Mahjong')
    plt.xlabel('Substrate [S] (Tiles Remaining in Wall)')
    plt.ylabel('Reaction Velocity [V] (Win Probability)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('mahjong_kinetics_curve.png', dpi=300)
    print("Graph saved to 'mahjong_kinetics_curve.png'")
    plt.show()


if __name__ == "__main__":
    analyze()