<h1> DDoS and DoS </h1>

<p>Bir <b>DoS</b> atağı, aslında bir bilgisayarın bir server'a TCP ve UDP paketleriyle
flood yaratması sonucu oluşturulur.
<br><b>DDoS</b> atağında ise, bir bilgisayar yerine birden fazla bilgisayar (ya da sistem) tek bir sistemi
hedef alarak saldırıyı gerçekleştirir. Bu durumda TCP UDP paketleri farklı lokasyonlardan flood ile gelir</p>

<p> All <i>DDoS</i> = <i>DoS</i></p>
<p> All <i>DoS</i> != <i>DDoS</i></p>

<h2> <u>1. DoS Atakları</u> </h2>
<p>
DoS saldırılarının koordine edilebilmesi, modern kuruluşların yüzleşmek zorunda olduğu en yaygın siber güvenlik tehditlerinden biri haline gelmeleri anlamına geliyor. DoS saldırıları basit ama etkilidir ve hedefledikleri şirketlere veya bireylere yıkıcı zararlar verebilir. Tek bir saldırıyla bir kuruluş günler, hatta haftalarca devre dışı bırakılabilir.
</p>
<p>
1.1. <u>Buffer Overflow Atakları</u><br>
C/C++ gibi dillerde RAM'de tutulan veri oldukça kıymetlidir. Bu saldırı tipinde, attacker uygulamaya ekstra trafik overload eder. Bu da RAM/Heapte buffer overload'a sebep olur.
</p>
<p>
1.2. <u>Ping of Death or ICMP Flood</u><br>
ICMP : Internet Control Message Protocol
<br>Bu protokol sayesinde network device'ları (router etc.) IP paketlerinin geçmesinde sıkıntı olduğunda error mesajları basar.<br>Bu atak tipindeyse bir ICMP Flood yaratılmış olur.
</p>
<p>
1.3. <u>SYN Flood</u><br>
SYN Flood ataklarında, server'a connection kurmak için bir send request atılır ancak hand shake tamamlanmaz. Sürekli tekrarlanırsa, network diğer connectionlara vakit ayıramaz ve bloke hale gelir.
</p>
<p>1.4. <u>Tear Drop Attack</u><br>
Attacker, network'e fazlaca segmente edilmiş düzensiz IP paketi gönderir. Segmende edilmiş paketler düzensiz offsetlerle karışık halde sürekli gönderildiği için, network bunu resegment ve reorder etmekle confuse olur ve bir süre sonra yorulur ve çöker.
</p>
<br><h2> <u>2. DDoS Atakları</u> </h2>
<p>
DDoS atağının en büyük artısı saldırganın kaynağının tespit edilemesinin zorlaşmasıdır. Saldırgan, birden fazla sistemi kullanarak saldırıyı gerçekleştirir. Master - Slave ilişkisi gibi düşünürsek, slave'lere zombie ya da bot diyebiliriz. Master bunları uzaktan kumanda eder.
</p>
<p>
2.1.1 <u>Volumetric Attacks</u><br>
Bu saldırı tipinin amacı, hedef sistemin bant genişliğini tüketmektir. Bant genişliği tüketildiğinde diğer cihaz ve kullanıcılar sistemi kullanamaz. Hacimsel saldırılarda genelde ping of detach (ICMP echo requests) kullanılarak bir flood yratılır
</p>
<p>
2.1.2 <u>Fregmentation Attacks</u><br>
Fregmentation DoS atağını birden fazla slave ile kullanarak sistemi yavaşlatır ve bir süre sonra cevap verememesini sağlar.
</p>
<p>
2.1.3. <u>TCP State Exhaustion Attack</u><br>
Sistemin veya Firewall'ın connection sayısını aşmasını sağlamaya çalışır. Bu sayede sistem daha fazla connection kabul edemez.
</p>
<p>2.1.4. <u>Application Layer Attacks</u><br>
Application layer veya Layer 7 atakları, application serverları hedef alır veya resourceları bir rsürü process ve transaction yaratarak tüketmeyi hedefler.
</p>

<h3> 2.2 DDoS Attack Forms </h3>
<p> 2.2.1 <u> Ping Of Death </u></p>
<p>Multiple ping gönderilir. Max paket uzunluğundan daha uzun IP Paketleri gönderilebilir. Bu paketler fragments olarak gönderildiğinden, network bu fragmentleri reassembe ederken network resourceları yorar.
</p>
<p> 2.2.2 <u> UDP Floods </u></p>
<p>Basitçe UDP paketleri gönderilir. Host application paketi bekler ancak application paketi gelmez. Bu şekilde network resourceları consume edilir ve bir süre sonra cevap veremez.
</p>
<p> 2.2.3 <u> Ping Floods </u></p>
<p>ICMP echo request gönderilir. Host makine ICMP echo response atamadan başka ICMP echo requestler gönderilir. Host kendi BW'sini genişletse de saldırı boyutu artarak sistemi bloklar.
</p>
<p> 2.2.4 <u> SYN Floods </u></p>
<p>Birden fazla makineden SYN flood yapılma şekli
</p>
<p> 2.2.5 <u> Slowloris </u></p>
<p>Robert Hansen (RSnake) tarafından bulunmuş bir atak çeşididir. Attacker, birden fazla HTTP Request gönderir ancak bunları tamamlamaz. HTTP headerler periyodik olarak tekrarlanır. Bu atak tercih edilen bir çeşittir çünkü attacker için çok fazla BW gerektirmez. Bu şekilde sistemi yorar.
</p>
<p> 2.2.6 <u> HTTP Flood </u></p>
<p>HTTP POST&GET Requestleriyle oluşturulan flood tipi.
</p>
<p> 2.2.7 <u> Zero-Day Attacks </u></p>
<p>HTTP POST&GET Requestleriyle oluşturulan flood tipi.
</p>
