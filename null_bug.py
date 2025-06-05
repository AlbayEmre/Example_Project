def cause_null_bug():
    user = None
    print(user["name"])  # Null (None) obje üzerinden erişim hatası
