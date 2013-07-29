# Django Meteoroloji Sitesi

Bu açıklama dokümanı, aşağıdaki bölümlerden meydana gelmektedir:

- **Amaç**, geliştirilecek projenin amacını tanımlamaktadır,
- **Ölçüm Cihazları**, projeye veri sağlayan ölçüm cihazlarının niteliklerini tanımlamaktadır,
- **Senaryo Betik Dosyası**, ölçümlerin toplanma faaliyetinin modellenmesinde kullanılacak senaryo mekanizmasını açıklamaktadır,
- **Portal**, django çatısı kullanılarak geliştirilecek portal ile ilgili özellikleri tanımlamaktadır.
- **Kurallar**, geliştirme faaliyeti sırasında uyulması gereken kural ve prensipleri özetlemektedir,
- **Değer Katıcı Nitelikler**, geliştirilen üründe bulunması halinde proje değerini artıracak olup, daha ileri teknikler gerektirmeleri itibarı ile ayrı tutulmuş özellikleri tanımlamaktadır.

## Amaç

Projenin amacı, farklı coğrafi konumlara yerleştirilmiş ölçüm cihazlarından alınan hava durumu verilerinin görüntüleneceği bir portal oluşturmaktır.

## Ölçüm Cihazları

Sensörlerden gelen veriler, proje deposu **test** dizini altında hazır olarak verilmiş olan betik dosyaları tarafından sağlanacaktır. Söz konusu betik dosyaları, sensörlerin değiştirilemez çıktılarını tanımladıkları için, bu dosyaların değiştirilmemeleri gerekmektedir.

Tüm ölçüm cihazı betik dosyaları çalıştırılırken konum (location) bilgisini girdi olarak alacaklardır.

Bu betik dosyalarının her birinin kullanım açıklamaları, takip eden bölümler altında verilmektedir.

### Sıcaklık Ölçüm Cihazı

Sıcaklık ölçüm cihazı çıktısı, **test** dizini altında yer alan **temperature.py** python betiği tarafından modellenmektedir.

Betik çalıştırıldığında,

    [location]|[time]|[temperature]

biçimine uygun çıktı üretmektedir. Bu biçim içerisinde,

* **[location]**, ölçüm cihazının bulunduğu konum (şehir, vb.) bilgisi,
* **[time]**, "Yıl-Ay-Gün Saat:Dakika:Saniye" biçiminde zaman bilgisi,
* **[temperature]**, derece cinsinden sıcaklık bilgisi

olarak üretilmektedir. Bu bağlamda örnek bir girdi-çıktı işlemi,

    $ ./test/temperature.py ANKARA

    ANKARA|2013-07-29 18:30:05|29.2C

biçiminde olacaktır.

### Basınç Ölçüm Cihazı

Basınç ölçüm cihazı çıktısı, **test** dizini altında yer alan **pressure.py** python betiği tarafından modellenmektedir.

Betik çalıştırıldığında,

    [location]|[time]|[pressure]

biçimine uygun çıktı üretmektedir. Bu biçim içerisinde, **location** ve **time** alanları Sıcaklık Ölçüm Cihazı başlığı altında belirtildiği biçimde olup,

* **[pressure]**, mm cıva cinsinden basınç değeri

olarak üretilmektedir. Bu bağlamda örnek bir girdi çıktı işlemi,

    $ ./test/pressure.py KONYA
    
    KONYA|2013-07-29 18:40:19|758.4mmHg

biçiminde olacaktır.

### Nem Ölçüm Cihazı

Nem ölçüm cihazı çıktısı, **test** dizini altında yer alan **humidity.py** python betiği tarafından modellenmektedir.

Betik çalıştırıldığında,

    [location]|[time]|[humidity]

biçimine uygun çıktı üretmektedir. Bu biçim içerisinde, **location** ve **time** alanları Sıcaklık Ölçüm Cihazı başlığı altında belirtildiği biçimde olup,

* **[humidity]**, yüzde cinsinden nemlilik değeri

olarak üretilmektedir. Bu bağlamda örnek bir girdi-çıktı işlemi,

    $ ./test/humidity.py MERSIN
    
    MERSIN|2013-07-30 04:12:17|51.9%

biçiminde olacaktır.

### Rüzgar Ölçüm Cihazı

Rüzgar ölçüm cihazı çıktısı, **test** dizini altında yer alan **wind.py** python betiği tarafından modellenmektedir.

Betik çalıştırıldığında,

    [location]|[time]|[speed]|[direction]

