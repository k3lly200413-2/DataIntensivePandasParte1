def main():
    DATA_URL = "https://github.com/datascienceunibo/dialab2024/raw/main/Preprocessing_con_pandas/usa_census.npz"

    import os.path
    if not os.path.exists("usa_census.npz"):
        from urllib.request import urlretrieve
        urlretrieve(DATA_URL, "usa_census.npz")


if __name__ == "__main__":
    main()