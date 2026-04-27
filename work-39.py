

# 48 EKUK (LCM)
def ekuk(a, b):
    return a * b // ekub(a, b)

# 49 EKUK3
def ekuk3(a, b, c):
    return ekuk(ekuk(a, b), c)

# 50 TimeToHMS
def time_to_hms(T):
    h = T // 3600
    m = (T % 3600) // 60
    s = T % 60
    return h, m, s

# 51 IncTime
def inc_time(h, m, s, t):
    total = h*3600 + m*60 + s + t
    return time_to_hms(total)

# 52 Kabisa yil
def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

# 53 Oy kunlari
def month_days(m, y):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    elif m == 2:
        return 29 if is_leap(y) else 28

# 54 Oldingi sana
def prev_date(d, m, y):
    d -= 1
    if d == 0:
        m -= 1
        if m == 0:
            m = 12
            y -= 1
        d = month_days(m, y)
    return d, m, y

# 55 Keyingi sana
def next_date(d, m, y):
    d += 1
    if d > month_days(m, y):
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
    return d, m, y

# 56 Masofa
def leng(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# 57 Perimetr
def perim(x1,y1,x2,y2,x3,y3):
    return (leng(x1,y1,x2,y2) +
            leng(x2,y2,x3,y3) +
            leng(x3,y3,x1,y1))

# 58 Yuza (Heron)
def area(x1,y1,x2,y2,x3,y3):
    a = leng(x1,y1,x2,y2)
    b = leng(x2,y2,x3,y3)
    c = leng(x3,y3,x1,y1)
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

# 59 Masofadan balandlik
def dist(xa,ya,xb,yb,xp,yp):
    s = area(xa,ya,xb,yb,xp,yp)
    ab = leng(xa,ya,xb,yb)
    return 2*s/ab

# 60 Uchburchak balandliklari
def heights(xa,ya,xb,yb,xc,yc):
    ha = dist(xb,yb,xc,yc,xa,ya)
    hb = dist(xa,ya,xc,yc,xb,yb)
    hc = dist(xa,ya,xb,yb,xc,yc)
    return ha, hb, hc