biçimine uygun çıktı üretmektedir. Bu biçim içerisinde, **location** ve **time** alanları Sıcaklık Ölçüm Cihazı başlığı altında belirtildiği biçimde olup,

* **[speed]**, knots biriminde rüzgar hızı,
* **[direction]**, kuzeyden ölçülen derece biriminde rüzgar yönü

olarak üretilmektedir. Bu bağlamda örnek bir girdi-çıktı işlemi,

    $ ./test/wind.py IZMIR
    
    IZMIR|2013-07-30 07:14:24|18knts|130deg

biçiminde olacaktır.

## Senaryo Betik Dosyası

Ölçüm cihazlarından değer alınma senaryoları, yine **test** dizini altında yer alacak olan senaryo betik dosyaları tarafından yerine getirilecektir. Bu dizin altında bulunan **scenario.sh** örnek senaryosu referans alınarak, geliştirilecek uygulamanın testine yönelik yeni senaryo betikleri, yine bu dizin altında oluşturulabilecektir.

Her bir yeni senaryo betiğinin kısa tanımlaması, betik dosyası başında açıklama satırları ile belirtilecektir.

## Portal

Django ile geliştirilecek web portalinin yerine getirmesi beklenen görev, birden fazla noktada çalıştırılabilecek olan ölçüm cihazlarından alınacak çıktıları bir veritabanında toplamak ve bu verileri konumlara göre sınıflandırarak son kullanıcıya anlamlı bir durum özeti sunmaktır.

Bu kapsamda geliştiricinin, önceki bölümlerde tarif edilen ölçüm cihazı çıktılarını *gerçek-zamanlı* olarak işleyerek veritabanına aktarmak için bir çözüm oluşturması gerekmektedir.

Betik dosyalarından dinamik olarak akmakta olan bilgilerin, django uygulaması tarafından gerçek ölçüm cihazlarından gelen veriler olarak kabul edilmesi ve seçilen bir konum için, o konumdan en son raporlanan tüm ölçüm bilgilerini dinamik olarak kullanıcıya sunması gerekmektedir.

## Kurallar

- Geliştirme sırasında Django-1.5.1 sürümü kullanılacaktır.

- Proje, geliştiricinin django çatısını kullanım kabiliyetini ölçme amaçlı verildiği için, kullanıcı arayüzlerinin çok detaylı olması beklenmemektedir. Ancak, sağlanacak kullanıcı arayüzünün, yalın ve kolay kullanımlı olması beklenmektedir.

- Proje deposu içerisinde django proje çatısı oluşturulmuştur. Geliştirme sırasında bu çatıya uyulması beklenmektedir.

- Proje ayarlarında kullanılacak mutlak dizinlerin farklı bilgisayarlar üzerinde sorun olmaması adına, geliştirme faaliyetlerinin ```/srv/DjangoChallenge``` mutlak dizini altında gerçekleştirilmesi beklenmektedir.

- Tanımlanacak veritabanı modelleri için django admin arayüzünün faal hale getirilmesi istenmektedir.

- Geliştirme sırasında kaydedilen ilerlemenin depoya toplu olark değil, sık ve düzenli olarak aktarımı (commit/push) beklenmektedir.

- Kullanılması beklenen kütüphane ve diller, HTML5, CSS3, Javascript için JQuery, python/Django ve betikler için python/bash'tir.

## Değer Katıcı Nitelikler

- Sayfa içeriklerinin güncellenmesi için jquery/ajax tekniklerine başvurulması,

- Dinamik istemci (tarayıcı) güncellemeleri için socket.io vb. kullanımı,

- Tanımlanan amacı zenginleştirici (ölçümlere yönelik grafik vb.) ek içerik.

- Geliştirme sırasında proaktif bir tutum izlenmesi ve akla gelen yapıcı önerilerin paylaşılması.

## Öneriler ve Kaynaklar

- [Django Project](http://www.djangoproject.com) ve [Django Book](http://www.djangobook.com) web siteleri geliştirme sırasında en sağlam referans kaynağı olacaktır. Özellikle ihtiyaç duyulması halinde, ["tutorial"](https://docs.djangoproject.com/en/1.5/intro/tutorial01/) bölümünün tekrarlanması faydalı olacaktır.

- Bir oturuşta projeyi tamamlamaya çalışmak yerine, ara dönüm noktalarında geri bildirim alınarak geliştirme yapılması, ileride yaşanabilecek zaman kayıplarının ve hedeften sapmaların asgari seviyede kalmasını sağlayacaktır.

