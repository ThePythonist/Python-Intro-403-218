info1 = {
    "name": "mellat",
    "type": "private",
    "services": ["financial", "banking", "insurance"],
    "shareholder": {
        "دولت جمهوری اسلامی ایران": 11.16,
        "شرکت سرمایه گذاری استان تهران": 1.72,
        "شرکت شیرین عسل": 1.21
    },
}

info2 = {
    "subsidiaries": ["صرافی ملت", "معین گردشگری ملت", "تجارت بین المللی آتیه"]
}

info1.update(info2)

print(info1)
