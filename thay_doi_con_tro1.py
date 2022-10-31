import turtle


# Chỉ cho phép là hình tròn, hình vuông và hình con rùa
hinh_dang = input("Nhập vào hình dáng mong muốn của con trỏ: ")
# Chỉ cho phép màu đỏ, màu xanh da trời, màu vàng
mau_sac = input("Nhập vào màu sắc cho con trỏ: ")

turtle.bgcolor("black")
turtle.title("Chương trình thay đổi hình dáng màu sắc con rùa")
# Kiểm tra biến hình dáng người dùng nhập vào có đúng không
# Kiểm tra màu sắc người dùng nhập vào có đúng không

 # Kiểm tra hình dáng
if(hinh_dang == "circle" or hinh_dang == "square" or hinh_dang == "turtle"):
    turtle.shape(hinh_dang)
    #Kiểm tra màu sắc
    if(mau_sac == "red" or mau_sac == "blue" or mau_sac == "yellow"):
        turtle.color(mau_sac)
    else:
        print("Màu sắc nhập vào không hợp lệ")
else:
    print("Hình dáng nhập vào không hợp lệ")

    
    
turtle.done()