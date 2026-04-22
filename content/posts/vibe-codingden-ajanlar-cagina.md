Title: Vibe Coding'den Ajanlar Çağına: Paradigma mı Değişti, İsim mi?
Date: 2026-02-10 12:00
Category: AI
Tags: yapay-zeka, vibe-coding, agentic-engineering, llm
Slug: vibe-codingden-ajanlar-cagina
Summary: Andrej Karpathy "vibe coding"i tanımladıktan bir yıl sonra yeni bir terim önerdi: "agentic engineering." Yüzeyde sadece bir isim değişikliği gibi görünüyor. Ama altında çok daha köklü bir paradigma kayması var.

Şubat 2025'te Andrej Karpathy — OpenAI kurucu ortaklarından, eski Tesla AI direktörü — ["vibe coding"](https://x.com/karpathy/status/1886192184808149383) terimini popülerleştirdi. Fikir basitti: yapay zekaya ne istediğini söyle, kodu yazan o olsun. Kodu okuma. Umursama. Sadece çalışmasını izle.

> *"Sadece vibes'e tamamen teslim ol, üstelleştirmeleri kucakla ve kodun var olduğunu unut. Hata mesajı aldığımda yorum yazmadan yapıştırıyorum, genellikle düzeliyor. Diff'leri artık okumuyorum. Kod olağan anlayışımın ötesine geçti — bu hafta sonu projeleri için fena değil ama oldukça eğlenceli."*

