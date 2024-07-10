Code này chỉ để thử đẩy 1 folder lên github ^__^

### B1: Kết nối với SSH trên Ubuntu:
     
      ssh-keygen -t rsa -b 4096 -C "thichchoivelkoz@gmail.com"
Nó hỏi gì thì cứ nhấn Enter, bước này là để tạo khóa SSH.
Khởi động ssh-agent:
     
      eval "$(ssh-agent -s)"
Thêm khóa SSH vào ssh-agent:
     
      ssh-add ~/.ssh/id_rsa
Lệnh tiếp theo trả về cái gì thì copy hết mã đó, rồi tạo SSH key trên github ở B2
     
      cat ~/.ssh/id_rsa.pub
### B2: Tạo SSH key trên github của bạn:
Đăng nhập vào GitHub và truy cập Settings.
     
      https://github.com/settings/keys
Trong phần "SSH and GPG keys", nhấp vào "New SSH key".
Đặt một tiêu đề cho khóa (ví dụ: "Ubuntu Laptop") và dán nội dung khóa SSH công khai mà bạn đã sao chép vào ô "Key".
Nhấp vào "Add SSH key" để thêm khóa.
### B3: Chạy lệnh sau để test xem kết nối SSH đã oke chưa:
     
      ssh -T git@github.com
Nếu hiện: Hi username! You've successfully authenticated, but GitHub does not provide shell access.
--> Success!
### B4: Nếu folder đã được git init thì chạy git push, nếu không:
     
      echo "# RobotVisai" >> README.md
      git init
      git add README.md
      git commit -m "first commit"
      git branch -M main
      git remote add origin git@github.com:phamduyaaaa/RobotVisai.git
      git push -u origin main
