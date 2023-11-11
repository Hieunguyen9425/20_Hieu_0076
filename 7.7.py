def doi_tien(money):
    menh_gia = [500000, 200000, 100000, 50000]
    so_to_tien = []
    tien_du = money

    for menhgia in menh_gia:
        so_to = tien_du // menhgia
        if so_to > 0:
            so_to_tien.append((menhgia, so_to))
            tien_du %= menhgia

    return so_to_tien, tien_du

so_tien_goc = 1375000
so_to_tien, tien_du = doi_tien(so_tien_goc)

print(f"Số tiền muốn đổi: {so_tien_goc}")
for menhgia, so_to in so_to_tien:
    print(f"Số tờ {menhgia}: {so_to} ")
print(f"Tiền còn lại: {tien_du}")