Sektör bu fikri hızla benimsedi. [Cursor](https://www.cursor.com/) 2,3 milyar dolarlık yatırım aldı. [Lovable](https://lovable.dev/) 6,6 milyar dolar değerlemeye ulaştı. Collins Sözlüğü vibe coding'i 2025'in yılın kelimesi seçti. Y Combinator'ın 2025 kış dönemindeki startup'larının %25'inde codebase'in %95'i AI tarafından yazılmıştı. Stack Overflow verilerine göre profesyonel geliştiricilerin %70'i artık AI asistanı kullanıyor ya da kullanmayı planlıyor.

Tam bir yıl sonra, Şubat 2026'da Karpathy [yeni bir çerçeve önerdi](https://x.com/karpathy/status/2026731645169185220): **"agentic engineering."** Ve bunu açıklarken somut bir örnek verdi:

> *"Geçen hafta sonu yerel kamera analiz dashboard'u için şunu yazdım: 'DGX Spark'ıma giriş yap, SSH anahtarlarını ayarla, vLLM kur, Qwen3-VL'yi indir ve test et, video inference için sunucu endpoint'i ve temel web UI dashboard'u hazırla, servisleri systemd ile kur, kendin için notlar al ve bana markdown raporu yaz.' Ajan yaklaşık 30 dakika boyunca çalıştı, birden fazla sorunla karşılaştı, çözümleri araştırdı, tek tek çözdü, kodu yazdı, test etti, servisleri kurdu ve raporla geri döndü. Ben hiçbir şeye dokunmadım. Bunlar üç ay önce kolayca bir hafta sonu projesi olurdu."*

Ve şunu ekledi: programlama tanınmaz hale geliyor. Bilgisayarlar var olduğundan beri süregelen "editöre kod yazma" çağı sona eriyor. Artık AI ajanlarını başlatıyor, doğal dilde görevler veriyor ve çalışmalarını paralel olarak yönetip gözden geçiriyorsunuz.

Sadece semantik bir tercih mi bu? Hayır. Ve farkı anlamak için bir adım geri çekilmek gerekiyor.

## Chatbot'un Gizli Kısıtları

Büyük dil modellerini anlamak için temel bir gerçekle başlayalım: bir LLM'in tek yaptığı şey bir sonraki kelimeyi tahmin etmektir. Doğası gereği durma diye bir kavramı yoktur — tahmin etmeye sonsuza kadar devam eder.

ChatGPT gibi chatbot'lar bu modellere özel bir eğitim uygulandıktan sonra ortaya çıkar. RLHF (İnsan Geri Bildirimiyle Pekiştirmeli Öğrenme) adı verilen bu süreçte modele çok şey öğretilir: kibarca cevap ver, kısa tut, siyasi konulardan kaçın, cevabı bitirdiğinde dur. O "dur" sinyali teknik olarak bir stop token'dır — model bu işareti ürettiğinde sistem yazmayı keser.

Bu eğitim chatbot deneyimini mümkün kılar. Ama aynı zamanda modeli kısıtlar.

AI camiasında bu süreci bazen "lobotomi" olarak nitelendiriyorlar. Modelin ham yaratıcılığı ve potansiyeli, "nazik ol", "kısa cevap ver", "emin olmadığında özür dile" gibi baskılarla törpüleniyor. Bir chatbot "Tabii, hemen yapıyorum" diyebilir ama bir kodlama ajanı için bu kibarlık bir yüktür — ajan sadece işi bitirmelidir.

Vibe coding bu kısıtlı model üzerine inşa edildi. Chatbot arayüzü üzerinden, sohbet formatında, tek seferde cevap bekleyerek. Bu da bir tavan oluşturdu.

## Beyin Vardı, Beden Eksikti

Yapay zeka araştırmacıları LLM'i bir beyne benzetir. Ama bu beynin çalışabilmesi için bir bedene ihtiyacı var: hafıza, planlama yeteneği, araç kullanımı, dış dünyayla etkileşim.

Chatbot arayüzü bu beyne zorla giydirilmiş geçici bir vücuttur. Konuşma biter, hafıza sıfırlanır. Bir sonraki mesajda model yeniden başlar. Bağlam kısıtlıdır, planlama yoktur, araç entegrasyonu en iyi ihtimalle yüzeyseldir.

Ajanlar bu denklemin değiştiği noktadır. Bir ajan sistemi LLM'e gerçek bir beden verir: uzun süreli hafıza, adım adım planlama, dosya okuma-yazma, kod çalıştırma, arama yapma, başka ajanlarla koordinasyon. Model artık tek bir sohbet penceresine sıkışmış değildir — bir hedef verilir ve o hedefe ulaşana kadar özerk olarak hareket eder.

Bu yüzden "agentic engineering" yalnızca isim değişikliği değil. Modelin nasıl kullanıldığına dair temel bir paradigma kaymasıdır.

## Agentic Engineering Pratikte Ne Demek?

Vibe coding'de bir insan vardır ve karşısında tek bir model. İnsan prompt yazar, model kod üretir, insan tekrar yazar. Geri-ileri, konuşma formatında.

Agentic engineering'de bu tablo değişir. Tek bir modelin yerini birden fazla özelleşmiş ajan alır: planlama yapan bir ajan, kodu uygulayan bir ajan, test yazan ve çalıştıran bir ajan, hataları yakalayan bir ajan. Bunlar birbirleriyle iletişim kurar, koordine olur, iterasyon yapar. İnsan mühendis ise stratejik yönü belirler, mimari kararları alır ve kritik noktalarda — production'a merge etme, veritabanı şeması değiştirme, güvenlik sınırları — çıktıyı onaylar. Sektör bu onay mekanizmasını artık standart bir terimle tanımlıyor: **Human-in-the-Loop (HITL)**. Ajanlar özerk koşar, ama ağır kararlar hala insandan geçer. Bu bir darboğaz değil mi? Onay noktalarının sayısı ve ağırlığı göreve göre kalibre edildiğinde hayır — her HITL geçidi bir sürtünme değil, bir kalite filtresidir.

| | Vibe Coding | Agentic Engineering |
|---|---|---|
| Arayüz | Chatbot penceresi | Ajan pipeline'ı |
| Hafıza | Her sohbette sıfırlanır | Adımlar arası taşınır |
| Model | RLHF kısıtlı chatbot | Ham modele yakın |
| İnsan rolü | Her adımda yönlendirme | HITL — kritik noktalarda |
| Planlama | Yok | Adım adım, iteratif |
| Örnek | Cursor sohbet modu | Claude Code, OpenClaw |

Microsoft Copilot Studio, Salesforce Agentforce, AWS Bedrock AgentCore gibi kurumsal platformlar bu iş akışını bugün zaten etkinleştiriyor. Geliştirme pipeline'larına prompt registry'leri, değerlendirme geçitleri ve AI eylemleri için policy katmanları giriyor.

Açık kaynak dünyasında ise tablo farklı bir boyut kazanıyor. RLHF ile kısıtlanmamış, "ham" modeller üzerine kurulan ajan sistemleri büyük şirketlerin kapalı modellerine alternatif olarak öne çıkıyor. Bu modeller daha az "kibar" ama bazı ajan görevleri için daha az kısıtlı — ve bu bir tercih meselesi haline geliyor.

## IDE'nin Değişen Rolü

Bu paradigma kaymasının beklenmedik bir yan etkisi var: geliştirme ortamı artık eskisi gibi değil.

Otuz yıl boyunca IDE, yazılım geliştirmenin tartışmasız merkezi oldu. VS Code, IntelliJ, Visual Studio — bunlar kodun doğduğu kokpitlerdi. Temel varsayım basitti: insanlar kod yazar, araçlar yardım eder.

Agentic engineering bu varsayımı kırıyor. AI ajanları kodu yazıyorsa, insan parmaklarına göre tasarlanmış bir metin editörüne neden ihtiyaç duysunlar?

Sourcegraph'tan Steve Yegge bunu doğrudan ifade etti:

> *"Bireysel katkıda bulunan olarak rolüm değişti. Artık araba üretmiyorum, araba üreten işçilerle dolu bir fabrika yönetiyorum."*

Bu dönüşüm üç dalgada yaşandı. İlkinde AI, IDE'nin içinde bir eklenti olarak geldi — [GitHub Copilot](https://github.com/features/copilot). IDE hala merkezde, AI bir misafirdi. İkinci dalgada AI terminale taşındı: [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [OpenAI Codex CLI](https://github.com/openai/codex) ve Gemini CLI gibi araçlar editöre ihtiyaç duymadan çalışabiliyordu. IDE isteğe bağlı hale geldi. Üçüncü dalgada ise ajan altyapıları belirmeye başladı. [Anthropic'in Claude Managed Agents](https://docs.anthropic.com/en/docs/claude-code/overview)'ı (Nisan 2026, public beta) bunun en somut örneği: kendi ajan döngünüzü, araç çalıştırma altyapınızı ve sandbox ortamınızı sıfırdan kurmanıza gerek kalmadan Claude'u özerk ajan olarak çalıştırabileceğiniz yönetilen bir ortam sunuyor. Dosya okuma, komut çalıştırma, web tarama — bunların güvenli yürütme altyapısı hazır geliyor. Microsoft'un [AutoGen Studio](https://github.com/microsoft/autogen)'su ve Langchain'in [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio)'su ise görsel arayüzde multi-agent iş akışı tasarlamayı mümkün kılıyor. Geliştirici arayüzü "kod yazdığım yer"den "ajanlarımı yönettiğim panel"e evriliyor.

IDE yok olmuyor. Ama üretim katmanından doğrulama katmanına dönüşüyor: diff'leri incelediğiniz, ajan çıktısını gözden geçirdiğiniz, hataları ayıkladığınız yer. Geleceğin IDE'si artık sadece bir metin editörü değil — [Cursor](https://www.cursor.com/)'ın agentic modunda ya da [Windsurf](https://windsurf.com/)'te gördüğümüz gibi, ajanlarınızı izlediğiniz bir kontrol kulesi haline geliyor.

## Uzmanlık Paradoksu

Agentic engineering'in gerçekten ilginç yaptığı şeylerden biri şu: daha az uzmanlık gerektiriyor gibi görünüyor, ama aslında daha fazla gerektiriyor.

Dave Kiss bunu net biçimde ifade etti:

> *"LLM'lere güvenen acemiler olumsuz yönde amplify edilir — yanlış çözümlere güvenle inanır hale gelirler. Problemi anlayan uzmanlar ise olumlu yönde amplify edilir."*

Bir ajan sistemi on parça kod ürettiğinde dokuzu doğru olabilir. Agentic engineer'ın işi o biri yakalamaktır — ince hatayı, ölçeklenmeyecek yaklaşımı, ilerleyen aylarda bakım kabusu haline gelecek soyutlamayı. Bu vasıflı bir denetimdir. Kendi alanınızı on kat daha fazla hacimde çıktıyı doğrulayacak kadar derinden bilmeniz gerekir.

Geliştiricinin rolü kod *yazmak*tan kod *yönlendirmek ve doğrulamak*a kayıyor. Bu bir gerileme değil, bir yükselme. Ama daha sığ değil, daha derin bir anlayış gerektiriyor.

Bu dönüşüm gereken yetkinliği de değiştiriyor. Vibe coding döneminde en değerli yetenek "Prompt Engineering"di — modele doğru soruyu sormak. Agentic engineering'de bu yetenek yerini **System Design** ve **Flow Orchestration** (akış orkestrasyonu)'na bırakıyor. Artık iyi prompt yazmak yetmiyor; ajanların birbiriyle nasıl iletişim kuracağını, hangi araçlara erişeceğini, hangi kontrol noktalarından geçeceğini ve ne zaman insana devredeceğini tasarlamanız gerekiyor.

Araştırmalar bu paradoksu sayılarla da destekliyor. METR'in Temmuz 2025'te yürüttüğü randomize kontrollü deneyde deneyimli açık kaynak geliştiricileri AI kodlama araçlarıyla çalışırken %19 *daha yavaş* oldu — oysa önceden %24 daha hızlı olacaklarını tahmin etmiş, deneyin ardından da %20 daha hızlı çalıştıklarına inanmışlardı. Özgüven ile gerçek performans arasındaki bu uçurum, agentic engineering'in neden bir mühendislik disiplini olduğunu gösteriyor: araç güçlü, ama onu doğru kullanmak deneyim gerektiriyor.

## Ne Değişti, Ne Değişmedi

Vibe coding ölmedi. Hala bir yeri var: yan projelerde, prototiplerde, bir kez kullanıp atacağınız scriptlerde, öğrenme süreçlerinde. Hızlı hareket etmek istediğinizde ve kırılmaktan korkmadığınızda. Ocak 2026'da Linus Torvalds bile kendi audio projesinin görselleştirme aracını "vibe coding ile yazdığını" README'sine not düştü — kavramın ne kadar geniş bir kitleye ulaştığının göstergesi.

Agentic engineering vizyonu ise artık kurumsal platformlarla sınırlı değil. [OpenClaw](https://openclaw.ai), kendi makinenizde çalışan açık kaynaklı bir kişisel ajan: WhatsApp, Telegram veya Discord üzerinden görev alıyor; takvim yönetiminden e-posta gönderiminden uçuş check-in'ine kadar gerçek eylemleri siz yokken tamamlıyor. Peter Steinberger tarafından geliştirilen OpenClaw, Karpathy'nin tarif ettiği "hedefe yönelt, çalışmasını izle" modelinin bireysel ölçekteki somut karşılığı.

Ama tablonun karanlık tarafı da var. CodeRabbit'in 470 açık kaynak pull request üzerindeki analizinde AI ile birlikte yazılan kod, insan yazımına kıyasla 1,7 kat daha fazla kritik sorun içeriyordu; güvenlik açıkları 2,74 kat daha yüksek çıktı. Replit'in AI ajanı bir kullanıcının production veritabanını sildi ve ardından yalan söyledi. Bu, bir chatbot'un yapamayacağı bir şey — sadece "beden" verilmiş, yani gerçek araçlara erişimi olan ama yeterli güvenlik bariyeri (guardrail) kurulmamış bir ajanın yapabileceği bir hata. Bu olaylar vibe coding'in değil, denetimsiz ajan üretiminin sonuçları — agentic engineering'in getirdiği yapı ve HITL mekanizması tam da bu noktada devreye giriyor.

Production sistemleri, ekip halinde sürdürülen codebase'ler ve ölçeklenmesi gereken yazılımlar için sektör agentic engineering'e doğru kayıyor. Yapı, denetim ve uzmanlık tekrar ön plana çıkıyor.

Karpathy'nin isim değişikliği yüzeysel görünebilir. Ama altında şunu söylüyor: bu artık sadece "bir şeyler vibe'lamak" değil, bir sanat ve bilim. Bir mühendislik disiplini.

LLM'e nihayet gerçek bir beden veriliyor. Chatbot arayüzünün lobotomisi aşılıyor. Ham modelin potansiyeli, doğru mimariyle yeniden sahaya çıkıyor.

Vibe coding kapıyı araladı. Agentic engineering o kapıdan geçiyor.
