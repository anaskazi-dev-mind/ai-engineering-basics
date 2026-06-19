raw_names = ["rAhUl", "AnAs", "YuSuF", "eLoN Musk", "     "]

clean_names = [name.strip().title() for name in raw_names if name.strip != ""]

print(clean_names)