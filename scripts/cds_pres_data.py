import cdsapi

c = cdsapi.Client()

start_date = '20190112'
end_date   = '20190115'

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type':'reanalysis',
        'format':'grib',
        'pressure_level':[
            '1','2','3',
            '5','7','10',
            '20','30','50',
            '70','100','125',
            '150','175','200',
            '225','250','300',
            '350','400','450',
            '500','550','600',
            '650','700','750',
            '775','800','825',
            '850','875','900',
            '925','950','975',
            '1000'
        ],
        'date':f'{start_date}/{end_date}',
        'area':'12/90/-12/150',
        'time':'00/to/23/by/6',
        'variable':[
            'geopotential','relative_humidity','specific_humidity',
            'temperature','u_component_of_wind','v_component_of_wind'
        ]
    },
    f'ERA5-{start_date}-{end_date}-pl.grib')
