# Metode *Downscaling* 

<span class='git-page-authors'>
    <b>Oleh:</b> 
    <a href='mailto:nooragung97@gmail.com'>
        Agung Baruna Setiawan Noor
    </a>
</span>

Metode *downscaling* adalah cara mendapatkan informasi lebih detil pada skala tinggi. Kata *downscaling* biasanya merujuk pada peningkatan resolusi spasial maupun temporal. Metode ini memiliki dua pendekatan, yaitu statistik dan dinamik. Di dalam ilmu iklim, metode ini umum digunakan pada model iklim global (*Global Climate Model*/GCM). 

GCM adalah alat utama dan paling komprehensif yang digunakan dalam simulasi iklim pada masa lalu maupun masa mendatang. GCM memiliki kemampuan dalam melakukan simulasi variabilitas iklim dan sifat-sifat fisis di permukaan bumi dengan perhitungan secara matematis yang menggambarkan proses, interaksi, dan timbal balik pada atmosfer, laut, dan biotik. Kelemahan dalam GCM adalah ketidakmampuan menangkap kejadian-kejadian iklim pada skala regional maupun lokal karena memiliki resolusi spasial yang terlalu kasar sekitar >100 km. Metode *downscaling* di dalam ilmu iklim umum digunakan pada kajian hidrologi [@piani2010suhu], pertanian [@glotter2014], dan sistem perkotaan [@smid2018].


# Kategori Teknik *Downscaling*

Wilby dan Wigley mengelompokkan teknik *downscaling* menjadi 4 kategori, yaitu [@wilby1997]:

### 1. Regresi

Metode regresi merupakan metode *downscaling* paling awal yang telah digunakan pada kajian perubahan iklim. Hal ini dapat dibuktikan dari penelitian oleh Kim pada tahun 1984 [@kim1984]. Pendekatan ini secara umum membangun hubungan linier atau non-linier antara parameter titik lokasi dengan prediktor variabel dari resolusi kasar. Contoh dari metode ini adalah regresi linier sederhana, regresi linier berganda, *artificial neural network* (ANN), regresi komponen utama (*Principle Component Regression*/PCR), dan lain sebagainya. Sudah banyak penelitian yang menerapkan metode ini untuk kajian perubahan iklim [@pahlavan2018] [@huth2000] [@goly2014] [@sachindra2014]. 

### 2. Pola cuaca (*Weather pattern approaches*)

Metode ini dibangun dari hubungan statistik dari variabel cuaca di stasiun observasi atau rata-rata area dengan klasifikasi cuaca tertentu yang dapat diturunkan secara objektif maupun subyektif. Prosedur secara objektif meliputi komponen utama, *canonical correlation analyses* (CCA), aturan *fuzzy*, dan neural networks. Contoh prosedur pengelompokkan pola cuaca, yaitu European Grosswetterlagen dan British Isles Lamb Weather Types. 

### 3. Model pembangkit cuaca stokastik

Model WGEN [@richardson1981] merupakan contoh dari pendekatan ini. Model WGEN dapat membangkitkan data curah hujan harian yang diperoleh dari peluang kejadian hujan (hujan dan tidak hujan) dengan menggunakan rantai Markov order satu. Model ini telah digunakan dalam kajian perubahan iklim dan analisis dampak. Model stokastik yang telah diperoleh dari data observasi deret waktu dapat divalidasi dengan GCM dan perlu dikalibrasi terlebih dahulu.

### 4. *Limited-area climate models* (LAM)

Opsi langkah terakhir untuk melakukan *downscaling* terhadap GCM adalah dengan menyematkan model iklim area terbatas yang beresolusi lebih tinggi. GCM digunakan sebagai penentuan kondisi batas. Sebenarnya, LAM pada waktu saat ini dapat diistilahkan sebagai *Regional Climate Model* (RCM). RCM memiliki resolusi spasial <100 km. RCM memerlukan sumber daya komputer yang hampir sama dengan menjalankan GCM. RCM memiliki kemampuan dalam mensimulasikan proses-proses atmosfer pada skala meso, seperti curah hujan orografis dan konveksi awan. Contoh dari RCM adalah *Weather Research Forecasting* (WRF) [@skamarock2019] dan RegCM.


\bibliography