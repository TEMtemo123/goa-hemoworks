# დაუსრულებელი სია, რომელიც შეიცავს სხვადასხვა კატეგორიას
categories = [
    {
        "category": "მანქანა",
        "favorites": [
            "mersedes banan",   # 1 ადგილი
            "mersedes gt 63",          # 2 ადგილი
            "mersedes akula",          # 3 ადგილი
        ]
    },
    {
        "category": "ხილი",
        "favorites": [
            "ვაშლი",         # 1 ადგილი
            "მსხალი",         # 2 ადგილი
            "ბანანი"            # 3 ადგილი
        ]
    },
    {
        "category": "საკვები",
        "favorites": [
            "პიცა",             # 1 ადგილი
            "ჰამბურგერი",       # 2 ადგილი
            "სუში"            # 3 ადგილი
        ]
    },
    {
        "category": "ფილმი",
        "favorites": [
            "THOR",   # 1 ადგილი
            "spiderman",     # 2 ადგილი
            "marvel"        # 3 ადგილი
        ]
    }
]

# სიის დაბეჭდვა
for category in categories:
    print(f"კატეგორია: {category['category']}")
    print("საყვარელი:")
    for index, favorite in enumerate(category['favorites'], start=1):
        print(f"{index}. {favorite}")
    print()  # ცარიელი ხაზი სექციების შორის

