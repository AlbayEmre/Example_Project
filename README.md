# Buggy Project

Bu proje Coverity ve benzeri statik analiz araçlarında test yapılması için bilerek hatalı kodlar içerir.

### İçerdiği Açıklar:
- `null_bug.py`: NoneType üzerinden erişim hatası
- `unreachable_bug.py`: Ulaşılamayan kod
- `type_bug.py`: Hatalı tip kullanımı (int + str)
- `logic_bug.py`: Mantıksal hata (tek sayıları çift sanmak)
- `loop_bug.py`: Sonsuz döngü

> Not: `main.py` içerisinde sonsuz döngü yoruma alınmıştır, çalıştırmak istersen satırı açabilirsin.
