Nama    : Naufal Mahdy Hanif
NPM     : 2206082335
Kelas   : E
Adaptable : https://ambatustore.adaptable.app/


Tugas 2 :
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

Tugas 3:
1. POST adalah method yang digunakan untuk submit data atau mengirim data ke database atau API, sedangkan GET adalah method untuk mengambil data atau fetch data dari database atau API.
2. HTML mempresentasikan object data dalam struktur saat web diload
    XML merepresentasikan data dalam bentuk pohon yang memiliki anak, setiap elemen dimuat dalam sebuah tag yang memiliki closing tag
    JSON merepresentasikan data dalam bentuk yang mirip javascript object, data dalam bentuk name/value, lebih mudah digunakan daripada xml
3. JSON lebih dipilih karena compact, simpel, lebih cepat untuk diparse dan dibuat untuk aplikasi AJAX.
4. 
- Saya menmbuat forms berdasarkan model yang sudah saya buat di forms.py
- saya membuat fungsi di views untuk menyimpan data yang disubmit oleh forms POST.
- saya membuat fungsi di views untuk fetch data dari database baik dengan filter maupun untuk semua object item, yang data tersebut akan digunakan di show_items, show_json, show_xml, show_json_by_id, show_xml_by_id.
- saya membuat path url untuk mengakses fungsi pada views.py
- saya mengkustomisasi page html agar dapat menerima data yang disediakan dari views.py dan juga dapat menjalankan beberapa perintah seperti for loop untuk membuat row table sesuai jumlah data yang ada.
- saya memberi sedikit styling pada page-page yang sudah ada di folder static, dan mengkonfigurasi direktori static di settings.py, lalu menginclude static pada template yang sudah ada.
- saya menambah bonus dengan menampilkan jumlah item yang ada di menu item
5. 
- ![HTML ONLY](static\screenshots\SS HTML.png)
- ![JSON ID](static\screenshots\SS JSON ID.png)
- ![JSON ONLY](static\screenshots\SS JSON.png)
- ![XML ID](static\screenshots\SS XML ID.png)
- ![XML ONLy](static\screenshots\SS XML.png)

Tugas 4:
1. usercreationform adalah sebuah kelas di django yang dapat digunakan untuk menciptakan user pada django, kita tidak perlu membuat form user lagi secara manual namun bisa menggunakan usercreationform. kelebihan dari menggunakan usercreationform adalah dapat wujudnya yang bisa digunakan langsung tanpa perlu banyak menulis kode lagi, sementara kekurangan dari usercreationform adalah kustomisasi yang minim, dan field yang bisa ditebak.

2. Autentikasi adalah proses memverifikasi siapa kita, sementara Autorisasi adalah proses untuk memastikan bahwakita memiliki akses untuk sesuatu. Keduanya penting untuk menjaga bagian-bagian dari web-app berdasarkan privilege sehingga terhindar dari hal-hal yang tidak diinginkan.

3. Lebih aman jika dibanding denang persistent cookie. Namun, default session cookie masih memiliki beberapa potensi kelemahan seperti bisa ditap jika kita mengakses web melalui public network. Orang lain bisa menyalahgunakan cookie yang diambil tersebut.

4. 
- Saya mengimport modul yang dibutuhkan untuk redirect, menggunakan usercreationform, memberi pesan, autentikasi, login, dan logout
- Saya membuat fungsi register dan login pada views.py, pada register saya menggunakan usercreationform sebagai form.
- saya mengimpor kedua fungsi tersebut ke urls.py lalu membuat path untuk kedua fungsi tersebut.
- saya menyiapkan templates untuk halaman register dan login, kedua templates tersebut saya hubungkan dengan stylesheet dan script bootstrap
- saya mengutilisasi package widget tweaks untuk memberi class pada input-input form di halaman register
- saya membuat fungsi untuk logout pada views.py, lalu menngimpor fungsi logout di urls.py dan membuat path untuk logout
- saya menambahkan button logout pada navbar untuk semua page, kecuali page login dan register
- saya merestriksi akses halaman main, create_item, dan item dengan login_required
- saya menset cookie last_login pada fungsi login, dan menambahkan request.user.username pada menu main dan item
- saya menambahkan atribut last_login menggunakan cookie last_login pada halaman main
- saya juga menambahkan untuk menghapus cookie pada logout
- saya membuat hubungan antara model item dengan user, meggunakan foreignkey, sehingga item terhubung dengan user. fungsi seperti create item juga saya ubah untuk menyesuaikan.
- pada fungsi show_item, saya menunjukkan item berdasarkan filter user yang saat ini sedang mengakses.
- saya melakukan migrasi dan selesai.
- saya sempat menambahkan metode untuk update amount dan delete item dengan menambahkan value id pada button dan memberi nama button lalu mengakses via fungsi create_item di views.py