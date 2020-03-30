import numpy as np
import math 
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt

# parsing ASTOS
#11 -> acceleration (m/s2)
#33 -> altitdue (km)
#60 -> Atmosphere pressure (Pascal)
#64 -> Burn Time (s)
#76 -> Drag Force (kN)
#141 -> Mach Number (dimensionless)
#223 -> Speed of Sound (m/s)
#231 -> Total Thrust (kN)
df = pd.read_csv("ASTOS_TabsDelimited_24082019.txt", sep="\t", skiprows=3, usecols=[11,33,60,64,76,141,223,231], names=["acc","alt","atp","burn_t","drag_f","mach","sos","thrust"])

# Atmospheric pressure vs altitude
p = np.multiply(101325, np.exp(-df["alt"]/7.4))
altfig = plt.figure(figsize=(10,5))
plt.plot(df["alt"], p, label="Equation")
plt.plot(df["alt"], df["atp"], label="Astos" )
plt.title("Atmospheric Pressure vs Altitude (km)")
plt.legend()
## The two plots almost correspond

# Total compressive force on the rocket
total = np.add(df["drag_f"],df["thrust"])
totalplot = plt.figure(figsize=(10,5))
plt.plot(df["alt"],total, label="Total Compressive Load")
plt.plot(df["alt"], df["drag_f"], label="Drag Force")
plt.plot(df["alt"], df["thrust"], label="Engine Thrust")
plt.legend()
plt.title("Total Compressive Force (kN) vs Altitude (km)")
plt.savefig("maxq.png")

print("Maximum compressive load on the rocket is %s kN" %(max(total)))
idxmax = total.argmax()
velmax = np.multiply(df.loc[49,"sos"],df.loc[49,"mach"])
altmax = df.loc[49,"alt"]
print("Velocity and Altitude of max q is %s and %s" %(velmax,altmax))
print("Mach is %s" %(df.loc[49,"mach"]))
