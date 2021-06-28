# Data

Data yang digunakan adalah data suhu udara bulanan (1850-2005) dan RCP 4.5 (2006-2100) dari model ACCESS dan data Climate Research Unit (CRU). Model ACCESS memiliki resolusi spasial 1.875 x 1.25, sedangkan CRU memiliki resolusi spasial 0.5 x 0.5. Pengolahan data dilakukan menggunakan bahasa pemrograman R. *Package* R yang dibutuhkan adalah sebagai berikut. 

```r
library(raster)
library(fields)
library(rasterVis)
library(ncdf4)
library(PCICt)
```