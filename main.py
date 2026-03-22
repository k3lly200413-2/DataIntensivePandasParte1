import numpy as np


def main():
    DATA_URL = "https://github.com/datascienceunibo/dialab2024/raw/main/Preprocessing_con_pandas/usa_census.npz"

    import os.path
    if not os.path.exists("usa_census.npz"):
        from urllib.request import urlretrieve
        urlretrieve(DATA_URL, "usa_census.npz")
    
    data = np.load("usa_census.npz")
    for name, array in data.items():
        print(f"{name:>15}: {array.dtype!s:>8} {array.shape}")
        # "!s" = converti in stringa con str(x) in modo da poter applicare formato
        # ">N" = riserva N caratteri e allinea a destra


if __name__ == "__main__":
    main()