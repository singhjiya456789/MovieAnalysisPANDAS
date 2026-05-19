import pandas as pd 

data = {
    "Movie": [
        "Angoor", "Jaane Bhi Do Yaaro", "3 Idiots", "Stree",
        "Sholay", "Dhoom", "War", "Krrish",
        "Dilwale Dulhania Le Jayenge", "Kabir Singh", "Jab We Met", "Veer-Zaara",
        "Hum Saath Saath Hain", "Kabhi Khushi Kabhie Gham", "Bajrangi Bhaijaan", "Taare Zameen Par",
        "Koi... Mil Gaya", "Ra.One", "Robot", "PK"
    ],

    "release_year": [
        1982, 1983, 2009, 2018,
        1975, 2004, 2019, 2006,
        1995, 2019, 2012, 2004,
        1999, 2001, 2015, 2007,
        2003, 2011, 2010, 2014
    ],

    "rating": [
        8.3, 8.2, 8.4, 7.5,
        8.1, 6.7, 7.1, 7.3,
        8.0, 7.0, 7.6, 7.4,
        7.9, 8.1, 8.5, 8.4,
        7.2, 6.8, 7.6, 7.8
    ],

    "views": [
        1200000, 900000, 5000000, 3000000,
        7000000, 6000000, 4500000, 5500000,
        8000000, 4000000, 3500000, 5000000,
        2500000, 6000000, 10000000, 7000000,
        3000000, 4500000, 4000000, 6500000
    ],

    "genres": [
        "Comedy", "Comedy", "Comedy", "Comedy",
        "Action", "Action", "Action", "Action",
        "Romance", "Romance", "Romance", "Romance",
        "Family", "Family", "Family", "Family",
        "Sci-Fi", "Sci-Fi", "Sci-Fi", "Sci-Fi"
    ]
}

df = pd.DataFrame(data)



while True:
    print("Movie Analysis Using Pandas")
    print("1.show All Movie")
    print("2.Highest Rated Movie")
    print("3.oldest Movie")
    print("4.Newest Movie")
    print("5.Most watched Movie")
    print("6.show movie genre wise.")
    print("7.Most popular Movie")
    print("8.Exit")
    choice = input("Enter the choice :")
    print()
    if choice == "1":
        print(df)
    elif choice =="2":
        highrated=df[df["rating"]==df["rating"].max()]
        print(highrated)
    elif choice =="3":
        oldest=df[df["release_year"]==df["release_year"].min()]
        print(oldest)
    elif choice=="4":
        newest = df[df["release_year"]==df["release_year"].max()]
        print(newest)
    elif choice=="5":
        mostwatched=df[df["views"]==df["views"].max()]
        print(mostwatched)
    elif choice =="6":
        print(df.groupby("genres")["Movie"].apply(list))
    elif choice =="7":
        df["Popular"] = df["views"] * df["rating"]

        popular = df.sort_values(by="Popular", ascending=False)

        print(popular[["Movie", "Popular"]])
        print(popular.head())
    elif choice =="8":
        print("Enjoy movie :) ")
        break
    else:
        print("Invalid choice")
    