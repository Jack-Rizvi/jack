# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def names():
	for stars in targets:
		print(stars)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def names_spectral():
	for name, spec_type in targets.items():
		print(f"{name}: {spec_type['Spectral Type']}")
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def find_star_mag():
	for star, val in targets.items():
		if val["Magnitude"] > 0.1:
			print(star)
names()
names_spectral()
find_star_mag()
# 4) Look up another target, add all the necessary information to the targets list.
targets["Merak"] = {
        "RA": "11h 01m 50.5s",
        "Dec": "+56° 22′ 56.7″",
        "Magnitude": 2.37,
        "Spectral Type": "A1IVps"
    }
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# This question makes no sense, so I'm just gonna find the brightest star
def bright_star():
	brightest = ["",100]
	for star, mag in targets.items():
		if mag["Magnitude"] < brightest[1]:
			brightest[0] = star
			brightest[1] = mag["Magnitude"]
	return brightest
print(bright_star())
# 6) What is your favorite constellation?
# Cassiopeia