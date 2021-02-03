# Script tính điểm CPA và GPA các kỳ ở Bách khoa HN
## tl;dr
Tính điểm CPA/GPA HUST, tool hoạt động ổn tính đến ngày 03/02/2021.


## Introduction
Script này được sinh ra là bởi CPA và GPA các kỳ ở HUST thường cập nhật chậm, nhất là khi điểm thi lên hết rồi mà vẫn chưa có. Với một đứa thiếu kiên nhẫn như mình thì điều này là không chấp nhận được. 



## Setup & Run
Cài đặt thư viện dể đọc file .xlsx:
```bash
pip3 install -r requirements.txt
```

Để chạy thì đầu tiên bạn vào trang [CTT-SIS Bảng điểm cá nhân](https://ctt-sis.hust.edu.vn/Students/StudentCourseMarks.aspx) rồi copy bảng vào file `all_grades.xlsx`. Nếu mà điểm thi mới nhất chưa có thì bạn có thể thêm thủ công vào file excel.

Chạy script:
```py
python3 calculate_gpa_and_cpa.py
```



## Known issues
Vì mình viết vội script này trong 15 phút (ít hơn cả thời gian mình viết cái README này) nên là code rất dirty.

Để đảm bảo script hoạt động chuẩn thì bạn cần kiểm tra các cột sau đây:
- Cột 0: kỳ học (vd: 20201)
- Cột 3: số tín chỉ (vd: 2)
- Cột 7: tổng điểm theo chữ (vd: A+)



