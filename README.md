Nama    : Naufal Mahdy Hanif
NPM     : 2206082335
Kelas   : E

1.
- Cara menyelesaikan checklist membuat project baru, saya membuat direktori baru lalu menginisiasi git pada direktori tersebut.
- Saya mengkonfigurasi git pada direktori tersebut.
- Saya membuat repository pada github lalu menghubungkannya dengan local repository.
- Saya membuat virtual environment lalu menjalankan virtual environment.
- Saya menginstall dependencies yang dibutuhkan termasuk django.
- Saya start project AmbatuStore, lalu mengkonfigurasi host.
- Saya membuat aplikasi main, lalu mengkonfigurasi app project pada settings.py
- saya menmbuat templates html lalu menginiasi boilerplate dan mengkustomisasi desain pada template menggunakan bootstrap.
- saya mendesain model sesuai dengan nama atribut dan tipe field yang dibutuhkan.
saya melakukan migrasi model lalu mendefine fungsi untuk merender tampilan html pada views.py.
- saya mengkonfigurasi routing untuk page main dan page items pada tingkat app.
- saya mengkonfigurasi routing untuk app main pada tingkat project.
- saya test apakah status code dan page yang diberikan dari request main sudah aman dan sesuai.
- saya melakukan add, commit, dan push ke github repository.

2. ![alt text](Static\Screenshot (283).png)

3. Agar environments yang digunakan untuk django dan dapat dengan mudah direplikasi pada environment yang berbeda, juga memastikan agar tidak terjadi konflik pada versi dependensi yang berbeda pada project yang berbeda. Bisa untuk membuat aplikasi berbasis django tanpa memulai virtual environment, tapi beresiko untuk terjadi konflik dependensi pada proyek yang berbeda. 

4. 
- MVT adalah konsep arsitektur web yang memisahkan komponen-komponen utama dari webapp tersebut. Model yang dimaksud adalah komponen yang bertugas untuk mengelola data dari aplikasi, komponen yang bertugas pada bidang logika dan struktur data. View adalah komponen yang menangani presentasi, tampilan yang akan disajikan pengatur data dari model untuk ditampilkan. Template adalah komponen untuk tampilan yang digunakan untuk menstruktur data dari view pada tampilan untuk user.
- MVC adalah model yang membagi pengembangan webapp pada tiga komponen. Model adalah komponen yang menyimpan data aplikasi, model bertanggung jawab untuk mengatur logic dan komunikasi dengan database. View bertanggung jawab untuk user interface. COntroller bertanggung jawab untuk membangun hubungan antara model dan view.
- MVVM memiliki model yang memiliki tiga komponen, yaitu Model, View, dan ViewModel. Model adalah komponen yang bertangungjawab pada abstraksi dari sumber data. View adalah komponen yang bertanggungjawab untuk memberitahu viewmodel tentang aksi dari user. Viewmodel adalah komponen yang menghubungkan model dan view. Viewmodel juga bertanggungjawab untuk pengolahan.
