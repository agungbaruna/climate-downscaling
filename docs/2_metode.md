# Metode *Statistical Downscaling*

*Statistical Downscaling* melibatkan hubungan antara data historis atmosfer dalam skala besar dengan karakteristik iklim lokal. Secara komputasi, sumber daya yang diperlukan untuk menerapkan pendekatan ini lebih efisien dan murah jika dibandingkan dengan pendekatan *Dynamical Downscaling*. Akan tetapi, metode ini memerlukan data observasi dengan kualitas data yang tinggi dan kemungkinan hanya bisa diterapkan pada data bulanan.    

## Metode Delta

Cara paling sederhana melakukan *downscaling* dari data GCM adalah dengan mencari faktor atau **delta** dan kemudian ditambahkan ke data observasi pada periode dasar. Metode ini dapat digunakan apabila data pada periode tertentu memiliki distribusi normal, seperti suhu udara dan curah hujan bulanan dan tidak dapat diterapkan pada data distribusi non-normal, seperti curah hujan harian serta tidak cocok pada analisis ekstrem. Delta didefinisikan sebagai perbedaan antara rata-rata klimatologi (30 tahun) dari variabel iklim pada periode masa depan dan historis. 

Langkah-langkah *downscaling* menggunakan metode Delta adalah sebagai berikut [@navarro2020].

1. Menghitung rata-rata variabel iklim 30 tahun pada periode dasar (*baseline*) dari model GCM
2. Menghitung anomali/delta antara rata-rata 30 tahun data masa depan dengan data dasar dengan persamaan $\Delta X_{i} = X_{Fi} - X_{Ci}$ untuk data suhu udara 
sedangkan persamaan $\Delta X_{i} = \frac{X_{Fi} - X_{Ci}}{X_{Ci}}$ untuk data curah hujan, dimana $X_{Fi}$ dan $X_{Ci}$ secara berturut-turut adalah rata-rata data 30 tahun di masa depan dan historis pada bulan ke-i. 
3. Mengubah nilai dari data grid menjadi data point untuk kemudian dilakukan interpolasi
4. Tambahkan data grid hasil interpolasi ke data iklim observasi dengan persamaan $X_{DCi} = X_{OBSi} + \Delta X_{Ii}$ untuk data suhu udara dan persamaan $X_{DCi} = X_{OBSi} * (1 + \Delta X_{Ii})$ untuk data curah hujan, dimana $X_{Fi}$ dan $X_{Ci}$ secara berturut-turut adalah rata-rata data 30 tahun di masa depan dan historis pada bulan ke-i. 

## Metode Regresi Linier 

Selain metode Delta, teknik *Statistical Downscaling* dengan metode regresi linier juga mudah dilakukan. Metode regresi linier menghubungkan antara variabel atmosfer yang berperan sebagai prediktor (mis. ketinggian geopotensial, kelembapan spesifik) dengan variabel cuaca lokal yang berperan sebagai prediktan (mis. curah hujan dan suhu udara). Metode ini cukup sering digunakan dari beberapa penelitian [@pahlavan2018] [@huth2000] [@goly2014] [@sachindra2014].

\begin{equation} \label{eq:mlr}
  Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_n X_n 
\end{equation}

Prediktor dari data GCM perlu diseleksi yang memiliki korelasi tertinggi terhadap prediktan. Jika terdapat banyak prediktor yang akan digunakan untuk mengestimasi prediktan, korelasi antar prediktor perlu dihindari. Beberapa cara untuk menyeleksi prediktor tersebut di antaranya adalah metode *Stepwise Regression*, *Artificial Neural Networks* (ANN), dan *Mixed Integer Non Linear Programming* (MINLP) [@teegavarapu2018]. 

\bibliography