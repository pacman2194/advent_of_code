data = [ 1974, 1773, 1841, 1932, 1951, 1852, 2000, 1988, 1998, 1670, 969, 2008, 1713, 2007, 1916, 1286, 1652, 1821, 1730, 2002, 1761, 1656, 814, 1999, 2010, 1936, 1794, 1905, 1250, 1920, 1986, 1709, 1914, 1681, 1820, 1982, 1961, 1931, 1331, 1923, 1972, 1631, 1643, 1719, 1926, 1994, 1952, 1981, 1847, 1774, 1296, 1946, 873, 2005, 173, 2006, 1960, 1872, 1894, 1695, 1769, 1800, 1734, 1675, 1860, 1383, 1947, 1768, 1827, 1877, 1721, 1738, 384, 1996, 1958, 1909, 1639, 1831, 1212, 1627, 1699, 1661, 1653, 1748, 1919, 1983, 1223, 1690, 1948, 1218, 1971, 1969, 1753, 1957, 1977, 1943, 1978, 1778, 1937, 1868, 1641, 1979, 1854, 1959, 1739, 2004, 1964, 760, 1890, 1701, 1940, 1840, 1817, 1966, 1799, 1941, 1934, 1929, 1962, 1691, 1927, 1764, 1945, 795, 1993, 1804, 1693, 1970, 1728, 1818, 1545, 1992, 1965, 1786, 2009, 1980, 1698, 1647, 1935, 1880, 1921, 1904, 1953, 1871, 1671, 1826, 1989, 1950, 1791, 1990, 1949, 1301, 1975, 1968, 1895, 1208, 1424, 1985, 1665, 1685, 1942, 1669, 64, 1832, 1995, 1987, 1955, 352, 1984, 1925, 1891, 1933, 1679, 2001, 1930, 1991, 1227, 1973, 1723, 1683, 132, 1718, 1944, 1908, 1900, 1657, 1954, 92, 1997, 1938, 1976, 1747, 1226, 1782, 1963, 1746, 1540, 1759, 1939, 1743 ]
data.sort()

def two_sum(data, goal):
    """
    return a tuple containing the two numbers whose sum is equal to the goal
    """
    i = 0
    j = -1
    while True:
        if i - j == len(data):
            return None
        if data[i] + data[j] > goal:
            j -= 1
        elif data[i] + data[j] < goal:
            i += 1
        else:
            return data[i], data[j]

def three_sum(data, goal):
    """
    return a tuple containing the three numbers whose sum is equal to the goal
    """
    i = 0
    j = -1
    for k in range(0, len(data)-2):
        new_goal = goal - data[k]
        new_data = data[k+1:]
        while True:
            if i - j == len(new_data):
                i = 0
                j = -1
                break
            if new_data[i] + new_data[j] > new_goal:
                j -= 1
            elif new_data[i] + new_data[j] < new_goal:
                i += 1
            else:
                return new_data[i], new_data[j], data[k]

result = two_sum(data, 2020)
if result == None:
    print('No solution found.')
else:
    print(f'{result[0]} + {result[1]} = {result[0] + result[1]}')
    print(f'{result[0]} * {result[1]} = {result[0] * result[1]}')

result = three_sum(data, 2020)
if result == None:
    print('No solution found.')
else:
    print(f'{result[0]} + {result[1]} + {result[2]}  = {result[0] + result[1] + result[2]}')
    print(f'{result[0]} * {result[1]} * {result[2]}  = {result[0] * result[1] * result[2]}')
