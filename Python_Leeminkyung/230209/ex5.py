'''2023-02-09
차트 그리기'''

import matplotlib.pyplot as plt

years=[1950,1960,1970,1980,1990,2000,2010]
gdp=[67.0, 80.0, 257.0, 1686.0, 605, 11865.3, 22105.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title('GDP per capita')

plt.ylabel("dollars")
plt.savefig('gdp_per_capita',dpi=600)