# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18b8AnWl2TqfPrQENTP4soqLTRaKOj1vq
"""

import pandas as pd
baza={
    "FISH":["Qadamova Zulayho", "Xalilov Durbek", "Djalilov M", "Jorayeva G", "Arabboyev A", "Turdimatov M", "Abdullayeva M", "Abduvaliyev I"],
    "Fan nomi":["Sun'iy intellekt", "Sun'iy intellekt", "Kompyuterni tahkil etish", "Elektronika va sxemalar", "Kiberxavfsizlik asoslar", "Kiberxavfsizlik asoslar", "Ma'lumotlar tuzilmasi va algoritmlar ", "Kompyuterni tashlik etish" ],
    "Mashg'ulot turi":["amaliy", "ma'ruza", "ma'ruza", "ma'ruza", "amaliy", "ma'ruza", "amaliy", "amaliy"],
    "Kafedrasi":["Axborot texnologiyalari", "Axborot texnologiyalari","Kompyuter tizimlari", "Tabiiy fanlar", "Axborot xavfsizligi", "Axborot xavfsizligi", "Axborot texnologiyalari", "Axborot texnologiyalari" ]
}

db=pd.DataFrame(baza)
print(db)

db.to_excel("teacher.xlsx")
print(db)