def calculate_taxi_fare(vehicle_type, distance_km, waiting_minutes):
    if vehicle_type == 4:
        initial_fare = 11000  # Giá mở cửa cho xe 4 chỗ
        price_per_km_within_20km = 12100  # Giá trong phạm vi 20km cho xe 4 chỗ
        price_per_km_beyond_20km = 10000  # Giá từ km thứ 21 trở đi cho xe 4 chỗ
    elif vehicle_type == 7:
        initial_fare = 13000  # Giá mở cửa cho xe 7 chỗ
        price_per_km_within_30km = 14100  # Giá trong phạm vi 30km cho xe 7 chỗ
        price_per_km_beyond_30km = 12000  # Giá từ km thứ 31 trở đi cho xe 7 chỗ
    else:
        return "Loại xe không hợp lệ. Vui lòng chọn 4 hoặc 7 chỗ."

    if distance_km <= 0:
        return "Khoảng cách không hợp lệ."

    if vehicle_type == 4:
        if distance_km <= 0.8:
            fare = initial_fare
        elif distance_km <= 20:
            fare = initial_fare + (distance_km - 0.8) * price_per_km_within_20km
        else:
            fare = initial_fare + 19.2 * price_per_km_within_20km + (distance_km - 20) * price_per_km_beyond_20km
    elif vehicle_type == 7:
        if distance_km <= 0.8:
            fare = initial_fare
        elif distance_km <= 30:
            fare = initial_fare + (distance_km - 0.8) * price_per_km_within_30km
        else:
            fare = initial_fare + 29.2 * price_per_km_within_30km + (distance_km - 30) * price_per_km_beyond_30km

    # Xử lý tiền chờ
    if waiting_minutes > 5:
        waiting_fee = (waiting_minutes - 5) * 800
        fare += waiting_fee

    return fare

# Nhập thông tin và tính cước
vehicle_type = int(input("Nhập loại xe (4 hoặc 7 chỗ): "))
distance_km = float(input("Nhập khoảng cách (km): "))
waiting_minutes = int(input("Nhập thời gian chờ (phút): "))

fare = calculate_taxi_fare(vehicle_type, distance_km, waiting_minutes)
if isinstance(fare, str):
    print(fare)
else:
    print(f"Cước taxi là: {fare} đồng")