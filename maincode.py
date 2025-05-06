import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

# Function to create the plot
def create_plot(luminosity, exoplanets, planet_labels):
    d_inner = 0.95 * np.sqrt(luminosity)
    d_outer = 1.37 * np.sqrt(luminosity)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)

    outer_hz = plt.Circle((0, 0), d_outer, color='green', alpha=0.5, label="Outer HZ")
    inner_hz = plt.Circle((0, 0), d_inner, color='blue', alpha=0.5, label="Inner HZ")
    
    ax.add_patch(outer_hz)
    ax.add_patch(inner_hz)

    angle_step = 360 / len(exoplanets)
    for i, (semi_major_axis, label) in enumerate(zip(exoplanets, planet_labels)):
        angle = np.radians(i * angle_step)
        x = semi_major_axis * np.cos(angle)
        y = semi_major_axis * np.sin(angle)
        ax.plot(x, y, 'ro')  # 'ro' for red dots
        ax.text(x + 0.1, y, label, fontsize=8, color='black', ha='center', va='center')
    
    star = plt.Circle((0, 0), 0.03, color='yellow', label="Star")
    ax.add_patch(star)

    ax.set_xlabel("AU (Astronomical Units)")
    ax.set_ylabel("AU (Astronomical Units)")
    ax.set_title("Exoplanets and Habitable Zone")
    ax.legend()
    ax.grid()

    plt.show()

# Function to handle planetary system selection
def select_planetary_system():
    selected_index = system_combobox.current()
    if selected_index == -1:
        messagebox.showerror("Error", "Please select a planetary system.")
        return

    system = planetary_systems[selected_index]
    details = (
        f"Name: {system['name']}\n"
        f"Radius: {system['radius']} Solar radius\n"
        f"Temperature: {system['temperature']} K\n"
        f"Luminosity: {system['luminosity']} Solar luminosity\n"
        f"Distance: {system['distance']} light years"
    )
    
    # Display planetary system details
    details_label.config(text=details)

    # Populate the exoplanet dropdown
    exoplanet_combobox['values'] = system['planet_labels']
    exoplanet_combobox.set("")  # Clear previous selection

    # Clear exoplanet details
    exoplanet_data_label.config(text="")

    # Plot the habitable zone and exoplanets
    create_plot(system['luminosity'], system['exoplanets'], system['planet_labels'])

# Function to handle exoplanet selection
def select_exoplanet():
    selected_planet_index = exoplanet_combobox.current()
    if selected_planet_index == -1:
        messagebox.showerror("Error", "Please select an exoplanet.")
        return

    # Get the selected planetary system
    selected_system_index = system_combobox.current()
    system = planetary_systems[selected_system_index]

    # Get details of the selected exoplanet
    planet_name = system['planet_labels'][selected_planet_index]
    eccentricity = system['eccentricity'][selected_planet_index]
    status = system['status'][selected_planet_index]
    mass = system['mass'][selected_planet_index]
    orbital_period = system['orbital_period_period_period_period'][selected_planet_index]

    # Display the exoplanet details
    exoplanet_details = (
        f"Planet: {planet_name}\n"
        f"Eccentricity: {eccentricity}\n"
        f"Status: {status}\n"
        f"Mass: {mass}\n"
        f"Orbital Period: {orbital_period} days"
    )
    exoplanet_data_label.config(text=exoplanet_details)

# Function to handle custom data input
def plot_custom_data():
    try:
        luminosity = float(luminosity_entry.get())
        exoplanets = list(map(float, exoplanets_entry.get().split(',')))
        planet_labels = planet_labels_entry.get().split(',')
        if len(exoplanets) != len(planet_labels):
            messagebox.showerror("Error", "Number of exoplanets and labels must match.")
            return
        create_plot(luminosity, exoplanets, planet_labels)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Planetary systems data
