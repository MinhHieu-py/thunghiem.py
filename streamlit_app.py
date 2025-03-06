import streamlit as st

# Dữ liệu cho từng loại khủng long
dinosaur_data = {
    "Khuung long bay": {
        "Pteranodon": {
            "image": "https://static.wikia.nocookie.net/isle/images/2/29/The_isle_pteranodon_new_2020.jpeg/revision/latest?cb=20200825030749",
            "thong tin":'Chi Thằn lằn bay không răng, từ Creta muộn, là chi thằn lằn bay sống cách đây 89,3-70,6 triệu năm trước ở Bắc Mỹ, là một trong những chi thằn lằn bay lớn nhất với sải cách lên đến 6 mét. Pteranodon không phải khủng long',
            "video": "https://youtu.be/9-KxJFkgExo?si=USf_UMGVNRLG-Kea",
        },
        "Quetzalcoatlus": {
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtjmVHQIuc4QExLAb-ECAa34XPhG77ybVIXw&s",
            "thong tin":"là một chi Pterosauria sống vào cuối kỷ Creta ở Bắc Mỹ (tầng Maastrichtian) là động vật bay lớn nhất cùng với Hatzegopteryx vì 2 loài này lớn ngang nhau, khi đứng thẳng chúng cao ngang hươu cao cổ.",
            "video": "https://youtu.be/YvQRH1BvKSk?si=iWPcibNSPpyOPXnx",
        },
        "Pterosaur": {
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-YL40xp3kCkWOFUci-_k78vF6JVmOa7v_lA&s",
            "thong tin " :" bất kỳ loài bò sát biết bay nào phát triển mạnh trong tất cả các thời kỳ ( kỷ Trias , kỷ Jura và kỷ Phấn trắng ) của Kỷ Trung sinh (cách đây 252,2 triệu đến 66 triệu năm). Mặc dù pterosaur không phải là khủng long , nhưng cả hai đều là archosaur , một nhóm mà chim và cá sấu cũng thuộc về. Pterosaur không chỉ là loài bò sát đầu tiên có khả năng bay. Chúng cũng là động vật có xương sống đầu tiên biết bay.",
            "video": "https://youtu.be/mfYuvlE78Nk?si=CQZJ5A45YKpzpHSd",
        }
    },
    "Khủng long ăn cỏ": {
        "Triceratops": {
            "image": " https://upload.wikimedia.org/wikipedia/commons/1/1e/Triceratops_BW.jpg",
            'thong tin ':'Triceratops hay được gọi là khủng long ba sừng hay tam giác long là một chi khủng long ăn cỏ thuộc họ Ceratopsidae, sống vào thời kỳ cuối kỷ Phấn Trắng ở Bắc',
            "video": "https://youtu.be/c6hPCX9NDrg?si=ZVgfTAm8wyfab8Rj",
        },
        "Brachiosaurus": {
            "image": "https://www.extinctanimals.org/wp-content/uploads/2015/10/Brachiosaurus.jpg",
            'thong tin':'Brachiosaurus là một chi khủng long sauropoda sống cuối kỷ Jura ở thành hệ Morrison của Bắc Mỹ. Trong tiếng Việt, chúng còn được gọi là uyển long. Nó lần đầu tiên được mô tả bởi Elmer S. Riggs vào năm 1903 từ các hóa thạch được tìm thấy trên sông Grand Canyon của phía tây Colorado, Hoa Kỳ',
            "video": "https://youtu.be/9kV0J0kc1QM?si=MnogFKXsjzSR7zOH",
        },
        "Stegosaurus": {
            "image": "https://e.khoahoc.tv/photos/image/102012/24/Stegosaurus.jpg",
            'thong tin':'Stegosaurus là một chi khủng long phiến sừng thuộc cận bộ Stegosauria, sống từ Jura muộn ở miền Tây Bắc Mỹ ngày nay. Do những đuôi nhọn và bọc giáp, Stegosaurus là một trong những khủng long dễ nhận ra nhất, cùng với Tyrannosaurus, Triceratops, và Diplodocus.',
            "video": "https://youtu.be/Guw3g-Wz6c0?si=lIprc9Sd8TEofxD4",
        }
    },
    "Khủng long ăn thịt": {
        "Tyrannosaurus Rex": {
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRURbOL5cPNBYndb1jLrJL1FqVhWkGFw55c0w&s",
            "video": "https://youtu.be/s-vP7WgMkpA?si=VjkZRcB9HOWcebAd",
            'thong tin' : 'Tyrannosaurus  có nghĩa là thằn lằn bạo chúa, được lấy từ tiếng Hy Lạp "tyrannos" (τύραννος) nghĩa là "bạo chúa", và "sauros" (σαῦρος) nghĩa là "thằn lằn"[1]), còn được gọi là Khủng long bạo chúa trong văn hóa đại chúng, là một chi khủng long chân thú sống vào cuối kỷ Phấn Trắng. Chi này chỉ gồm một loài duy nhất là Tyrannosaurus rex (thường rút gọn là T. rex). Chúng sinh sống ở nơi ngày nay là phía Tây của Bắc Mỹ, khi đó là một lục địa đảo, tên là Laramidia. Hóa thạch của Tyrannosaurus được tìm thấy trong các thành hệ địa chất có niên đại tầng Maastricht, khoảng 67-65,5 triệu năm về trước,[2] và là một trong những loài khủng long cuối cùng tồn tại trước sự kiện tuyệt chủng Phấn Trắng – Cổ Cận.',
        },
        "Velociraptor": {
            "image": "https://www.nhm.ac.uk/content/dam/nhm-www/discover/dinosaur-velociraptor/049420_H-full-width.jpg.thumb.1160.1160.png",
            "video": "https://youtu.be/C-scNW7Xtb0?si=Af9DT-GI8AI3yHKu",
            'thong tin' : 'Velociraptor tên gọi tắt là Raptor, là một chi khủng long theropoda thuộc họ Dromaeosauridae từng tồn tại vào cuối kỷ Creta, khoảng 83 đến 70 triệu năm trước. Hiện có hai loài được công nhận, một loài khác từng được phân vào chi này.',
        },
        "Allosaurus": {
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGLVhlw-Mvw1-MqdZS05PmOW_w9_cGAQw3Hg&s",
            "video": "https://youtu.be/OTd8Mf7K0jA?si=nN77w6i-49mtrWru",
            'thong tin ' : 'Allosaurus là một chi khủng long chân thú carnosauria lớn sống vào kỷ Jura Muộn cách đây 155 - 145 triệu năm. Danh pháp "Allosaurus" nghĩa đen là "thằn lằn dị biệt" bởi đốt sống của loài này khá độc đáo tại thời điểm phát hiện. Cái tên này được lấy theo',
        }
    },
    "Khủng long dưới nước": {
        "Mosasaurus": {
            "image": "https://gstatic.gvn360.com/2020/01/mosasaurus3_8967.jpg",
            "video": "https://youtu.be/UQQeSnrVSMw?si=4SaJljgh0e8ystY-",
            "thong tin " : 'Mosasaurus là chi điển hình của họ Mosasauridae, một nhóm bò sát có vảy thủy sinh đã tuyệt chủng. Chúng từng sinh sống cách đây 82-66 triệu năm trong giai đoạn Champagne và Maastricht của thế Phấn Trắng muộn.',
        },
        "Plesiosaurus": {
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTq1aLTlv5zl3EH1ockZtKRdwRmlP-3ie18vQ&s",
            "video": "https://youtu.be/Q1GY3ZDqRZU?si=8jrp2lJuG-cUCvsv",
            'thong tin' : 'Plesiosauria là một bộ các bò sát biển lớn, ăn thịt. Chúng tồn tại và phát triển từ khoảng 245 triệu năm tới 65 mya. Mary Anning là người đầu tiên phát hiện ra plesiosaur. Bà đã tìm thấy nó ở  tại Dorset, Anh trong mùa đông cuối năm 1820 đầu năm 1821', 
        },
        "Liopleurodon": {
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOivbJ1lLb_74GAYXq92MplXmE-kMRn4r56g&s",
            "video": "https://youtu.be/GXXBCXzgsps?si=SjzDB8MneMsiz5T7",
            'thong tin' : 'Một loài pliosaur đáng chú ý là Liopleurodon , một chi được tìm thấy trong các trầm tích giữa kỷ Jura ở Anh và miền bắc nước Pháp. Liopleurodon có ý nghĩa quan trọng vì một số hóa thạch có chất lượng khác nhau, dài từ 5 đến 25 mét (16 đến 85 feet) đã được xếp vào chi này, khiến nhiều chuyên gia…',
        }
    }
}

st.title("Giới thiệu về khủng long")

# Chọn loại khủng long
dinosaur_type = st.selectbox("Chọn loại khủng long:", list(dinosaur_data.keys()))

# Chọn khủng long cụ thể
dinosaur_name = st.selectbox("Chọn khủng long cụ thể:", list(dinosaur_data[dinosaur_type].keys()))

# Hiển thị thông tin khủng long
selected_dino = dinosaur_data[dinosaur_type][dinosaur_name]
st.image(selected_dino["image"], caption=dinosaur_name)
st.video(selected_dino["video"])
st.write(selected_dino['thong tin'])

# Chọn số vé
num_tickets = st.slider("Chọn số vé:", 1, 10)

# Nút submit
if st.button("Nộp vé"):
    st.success(f"Bạn đã mua {num_tickets} vé để xem {dinosaur_name}!")
