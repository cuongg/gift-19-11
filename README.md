# Món quà 19/11

Website tĩnh đã build sẵn. Toàn bộ nội dung được phục vụ từ thư mục `dist`; không cần Node.js, cài dependencies hay chạy build.

## Deploy

- **Vercel:** Import repository, chọn Framework Preset `Other`, bỏ trống Build Command và đặt Output Directory là `dist`. Repository có sẵn `vercel.json`.
- **Netlify:** Import repository; cấu hình `netlify.toml` đã đặt thư mục publish là `dist`, không cần build.
- **Static hosting khác:** Upload toàn bộ nội dung bên trong `dist` vào thư mục gốc của website.

Ứng dụng sử dụng đường dẫn `/assets/...` và `/content.json`, vì vậy cần phục vụ ở gốc tên miền, không đặt dưới đường dẫn con.

## Chạy trên máy

Cài Python rồi nhấp đúp `MO-TRANG.cmd`, hoặc chạy `python start.py`.
Mở http://127.0.0.1:8765 và giữ cửa sổ máy chủ mở khi xem trang.
Không mở `dist/index.html` trực tiếp bằng `file://`.

## Chỉnh nội dung

Nội dung cá nhân nằm trong `dist/content.json`; ảnh, âm thanh và tài nguyên nằm trong `dist/assets`.
Đây là bản xuất đã build, không bao gồm mã nguồn React/Vite ban đầu.
