# ================================
# BUS MANAGEMENT SYSTEM
# ================================

bus_list = []


# 1. Hàm xác định trạng thái lấp đầy
def xac_dinh_trang_thai(xe):

    empty_seats = xe["ghe_trong"]
    total_seats = xe["tong_ghe"]

    if empty_seats == 0:
        return "Hết vé"
    elif empty_seats < total_seats * 0.15:
        return "Hút khách"
    elif empty_seats <= total_seats * 0.8:
        return "Bình thường"
    else:
        return "Ế khách"



# Cập nhật doanh thu + trạng thái
def cap_nhat_xe(xe):

    sold_seats = xe["tong_ghe"] - xe["ghe_trong"]

    xe["doanh_thu"] = xe["gia_ve"] * sold_seats
    xe["trang_thai"] = xac_dinh_trang_thai(xe)



# ================================
# HIỂN THỊ DANH SÁCH
# ================================

def hien_thi_ds():

    if len(bus_list) == 0:
        print("Danh sách chuyến xe đang trống!")
        return


    print("\n" + "=" * 120)


    print(
        f"{'Mã CX':<10}"
        f"{'Tuyến đường':<25}"
        f"{'Giá vé':<15}"
        f"{'Ghế trống':<12}"
        f"{'Tổng ghế':<12}"
        f"{'Doanh thu':<18}"
        f"{'Trạng thái':<15}"
    )


    print("-" * 120)


    for bus in bus_list:

        print(
            f"{bus['ma']:<10}"
            f"{bus['tuyen']:<25}"
            f"{bus['gia_ve']:<15}"
            f"{bus['ghe_trong']:<12}"
            f"{bus['tong_ghe']:<12}"
            f"{bus['doanh_thu']:<18}"
            f"{bus['trang_thai']:<15}"
        )


    print("=" * 120)




# ================================
# THÊM CHUYẾN XE
# ================================

def them_xe():

    bus_id = input("Nhập mã chuyến xe: ").upper()


    if bus_id == "":
        print("Mã không được để trống!")
        return



    for bus in bus_list:

        if bus["ma"] == bus_id:

            print("Mã chuyến xe đã tồn tại!")
            return



    route = input("Nhập tuyến đường: ")


    if route == "":
        print("Tuyến đường không được để trống!")
        return



    price = int(input("Nhập giá vé: "))

    total = int(input("Nhập tổng số ghế: "))



    if price <= 0 or total <= 0:

        print("Giá vé và số ghế phải > 0")

        return



    bus = {

        "ma": bus_id,

        "tuyen": route,

        "gia_ve": price,

        "ghe_trong": total,

        "tong_ghe": total,

        "doanh_thu": 0,

        "trang_thai": ""

    }



    cap_nhat_xe(bus)


    bus_list.append(bus)


    print("Thêm chuyến xe thành công!")





# ================================
# ĐẶT VÉ
# ================================

def dat_ve():

    bus_id = input("Nhập mã chuyến xe: ").upper()



    for bus in bus_list:


        if bus["ma"] == bus_id:


            quantity = int(input("Nhập số vé đặt: "))



            if quantity <= 0:

                print("Số vé phải lớn hơn 0")

                return



            if quantity > bus["ghe_trong"]:

                print("Không đủ ghế trống!")

                return



            bus["ghe_trong"] -= quantity


            cap_nhat_xe(bus)


            print("Đặt vé thành công!")

            return



    print("Không tìm thấy mã chuyến xe!")





# ================================
# XÓA CHUYẾN XE
# ================================

def xoa_xe():

    bus_id = input("Nhập mã chuyến xe cần xóa: ").upper()



    for bus in bus_list:


        if bus["ma"] == bus_id:


            confirm = input(
                "Bạn có chắc muốn xóa chuyến xe này khỏi lịch trình không? (Y/N): "
            )



            if confirm.upper() == "Y":

                bus_list.remove(bus)

                print("Đã xóa chuyến xe!")

            else:

                print("Đã hủy thao tác")

            return



    print("Không tìm thấy chuyến xe!")





# ================================
# TÌM KIẾM
# ================================

def tim_kiem():

    keyword = input(
        "Nhập mã CX hoặc tuyến đường cần tìm: "
    ).lower()



    result = []



    for bus in bus_list:


        if (
            bus["ma"].lower() == keyword
            or keyword in bus["tuyen"].lower()
        ):

            result.append(bus)



    if len(result) == 0:

        print("Không tìm thấy!")

        return



    print("Kết quả tìm kiếm:")



    for bus in result:

        print(
            bus["ma"],
            "|",
            bus["tuyen"],
            "|",
            bus["trang_thai"]
        )





# ================================
# THỐNG KÊ
# ================================

def thong_ke():

    count = {

        "Hết vé":0,

        "Hút khách":0,

        "Bình thường":0,

        "Ế khách":0

    }



    for bus in bus_list:

        count[bus["trang_thai"]] += 1



    print("\nTHỐNG KÊ")



    for key,value in count.items():

        print(key,":",value)


def display_menu():
    print("")
    print("")
    print("")
    print("")
    print("")

# ================================
# MENU
# ================================
def main():
    while True:

        choice = input("Chọn chức năng: ")

        match choice:

            case "1":
                hien_thi_ds()

            case "2":
                them_xe()

            case "3":
                dat_ve()

            case "4":
                xoa_xe()

            case "5":
                tim_kiem()

            case "6":
                thong_ke()

            case "7":
                print("Cảm ơn đã sử dụng hệ thống!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")

# chạy chương trình
menu()