planetary_systems = [
    { 
        "name": "Sun",
        "luminosity": 1,
        "radius": 1,
        "temperature": 5772,
        "distance": 1,
        "exoplanets": [0.4, 0.73, 1, 1.52, 5.2, 9.5, 19, 30],
        "planet_labels": ["1.Mercury", "2.Venus", "3.Earth", "4.Mars",
                          "5.Jupiter", "6.Saturn", "7.Uranus", "8.Neptune"],
        "eccentricity": ["0.2056", "0.0068", "0.0167", "0.0934", "0.0484", "0.0541", "0.0472", "0.0086"],
        "status": ["Inhabitable"] * 8,
        "mass": ["-", "-", "-", "-", "-", "-", "15", "203"],
        "orbital_period_period_period_period": ["87.97", "224.70", "365.26", "686.98", "4,332.82", "10,755.70", "30,687.15", "60,190.03"]
    },
    {
        "name": "Kepler-90",
        "luminosity": 1.7,
        "radius": 1.2,
        "temperature": 6080,
        "distance": 2.790,
        "exoplanets": [0.074, 0.089, 0.107, 0.32, 0.42, 0.48, 0.71, 1.01],
        "planet_labels": ["1. Kepler-90b", "2. Kepler-90c", "3. Kepler-90i", "4. Kepler-90d",
                          "5. Kepler-90e", "6. Kepler-90f", "7. Kepler-90g", "8. Kepler-90h"],
        "eccentricity": ["-", "-", "-", "-", "-", "0.01", "0.049", "0.011"],
        "status": ["Inhabitable"] * 8,
        "mass": ["-", "-", "-", "-", "-", "-", "15", "203"],
        "orbital_period_period_period_period": ["7.008151", "8.719375", "14.44912", "59.73667", "91.93913", "124.9144", "210.60697", "331.60059"]
    },
    {
        "name": "TRAPPIST-1",
        "luminosity": 0.000566,
        "radius": 0.1192,
        "temperature": 2566,
        "distance": 40.66,
        "exoplanets": [0.0115, 0.0158, 0.0222, 0.02925, 0.03849, 0.4683, 0.6189],
        "planet_labels": ["1. TRAPPIST-1b", "2. TRAPPIST-1c", "3. TRAPPIST-1d", "4. TRAPPIST-1e",
                          "5. TRAPPIST-1f", "6. TRAPPIST-1g", "7. TRAPPIST-1h"],
        "eccentricity": ["0.05", "0.073", "0.05", "0.131", "0.051", "0.119", "0.15"],
        "status": ["Unconfirmed and Inhabitable", "Inhabitable", "Unconfirmed and Inhabitable",
                   "Inhabitable", "Inhabitable", "Inhabitable", "Habitable"],
        "mass": ["1.374", "1.308", "0.388", "0.692", "1.039", "1.321", "0.326"],
        "orbital_period_period_period_period": ["1.5108", "2.421937", "4.049219", "6.101013", "9.2075", "12.352446", "18.772886"]
    },
    {
        "name": "HD 10180",
        "luminosity": 1.64,
        "radius": 1.11,
        "temperature": 5911,
        "distance": 127.10,
        "exoplanets": [0.0222, 0.06412, 0.0904, 0.12859, 0.2699, 0.4929, 1.427, 3.381],
        "planet_labels": ["1. HD 10180b", "2. HD 10180c", "3. HD 10180i", "4. HD 10180d",
                          "5. HD 10180e", "6. HD 10180f", "7. HD 10180g", "8. HD 10180h"],
        "eccentricity": ["0.05", "0.073", "0.05", "0.131", "0.051", "0.119", "0.15", "0.095"],
        "status": ["Unconfirmed and Inhabitable", "Inhabitable", "Unconfirmed and Inhabitable",
                   "Inhabitable", "Inhabitable", "Inhabitable", "Habitable", "Inhabitable"],
        "mass": ["1.3", "13.2", "1.9", "12.0", "25.6", "19.4", "23.3", "46.3"],
        "orbital_period_period_period_period": ["1.17766", "5.75969", "9.655", "16.3570", "49.748", "122.744", "615", "2500"]
    },
    {
        "name": "HR 8832",
        "luminosity": 0.265,
        "radius": 0.748,
        "temperature": 4817,
        "distance": 21.336,
        "exoplanets": [0.03876, 0.06530, 0.06530, 0.2370, 0.3753, 3.11],
        "planet_labels": ["1. HR 8832b", "2. HR 8832c", "3. HR 8832f", "4. HR 8832d",
                          "5. HR 8832g", "6. HR 8832h"],
        "eccentricity": ["0", "0.062", "0.148", "0.138", "0", "0.06"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable and Existence Disputed",
                   "Inhabitable", "Habitable But Existence Disputed"],
        "mass": ["4.59", "4.23", ">7.3", ">6.17", ">11", ">98"],
        "orbital_period_period_period_period": ["3.092926", "6.76458", "22.717", "48.859", "94.2", "2100.6"]
    },
    {
        "name": "HD 40307",
        "luminosity": 0.23,
        "radius": 0.716,
        "temperature": 4977,
        "distance": 42.179,
        "exoplanets": [0.0468, 0.0799, 0.1321, 0.1886, 0.247, 0.600],
        "planet_labels": ["1. HD 40307b", "2. HD 40307c", "3. HD 40307d", "4. HD 40307e",
                          "5. HD 40307f", "6. HD 40307g"],
        "eccentricity": ["0.20", "0.06", "0.07", "0.15", "0.02", "0.29"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable and Existence Disputed",
                   "Inhabitable", "Habitable But Existence Disputed"],
        "mass": ["4.0", "6.6", "9.5", "3.5", "5.2", "7.1"],
        "orbital_period_period_period_period": ["4.3123", "9.6184", "20.432", "34.62", "51.76", "197.8"]
    },
    {
        "name": "HD 34445",
        "luminosity": 2.01,
        "radius": 1.38,
        "temperature": 5836,
        "distance": 150.5,
        "exoplanets": [0.2687, 0.4817, 0.7181, 1.543, 2.075, 6.36],
        "planet_labels": ["1. HD 34445b", "2. HD 34445c", "3. HD 34445d", "4. HD 34445e", "5. HD 34445f", "6. HD 34445g"],
        "eccentricity": ["0.20", "0.06", "0.07", "0.15", "0.02", "0.29"],
        "status": ["Inhabitable"] * 6,
        "mass": ["4.0", "6.6", "9.5", "3.5", "5.2", "7.1"],
        "orbital_period_period_period_period": ["4.3123", "9.6184", "20.432", "34.62", "51.76", "197.8"]
    },
    {
        "name": "HD 125612",
        "luminosity": 1.09,
        "radius": 1.05,
        "temperature": 5900,
        "distance": 188.6,
        "exoplanets": [0.0524, 1.372, 3.982],
        "planet_labels": ["1. HD 125612c", "2. HD 125612b", "3. HD 125612d"],
        "eccentricity": ["0.049", "0.4553", "0.115"],
        "status": ["Inhabitable", "Habitable", "Inhabitable"],
        "mass": ["0.055", "3.1", "7.178"],
        "orbital_period_period_period_period": ["4.15514", "557.04", "2822.7"]
    },
    {
        "name": "HD 134606",
        "luminosity": 1.161,
        "radius": 1.158,
        "temperature": 5576,
        "distance": 87.44,
        "exoplanets": [0.0527, 0.1046, 0.1784, 0.3007, 1.941],
        "planet_labels": ["1. HD 134606e", "2. HD 134606b", "3. HD 134606f", "4. HD 134606c", "5. HD 134606d"],
        "eccentricity": ["0.2", "0.092", "0.081", "0.055", "0.092"],
        "status": ["Inhabitable"] * 5,
        "mass": ["2.34", "9.09", "5.63", "11.31", "44.8"],
        "orbital_period_period_period_period": ["4.3203", "12.089", "26.915", "58.883", "966.5"]
    },
    {
        "name": "HD 37124",
        "luminosity": 0.839,
        "radius": 0.92,
        "temperature": 5763,
        "distance": 103.4,
        "exoplanets": [0.53364, 1.7100, 2.807],
        "planet_labels": ["1. HD 37124b", "2. HD 37124c", "3. HD 37124d"],
        "eccentricity": ["0.054", "0.125", "0.16"],
        "status": ["Inhabitable"] * 3,
        "mass": ["0.675", "0.652", "0.69"],
        "orbital_period_period_period_period": ["154.378", "885.5", "1862"]
    },
    {
        "name": "HD 9446",
        "luminosity": 1.1,
        "radius": 0.984,
        "temperature": 5793,
        "distance": 163.7,
        "exoplanets": [0.1892, 0.646, 7],
        "planet_labels": ["1. HD 9446b", "2. HD 9446c", "3. HD 9446d"],
        "eccentricity": ["0.20", "0.06", "-"],
        "status": ["Inhabitable"] * 3,
        "mass": ["0.687", "1.71", "1.5"],
        "orbital_period_period_period_period": ["30.0608", "189.6", "-"]
    },
    {
        "name": "HD 141399",
        "luminosity": 1.59,
        "radius": 1.46,
        "temperature": 1.46,
        "distance": 120.85,
        "exoplanets": [0.415, 0.689, 2.09, 5.0],
        "planet_labels": ["1. HD 141399b", "2. HD 141399c", "3. HD 141399d", "4. HD 141399e"],
        "eccentricity": ["0.04", "0.048", "0.074", "<0.1"],
        "status": ["Inhabitable"] * 4,
        "mass": ["0.451", "1.33", "1.18", "0.66"],
        "orbital_period_period_period_period": ["94.44", "201.99", "1069.8", "3370"]
    },
    {
        "name": "HD 160691 (Mu Arae)",
        "luminosity": 1.879,
        "radius": 1.280,
        "temperature": 5974,
        "distance": 50.89,
        "exoplanets": [0.092319, 0.9347, 1.522, 5.204],
        "planet_labels": ["1. HD 160691c (Dulcinea)", "2. HD 160691d (Rocinante)", "3. HD 160691b (Quijote)", "4. HD 160691e (Sancho)"],
        "eccentricity": ["0.090", "0.055", "0.041", "0.049"],
        "status": ["Inhabitable", "Inhabitable", "Habitable", "Inhabitable"],
        "mass": ["≥0.032", "≥0.448", "≥1.65", "≥1.932"],
        "orbital_period_period_period_period": ["9.638", "308.36", "644.92", "4019"]
    },
    {
        "name": "HD 134606",
        "luminosity": 1.161,
        "radius": 1.158,
        "temperature": 5576,
        "distance": 87.44,
        "exoplanets": [0.0527, 0.1046, 0.1784, 0.3007, 1.941],
        "planet_labels": ["1. HD 134606e", "2. HD 134606b", "3. HD 134606f", "4. HD 134606c", "5. HD 134606d"],
        "eccentricity": ["0.2", "0.092", "0.081", "0.055", "0.092"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["2.34", "9.09", "5.63", "11.31", "44.8"],
        "orbital_period_period_period_period": ["4.3203", "12.089", "26.915", "58.883", "966.5"]
    },
    {
        "name": "HD 181433",
        "luminosity": 0.34,
        "radius": 0.80,
        "temperature": 4909,
        "distance": 88.03,
        "exoplanets": [0.080, 1.76, 3.00],
        "planet_labels": ["1. HD 181433b", "2. HD 181433c", "3. HD 181433d"],
        "eccentricity": ["0.396", "0.28", "0.48"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["≥0.0238", "≥0.64", "≥0.54 MJ"],
        "orbital_period_period_period_period": ["9.3743", "962", "2172"]
    },
    {
        "name": "HD 21693",
        "luminosity": 0.66,
        "radius": 0.93,
        "temperature": 5430,
        "distance": 108.6,
        "exoplanets": [0.1455, 0.25864],
        "planet_labels": ["1. HD 21693b", "2. HD 21693c"],
        "eccentricity": ["0.12", "0.07"],
        "status": ["Inhabitable", "Inhabitable"],
        "mass": ["≥8.23M🜨", "≥17.37M🜨"],
        "orbital_period_period_period_period": ["22.6786", "53.7357"]
    },
    {
        "name": "HD 20781",
        "luminosity": 0.49,
        "radius": 1.17,
        "temperature": 5256,
        "distance": 117.3,
        "exoplanets": [0.0529, 0.1004, 0.1647, 0.3374],
        "planet_labels": ["1. HD 20781b", "2. HD 20781c", "3. HD 20781d", "4. HD 20781e"],
        "eccentricity": ["0.10", "0.09", "0.11", "0.06"],
        "status": ["Inhabitable", "Inhabitable", "Habitable", "Inhabitable"],
        "mass": ["≥1.93M🜨", "≥5.33M🜨", "≥10.61M🜨", "≥14.03M🜨"],
        "orbital_period_period_period_period": ["5.3135", "13.8905", "29.1580", "85.5073"]
    },
    {
        "name": "HD 40307",
        "luminosity": 0.23,
        "radius": 0.716,
        "temperature": 4977,
        "distance": 42.179,
        "exoplanets": [0.0468, 0.0799, 0.1321, 0.1886, 0.247, 0.600],
        "planet_labels": ["1. HD 40307b", "2. HD 40307c", "3. HD 40307d", "4. HD 40307e", "5. HD 40307f", "6. HD 40307g"],
        "eccentricity": ["0.20", "0.06", "0.07", "0.15", "0.02", "0.29"],
        "status": ["Inhabitable", "Inhabitable", "Habitable", "Inhabitable And Existence Disputed", "Inhabitable", "Habitable But Existence Disputed"],
        "mass": ["≥4.0M🜨", "≥6.6M🜨", "≥9.5M🜨", "≥3.5M🜨", "≥5.2M🜨", "≥7.1M🜨"],
        "orbital_period_period_period_period": ["4.3123", "9.6184", "20.432", "34.62", "51.76", "197.8"]
    },
    {
        "name": "HD 47186",
        "luminosity": 1.219,
        "radius": 1.12,
        "temperature": 5736,
        "distance": 121.94,
        "exoplanets": [0.050, 2.395],
        "planet_labels": ["1. HD 47186b", "2. HD 47186c"],
        "eccentricity": ["0.038 ± 0.020", "0.249 ± 0.073"],
        "status": ["Inhabitable", "Inhabitable"],
        "mass": ["≥0.07167 MJ", "≥0.35061 MJ"],
        "orbital_period_period_period_period": ["4.0845", "1353.6"]
    },
    {
        "name": "HD 69830",
        "luminosity": 0.622,
        "radius": 0.905,
        "temperature": 5394,
        "distance": 41.03,
        "exoplanets": [0.0764, 0.181, 0.622],
        "planet_labels": ["1. HD 69830b", "2. HD 69830c", "3. HD 69830d"],
        "eccentricity": ["0.128", "0.03", "0.08"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["≥10.1M🜨", "≥12.09M🜨", "≥12.26M🜨"],
        "orbital_period_period_period_period": ["8.66897", "31.6158", "201.4"]
    },
    {
        "name": "HD 93385",
        "luminosity": 1.42,
        "radius": 1.17,
        "temperature": 5823,
        "distance": 140.9,
        "exoplanets": [0.0756, 0.112, 0.2565],
        "planet_labels": ["1. HD 93385b", "2. HD 93385c", "3. HD 93385d"],
        "eccentricity": ["<0.295", "<0.20", "0.09"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["≥4.2M🜨", "≥7.1M🜨", "≥8.7M🜨"],
        "orbital_period_period_period_period": ["7.3426", "13.180", "45.85"]
    },
    {
        "name": "Kepler-20",
        "luminosity": 0.944,
        "radius": 0.9164,
        "temperature": 5495,
        "distance": 934,
        "exoplanets": [0.04565, 0.0637, 0.0936, 0.1387, 0.2055, 0.3474],
        "planet_labels": ["1. Kepler-20b", "2. Kepler-20e", "3. Kepler-20c", "4. Kepler-20f", "5. Kepler-20g", "6. Kepler-20d"],
        "eccentricity": ["<0.083", "<0.092", "<0.076", "<0.094", "≤0.16", "<0.082"],
        "status": ["Inhabitable", "Inhabitable", "Habitable", "Inhabitable", "Inhabitable And Existence Disputed", "Habitable"],
        "mass": ["9.7M🜨", "<0.76M🜨", "11.1M🜨", "<1.4M🜨", "≥19.96M🜨", "13.4M🜨"],
        "orbital_period_period_period_period": ["3.6961049", "6.0984882", "10.8540774", "19.578328", "34.940", "77.611455"]
    },
    {
        "name": "Kepler-62",
        "luminosity": 0.2565,
        "radius": 0.660,
        "temperature": 5062,
        "distance": 982,
        "exoplanets": [0.0553, 0.093, 0.120, 0.427, 0.718],
        "planet_labels": ["1. Kepler-62b", "2. Kepler-62c", "3. Kepler-62d", "4. Kepler-62e", "5. Kepler-62f"],
        "eccentricity": ["-", "-", "-", "-", "-"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["<9 M🜨", "<4 M🜨", "<14 M🜨", "<36 M🜨", "<35 M🜨"],
        "orbital_period_period_period_period": ["5.71493", "12.4417", "18.16406", "122.3874", "267.29"]
    },
    {
        "name": "Kepler-102",
        "luminosity": 0.117,
        "radius": 0.724,
        "temperature": 4909,
        "distance": 352.5,
        "exoplanets": [0.05521, 0.06702, 0.08618, 0.1162, 0.1656],
        "planet_labels": ["1. Kepler-102b", "2. Kepler-102c", "3. Kepler-102d", "4. Kepler-102e", "5. Kepler-102f"],
        "eccentricity": ["0.100", "<0.094", "<0.092", "<0.089", "<0.10"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["<1.1 M🜨", "<1.7 M🜨", "3.0 M🜨", "4.7 M🜨", "<4.3M🜨"],
        "orbital_period_period_period_period": ["5.286965", "7.071392", "10.3117670", "16.1456994", "27.453592"]
    },
    {
        "name": "Kepler-186",
        "luminosity": 0.055,
        "radius": 0.523,
        "temperature": 3755,
        "distance": 579,
        "exoplanets": [0.0378, 0.0574, 0.0861, 0.1216, 0.432],
        "planet_labels": ["1. Kepler-186b", "2. Kepler-186c", "3. Kepler-186d", "4. Kepler-186e", "5. Kepler-186f"],
        "eccentricity": ["<0.24", "<0.24", "<0.25", "<0.24", "<0.04"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["1.24M🜨", "2.1M🜨", "2.54 M🜨", "2.15M🜨", "1.44M🜨"],
        "orbital_period_period_period_period": ["3.8867907", "7.267302", "13.342996", "22.407704", "129.9444"]
    },
    {
        "name": "Kepler-442",
        "luminosity": 0.117,
        "radius": 0.60,
        "temperature": 4402,
        "distance": 1196,
        "exoplanets": [0.409],
        "planet_labels": ["1. Kepler-442b"],
        "eccentricity": ["0.04"],
        "status": ["Habitable"],
        "mass": ["2.3M🜨"],
        "orbital_period_period_period_period": ["112.3053"]
    },
    {
        "name": "Kepler-160",
        "luminosity": 1.01,
        "radius": 1.118,
        "temperature": 5471,
        "distance": 3060,
        "exoplanets": [0.05511, 0.1192, 0.17, 1.089],
        "planet_labels": ["1. Kepler-160b", "2. Kepler-160c", "3. Kepler-160d", "4. Kepler-160e"],
        "eccentricity": ["0", "0", "-", "0"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable", "Habitable but Existence Unconfirmed"],
        "mass": ["-", "-", "1—100 M🜨", "-"],
        "orbital_period_period_period_period": ["4.309397", "13.699429", "-", "378.417"]
    },
    {
        "name": "HD 20794",
        "luminosity": 0.6869,
        "radius": 0.93,
        "temperature": 5473,
        "distance": 9.704,
        "exoplanets": [0.1257, 0.3625, 1.3541],
        "planet_labels": ["1. HD 20794b", "2. HD 20794c", "3. HD 20794d"],
        "eccentricity": ["0.064", "0.077", "0.45"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["2.15", "2.98", "5.82"],
        "orbital_period_period_period_period": ["18.314", "89.68", "647.6"]
    },
    {
        "name": "Kepler-47",
        "luminosity": 	0.840,
        "radius": 	0.936,
        "temperature": 5636,
        "distance": 	3420 ,
        "exoplanets": [0.2877, 0.6992, 0.9638],
        "planet_labels": ["1. Kepler-47b", "2. Kepler-47d", "3. Kepler-47c"],
        "eccentricity": ["0.0210", "0.024", "0.044"],
        "status": ["Inhabitable", "Inhabitable", "Habitable"],
        "mass": ["2.07", "19.02", "3.17"],
        "orbital_period_period_period_period": ["49.4643", "187.366", "303.227"]
        
    },
     {
        "name": "Proxima Centauri",
        "luminosity": 0.001567,
        "radius": 	0.1542,
        "temperature": 2992,
        "distance": 4.2465 ,
        "exoplanets": [0.02885, 0.04856, 1.489],
        "planet_labels": ["1.Proxima Centauri-d", "2.Proxima Centauri-b", "3.Proxima Centauri-c"],
        "eccentricity": ["0.04", "0.02", "0.04"],
        "status": ["Inhabitable", "Inhabitable", "Habitable"],
        "mass": ["0.26", "1.07", "7"],
        "orbital_period_period_period_period": ["5.122", "11.1868", "1,928"]
        
    },
    {
        "name": "Barnard's Star",
        "luminosity": 0.00340,
        "radius": 0.187,
        "temperature": 3195,
        "distance":5.9629 ,
        "exoplanets": [2.3402, 3.1542, 4.1244,6.7392],
        "planet_labels": ["1.Barnard's Star-d", "2.Barnard's Star-b", "3.Barnard's Star-c", "4.Barnard's Star-e"],
        "eccentricity": ["0.04", "0.03", "0.08","0.04"],
        "status": ["Inhabitable", "Inhabitable", "Habitable","-"],
        "mass": ["0.263", "0.299", "0.335","0.193"],
        "orbital_period_period_period_period": ["2.3402", "3.1542", "4.1244","6.7392"]
    },
    {
        "name": "61 Virginis",
        "luminosity": 0.8222,
        "radius": 0.9867,
        "temperature":5538,
        "distance":	27.84 ,
        "exoplanets": [0.050, 0.216, 0.47],
        "planet_labels": ["1.61 Virginis-b", "2.61 Virginis-c", "3.61 Virginis-d"],
        "eccentricity": ["0.11", "0.07", "0.12"],
        "status": ["Inhabitable", "Inhabitable", "Habitable"],
        "mass": ["6.11", "19.33", "12.24"],
        "orbital_period_period_period_period": ["4.2150", "38.073", "123.12"]
    },
    {
        "name": "Upsilon Andromedae",
        "luminosity": 3.57 ,
        "radius": 1.57,
        "temperature":6614,
        "distance":	44.0 ,
        "exoplanets": [0.0594, 0.829, 2.51329],
        "planet_labels": ["1.Upsilon Andromedae-b(saffar)", "2.Upsilon Andromedae-c(samh)", "3.Upsilon Andromedae-d(majriti)"],
        "eccentricity": ["0.022", "0.260", "0.299"],
        "status": ["Inhabitable", "Inhabitable", "Habitable"],
        "mass": ["1.70", "13.98", "10.25"],
        "orbital_period_period_period_period": ["4.62", "241.26", "1,276.46"]
    },
    {
        "name": "47 Ursae Majoris",
        "luminosity": 1.48 ,
        "radius": 1.172,
        "temperature":5887,
        "distance":	45.30 ,
        "exoplanets": [2.10 , 3.6, 11.6],
        "planet_labels": ["1.47 Ursae Majoris-b(Taphao Thong)", "2.47 Ursae Majoris-c(Taphao Kaew)", "3.47 Ursae Majoris-d(majriti)"],
        "eccentricity": ["0.032", "0.098", "0.16"],
        "status": ["Inhabitable", "Inhabitable", "Habitable"],
        "mass": ["2.53", "0.540", "1.64"],
        "orbital_period_period_period_period": ["1,078", "2,391", "14,002"]
    },
   {
        "name": "82 G. Eridani",
        "luminosity": 0.6869 ,
        "radius": 0.93,
        "temperature":5473,
        "distance":	19.704 ,
        "exoplanets": [0.125 , 0.3625, 1.3541],
        "planet_labels": ["1.82 G. Eridani-b", "2.82 G. Eridani-c", "3.82 G. Eridani-d"],
        "eccentricity": ["0.064", "0.077", "0.45"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["2.15", "2.98", "5.82"],
        "orbital_period_period_period_period": ["18.3140", "89.68", "647.6"]
    },
    {
        "name": "55 Cancri A",
        "luminosity":0.617 ,
        "radius": 0.980,
        "temperature":5172,
        "distance":	40.95,
        "exoplanets": [0.01544 ,0.01544, 0.2373,0.7708,5.957],
        "planet_labels": ["1.55 Cancri A-e(Janssen)", "2.55 Cancri A-b(Galileo)", "3.55 Cancri A-c(Brahe)", "4.55 Cancri A-f(Harriot)","5.55 Cancri A-d(Lipperhey)"],
        "eccentricity": ["0.05", "0", "0.03","0.08","0.13"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable", "Habitable", "Inhabitable"],
        "mass": ["7.99", "0.8036", "51.2 ","47.8","3.12"],
        "orbital_period_period_period_period": ["0.73654625", "14.6516 ", "44.3989","259.88","5,574.2"]
    },
    {
        "name": "Pi Mensae",
        "luminosity":1.532 ,
        "radius":1.15,
        "temperature":6013,
        "distance":	59.65,
        "exoplanets": [0.06839 ,0.5, 3.311],
        "planet_labels": ["1.Pi Mensae-c", "2.Pi Mensae-d", "3.Pi Mensae-b"],
        "eccentricity": ["0", "	0.220", "0.642"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["3.63", "13.38", "12.325 "],
        "orbital_period_period_period_period": ["6.267852", "124.64", "2088.8"]
    },
     {
        "name": "HD 142 A",
        "luminosity":2.9 ,
        "radius":1.41,
        "temperature":6338,
        "distance":	85.39,
        "exoplanets": [0.474 ,1.039, 9.811],
        "planet_labels": ["1.HD 142 A-d", "2.HD 142 A-b", "3.HD 142 A-c"],
        "eccentricity": ["0.130", "	0.158", "0.277"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["0.260", "7.1", "10.901"],
        "orbital_period_period_period_period": ["108.5", "351.4", "10,159.6"]
    },
    {
        "name": "HD 63433",
        "luminosity":0.753 ,
        "radius":0.912,
        "temperature":5640,
        "distance":73.035,
        "exoplanets": [0.0503 ,0.0719,0.1458],
        "planet_labels": ["1.HD 63433-d", "2.HD 63433-b", "3.HD 63433-c"],
        "eccentricity": ["0.16", "0.24", "0.161"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["—", "21.76", "15.54"],
        "orbital_period_period_period_period": ["4.21", "7.11", "20.55"]
        
    },
    {
        "name": "HD 164922",
        "luminosity":0.703 ,
        "radius":0.999,
        "temperature":5390,
        "distance":71.69,
        "exoplanets": [0.1023,0.2292,0.3411,2.149],
        "planet_labels": ["1.HD 164922-d", "2.HD 164922-e", "3.HD 63433-c", "4.HD 164922-b"],
        "eccentricity": ["0.18", "0.086", "	0.096"],
        "status": ["Inhabitable", "Inhabitable", "Inabitable","Inhabitable"],
        "mass": ["4.74", "10.52", "14.3","0.344"],
        "orbital_period_period_period_period": ["12.4584", "41.763", "75.817","1,198.5","0.065"]
        
    },
    {
        "name": "HD 82943",
        "luminosity":1.54 ,
        "radius":1.17,
        "temperature":5944,
        "distance":90.31,
        "exoplanets": [0.746,1.18,2.145],
        "planet_labels": ["1.HD 82943-c", "2.HD 82943-b", "3.HD 82943-d"],
        "eccentricity": ["0.359", "0.219", "unsure"],
        "status": ["Inhabitable", "Inhabitable But just on the edge of Habitable zone", "Unconfirmed and Inhabitable"],
        "mass": ["14.39 Mass of Jupiter", "14.5 Mass of Jupiter", "0.29 Mass of Jupiter"],
        "orbital_period_period_period_period": ["219.3", "441.2", "1078"]
        
    },
    {
        "name": "HR 858",
        "luminosity":1.54 ,
        "radius":1.17,
        "temperature":5944,
        "distance":90.31,
        "exoplanets": [0.04888,0.06870,0.1046],
        "planet_labels": ["1.HR 858-b", "2.HR 858-c", "3.HR 858-d"],
        "eccentricity": ["0.359", "0.219", "unsure"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["3.55", "3.8", "7.1"],
        "orbital_period_period_period_period": ["3.585287", "5.973865", "11.230511"]
        
    },
     {
        "name": "HD 204313",
        "luminosity":1.18 ,
        "radius":1.08,
        "temperature":5783,
        "distance":157,
        "exoplanets": [0.2099,3.185,7.457],
        "planet_labels": ["1.HD 204313-c", "2.HD 204313-b", "3.HD 204313-e"],
        "eccentricity": ["0.059", "	0.100", "0.253"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["17.6", "4.615", "15.317"],
        "orbital_period_period_period_period": ["34.905", "2041.1", "7325.6"]
        
    },
    {
        "name": "HD 3167",
        "luminosity":0.56 ,
        "radius":0.880,
        "temperature":5261,
        "distance":154.3,
        "exoplanets": [0.01796,0.0763,0.1776,0.3885],
        "planet_labels": ["1.HD 3167-b", "2.HD 3167-d", "3.HD 3167-c", "4.HD 3167-e"],
        "eccentricity": ["0 ", "0.12", "0.060", "0.15"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable","Inhabitable"],
        "mass": ["4.97", "4.33", "11.13","8.41"],
        "orbital_period_period_period_period": ["0.959641", "8.4112", "29.8454","96.63"]
        
    },
    {
        "name": "HIP 14810",
        "luminosity":0.99 ,
        "radius":1.08,
        "temperature":5535,
        "distance":164.9,
        "exoplanets": [0.0696,0.549,1.94],
        "planet_labels": ["1.HIP 14810-b", "2.HIP 14810-c", "3.HIP 14810-d"],
        "eccentricity": ["0.14399", "0.1566", "0.185"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["3.9 Mass of Jupiter", "1.31 Mass of Jupiter", "0.59 Mass of Jupiter"],
        "orbital_period_period_period_period": ["6.673892", "147.747", "981.8"]
        
    },
    {
        "name": "HD 191939",
        "luminosity":0.65 ,
        "radius":0.94,
        "temperature":5348,
        "distance":	174.4,
        "exoplanets": [0.0804,0.1752,0.2132,0.407,0.812,3.2],
        "planet_labels": ["1.HD 191939-b", "2.HD 191939-c", "3.HD 191939-d","4.HD 191939-e","5.HD 191939-g","6.HD 191939-f"],
        "eccentricity": ["0.031", "0.034", "0.031","0.031","0.030","Unsure"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable", "Habitable", "Inhabitable"],
        "mass": ["10.00", "8.0", "2.80","112.2","13.5","2.08 Mass of Jupiter"],
        "orbital_period_period_period_period": ["8.8803256", "28.579743", "38.353037","101.12","284","2200"]
        
    },
    {
        "name": "HD 109271",
        "luminosity":1.649 ,
        "radius":1.295,
        "temperature":5783,
        "distance":	182.1,
        "exoplanets": [0.079,0.196,1],
        "planet_labels": ["1.HD 109271-b", "2.HD 109271-c", "3.HD 109271-d"],
        "eccentricity": ["0.25", "0.15", "0.36"],
        "status": ["Inhabitable", "Inhabitable", "Unconfirmed and Inhabitable"],
        "mass": ["0.054 Mass of Jupiter", "0.076 Mass of Jupiter", "1.3 Mass of Jupiter"],
        "orbital_period_period_period_period": ["7.8543", "30.93", "430"]
        
    },
    {
        "name": "HD 108236",
        "luminosity":0.707 ,
        "radius":0.876,
        "temperature":5660,
        "distance":	210.6,
        "exoplanets": [0.0451,0.0626,0.1087,0.1348,0.1773],
        "planet_labels": ["1.HD 108236-b", "2.HD 108236-c", "3.HD 108236-d", "4.HD 108236-e", "5.HD 108236-f"],
        "eccentricity": ["0.067", "0.091", "0.075","0.073","0.024"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable","Inhabitable","Inhabitable"],
        "mass": ["4.23 ", "8.90", "7.75","8.2","3.95"],
        "orbital_period_period_period_period": ["3.7958785", "6.2036717", "14.175818","19.5901277" , "29.53935"]
        
    },
    {
        "name": "V1298 Tauri",
        "luminosity":0.934 ,
        "radius":1.33,
        "temperature":4970 ,
        "distance":	354,
        "exoplanets": [0.0825,0.1083,0.1688,0.308],
        "planet_labels": ["1.V1298 Tauri-b", "2.V1298 Tauri-c", "3.V1298 Tauri-d", "4.V1298 Tauri-e"],
        "eccentricity": ["0.43", "0.21", "0.29","0.57"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable","Inhabitable"],
        "mass": ["17 ", "41", "20","0.66"],
        "orbital_period_period_period_period": ["8.24958", "12.4032", "24.1396 ","50.29" ]
        
    },
    {
        "name": "HIP 41378",
        "luminosity":1.6 ,
        "radius":1.25,
        "temperature":6251 ,
        "distance":	345.7,
        "exoplanets": [0.1283,0.2161,0.3227,0.88,1.06,1.37],
        "planet_labels": ["1.HIP 41378-b", "2.HIP 41378-c", "3.HIP 41378-g", "4.HIP 41378-d","5.HIP 41378-e","6.HIP 41378-f"],
        "eccentricity": ["0.07", "0.04", "0.06","0.06 ","0.14","0"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable","Inhabitable","Inhabitable","Habitable"],
        "mass": ["6.89 ", "4.4 ", "7.0","4.6","12","12"],
        "orbital_period_period_period_period": ["15.57208", "31.706038", "62.06 ","278.3618","369","542.07975" ]
        
    },
    {
        "name": "WASP-132",
        "luminosity":0.253 ,
        "radius":0.753,
        "temperature":4714 ,
        "distance":	403,
        "exoplanets": [0.01833,0.0674,2.71],
        "planet_labels": ["1.WASP-132-c", "2.WASP-132-b", "3.WASP-132-d"],
        "eccentricity": ["Unsure", "0.0163", "0.120"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["6.26 ", "0.428 ", "5.16"],
        "orbital_period_period_period_period": ["1.01153624", "7.1335164", "1816.6 "]
        
    },
    {
        "name": "WASP-47",
        "luminosity":1.16 ,
        "radius":1.16,
        "temperature":5576  ,
        "distance":	881,
        "exoplanets": [0.017,0.052,0.087,1.42],
        "planet_labels": ["1.WASP-47-e", "2.WASP-47-b", "3.WASP-47-d","4.WASP-47-c"],
        "eccentricity": ["0.03", "	0.0028", "0.00600","0.296"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable", "Habitable"],
        "mass": ["9.0 ", "363.6 ", "15.5","398.9"],
        "orbital_period_period_period_period": ["0.789592", "4.1591289", "9.03077 ","588.5 "]
        
    },
     {
        "name": "HAT-P-13",
        "luminosity":4.0 ,
        "radius":1.73,
        "temperature":5720  ,
        "distance":800,
        "exoplanets": [0.04313,1.188],
        "planet_labels": ["1.HAT-P-13-b", "2.HAT-P-13-c"],
        "eccentricity": ["0.0093", "0.6616"],
        "status": ["Inhabitable", "Inhabitable"],
        "mass": ["0.906 Mass of Jupiter ", "14.28  Mass of Jupiter "],
        "orbital_period_period_period_period": ["2.91624039", "445.81"]
        
    },
    {
        "name": "Kepler-25",
        "luminosity":2.406 ,
        "radius":1.297,
        "temperature":6270  ,
        "distance":787,
        "exoplanets": [0.068,0.11,0.416422],
        "planet_labels": ["1.Kepler-25-b", "2.Kepler-25-c","3.Kepler-25-d"],
        "eccentricity": ["0.0029", "0.0061","0.13"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["8.7 ", "15.2","71.9"],
        "orbital_period_period_period_period": ["6.238297", "12.7207","122.4"]
        
    },
    {
        "name": "Kepler-48",
        "luminosity":0.5137 ,
        "radius":0.897,
        "temperature":5160  ,
        "distance":1010,
        "exoplanets": [0.054,0.086,0.23,1.9,5.7],
        "planet_labels": ["1.Kepler-48-b", "2.Kepler-48-c","3.Kepler-48-d","4.Kepler-48-e","5.Kepler-48-f"],
        "eccentricity": ["Unsure","Unsure","Unsure","0.003","0.01"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["6.8 ", "11.1","9","2.16 Mass of Jupiter","0.93 Mass of Jupiter"],
        "orbital_period_period_period_period": ["4.78", "9.67","42.9","1001","5205"]
        
    },
    {
        "name": "Kepler-88",
        "luminosity":0.598 ,
        "radius":0.897,
        "temperature":5466,
        "distance":1231,
        "exoplanets": [0.098,0.15525,2.45],
        "planet_labels": ["1.Kepler-88-b", "2.Kepler-88-c","3.Kepler-88-d"],
        "eccentricity": ["0.05561","0.05724","0.41"],
        "status": ["Inhabitable", "Inhabitable", "Inhabitable"],
        "mass": ["9.5 ", "0.674 Mass of Jupiter","3.05 Mass of Jupiter"],
        "orbital_period_period_period_period": ["10.91647", "22.26492","1403"]
        
    },
    {
        "name": "HD 38529",
        "luminosity":6.16 ,
        "radius":2.678,
        "temperature":5619,
        "distance":137.54,
        "exoplanets": [0.1278,3.226],
        "planet_labels": ["1.HD 38529-b", "2.HD 38529-c"],
        "eccentricity": ["0.259","0.357"],
        "status": ["Inhabitable", "Inhabitable"],
        "mass": ["0.8047 ", "10.380"],
        "orbital_period_period_period_period": ["14.30978", "2127.6"]
        
    }, {
        "name": "Kepler-442",
        "luminosity":1.2 ,
        "radius":1.11,
        "temperature":5757,
        "distance":1810,
        "exoplanets": [0.409],
        "planet_labels": ["1.Kepler-442-b"],
        "eccentricity": ["0.04"],
        "status": ["Habitable"],
        "mass": ["2.3"],
        "orbital_period_period_period_period": ["112.3053"]
        
    },
    {
        "name": "Kepler-452",
        "luminosity":0.117 ,
        "radius":0.6,
        "temperature":4402,
        "distance":1196,
        "exoplanets": [1.046],
        "planet_labels": ["1.Kepler-452-b"],
        "eccentricity": ["-"],
        "status": ["Inhabitable"],
        "mass": ["5"],
        "orbital_period_period_period_period": ["384.843"]
    
    },
    {
        "name": "Kepler-22",
        "luminosity":0.79 ,
        "radius":0.869,
        "temperature":5596,
        "distance":644,
        "exoplanets": [0.812],
        "planet_labels": ["1.Kepler-22-b"],
        "eccentricity": ["0.72"],
        "status": ["Inhabitable"],
        "mass": ["9.1"],
        "orbital_period_period_period_period": ["289.863"]
    },
    {
        "name": "HD 1461",
        "luminosity":1.1893 ,
        "radius":1.2441,
        "temperature":5386,
        "distance":76.5,
        "exoplanets": [0.0634, 0.1117],
        "planet_labels": ["1.HD 1461-b", "2.HD 1461-c"],
        "eccentricity": ["0.131", "0.228"],
        "status": ["Inhabitable","Inhabitable"],
        "mass": ["6.44", "5.59"],
        "orbital_period_period_period_period": ["5.771", "13.5052"]
    }
]

# Create the main window
root = tk.Tk()
root.title("Habitable Zone Mapping")
root.geometry("800x1000")  # Set a larger window size
root.configure(bg="#f0f0f0")  # Set background color

# Define a larger font
font_large = ("Helvetica", 14)

# Header
header_label = tk.Label(root, text="Habitable Zone Mapping", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
header_label.pack(pady=20)

# Planetary system selection frame
system_frame = tk.Frame(root, bg="#f0f0f0")
system_frame.pack(pady=10, padx=20, fill="x")

system_label = tk.Label(system_frame, text="Select a Planetary System:", font=font_large, bg="#f0f0f0")
system_label.pack(anchor="w")

system_combobox = ttk.Combobox(system_frame, values=[system["name"] for system in planetary_systems], font=font_large)
system_combobox.pack(fill="x", pady=5)

select_button = tk.Button(system_frame, text="Show System Details", command=select_planetary_system, font=font_large, bg="#4CAF50", fg="white")
select_button.pack(pady=10)

# Details frame
details_frame = tk.Frame(root, bg="#f0f0f0")
details_frame.pack(pady=10, padx=20, fill="x")

details_label = tk.Label(details_frame, text="", font=("Helvetica", 12), justify="left", bg="#f0f0f0", anchor="w")
details_label.pack(fill="x")

# Exoplanet selection frame
exoplanet_frame = tk.Frame(root, bg="#f0f0f0")
exoplanet_frame.pack(pady=10, padx=20, fill="x")

exoplanet_label = tk.Label(exoplanet_frame, text="Select an Exoplanet:", font=font_large, bg="#f0f0f0")
exoplanet_label.pack(anchor="w")

exoplanet_combobox = ttk.Combobox(exoplanet_frame, font=font_large, state="readonly")
exoplanet_combobox.pack(fill="x", pady=5)

exoplanet_button = tk.Button(exoplanet_frame, text="Show Exoplanet Details", command=select_exoplanet, font=font_large, bg="#4CAF50", fg="white")
exoplanet_button.pack(pady=10)

exoplanet_data_label = tk.Label(exoplanet_frame, text="", font=("Helvetica", 12), justify="left", bg="#f0f0f0", anchor="w")
exoplanet_data_label.pack(fill="x")

# Custom data input frame
custom_frame = tk.Frame(root, bg="#f0f0f0")
custom_frame.pack(pady=20, padx=20, fill="x")

custom_label = tk.Label(custom_frame, text="Or Enter Custom Data:", font=font_large, bg="#f0f0f0")
custom_label.pack(anchor="w")

luminosity_label = tk.Label(custom_frame, text="Luminosity (in Solar luminosity):", font=font_large, bg="#f0f0f0")
luminosity_label.pack(anchor="w")
luminosity_entry = tk.Entry(custom_frame, font=font_large)
luminosity_entry.pack(fill="x", pady=5)

exoplanets_label = tk.Label(custom_frame, text="Exoplanets (comma-separated, in AU):", font=font_large, bg="#f0f0f0")
exoplanets_label.pack(anchor="w")
exoplanets_entry = tk.Entry(custom_frame, font=font_large)
exoplanets_entry.pack(fill="x", pady=5)

planet_labels_label = tk.Label(custom_frame, text="Planet Labels (comma-separated):", font=font_large, bg="#f0f0f0")
planet_labels_label.pack(anchor="w")
planet_labels_entry = tk.Entry(custom_frame, font=font_large)
planet_labels_entry.pack(fill="x", pady=5)

plot_button = tk.Button(custom_frame, text="Plot Custom Data", command=plot_custom_data, font=font_large, bg="#4CAF50", fg="white")
plot_button.pack(pady=10)

# Run the application
root.mainloop()
