import numpy as np
import pandas as pd

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

if __name__ == "__main__":
    main()