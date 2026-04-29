Title: Vibe Coding'in Çarptığı Duvar
Date: 2026-04-21 10:00
Category: AI
Tags: yapay-zeka, legacy-kod, vibe-coding
Slug: vibe-coding-in-carptigi-duvar
Summary: Claude Code, Cursor ve GitHub Copilot'u aynı anda açık bırakıp production'da çalışan gerçek bir legacy codebase'e girdim. Vibe coding vaatlerinin nerede çöktüğünü anlatan bir saha notu.

Bir noktada merak ettim: AI araçları gerçekten işe yarıyor mu, yoksa ben sadece temiz projelerde mi kullanıyorum?

Bu soruyu kafama taktıktan sonra bir deney yaptım. [Claude Code](https://docs.anthropic.com/en/docs/claude-code)'u, [Cursor](https://www.cursor.com/)'ı ve [GitHub Copilot](https://github.com/features/copilot)'u aynı anda açık bırakıp production'da çalışan eski bir codebase'e girdim. Üç araç, tek sistem, karşılaştırmalı test.

Sonuçlar beklediğimden çok farklıydı. Ama asıl sürpriz araçların başarısız olması değildi. *Neden* başarısız oldukları.

## Araçlar Hakkında Beklentilerimi Netleştirelim

Önce şunu söyleyeyim: AI kodlama araçları iyi. Gerçekten iyi. Temiz bir projede, modern bir stack'te, iyi tanımlanmış görevlerle çalışıyorsanız verimlilik artışı tartışmasız. Ben de günlük işlerimde kullanıyorum, faydasını görüyorum.

LinkedIn'de "vibe coding ile saatte SaaS yazdım" diyen insanları okuduğumda artık itiraz etmiyorum. Greenfield projede, doğru araçla, doğru bağlamda [bu tamamen mümkün](/blog/vibe-codingden-ajanlar-cagina.html). [Karpathy'nin önerdiği](https://x.com/karpathy/status/1886192184808149383) "sadece ne istediğini söyle, bırak yapsın" yaklaşımı bazı durumlarda gerçekten çalışıyor.

Ama bazı durumlarda çalışmıyor. Ve bu "bazı durumlar" yazılım dünyasının büyük çoğunluğunu kapsıyor.

## Sistemle Tanışma

Görevin kendisi netti: eskiyle yazılmış bir frontend'i modern bir framework'e taşımak. Ama bunu yapabilmek için mevcut sistemi anlamak gerekiyordu: hangi API'ler var, frontend ne çağırıyor, veri nereden geliyor?

Okumaya başladım.

Production'da yıllardır çalışan, kritik bir sistemdi. Dokümantasyonu ya yoktu ya da "bu metod ne yapıyor?" sorusuna "kodu oku" cevabı veriyordu. Backend'de günümüzde artık neredeyse kullanılmayan bir Python API kütüphanesi vardı. Modern alternatifleri milyonlarca satır açık kaynak örnekle eğitim setlerinde yer bulurken bu kütüphane yok denecek kadar az temsil ediliyor.

Frontend katmanından API katmanı olmadan direkt veritabanı çağrısı. Frontend'den direkt sistem komutu çağrısı, script tetikleme. Backend'de olması gereken iş mantığının önemli bir bölümü frontend'e sızmış.

Bu noktada şunu açıkça söylemek istiyorum: bu kodları yazan insanlar hakkında hiçbir yargım yok. O dönemin deadline'ları, o dönemin bilgisi, o dönemin kısıtlarıyla çalışmışlar. Bugün "temiz kod" diye öğretilen şeylerin yarısı o yıllarda henüz standart değildi. Ve büyük ihtimalle bugün biz de yarın birileri "bunlar ne yapmış?" diyeceği şeyler yazıyoruz.

Sorun mirasın kendisi değil, bu mirasa modern araçlar girdiğinde ne olduğu.

## Üç Araç, Bir Codebase

Claude Code sistemi taramaya başladı. Shell çağrılarını gördü. Veri akışının nerede başlayıp nerede bittiğini bulmaya çalıştı. Bağlantıları takip etti, ama bağlantılar standart değildi. Temiz bir REST endpoint yok, controller yok, service layer yok. AI'ın "bu bir API, bu bir model, bunlar birbirini şöyle çağırıyor" diyebileceği yapı yoktu.

Cursor öneriler verdi. Her önerisi "iyi kurulmuş bir sistemde böyle yapardık" mantığıyla geldi. Teknik olarak doğruydu. Ama mevcut sisteme entegre etmek imkansızdı, çünkü öneri var olan sistemi değil hayal edilen sistemi varsayıyordu: frontend'in nereye bağlandığını değil, nereye bağlanması gerektiğini.

GitHub Copilot shell çağrılarını görünce "bu güvensiz" diye işaretledi. Doğru teşhis. Ama alternatif öneremedi, çünkü bu sistemin bağlamında ne kullanılacağını bilemedi.

Üçü de farklı şekillerde çuvalladı. Ama dikkat edin: *halüsinasyon* değildi bu. Halüsinasyon "tamamen uydurulmuş bilgi" demek. Burada olan farklıydı: üç araç da gerçek ama standart dışı bir sistemi anlayamadı ve cevaplarını kendi training data'sındaki kalıplara göre verdi. Makine öğrenmesinde [**selection bias** (seçim yanlılığı)](https://en.wikipedia.org/wiki/Selection_bias) olarak bilinen bir sorun bu: model eğitim verisinde baskın olan kalıpları "normal" kabul eder, standart dışı bir yapıyla karşılaşınca onu kendi şablonuna göre yeniden yorumlar. Yani bu sistem için değil, *olması gereken* sistem için çalıştılar.

Copilot'un shell çağrısını "güvensiz" bulup sistemi "düzeltmeye" kalkıştığını hayal edin: yıllardır çalışan ama tuhaf olan o script'i siler, yerine "doğru" bir alternatif koyar ve production çöker. Doğru teşhis, yanlış eylem. Legacy sistemlerde en tehlikeli an AI'ın "şunu düzelteyim" dediği andır. [Amazon'un Mart 2026'da yaşadığı altı saatlik kesinti](https://www.digitaltrends.com/computing/ai-code-wreaked-havoc-with-amazon-outage-and-now-the-company-is-making-tight-rules/) (6,3 milyon kayıp sipariş) inceleme sürecini atlayan AI destekli bir kod değişikliğine bağlandı. Fonksiyonel görünen, test geçen, ama sistem bağlamını kaçıran bir değişiklik.

## Asıl Sorun Context Window Değil

"AI büyük codebase'leri anlayamıyor, context window yetersiz." Bunu çok duyarsınız. Doğru, ama bu hikayenin yalnızca yüzey kısmı.

AI modelleri milyonlarca açık kaynak kodu üzerinde eğitildi. Bu örneklerin büyük çoğunluğu belirli kalıpları takip ediyor: REST API, MVC, dependency injection, SOLID prensipleri. Model bu kalıpları "normal" kabul ediyor.

Şimdi önüne frontend'den direkt veritabanı çağrısı yapan bir sistem koyun. Model bunu görüyor, ama bu pattern training data'sında ya hiç yok ya da anti-pattern olarak işaretlenmiş. Sonuç: AI "bu bağlamı anlayamıyorum" değil, "bu bağlam var olamaz" moduna giriyor. Ve standart kalıba göre cevap üretiyor.

Daha büyük bir context window bu sorunu çözmez. Sistemi daha fazla görmesi, o sistemin standart dışı olduğu gerçeğini değiştirmiyor. İkinci bir katman daha var: [model stateless çalışır](https://atlan.com/know/are-llms-stateless/). Her prompt bağımsız bir karardır; önceki adımda ne önerdiğini, neden önerdiğini hatırlamaz. Bu, büyük bir sistemde mimari tutarlılığı insan gözetimi olmadan sağlamanın imkansız olduğu anlamına gelir.

## Bu Yalnız Bir Sistemin Sorunu Değil

Kritik altyapı yazılımlarında bu tablo yaygın. Kurumsal yazılım dünyasında daha da yaygın. Büyük ölçekli sistemlerin önemli bir kısmı (sektör ve coğrafyadan bağımsız olarak) yıllar içinde büyümüş, yamana yamana geliştirilmiş yapılar. İş mantığı sadece kaynak kodda değil; stored procedure'larda, config dosyalarında, bazen de yalnızca birinin kafasında.

"Ahmet Bey 10 yıldır burada, o sistemi en iyi o biliyor" cümlesini duymuşsunuzdur. Bu ["kurumsal hafıza"](https://devblogs.microsoft.com/premier-developer/tribal-knowledge-the-anti-devops-culture/) (literatürde *tribal knowledge*) denen şey: belgelenmemiş, test edilmemiş, sadece yaşanarak öğrenilmiş kurallar. Yapay zeka bu bilgiyi göremez, çünkü o bilgi hiçbir zaman koda dönüşmemiş.

Ekiplerin çoğu bu yüzden geliştirici değil itfaiyeci olarak çalışıyor. Yeni özellik eklemek yerine eski metodun beklenmedik yan etkisini bulmak için saatler harcıyorlar. Geçtiğimiz yıl sektörde konuşulmaya başlanan ["vibe coding hangover'ı"](https://www.fastcompany.com/91398622/the-vibe-coding-hangover-is-upon-us) tam da buydu: kıdemli mühendisler AI üretimi kodla çalışırken yaşadıkları "development hell"i dile getiriyordu. [Stack Overflow'un 2025 anketi](https://survey.stackoverflow.co/2025/ai/) de aynı tabloyu gösteriyor: geliştiricilerin %66'sının en büyük şikayeti "neredeyse doğru ama tam değil" AI çıktıları, %45'i ise AI üretimi kodu debug etmenin daha çok zaman aldığını söylüyor. Bu tabloda AI araçları daha hızlı yanlış önerir.

Bu hatalar çoğunlukla "happy path"te gizlenir. AI girdiler temizken, varsayımlar geçerliyken iyi çalışır. Edge case'ler (kullanıcının beklenmedik davranışı, standart dışı veri, sistem yük altındayken) genellikle modelin training data'sında temsil edilmeyen yerlerde kalır. Daha da tehlikelisi "sessiz hata": sistem çalışır, test geçer, ama yanlış sonuç üretir. [Araştırmalar production'daki mantık hatalarının %60'ının bu kategoride olduğunu gösteriyor](https://spectrum.ieee.org/ai-coding-degrades). Crash olmadığı için de uzun süre fark edilmez.

## Peki AI Ne İşe Yarıyor Burada?

Legacy sistemlerde yapay zekayı "yeni kod yazan asistan" olarak konumlandırmak yanlış seçim. Ama bu "kullanma" demek değil.

| Yanlış: "Yeni kod yazan asistan" | Doğru: "Arkeolog" |
|---|---|
| "Bu spagetti kodu refactor et" | "Bu fonksiyon hangi tabloları etkiliyor?" |
| Direkt modernizasyon | Önce test ağı kur |
| AI kodu değiştirir | AI mevcut davranışı belgeler |
| Yapı dayatır | Mevcut yapıyı anlamlandırır |
| Daha hızlı teknik borç üretir | Modernizasyon için zemin oluşturur |

AI bu sistemlerde arkeolog gibi çalışabilir. Kodu okuyup ne yaptığını açıklaması, dokümantasyon üretmesi, stored procedure'lardaki iş mantığını gün yüzüne çıkarması... Bunlarda gerçekten işe yarıyor. Eski sistemi unit testlerle sarmak, mevcut davranışı belgelemek, bağımlılık haritası çıkarmak; yani "bu modülü değiştirirsem ne etkilenir?" sorusunu sormak.

Fark yaratan şey prompt'u nasıl kurduğunuz. "Bu spagetti kodu refactor et" demek yerine: *"Bu fonksiyonun veritabanındaki hangi tabloları etkilediğini listele"* veya *"Bu modülün dış bağımlılıklarını ve çağrıldığı yerleri harita olarak çıkar"* dediğinizde AI bir yapı dayatmak yerine mevcut yapıyı anlamlandırmaya çalışır. Keşif soruları, inşa emirleri değil.

Legacy sistemlerde AI'ın bir diğer güçlü olduğu alan **test yazmaktır**. Kodu tam anlayamasa bile mevcut davranışı belgelemeye yetecek kadar anlayabilir. Eski sisteme hiç dokunmadan etrafına unit test ağı örmesi (Michael Feathers'ın klasikleşmiş [*karakterizasyon testi*](https://en.wikipedia.org/wiki/Characterization_test) yaklaşımı), modernizasyonun en kritik ilk adımıdır; neyin bozulduğunu ancak o ağ varsa görebilirsiniz. AI test yazmada kod yazmaktan çok daha güvenilirdir: "bunu refactor et" riskli, "bu fonksiyonun mevcut davranışını test et" görece güvenlidir.

Bu arkeoloji çalışmasını yaparsanız modernizasyon için bir zemin oluşur. O zemin üzerinde yeni kod yazarken AI gerçekten hız katar. Ama kazı yapmadan doğrudan inşa etmeye çalışırsanız, daha hızlı teknik borç üretirsiniz.

## Duvar Nerede?

Vibe coding hız problemine çözüm getiriyor, ama karmaşıklık problemine değil. AI araçları gerçekten güçlü, vizyon doğru. Ama bu vizyon, altyapısı hazır sistemler için geçerli.

Yazılım dünyasının büyük çoğunluğu o altyapıya henüz sahip değil. Birikmiş on yılların gerçeği bu. Kritik sistemler çalışıyor, iş süreçleri yürüyor; ama o sistemi bilen insanlar ayrıldığında ne olacak sorusu yanıtsız kalıyor.

Yapay zeka bu durumu kendi kendine çözmez. Ama doğru kullanılırsa o çözümün bir parçası olabilir. Önce anlamak, sonra belgelemek, sonra test etmek, sonra modernize etmek.

Vibe coding'in çarptığı duvar teknik bir duvar değil aslında. Onlarca yıllık birikmiş teknik borcun duvarı. Ve o duvarı aşmanın kestirmesi yok.
