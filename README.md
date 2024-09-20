VietAI-x-CoderSchool

# Hướng Dẫn Fork và Clone Repository VietAI-x-CoderSchool

## Bước 1: Fork Repository
1. Truy cập vào repository GitHub tại [VietAI-x-CoderSchool](https://github.com/LeKhacDuy/VietAI-x-CoderSchool).
2. Ở góc trên bên phải, nhấp vào nút **Fork**. Điều này sẽ tạo một bản sao của repository dưới tài khoản GitHub của bạn.

## Bước 2: Clone Repository Đã Fork
1. Sau khi fork, vào tài khoản GitHub của bạn và tìm repository đã được fork.
2. Sao chép URL của repository bạn vừa fork. Nó sẽ trông như thế này:
   ```bash
   https://github.com/ten-tai-khoan-cua-ban/VietAI-x-CoderSchool.git
   ```
3. Mở terminal (hoặc Git Bash trên Windows), và chạy lệnh sau để clone repository về máy tính của bạn:
   ```bash
   git clone https://github.com/ten-tai-khoan-cua-ban/VietAI-x-CoderSchool.git
   ```
4. Di chuyển vào thư mục của repository:
   ```bash
   cd VietAI-x-CoderSchool
   ```

## Bước 3: Thêm Repository Gốc Là Remote Upstream
Để giữ cho bản fork của bạn luôn đồng bộ với repository gốc, hãy thêm repository gốc làm một remote có tên là `upstream`:
1. Chạy lệnh sau:
   ```bash
   git remote add upstream https://github.com/LeKhacDuy/VietAI-x-CoderSchool.git
   ```
2. Cập nhật thông tin mới của Git:
   ```bash
   git fetch upstream
   ```

### 3a. Nếu nhánh đó mới:
Sử dụng lệnh sau để chuyển sang nhánh đó:
   ```bash
   git checkout Ten_Nhanh
   ```

### 3b. Nếu nhánh đó cũ:
Sử dụng lệnh sau để merge thay đổi từ repository gốc:
   ```bash
   git merge upstream/Ten_Nhanh
   ```

## Các Lệnh Cơ Bản Khi Sử Dụng GitHub
- `git branch`: Hiển thị các nhánh bên trong dự án của bạn.
- `git checkout <Tên_Nhanh>`: Thay đổi nhánh của bạn.
- `git pull`: Lấy dữ liệu mới về từ remote.
- `git add`: Thêm thay đổi vào khu vực chuẩn bị (staging).
- `git commit -m "Tin nhắn commit"`: Chấp nhận thay đổi kèm theo lời nhắn.
- `git push`: Đẩy thay đổi lên GitHub.

**Lưu ý**: Khi muốn chuyển nhánh (branch), hãy commit toàn bộ thay đổi tại branch hiện tại trước khi đổi branch.

