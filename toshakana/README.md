- Lỡ đặt tên toshakana rồi bây h đổi thì sợ lỗi nên để luôn
- sử dụng câu lệnh để chạy web: python3 manage.py runserver 0.0.0.0:8000

1. Cài django để tạo môi trường ảo chạy web:
- sử dụng python 3
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website
- tạo môi trường ảo mkvirtualenv my_django_environment
- xoá môi trường ảo rmvirtualenv my_django_environments



2. cài mariadb
- cài này quên mất để làm j rồi: sudo pip3 install virtualenvwrapper
- stop mariadb: brew services stop mariadb
- start mariadb: brew services start mariadb
- restart mariadb: brew services restart mariadb
- tên cơ sở dữ liệu: weather_his
- thông tin cơ sở dữ liệu: nằm ở /toshakana/settings.py dòng 78 : DATABASES

3. Kết nối db:
https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04
- python3 manage.py makemigrations
- python3 manage.py migrate
- truy cập vào web local của mình sử dụng link: http://127.0.0.1:8000/homepage/

4. tạo bảng 
- Script_db_toshakana.sql : chứa script để tạo bảng và import bảng trong cơ sở dữ liệu weather_his

5. sử dụng django-pandas:


n. Không biết để làm gì
- chưa thấy tác dụng của nó trong bài này: dăng nhập vào đây http://127.0.0.1:8000/admin
sử dụng
Username (leave blank to use 'phanngl'): thaonguyen
Email address: thao.nguyentt2811@hcmut.edu.vn
Password:12345678