import numpy as np
import pandas as pd

def getSquareArea(array_to_use):
    return array_to_use * 2.59

def getDensity(population, area):
    return population / area

def main():
    DATA_URL = "https://github.com/datascienceunibo/dialab2024/raw/main/Preprocessing_con_pandas/usa_census.npz"

    import os.path
    if not os.path.exists("usa_census.npz"):
        from urllib.request import urlretrieve
        urlretrieve(DATA_URL, "usa_census.npz")
    
    data = np.load("usa_census.npz")
    # for name, array in data.items():
        # print(f"{name:>15}: {array.dtype!s:>8} {array.shape}")
        # "!s" = converti in stringa con str(x) in modo da poter applicare formato
        # ">N" = riserva N caratteri e allinea a destra

    population = pd.Series(data["population"], index=data["states"])
    
    print(population.head(7))   
    
    print(population.values[:5])
    print(population.index[:5])
    print(len(population))
    print(population.size)
    
    
    # Prints the value associated with the Key
    print(population["California"])
    # Prints the values between the two keys
    print(population["Arizona": "Colorado"])
    # Same thing but if sorted prints the Keys between the two letters 
    print(population["S": "V"])
    
    west_coast = ["Washington", "Oregon", "California"]

    print(population[west_coast])
    
    area = pd.Series(data["area"], index=data["states"])
    other_state = pd.Series(data["other_state"], index=data["states"])
    from_abroad = pd.Series(data["from_abroad"], index=data["states"])

    print("population\n")
    print((population / 1_000_000).head(3))
    print("\nlog10")
    print(np.log10(population).head(3))
    print("\narea")
    area_km2 = getSquareArea(area)
    print(getSquareArea(area)[:3])
    print("\nDensity")
    print(getDensity(population, getSquareArea(area))[:3])
    
    is_small = area <= 5000
    print(is_small.head(10))
    print("\n")
    print(area[area <= 5000])
    # Same as area[is_small]
    
    print("\n")
    # places that are smaller than 5000 and have more than 1000000 citizens 
    print(population[is_small & (population > 1_000_000)])
    
    
    print("\n", population.sum())
    print("\n", population.max())
    # etichetta del valore maggiore
    print("\n", population.idxmax())
    # same with min
    print("\nArea min\n")
    print(area.idxmin())
    print("\ndensity\n")
    print(getDensity(population[area.idxmin()], area[area.idxmin()]))

    print("\n",(population > 1_000_000).sum())
    
    print("\npopulation\n", population[west_coast].sum())
    print("\n avarege density with at least 10M\n", getDensity(population[population>=10_000_000], area).mean())
    
    census = pd.DataFrame({
    "population": population,
    "from_abroad": from_abroad,
    "area": area_km2
    })
    
    # print(census.head(5))
    
    # first four rows
    # print(census.values[:4])
    # first four states
    # print(census.index[:4])
    # print(census.columns)
    # number or rows and columns
    # print(census.shape)
    
    # We pass a matrix that shows how many people moved from one state to another and as rows and columns we have the names of the states
    # columns is from where rows is to where people go
    state_to_state = pd.DataFrame(data["state_to_state"], index=data["states"], columns=data["states"])
    # print(state_to_state)
    
    # print(state_to_state.head(5))
    print(census["population"].head(3))
    
    census["density"] = census["population"] / census["area"]
    
    print(census.describe())
    
    print(census["area"].idxmax())
    
    print(state_to_state["Arizona"].sum())
    
    print(state_to_state.sum(axis=1).idxmin())
    
    # Selections
    print(census.loc["California", :"from_abroad"])
    
    print(census.loc[census["population"] < 700_000])
    
    print(state_to_state.iloc[:3, :5])
    
    # print only the first 3 rows and only the column population
    print(census.iloc[:3].loc[:, "population"])
    
    print(census.sort_values("population", ascending=False).head(5))
        
if __name__ == "__main__":
    main()