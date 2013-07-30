#!/bin/bash

# Bu dosya üzerinde, betik çıktılarının işlenebilmesine yönelik değişiklikler yapılabilecektir.

# Her beş saniyede bir tekrarlanır.
while [ 1 ]; do

# ANKARA ölçüm değerleri
./temperature.py ANKARA
./pressure.py ANKARA
./wind.py ANKARA
./humidity.py ANKARA

# ISTANBUL ölçüm değerleri
./temperature.py ANKARA
./pressure.py ANKARA
./wind.py ANKARA
./humidity.py ANKARA

# IZMIR ölçüm değerleri
./temperature.py ANKARA
./pressure.py ANKARA
./wind.py ANKARA
./humidity.py ANKARA

# EDIRNE ölçüm değerleri
./temperature.py ANKARA
./pressure.py ANKARA

sleep 5

done
