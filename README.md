# GIF Atölyesi (videotogif)

ezgif.com tarzı, tamamen çevrimdışı çalışan **video → GIF** uygulaması. Tek HTML dosyası; sunucu, kurulum ve internet gerektirmez. Windows için ~2,6 MB'lık hafif bir `.exe` sürümü de var.

## Kullanım

- **Tarayıcıda:** `gif-atolyesi.html` dosyasını Chrome ile açın.
- **Windows uygulaması:** `releases/GifAtolyesi.exe` dosyasına çift tıklayın (kendi penceresinde açılır). Sistemde *Microsoft Edge WebView2 Runtime* olmalıdır (Windows 11'de ve güncel Windows 10'da hazır gelir).

## Özellikler

- **Video → GIF:** başlangıç/bitiş, boyut (genişliğe/yüksekliğe göre), kırpma (oran veya siyah kenarları otomatik kaldırma).
- **Her şey videodan okunur:** çözünürlük, süre ve kare hızı (FPS) videodan algılanır; kare sayısı için sabit bir sınır yoktur, tek sınır belleğe sığmaktır. Canlı bellek tahmini gösterilir, "Belleğe sığdır" boyutu otomatik küçültür. 1080p'ye kadar çözünürlük desteklenir.
- **Akış modu:** kareler belleğe biriktirilmeden çıkarıldıkça GIF'e kodlanır; bellek sabit kalır. Belleğe sığmayan işler (ör. 1080p, 35 sn) otomatik bu modda yapılır, düzenleme araçları o çıktıda kapalıdır. Kareler oynatma sırasında ardışık yakalanır (kare başına arama yapılmaz), bu yüzden hızlıdır.
- **Çıktı:** k-means / Floyd–Steinberg / Bayer / dither yok, 8–256 renk, tek veya kare başına palet, kare farkı optimizasyonu, döngü sayısı, hedef boyuta (KB) sıkıştırma.
- **Düzenleme:** boyutlandır, kırp, döndür/çevir, ters çevir, hız, bumerang, efektler, metin, resim ekle, sansür, tuval, kare silme/çoğaltma/taşıma/kesme, geri al.
- **Kaynaklar:** videodan, görsellerden, mevcut GIF'ten, ekran kaydından.
- **Dışa aktarma:** GIF, MP4/WebM, PNG kareleri (ZIP), tek kare PNG.

## Sınırlar

- Video biçimini tarayıcı çözer; MP4 (H.264), WebM, OGG genelde çalışır, AVI/WMV/FLV/MKV'nin çoğu açılmaz.
- GIF en fazla 50 fps destekler (10 ms gecikme tarayıcılarda 100 ms'ye yuvarlanır).

## Yapı

```
gif-atolyesi.html      tek dosya uygulama (kaynak)
releases/GifAtolyesi.exe   Windows (Neutralino + WebView2), ~2,6 MB
desktop/               exe projesi (Neutralino yapılandırması, kaynaklar)
icon/                  ikon (PNG, ICO) ve üretim betiği
```

## exe'yi yeniden derleme

```bash
cp gif-atolyesi.html desktop/resources/index.html
cd desktop
npm i -g @neutralinojs/neu            # bir kez
neu update                            # bin/ ve resources/js/neutralino.js indirir
node tools/set_icon.js bin/neutralino-win_x64.exe ../icon/icon.ico   # (npm i resedit gerekir)
neu build --release --embed-resources
# çıktı: dist/GifAtolyesi/GifAtolyesi-win_x64.exe
```
