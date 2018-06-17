def nhapmang ( array_ ):
    array_ = []
    So_phantu = int (input("Nhap so phan tu trong mang "))
    array_.insert(0, 2)
    Tong = 0
    for i in range (So_phantu):
        if i%2==1:
            array_.insert(i, -1)
        else:
            Tong = Tong + 1
            array_.insert(i, mang[0]-0.5*Tong)
    print(*array_, sep = ". ")