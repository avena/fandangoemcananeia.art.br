# Estrutura do site Fandango em Cananéia (versão estática)

**Origem:** <https://www.fandangoemcananeia.art.br/>  
**Servidor de produção:** Dreamhost (Apache 2.4 + PHP 8.5.5 via FastCGI)  
**Atualizado em:** 2026-06-05 (Plano D deploy)  
**Total de páginas:** 72 (incluindo `404.html`)  
**Total de assets únicos referenciados:** 1076  
**Tamanho total do site local:** ~245 MB

## 🚦 Estado atual (junho/2026)

| Item | Status |
|------|--------|
| Servidor | Dreamhost (Apache 2.4 + PHP 8.5.5) |
| URLs | `.html` (sem clean URLs — ver nota abaixo) |
| Loop 301 | ✅ Resolvido (Plano D) |
| HTTPS | ✅ Forçado |
| `sitemap.xml` | 70 URLs com `.html` + 1 homepage = 71 total |
| `phpinfo.php` (debug) | No servidor (remover quando não precisar mais) |
| Último deploy | `8a96099` (Plano D) + `475df28` (fix sitemap `ª`) |

> **Por que `.html` nas URLs?** O servidor Dreamhost tem uma config global
> (acima do `.htaccess`) que força trailing-slash em diretórios. Regras de
> rewrite no `.htaccess` para gerar URLs limpas (`/Cananeia/` em vez de
> `/Cananeia.html`) entravam em **loop infinito de 301**. A solução foi
> aceitar URLs com `.html` e servir os arquivos diretamente, sem rewrite.
> O site está 100% funcional.

Site estático local pronto para abrir no navegador. Para publicar, o conteúdo de `site/` vai para a **raiz do servidor web**.

(Os caminhos nesta documentação referem-se aos arquivos dentro de `site/`.)

## URLs servidas pelo servidor

| URL pública | Arquivo local |
|-------------|---------------|
| `/` | `index.html` |
| `/Cananeia.html` | `Cananeia.html` |
| `/Ze-Pereira.html` | `Ze-Pereira.html` |
| `/1ª-Festa-do-Fandango-Caicara-de.html` | `1ª-Festa-do-Fandango-Caicara-de.html` |
| `/404.html` (página de erro) | `404.html` |
| `/sitemap.xml` | `sitemap.xml` |
| `/robots.txt` | `robots.txt` |

**URLs que retornam 404 (esperado):** `/Cananeia/` (sem `.html`), `/Cananeia` (sem `.html` e sem `/`), `/NaoExiste.html` (arquivo inexistente).

---

## Árvore de páginas

- [Início](index.html) (`index`)
  - [1ª Festa do Fandango Caiçara de Cananeia](1ª-Festa-do-Fandango-Caicara-de.html) (`1ª-Festa-do-Fandango-Caicara-de`)
  - [2ª Festa do Fandango Caiçara de Cananeia](2-Festa-do-Fandango-Caicara-de.html) (`2-Festa-do-Fandango-Caicara-de`)
  - [A volta dos mutirões...](Os-tamancos-vao-bater-no-proximo.html) (`Os-tamancos-vao-bater-no-proximo`)
  - [Agenda](Agenda.html) (`Agenda`)
    - [Fandango na Trilha da Juréia](Colheita-de-arroz.html) (`Colheita-de-arroz`)
    - [Festa caiçara em Pedrinhas](Festa-caicara-em-Pedrinhas.html) (`Festa-caicara-em-Pedrinhas`)
    - [Festa de Santo André](Festa-da-Tainha.html) (`Festa-da-Tainha`)
  - [Alegria, alegria... tudo entregue!!!](FESTA-DE-LANCAMENTO.html) (`FESTA-DE-LANCAMENTO`)
  - [Caiçaras no cerrado...](Fandangueiros-de-Cananeia-foram-a.html) (`Fandangueiros-de-Cananeia-foram-a`)
  - [Cananéia](Cananeia.html) (`Cananeia`)
    - [Cultura](Cultura.html) (`Cultura`)
    - [História](Natureza.html) (`Natureza`)
    - [Natureza](Natureza-80.html) (`Natureza-80`)
  - [Fandango](Fandango.html) (`Fandango`)
    - [Fandango Caiçara](O-que-e.html) (`O-que-e`)
    - [Música, dança e instrumentos](Ontem-e-hoje.html) (`Ontem-e-hoje`)
    - [Patrimônio Cultural](Patrimonio-Cultural.html) (`Patrimonio-Cultural`)
    - [Vídeos e fotos](Videos-e-fotos.html) (`Videos-e-fotos`)
  - [Fandango Caiçara: patrimônio cultural do Brasil](Registro-do-Fandango-Caicara-como.html) (`Registro-do-Fandango-Caicara-como`)
  - [Fandangueiros](Mestres.html) (`Mestres`)
    - [Agostinho Gomes](Agostinho-Gomes.html) (`Agostinho-Gomes`)
    - [André Pires](Andre-Pires.html) (`Andre-Pires`)
    - [Beto Pereira](Beto-Pereira.html) (`Beto-Pereira`)
    - [Cleberbio](Cleberbio.html) (`Cleberbio`)
    - [Hugo Emiliano](Seu-Hugo.html) (`Seu-Hugo`)
    - [João Alves](Joao-Alves.html) (`Joao-Alves`)
    - [João Firmino](Joao-Firmino.html) (`Joao-Firmino`)
    - [João da Toca (In memorian)](Joao-da-Toca-In-memorian.html) (`Joao-da-Toca-In-memorian`)
    - [Leonildo Pereira](Arnaldo-Pereira.html) (`Arnaldo-Pereira`)
    - [Nelson Franco (Pica-pau)](Nelson-Franco-Pica-pau.html) (`Nelson-Franco-Pica-pau`)
    - [Paulinho Pereira](Paulinho-Pereira.html) (`Paulinho-Pereira`)
    - [Zé Pereira](Ze-Pereira.html) (`Ze-Pereira`)
    - [Ângelo Ramos](Angelo-Ramos.html) (`Angelo-Ramos`)
  - [Fandangueiros e Puxirão premiados!!!](Apresentacao-da-Katya-Teixeira-e.html) (`Apresentacao-da-Katya-Teixeira-e`)
  - [Grupo Esperança lançará CD na Ilha](Grupo-Esperanca-lancara-CD-na-Ilha.html) (`Grupo-Esperanca-lancara-CD-na-Ilha`)
  - [Grupo Esperança na estrada e finalizando seu disco](Grupo-Esperanca-circulara-pelo.html) (`Grupo-Esperanca-circulara-pelo`)
  - [Grupos](Grupos.html) (`Grupos`)
    - [Batido São Gonçalo](Grupo-de-Fandango-Batido-Sao.html) (`Grupo-de-Fandango-Batido-Sao`)
    - [Caiçaras do Acaraú](Caicaras-do-Acarau.html) (`Caicaras-do-Acarau`)
    - [Esperança](Esperanca.html) (`Esperanca`)
    - [Família Neves](Familia-Neves.html) (`Familia-Neves`)
    - [Família Pereira](Familia-Pereira.html) (`Familia-Pereira`)
    - [Fandangueiros do Ariri](Fandangueiros-do-Ariri.html) (`Fandangueiros-do-Ariri`)
    - [Fandangueiros do Continente](Fandangueiros-do-Continente.html) (`Fandangueiros-do-Continente`)
    - [Jovens Fandangueiros do Itacuruçá](Fandangueiros-do-Itacuruca.html) (`Fandangueiros-do-Itacuruca`)
    - [Terra Firme](Terra-Firme.html) (`Terra-Firme`)
    - [Violas de Ouro São Paulo Bagre](Violas-de-Ouro-Sao-Paulo-Bagre.html) (`Violas-de-Ouro-Sao-Paulo-Bagre`)
  - [Kátya Teixeira e fandango caiçara: encontro perfeito](Katya-Teixeira-no-SESC-Belenzinho.html) (`Katya-Teixeira-no-SESC-Belenzinho`)
  - [Lembranças de um fandango caiçara...](Lembrancas-de-um-fandango-caicara.html) (`Lembrancas-de-um-fandango-caicara`)
  - [Mestre Zé Pereira em Cuba](Mestre-Ze-Pereira-em-Cuba.html) (`Mestre-Ze-Pereira-em-Cuba`)
  - [Mutirão colheita de arroz na Comunidade do Varadouro](Cruzeiro-EducArte-visita-a-cidade.html) (`Cruzeiro-EducArte-visita-a-cidade`)
  - [Navegue](Na-Web.html) (`Na-Web`)
  - [Notícias](Noticias.html) (`Noticias`)
  - [O galo canta...](O-galo-canta.html) (`O-galo-canta`)
  - [O projeto Puxirão participou da 12ª OID](O-projeto-Puxirao-participou-da.html) (`O-projeto-Puxirao-participou-da`)
  - [Programa Puxirão: fandango caiçara e software livre](Cultura-Digital.html) (`Cultura-Digital`)
  - [Prêmio Fandango Caiçara](Premio-Fandango-Caicara.html) (`Premio-Fandango-Caicara`)
  - [Puxirão](Puxirao.html) (`Puxirao`)
    - [Equipe](Equipe.html) (`Equipe`)
    - [Fernando Oliveira (autor)](Fernando-Oliveira.html) (`Fernando-Oliveira`)
    - [Natália Latansio (autora)](Natalia-Latansio.html) (`Natalia-Latansio`)
    - [Objetivos](Objetivos.html) (`Objetivos`)
    - [Parceiros](Parceiros.html) (`Parceiros`)
    - [Produtos sociais](Produtos-sociais.html) (`Produtos-sociais`)
      - [Filme](Filme.html) (`Filme`)
      - [HQ](article18.html) (`article18`)
      - [Músicas](Musicas.html) (`Musicas`)
      - [Portal Web](Portal-Web.html) (`Portal-Web`)
    - [Projeto](Projeto.html) (`Projeto`)
  - [Tá chegando a hora...](Ta-chegando-a-hora.html) (`Ta-chegando-a-hora`)

---

## Detalhamento por página

Para cada página, lista dos assets (imagens, CSS, JS) referenciados e confirmados como baixados em `site/`.

### 1ª Festa do Fandango Caiçara de Cananeia

- **Slug:** `1ª-Festa-do-Fandango-Caicara-de`
- **URL original:** <https://www.fandangoemcananeia.art.br/1ª-Festa-do-Fandango-Caicara-de>
- **Arquivo local:** `site/1ª-Festa-do-Fandango-Caicara-de.html` (63 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 181

  **Imagens (162):**

  - `IMG/jpg/12232699_1075508925839028_5605818588108382832_o.jpg` (228 KB)
  - `IMG/jpg/12322609_1076250022431585_3327245267137528295_o_1_.jpg` (103 KB)
  - `IMG/jpg/12322617_1076249762431611_6554320287414218485_o.jpg` (183 KB)
  - `IMG/jpg/13115950_1076250862431501_2214173033235536381_o.jpg` (268 KB)
  - `IMG/jpg/13115950_1076251335764787_2187071644458492560_o.jpg` (206 KB)
  - `IMG/jpg/13227655_1076251132431474_3297021200732566116_o.jpg` (280 KB)
  - `IMG/jpg/13227655_1076251132431474_3297021200732566116_o_1_.jpg` (280 KB)
  - `IMG/jpg/13227661_1075507055839215_3375345727391640019_o.jpg` (272 KB)
  - `IMG/jpg/13227812_1076250242431563_8735647375495910503_o.jpg` (228 KB)
  - `IMG/jpg/13243969_1076250365764884_203265086870310951_o.jpg` (311 KB)
  - `IMG/jpg/13247866_1075513949171859_6672840712381833689_o.jpg` (326 KB)
  - `IMG/jpg/13248398_1075506249172629_8789655659657964287_o.jpg` (281 KB)
  - `IMG/jpg/13248399_1075505549172699_7845213277083426642_o.jpg` (265 KB)
  - `IMG/jpg/13254664_1075513179171936_8381867252378284812_o.jpg` (267 KB)
  - `IMG/jpg/13254670_1075507589172495_3345273443506609490_o.jpg` (306 KB)
  - `IMG/jpg/13254738_1075512429172011_3300565288310940985_o.jpg` (340 KB)
  - `IMG/jpg/13254760_1075511689172085_5153974210411206731_o.jpg` (225 KB)
  - `IMG/jpg/13267998_1075512232505364_2055320635613483972_o.jpg` (291 KB)
  - `IMG/jpg/13268016_1075511585838762_5599236152025617550_o.jpg` (266 KB)
  - `IMG/jpg/13268055_1075506905839230_7412188209502901435_o.jpg` (428 KB)
  - `IMG/jpg/13268135_1075511629172091_8064686998844360395_o.jpg` (199 KB)
  - `IMG/jpg/13268229_1076251589098095_9142089765239863972_o.jpg` (335 KB)
  - `IMG/jpg/13268250_1075506549172599_8005272368799160650_o.jpg` (290 KB)
  - `IMG/jpg/13268262_1076250185764902_5235453477401747154_o.jpg` (255 KB)
  - `IMG/jpg/13268288_1076250809098173_7417392197269641431_o.jpg` (341 KB)
  - `IMG/jpg/13268421_1076251059098148_8285972990412760086_o.jpg` (320 KB)
  - `IMG/jpg/13268428_1076249889098265_7391958302521835022_o.jpg` (209 KB)
  - `IMG/jpg/13301232_1079306192125968_6565624680067977961_o.jpg` (214 KB)
  - `IMG/jpg/13301243_1079233045466616_1012719379065694745_o.jpg` (153 KB)
  - `IMG/jpg/13301251_1076249872431600_7001801613887811405_o_1_.jpg` (363 KB)
  - `IMG/jpg/13301337_1076250462431541_792534431475515374_o.jpg` (292 KB)
  - `IMG/jpg/13301364_1079272848795969_6466149809670572416_o.jpg` (293 KB)
  - `IMG/jpg/13301403_1079264832130104_7880301696929559403_o.jpg` (172 KB)
  - `IMG/jpg/13301434_1079258775464043_556841763103857873_o.jpg` (224 KB)
  - `IMG/jpg/13301445_1079241702132417_8599050701711931169_o.jpg` (286 KB)
  - `IMG/jpg/13301460_1075506435839277_4472644495761402809_o.jpg` (504 KB)
  - `IMG/jpg/13301467_1079235882132999_7115892130661602507_o-2.jpg` (164 KB)
  - `IMG/jpg/13301467_1079235882132999_7115892130661602507_o.jpg` (164 KB)
  - `IMG/jpg/13301477_1079237918799462_1150778034860330981_o.jpg` (207 KB)
  - `IMG/jpg/13301482_1079306335459287_4564108995514419407_o.jpg` (203 KB)
  - `IMG/jpg/13301508_1079273075462613_5191430013365146921_o.jpg` (239 KB)
  - `IMG/jpg/13301525_1079237702132817_4650437282204768244_o.jpg` (282 KB)
  - `IMG/jpg/13301526_1079233382133249_2244378613599543582_o.jpg` (146 KB)
  - `IMG/jpg/13301549_1079271878796066_8725811155358072905_o.jpg` (345 KB)
  - `IMG/jpg/13304991_1079238615466059_343727537094328064_o.jpg` (228 KB)
  - `IMG/jpg/13304998_1075505622506025_5307362293781662973_o.jpg` (286 KB)
  - `IMG/jpg/13305031_1079232242133363_6383484558218265512_o.jpg` (190 KB)
  - `IMG/jpg/13305046_1079236825466238_2995937111962437851_o-2-r90.jpg` (348 KB)
  - `IMG/jpg/13305046_1079236825466238_2995937111962437851_o.jpg` (317 KB)
  - `IMG/jpg/13305078_1076250372431550_6060155569853427574_o_1_.jpg` (325 KB)
  - `IMG/jpg/13305085_1076249649098289_6732477892388314606_o.jpg` (209 KB)
  - `IMG/jpg/13305111_1079266912129896_7465233908329698137_o.jpg` (263 KB)
  - `IMG/jpg/13305114_1075512685838652_416112188580598250_o.jpg` (261 KB)
  - `IMG/jpg/13305121_1076250189098235_47026192685506384_o.jpg` (223 KB)
  - `IMG/jpg/13305152_1076249805764940_5472514652783038420_o.jpg` (198 KB)
  - `IMG/jpg/13305159_1076249652431622_7859957590042090335_o.jpg` (183 KB)
  - `IMG/jpg/13305194_1079277302128857_28012014208633729_o.jpg` (278 KB)
  - `IMG/jpg/13305198_1076250439098210_3091114935182458091_o.jpg` (290 KB)
  - `IMG/jpg/13305211_1075506185839302_1521389449692546432_o.jpg` (314 KB)
  - `IMG/jpg/13308143_1075505475839373_8617823150311030811_o.jpg` (304 KB)
  - `IMG/jpg/13308167_1079272602129327_8179316623690420645_o.jpg` (293 KB)
  - `IMG/jpg/13308189_1079243678798886_7846421594724192257_o.jpg` (348 KB)
  - `IMG/jpg/13308192_1079261288797125_1857638973285448691_o.jpg` (195 KB)
  - `IMG/jpg/13308242_1076250495764871_2861905761117262623_o_1_.jpg` (171 KB)
  - `IMG/jpg/13308244_1079232088800045_4492478252374015322_o.jpg` (192 KB)
  - `IMG/jpg/13308267_1079294985460422_8870735566719178576_o.jpg` (272 KB)
  - `IMG/jpg/13308276_1076250749098179_77881283741477945_o.jpg` (327 KB)
  - `IMG/jpg/13308282_1079278155462105_6282167973235583479_o-2.jpg` (299 KB)
  - `IMG/jpg/13308282_1079278155462105_6282167973235583479_o.jpg` (299 KB)
  - `IMG/jpg/13308367_1079244018798852_6374241505280355498_o-2.jpg` (232 KB)
  - `IMG/jpg/13308367_1079244018798852_6374241505280355498_o.jpg` (232 KB)
  - `IMG/jpg/13308375_1076250619098192_2515131669200408875_o.jpg` (249 KB)
  - `IMG/jpg/13308428_1079239662132621_4859702617482708345_o.jpg` (274 KB)
  - `IMG/jpg/13308442_1079253068797947_422123339998009295_o.jpg` (151 KB)
  - `IMG/jpg/13308444_1079304242126163_89161860595507219_o.jpg` (279 KB)
  - `IMG/jpg/13308488_1075509422505645_3949798281796077254_o.jpg` (204 KB)
  - `IMG/jpg/13308525_1076251439098110_6036076940515550509_o.jpg` (289 KB)
  - `IMG/jpg/13308550_1076249839098270_4883271374426646217_o_1_.jpg` (200 KB)
  - `IMG/jpg/13308609_1075511315838789_9107661089301342425_o.jpg` (222 KB)
  - `IMG/jpg/13308664_1076249709098283_4497695605271564645_o.jpg` (216 KB)
  - `IMG/jpg/13308675_1075514019171852_872171814626111930_o.jpg` (255 KB)
  - `IMG/jpg/13308736_1079233612133226_2211869573122895716_o.jpg` (131 KB)
  - `IMG/jpg/13308751_1079232422133345_7610360886389425605_o.jpg` (224 KB)
  - `IMG/jpg/13316834_1075509515838969_3345581327743928567_o.jpg` (217 KB)
  - `IMG/jpg/13316860_1079232325466688_8121208129251000448_o.jpg` (133 KB)
  - `IMG/jpg/13316865_1076250572431530_8341961384569737897_o.jpg` (227 KB)
  - `IMG/jpg/13316875_1076250565764864_7595415614020473374_o.jpg` (303 KB)
  - `IMG/jpg/13316937_1076251382431449_1200765745638391308_o.jpg` (266 KB)
  - `IMG/jpg/13316943_1076250795764841_4976588736733272852_o.jpg` (309 KB)
  - `IMG/jpg/13316947_1079254925464428_8715288332263052867_o.jpg` (317 KB)
  - `IMG/jpg/13316948_1079271605462760_8109040740058883396_o.jpg` (252 KB)
  - `IMG/jpg/13317023_1076251112431476_4749254368697072911_o.jpg` (268 KB)
  - `IMG/jpg/13320348_1079279955461925_4867954174403044922_o.jpg` (334 KB)
  - `IMG/jpg/13320358_1076250925764828_37028684721144178_o.jpg` (177 KB)
  - `IMG/jpg/13320407_1075513119171942_1014275378221738098_o_1_.jpg` (248 KB)
  - `IMG/jpg/13320476_1075514459171808_3483452810028514506_o.jpg` (288 KB)
  - `IMG/jpg/13320490_1079240085465912_2959664574583776144_o.jpg` (264 KB)
  - `IMG/jpg/13320499_1076249962431591_1375855808743073815_o_3_.jpg` (200 KB)
  - `IMG/jpg/13320542_1076251249098129_705318032552765465_o.jpg` (280 KB)
  - `IMG/jpg/13320709_1075507742505813_34628559811846009_o.jpg` (345 KB)
  - `IMG/jpg/13320729_1075507232505864_4363841272373930180_o.jpg` (190 KB)
  - `IMG/jpg/13320754_1075504435839477_7176507828282414998_o_1_.jpg` (239 KB)
  - `IMG/jpg/13320760_1079304715459449_7618488717471688342_o.jpg` (297 KB)
  - `IMG/jpg/13320767_1076250919098162_6582619854785036928_o.jpg` (356 KB)
  - `IMG/jpg/13320777_1076250032431584_4479185856217378334_o_1_.jpg` (172 KB)
  - `IMG/jpg/13320816_1079276868795567_9205606441263106793_o.jpg` (320 KB)
  - `IMG/jpg/13320854_1076249745764946_5496917782587217267_o.jpg` (218 KB)
  - `IMG/jpg/13320867_1079242912132296_4438057938149345807_o.jpg` (353 KB)
  - `IMG/jpg/13320879_1076251649098089_1687675040997717623_o.jpg` (336 KB)
  - `IMG/jpg/13320906_1079235438799710_5545362728803112078_o.jpg` (216 KB)
  - `IMG/jpg/13320973_1075514092505178_4817456437684159328_o.jpg` (179 KB)
  - `IMG/jpg/13323173_1079240728799181_5456903316701449326_o.jpg` (225 KB)
  - `IMG/jpg/13323214_1076250739098180_7818444116089433764_o.jpg` (307 KB)
  - `IMG/jpg/13323214_1076251422431445_3628475376404757073_o.jpg` (293 KB)
  - `IMG/jpg/13323228_1079297942126793_1003010045703220272_o.jpg` (219 KB)
  - `IMG/jpg/13323292_1079234662133121_5741200735555498133_o.jpg` (245 KB)
  - `IMG/jpg/13323298_1076249949098259_7943128451828005492_o_1_.jpg` (145 KB)
  - `IMG/jpg/13323355_1075512855838635_5684821247787901961_o.jpg` (295 KB)
  - `IMG/jpg/13323363_1076250359098218_2108330255088768358_o.jpg` (206 KB)
  - `IMG/jpg/13323367_1079275145462406_2431876237795502921_o.jpg` (225 KB)
  - `IMG/jpg/13323512_1079237082132879_2109532908944007723_o.jpg` (259 KB)
  - `IMG/jpg/13323513_1075512742505313_3610228213969166353_o.jpg` (274 KB)
  - `IMG/jpg/13323515_1075507169172537_899579967073891021_o-2.jpg` (220 KB)
  - `IMG/jpg/13323515_1075507169172537_899579967073891021_o.jpg` (220 KB)
  - `IMG/jpg/13323518_1079249105465010_6065675660289938105_o.jpg` (351 KB)
  - `IMG/jpg/13323529_1079233258799928_2522938225843835991_o.jpg` (215 KB)
  - `IMG/jpg/13323536_1075514259171828_6666236013877437924_o.jpg` (223 KB)
  - `IMG/jpg/13323537_1079239388799315_3602114513997349223_o.jpg` (298 KB)
  - `IMG/jpg/13323538_1076250685764852_8692891093287953061_o.jpg` (228 KB)
  - `IMG/jpg/13323585_1076250025764918_2761057211110763737_o_1_.jpg` (212 KB)
  - `IMG/jpg/13323603_1079268938796360_7132876966533624969_o.jpg` (272 KB)
  - `IMG/jpg/13323610_1079305225459398_5028620080807722668_o.jpg` (275 KB)
  - `IMG/jpg/13323628_1075514385838482_1964458915442237795_o.jpg` (260 KB)
  - `IMG/jpg/13323641_1076250072431580_3752937062430742132_o_1_.jpg` (306 KB)
  - `IMG/jpg/13323687_1079274712129116_4295417798424027501_o.jpg` (272 KB)
  - `IMG/jpg/13323712_1075507475839173_7175475575790670072_o.jpg` (357 KB)
  - `IMG/jpg/13323736_1079239042132683_4741258295288530791_o.jpg` (257 KB)
  - `IMG/jpg/13323738_1079263418796912_3366045151531122098_o.jpg` (213 KB)
  - `IMG/jpg/13323751_1079232828799971_1483253728786985874_o.jpg` (181 KB)
  - `IMG/jpg/13329382_1079274112129176_477610579421611231_o.jpg` (235 KB)
  - `IMG/jpg/13329437_1076250962431491_1529321515998963446_o.jpg` (340 KB)
  - `IMG/jpg/13329448_1079237332132854_8325931793984816528_o.jpg` (238 KB)
  - `IMG/jpg/13329502_1079234112133176_3043627520102021015_o.jpg` (144 KB)
  - `IMG/jpg/13329545_1079273645462556_329071289408680213_o.jpg` (225 KB)
  - `IMG/jpg/13340199_1079291628794091_7815085642707368623_o.jpg` (289 KB)
  - `IMG/jpg/13340286_1079233472133240_2829268272314942789_o.jpg` (133 KB)
  - `IMG/jpg/13346178_1079276595462261_3746320459417203682_o.jpg` (313 KB)
  - `IMG/jpg/13346244_1079244942132093_2020174106766753234_o.jpg` (123 KB)
  - `IMG/jpg/13346261_1079238348799419_3491593152137267775_o.jpg` (206 KB)
  - `IMG/jpg/13350241_1079306008792653_7912740921889825177_o.jpg` (191 KB)
  - `IMG/jpg/13350271_1079271422129445_9088097380591210485_o.jpg` (260 KB)
  - `IMG/jpg/13350306_1079274318795822_581816325619813363_o.jpg` (278 KB)
  - `IMG/jpg/13350348_1079280088795245_5300275541746692761_o.jpg` (305 KB)
  - `IMG/jpg/13350394_1079284695461451_2897359321383756457_o.jpg` (316 KB)
  - `IMG/jpg/13350414_1079240398799214_3600787127841262977_o.jpg` (228 KB)
  - `IMG/jpg/13350428_1079275845462336_3326696110935394754_o.jpg` (273 KB)
  - `local/cache-vignettes/L133xH100/programacao_festa_fandango-e1905.png` (31 KB)
  - `local/cache-vignettes/L137xH100/cartaz_festa_fandango-2-3e9da.png` (27 KB)
  - `local/cache-vignettes/L200xH107/arton87-99058.png` (40 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### 2ª Festa do Fandango Caiçara de Cananeia

- **Slug:** `2-Festa-do-Fandango-Caicara-de`
- **URL original:** <https://www.fandangoemcananeia.art.br/2%C2%AA-Festa-do-Fandango-Caicara-de>
- **Arquivo local:** `site/2-Festa-do-Fandango-Caicara-de.html` (58 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 149

  **Imagens (130):**

  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_01.jpg` (270 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_02.jpg` (244 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_03.jpg` (202 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_04.jpg` (297 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_05.jpg` (330 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_06.jpg` (304 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_07.jpg` (366 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_08.jpg` (259 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_09.jpg` (302 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_10.jpg` (237 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_11.jpg` (179 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_12.jpg` (321 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_13.jpg` (246 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_14.jpg` (266 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_15.jpg` (342 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_16.jpg` (329 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_17.jpg` (369 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_18.jpg` (355 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_19.jpg` (216 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_20.jpg` (335 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_21.jpg` (361 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_22.jpg` (269 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_23.jpg` (213 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_24.jpg` (236 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_25.jpg` (282 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_26.jpg` (191 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_27.jpg` (312 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_28.jpg` (283 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_29.jpg` (248 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_30.jpg` (309 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_31.jpg` (202 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_32.jpg` (164 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_33.jpg` (261 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_34.jpg` (220 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_35.jpg` (299 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_01.jpg` (170 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_02.jpg` (175 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_03.jpg` (228 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_04.jpg` (238 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_05.jpg` (227 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_06.jpg` (217 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_07.jpg` (146 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_08.jpg` (145 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_09.jpg` (152 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_10.jpg` (165 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_11.jpg` (233 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_12.jpg` (210 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_13.jpg` (240 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_14.jpg` (236 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_15.jpg` (214 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_16.jpg` (219 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_17.jpg` (215 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_18.jpg` (226 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_19.jpg` (276 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_20.jpg` (181 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_21.jpg` (225 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_22.jpg` (272 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_23.jpg` (219 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_24.jpg` (195 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_25.jpg` (307 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_26.jpg` (267 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_28.jpg` (385 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_01.jpg` (188 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_02.jpg` (283 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_04.jpg` (179 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_05.jpg` (247 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_07.jpg` (238 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_08.jpg` (196 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_09.jpg` (236 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_10.jpg` (187 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_16.jpg` (210 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_17.jpg` (149 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_18.jpg` (224 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_20.jpg` (303 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_21.jpg` (158 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_22.jpg` (147 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_23.jpg` (247 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_24.jpg` (287 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_25.jpg` (243 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_26.jpg` (203 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_27.jpg` (189 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_28.jpg` (207 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_29.jpg` (278 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_30.jpg` (235 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_31.jpg` (170 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_32.jpg` (178 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_34.jpg` (116 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_35.jpg` (241 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_36.jpg` (183 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_37.jpg` (236 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_38.jpg` (222 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_39.jpg` (238 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_41.jpg` (260 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_42.jpg` (238 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_45.jpg` (227 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_46.jpg` (280 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_47.jpg` (286 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_48.jpg` (344 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_49.jpg` (320 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_50.jpg` (332 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_51.jpg` (193 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_52.jpg` (352 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_53.jpg` (342 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_54.jpg` (247 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_55.jpg` (367 KB)
  - `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_56.jpg` (268 KB)
  - `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_36-3e9f9.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_38-94916.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_39-1e108.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_32-f08cd.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_33-02da7.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_11-b7116.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_12-26dd9.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_15-b16b6.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_19-3be2d.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_29-1a3fa.jpg` (9 KB)
  - `local/cache-vignettes/L178xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_30-689e1.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_03-9963b.jpg` (8 KB)
  - `local/cache-vignettes/L200xH107/arton88-b7848.png` (50 KB)
  - `local/cache-vignettes/L500xH375/2a_Festa_do_Fandango_Caicara_2018_dia2_35-18c2b-765e1.jpg` (48 KB)
  - `local/cache-vignettes/L500xH375/2a_Festa_do_Fandango_Caicara_2018_dia3_13-3516e-a7e3a.jpg` (47 KB)
  - `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_37-4d603.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_40-72fdd.jpg` (3 KB)
  - `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_41-81431.jpg` (3 KB)
  - `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_31-328ae.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_34-2cefe.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_14-240d1.jpg` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### A volta dos mutirões...

- **Slug:** `Os-tamancos-vao-bater-no-proximo`
- **URL original:** <https://www.fandangoemcananeia.art.br/Os-tamancos-vao-bater-no-proximo>
- **Arquivo local:** `site/Os-tamancos-vao-bater-no-proximo.html` (50 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 128

  **Imagens (109):**

  - `local/cache-vignettes/L134xH100/101_0243-60990.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/101_0248-c81d2.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/101_0249-1c60b.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/29-48aa3.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/30-86ba6.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/31-386bc.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/32-2-6e20f.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/33-503ef.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/34-6964f.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/35-2-f1414.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/36-53cad.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/37-2-c3846.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/38-2ba1a.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dsc01162-2-f7b80.jpg` (3 KB)
  - `local/cache-vignettes/L134xH100/dsc01172-fcc86.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/dsc01179-5fabd.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/dsc01182-4f52c.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/dsc01184-360a2.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dsc01186-dd120.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/dsc01191-2eaea.jpg` (3 KB)
  - `local/cache-vignettes/L134xH100/dsc01202-54041.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/dsc01229-34e3b.jpg` (3 KB)
  - `local/cache-vignettes/L134xH100/dsc01232-bfc37.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dsc01245-e7089.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dsc01253-c1b8a.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dsc01258-9657f.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/dsc01271-83903.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/dsc01292-3a984.jpg` (3 KB)
  - `local/cache-vignettes/L134xH100/dsc01293-8bd3c.jpg` (3 KB)
  - `local/cache-vignettes/L134xH100/dsc01295-15321.jpg` (3 KB)
  - `local/cache-vignettes/L134xH100/dsc01298-35b0c.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dsc01299-ac173.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dsc01310-ea1d2.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/dsc01320-3bea9.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/dsc01331-943f7.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/dsc01333-2d171.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/dsc01335-f6be9.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/dsc01336-03aae.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/dsc01343-dec80.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/dsc01345-3aa10.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/dsc01348-7d0dd.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dsc01354-6131c.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/dsc01359-70013.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/dsc01363-fb19a.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/dsc01367-14f18.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/dsc01368-8236b.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dsc01371-4ba78.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dsc01373-2de03.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/sdc11536-6d9fb.jpg` (3 KB)
  - `local/cache-vignettes/L134xH100/sdc11553-909f8.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/sdc11559-24973.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/sdc11560-a1185.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/sdc11566-fab31.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/sdc11578-18c90.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/sdc11582-3a08e.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/sdc11591-e5510.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/sdc11601-cf3d7.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/sdc11628-e821a.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/sdc11632-82915.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/sdc11639-2-2b755.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/sdc11654-58694.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/sdc11659-afe82.jpg` (3 KB)
  - `local/cache-vignettes/L134xH100/sdc11668-b2513.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/sdc11669-7f223.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/sdc11672-037ae.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/sdc11675-d5c2e.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/sdc11676-be4a9.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/sdc11694-c0aee.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/sdc11706-b98cc.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/sdc11715-19d44.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/sdc11732-d5114.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/sdc11744-77fe0.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/sdc11762-7d36c.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/sdc11764-53b16.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/sdc11765-db3c9.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/sdc11772-2-9c79d.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/sdc11772-4279f.jpg` (6 KB)
  - `local/cache-vignettes/L187xH100/arton28-a01bb-68055.png` (45 KB)
  - `local/cache-vignettes/L200xH108/arton28-69df8.png` (52 KB)
  - `local/cache-vignettes/L300xH400/ze_pereira_servindo_bebida-42019-86844.png` (196 KB)
  - `local/cache-vignettes/L400xH244/nascer_do_sol-e71df-4ab8d.png` (158 KB)
  - `local/cache-vignettes/L400xH275/ariri-7aa78-0627b.png` (157 KB)
  - `local/cache-vignettes/L400xH275/baile-dd3e7-3ed1f.png` (176 KB)
  - `local/cache-vignettes/L400xH275/causos-b9253-63970.png` (180 KB)
  - `local/cache-vignettes/L400xH275/cavacao-5e9cc-e0475.png` (260 KB)
  - `local/cache-vignettes/L400xH275/mutirao_colheita_arroz-a4159-57d83.png` (248 KB)
  - `local/cache-vignettes/L400xH275/varadouro-ee7b2-1efe0.png` (187 KB)
  - `local/cache-vignettes/L400xH275/ze_pereira_orientando-cbe23-2c9ad.png` (216 KB)
  - `local/cache-vignettes/L75xH100/101_0245-74d8f.jpg` (3 KB)
  - `local/cache-vignettes/L75xH100/dsc01209-r270-197be.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/dsc01237-r270-4a546.jpg` (3 KB)
  - `local/cache-vignettes/L75xH100/dsc01248-a564f.jpg` (3 KB)
  - `local/cache-vignettes/L75xH100/dsc01276-b95ec.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/dsc01307-r270-0f7fa.jpg` (3 KB)
  - `local/cache-vignettes/L75xH100/dsc01352-r270-30837.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/dsc01366-r270-aa52b.jpg` (3 KB)
  - `local/cache-vignettes/L75xH100/sdc11583-r270-78804.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/sdc11670-r90-ff29c.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/sdc11699-88433.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/sdc11703-3294d.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/sdc11716-b8fb5.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/sdc11718-7e6bf.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/sdc11729-35bd0.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/sdc11733-97933.jpg` (3 KB)
  - `local/cache-vignettes/L75xH100/sdc11737-3d846.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/sdc11739-4af3e.jpg` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Agenda

- **Slug:** `Agenda`
- **URL original:** <https://www.fandangoemcananeia.art.br/Agenda>
- **Arquivo local:** `site/Agenda.html` (21 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 25

  **Imagens (6):**

  - `local/cache-vignettes/L94xH100/arton30-00ddb.jpg` (4 KB)
  - `local/cache-vignettes/L94xH100/arton50-7111d.jpg` (4 KB)
  - `local/cache-vignettes/L94xH100/arton79-f005e.jpg` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Agostinho Gomes

- **Slug:** `Agostinho-Gomes`
- **URL original:** <https://www.fandangoemcananeia.art.br/Agostinho-Gomes>
- **Arquivo local:** `site/Agostinho-Gomes.html` (21 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L150xH200/arton56-d0013.jpg` (7 KB)
  - `local/cache-vignettes/L360xH270/u_13-3dc7c-5e932.jpg` (123 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Alegria, alegria... tudo entregue!!!

- **Slug:** `FESTA-DE-LANCAMENTO`
- **URL original:** <https://www.fandangoemcananeia.art.br/FESTA-DE-LANCAMENTO>
- **Arquivo local:** `site/FESTA-DE-LANCAMENTO.html` (43 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 124

  **Imagens (105):**

  - `local/cache-vignettes/L147xH100/convite-10842.png` (17 KB)
  - `local/cache-vignettes/L178xH100/DSCN8709-f035a.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/DSCN8715-092e4.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN8724-ac279.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/DSCN8728-1dd49.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/DSCN8748-5dd9b.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/DSCN8753-c41fb.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8759-a3630.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/DSCN8763-29ba9.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN8772-29725.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/DSCN8786-39bf7.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/DSCN8787-a8a5a.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN8795-33708.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/DSCN8799-33afa.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8817-06472.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8818-f8a0d.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8819-daf7e.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8820-e9af0.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN8822-8162b.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8823-03d71.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/DSCN8826-346de.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/DSCN8828-2acb0.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8832-08c78.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8836-12faf.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/DSCN8837-518b5.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN8838-970e5.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN8847-b8f3e.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/DSCN8856-37ea2.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN8857-77f23.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8858-3fe58.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8876-3fc6d.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8879-a4fb1.jpg` (4 KB)
  - `local/cache-vignettes/L178xH100/DSCN8884-fc4d8.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/DSCN8900-d3b49.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/DSCN8908-b4063.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8918-36575.jpg` (4 KB)
  - `local/cache-vignettes/L178xH100/DSCN8925-61cea.jpg` (9 KB)
  - `local/cache-vignettes/L178xH100/DSCN8929-f4748.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8936-fd26c.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8941-075d5.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN8947-8fc6f.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8949-15f17.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/DSCN8953-a2cdf.jpg` (4 KB)
  - `local/cache-vignettes/L178xH100/DSCN8955-e2c14.jpg` (3 KB)
  - `local/cache-vignettes/L178xH100/DSCN8957-343b5.jpg` (3 KB)
  - `local/cache-vignettes/L178xH100/DSCN8961-52055.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN8998-2cdd9.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN9048-cc4f2.jpg` (7 KB)
  - `local/cache-vignettes/L200xH108/arton75-b46aa.png` (50 KB)
  - `local/cache-vignettes/L572xH100/DSCN8781-cd4be.jpg` (14 KB)
  - `local/cache-vignettes/L57xH100/DSCN8711-6753c.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8713-4f8fa.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8716-bfab8.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8717-6a627.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8718-85ca3.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8721-4eaed.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8722-5d8cb.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8729-ca679.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8734-27182.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8735-a8fc8.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8736-ff543.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8738-0838e.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8739-94837.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8740-61da5.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8742-e20af.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8743-f94e7.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8744-d0dd1.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8745-4b934.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8747-9e93e.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8751-19874.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8755-39913.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8775-aa3d2.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8778-dc648.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8784-41252.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8791-abc83.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8792-22c70.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8793-54027.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8805-be49f.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8806-a0317.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8807-2f5b1.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8808-d36b0.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8809-93fe1.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8810-459a9.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8812-304ae.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8813-9667a.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8814-bc883.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8815-e0cb3.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8824-d785a.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8825-507e4.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8829-39266.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8844-520ad.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8845-104b4.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8846-19966.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8849-7e3e3.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8915-19364.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8917-r90-143a3.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8965-e590f.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN8967-0bfc9.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN8988-bed87.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSCN9004-404c7.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN9012-19505.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSCN9143-9cb27.jpg` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### André Pires

- **Slug:** `Andre-Pires`
- **URL original:** <https://www.fandangoemcananeia.art.br/Andre-Pires>
- **Arquivo local:** `site/Andre-Pires.html` (20 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L150xH100/arton62-ac108.jpg` (14 KB)
  - `local/cache-vignettes/L360xH270/u_23-1fd4b-fd240.jpg` (81 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Batido São Gonçalo

- **Slug:** `Grupo-de-Fandango-Batido-Sao`
- **URL original:** <https://www.fandangoemcananeia.art.br/Grupo-de-Fandango-Batido-Sao>
- **Arquivo local:** `site/Grupo-de-Fandango-Batido-Sao.html` (23 KB)
- **Status:** **OK**
- **Página pai:** `Grupos`
- **Assets referenciados:** 37

  **Imagens (18):**

  - `local/cache-vignettes/L134xH100/IMG_0428-1e09c.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/IMG_0946-57396.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/IMG_2310-c9542.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dia_folclore_sao_goncalo-6d091.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/saogoncalo-6cd3f.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/DSC02557-defe4.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSC02560-497c2.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSC02577-e5ad3.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSC02579-2-c8d06.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSC02590-0bbc7.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/DSCN6479-222c1.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN6482-e23aa.jpg` (7 KB)
  - `local/cache-vignettes/L186xH100/rc-25535-d91fa.jpg` (7 KB)
  - `local/cache-vignettes/L200xH108/arton66-6f07a.jpg` (7 KB)
  - `local/cache-vignettes/L400xH300/descerramento_da_placa_de_inauguracao-4468a.jpg` (59 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Beto Pereira

- **Slug:** `Beto-Pereira`
- **URL original:** <https://www.fandangoemcananeia.art.br/Beto-Pereira>
- **Arquivo local:** `site/Beto-Pereira.html` (21 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L350xH233/beto_pereira-0602c-034d3.png` (143 KB)
  - `local/cache-vignettes/L75xH100/arton78-0bc8b.png` (13 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Caiçaras do Acaraú

- **Slug:** `Caicaras-do-Acarau`
- **URL original:** <https://www.fandangoemcananeia.art.br/Caicaras-do-Acarau>
- **Arquivo local:** `site/Caicaras-do-Acarau.html` (23 KB)
- **Status:** **OK**
- **Página pai:** `Grupos`
- **Assets referenciados:** 38

  **Imagens (19):**

  - `local/cache-vignettes/L134xH100/DSC04613-67a22.jpg` (5 KB)
  - `local/cache-vignettes/L151xH100/IMG_6421-73739.jpg` (4 KB)
  - `local/cache-vignettes/L151xH100/IMG_6436-d316f.jpg` (6 KB)
  - `local/cache-vignettes/L151xH100/IMG_6453-0b7c7.jpg` (7 KB)
  - `local/cache-vignettes/L151xH100/IMG_6454-2-75442.jpg` (7 KB)
  - `local/cache-vignettes/L151xH100/IMG_6488-c60dd.jpg` (6 KB)
  - `local/cache-vignettes/L151xH100/IMG_6489-32a2b.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/dsc02190-f4e49.jpg` (7 KB)
  - `local/cache-vignettes/L182xH100/1-199fd.jpg` (5 KB)
  - `local/cache-vignettes/L200xH100/4-0515d.jpg` (6 KB)
  - `local/cache-vignettes/L200xH100/7-b184a.jpg` (9 KB)
  - `local/cache-vignettes/L200xH160/arton6-db64c.png` (64 KB)
  - `local/cache-vignettes/L320xH213/IMG_6454-7b620-3ac31.jpg` (39 KB)
  - `local/cache-vignettes/L57xH100/dsc02196-a23bd.jpg` (3 KB)
  - `local/cache-vignettes/L73xH100/3-cc70c.jpg` (3 KB)
  - `local/cache-vignettes/L77xH100/9-2-2d6b9.jpg` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Caiçaras no cerrado...

- **Slug:** `Fandangueiros-de-Cananeia-foram-a`
- **URL original:** <https://www.fandangoemcananeia.art.br/Fandangueiros-de-Cananeia-foram-a>
- **Arquivo local:** `site/Fandangueiros-de-Cananeia-foram-a.html` (22 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH108/arton65-2aa53.png` (44 KB)
  - `local/cache-vignettes/L500xH268/arton65-a141a-0886d-a8a37.png` (221 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Cananéia

- **Slug:** `Cananeia`
- **URL original:** <https://www.fandangoemcananeia.art.br/Cananeia>
- **Arquivo local:** `site/Cananeia.html` (23 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 27

  **Imagens (8):**

  - `local/cache-vignettes/L149xH100/arton53-9e41d.png` (32 KB)
  - `local/cache-vignettes/L150xH100/arton54-a2dc1.png` (25 KB)
  - `local/cache-vignettes/L150xH100/arton80-ffea8.png` (31 KB)
  - `local/cache-vignettes/L380xH214/cananeia-f225b.png` (120 KB)
  - `local/cache-vignettes/L500xH249/esquema_mapa-2-1257b.png` (142 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Cleberbio

- **Slug:** `Cleberbio`
- **URL original:** <https://www.fandangoemcananeia.art.br/Cleberbio>
- **Arquivo local:** `site/Cleberbio.html` (18 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 22

  **Imagens (3):**

  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Cultura

- **Slug:** `Cultura`
- **URL original:** <https://www.fandangoemcananeia.art.br/Cultura>
- **Arquivo local:** `site/Cultura.html` (46 KB)
- **Status:** **OK**
- **Página pai:** `Cananeia`
- **Assets referenciados:** 35

  **Imagens (16):**

  - `local/cache-vignettes/L150xH100/Canoa-56e83.jpg` (5 KB)
  - `local/cache-vignettes/L150xH100/arton54-a2dc1.png` (25 KB)
  - `local/cache-vignettes/L152xH250/enciclopedia_caicara-7017c-9e1a7.png` (63 KB)
  - `local/cache-vignettes/L159xH100/marco_itacuruca_ilhadocardoso_wordpress-edc03.png` (29 KB)
  - `local/cache-vignettes/L300xH242/seu_ezequiel-d01dc.png` (154 KB)
  - `local/cache-vignettes/L350xH221/festa_enseada-27f9b-20900.png` (166 KB)
  - `local/cache-vignettes/L350xH230/pereirinha-5a6d6-5c754.png` (177 KB)
  - `local/cache-vignettes/L350xH263/cerco_tainha_pereirinha-8a333-a800d.png` (146 KB)
  - `local/cache-vignettes/L350xH263/peixe_seco_enseada-60b3e-8929a.png` (187 KB)
  - `local/cache-vignettes/L367xH223/canoa_motor_ilha_comprida-0e9eb-f64f4.png` (134 KB)
  - `local/cache-vignettes/L400xH207/cerco_pesca-fe77c-98dfe.png` (156 KB)
  - `local/cache-vignettes/L400xH265/casa_caicara_andrea_damato-19902-38654.png` (224 KB)
  - `local/cache-vignettes/L500xH268/chamada_festa_santo_andre_2013_agenda-1f997-5a4f5.png` (191 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Equipe

- **Slug:** `Equipe`
- **URL original:** <https://www.fandangoemcananeia.art.br/Equipe>
- **Arquivo local:** `site/Equipe.html` (27 KB)
- **Status:** **OK**
- **Página pai:** `Puxirao`
- **Assets referenciados:** 46

  **Imagens (27):**

  - `local/cache-vignettes/L116xH104/image8886-d43cd.png` (20 KB)
  - `local/cache-vignettes/L120xH113/Sergio-204cc.png` (23 KB)
  - `local/cache-vignettes/L120xH114/Aldrin-fa415.png` (26 KB)
  - `local/cache-vignettes/L120xH114/Avena-0b69d.png` (24 KB)
  - `local/cache-vignettes/L120xH114/Banto-b7e74-1e0f7.png` (26 KB)
  - `local/cache-vignettes/L120xH114/Bruno-b60aa.png` (23 KB)
  - `local/cache-vignettes/L120xH114/Fernando-caa2a.png` (21 KB)
  - `local/cache-vignettes/L120xH114/Gabriel-01587.png` (26 KB)
  - `local/cache-vignettes/L120xH114/Luana-2-785f9.png` (25 KB)
  - `local/cache-vignettes/L120xH114/Luana1-a5ff3.png` (26 KB)
  - `local/cache-vignettes/L120xH114/Luana2-fe3ed.png` (25 KB)
  - `local/cache-vignettes/L120xH114/Luiz-0a006.png` (25 KB)
  - `local/cache-vignettes/L120xH114/Luma-a2a96.png` (25 KB)
  - `local/cache-vignettes/L120xH114/Mexicano-99b53.png` (23 KB)
  - `local/cache-vignettes/L120xH114/Natalia-93e3a.png` (25 KB)
  - `local/cache-vignettes/L120xH114/Solange-c52dc.png` (23 KB)
  - `local/cache-vignettes/L120xH114/Vitor-0e129-6843c.png` (23 KB)
  - `local/cache-vignettes/L120xH115/Cleber-6f234-bec67.png` (26 KB)
  - `local/cache-vignettes/L120xH115/Helo-5e01c.png` (25 KB)
  - `local/cache-vignettes/L120xH115/Ricardo-7cc56-b4cd0.png` (28 KB)
  - `local/cache-vignettes/L120xH94/Enrico-3d2cb.png` (21 KB)
  - `local/cache-vignettes/L120xH94/Will-0ffcf.png` (22 KB)
  - `local/cache-vignettes/L120xH95/Cacule-a4c20.png` (23 KB)
  - `local/cache-vignettes/L200xH113/arton39-81639.png` (34 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Esperança

- **Slug:** `Esperanca`
- **URL original:** <https://www.fandangoemcananeia.art.br/Esperanca>
- **Arquivo local:** `site/Esperanca.html` (27 KB)
- **Status:** **OK**
- **Página pai:** `Grupos`
- **Assets referenciados:** 38

  **Imagens (19):**

  - `local/cache-vignettes/L127xH100/p7140136-6a816.jpg` (5 KB)
  - `local/cache-vignettes/L133xH100/p7140141-15622.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/domingueira_esperanca-ebbe3.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSC01525-79c59.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSC01528-7b039.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSC01534-2f0dd.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSC01540-8fead.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSC01544-43291.jpg` (6 KB)
  - `local/cache-vignettes/L200xH159/arton8-c5668.jpg` (9 KB)
  - `local/cache-vignettes/L400xH267/fandangueiros-2-4077b-c896b.jpg` (30 KB)
  - `local/cache-vignettes/L57xH100/DSC01526-48b14.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSC01527-3c54c.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSC01529-32e24.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSC01531-21953.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/DSC01532-bbab3.jpg` (2 KB)
  - `local/cache-vignettes/L57xH100/DSC01533-421dd.jpg` (3 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Família Neves

- **Slug:** `Familia-Neves`
- **URL original:** <https://www.fandangoemcananeia.art.br/Familia-Neves>
- **Arquivo local:** `site/Familia-Neves.html` (24 KB)
- **Status:** **OK**
- **Página pai:** `Grupos`
- **Assets referenciados:** 34

  **Imagens (15):**

  - `local/cache-vignettes/L134xH100/IMG_7136-2-4cba3.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_7212-56458.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_7214-2-5102a.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/grupo-de-fandango-familia-neves-683e1.jpg` (6 KB)
  - `local/cache-vignettes/L151xH100/DSC052451-300x199-5bda7.jpg` (6 KB)
  - `local/cache-vignettes/L155xH100/Sem_titulo-34150.png` (36 KB)
  - `local/cache-vignettes/L178xH100/maxresdefault-ee575.jpg` (8 KB)
  - `local/cache-vignettes/L200xH113/arton4-15fcc.jpg` (9 KB)
  - `local/cache-vignettes/L400xH298/fandangueiro-2-34e5e-9257f.jpg` (36 KB)
  - `local/cache-vignettes/L67xH100/naty_414_-3ba61.jpg` (2 KB)
  - `local/cache-vignettes/L75xH100/P1010266-c6023.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/P1010272-06ad7.jpg` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Família Pereira

- **Slug:** `Familia-Pereira`
- **URL original:** <https://www.fandangoemcananeia.art.br/Familia-Pereira>
- **Arquivo local:** `site/Familia-Pereira.html` (22 KB)
- **Status:** **OK**
- **Página pai:** `Grupos`
- **Assets referenciados:** 22

  **Imagens (3):**

  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Fandango

- **Slug:** `Fandango`
- **URL original:** <https://www.fandangoemcananeia.art.br/Fandango>
- **Arquivo local:** `site/Fandango.html` (22 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 26

  **Imagens (7):**

  - `IMG/jpg/dsc00114.jpg` (64 KB)
  - `local/cache-vignettes/L134xH100/arton12-b7554.png` (25 KB)
  - `local/cache-vignettes/L150xH100/arton1-a1650.png` (30 KB)
  - `local/cache-vignettes/L150xH100/arton10-34a95.png` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Fandango Caiçara

- **Slug:** `O-que-e`
- **URL original:** <https://www.fandangoemcananeia.art.br/O-que-e>
- **Arquivo local:** `site/O-que-e.html` (20 KB)
- **Status:** **OK**
- **Página pai:** `Fandango`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH134/arton1-9aaa2.png` (49 KB)
  - `local/cache-vignettes/L300xH200/fandango_o_que_e_itacuruca-38737.png` (89 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Fandango Caiçara: patrimônio cultural do Brasil

- **Slug:** `Registro-do-Fandango-Caicara-como`
- **URL original:** <https://www.fandangoemcananeia.art.br/Registro-do-Fandango-Caicara-como>
- **Arquivo local:** `site/Registro-do-Fandango-Caicara-como.html` (21 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 23

  **Imagens (4):**

  - `local/cache-vignettes/L200xH118/arton69-dcc0f.jpg` (6 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Fandango na Trilha da Juréia

- **Slug:** `Colheita-de-arroz`
- **URL original:** <https://www.fandangoemcananeia.art.br/Colheita-de-arroz>
- **Arquivo local:** `site/Colheita-de-arroz.html` (18 KB)
- **Status:** **OK**
- **Página pai:** `Agenda`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L150xH161/arton30-4c1b2.jpg` (9 KB)
  - `local/cache-vignettes/L380xH285/chamada_fandango_jureia_agenda-2877f-68ca7.png` (158 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Fandangueiros

- **Slug:** `Mestres`
- **URL original:** <https://www.fandangoemcananeia.art.br/Mestres>
- **Arquivo local:** `site/Mestres.html` (24 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 28

  **Imagens (9):**

  - `IMG/jpg/P1070433.jpg` (30 KB)
  - `local/cache-vignettes/L133xH100/arton77-15840.png` (26 KB)
  - `local/cache-vignettes/L150xH100/arton61-2f9eb.jpg` (5 KB)
  - `local/cache-vignettes/L150xH100/arton62-ac108.jpg` (14 KB)
  - `local/cache-vignettes/L150xH98/arton57-4a034.jpg` (5 KB)
  - `local/cache-vignettes/L75xH100/arton78-0bc8b.png` (13 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Fandangueiros do Ariri

- **Slug:** `Fandangueiros-do-Ariri`
- **URL original:** <https://www.fandangoemcananeia.art.br/Fandangueiros-do-Ariri>
- **Arquivo local:** `site/Fandangueiros-do-Ariri.html` (22 KB)
- **Status:** **OK**
- **Página pai:** `Grupos`
- **Assets referenciados:** 28

  **Imagens (9):**

  - `local/cache-vignettes/L134xH100/IMG_7391-3c96e.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/IMG_7392-2-fe20a.jpg` (5 KB)
  - `local/cache-vignettes/L151xH100/_DSC0237-0e7ff.jpg` (6 KB)
  - `local/cache-vignettes/L200xH151/arton32-b0cb0.jpg` (9 KB)
  - `local/cache-vignettes/L360xH270/u_95-7d202-acf66.jpg` (165 KB)
  - `local/cache-vignettes/L75xH100/IMG_7387-9a35a.jpg` (3 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Fandangueiros do Continente

- **Slug:** `Fandangueiros-do-Continente`
- **URL original:** <https://www.fandangoemcananeia.art.br/Fandangueiros-do-Continente>
- **Arquivo local:** `site/Fandangueiros-do-Continente.html` (28 KB)
- **Status:** **OK**
- **Página pai:** `Grupos`
- **Assets referenciados:** 34

  **Imagens (15):**

  - `local/cache-vignettes/L134xH100/P1030265-754ff.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/P1030155-2-b8a5f.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/P1030176-2-50b98.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/P1030252-aee89.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/P1030307-b1417.jpg` (7 KB)
  - `local/cache-vignettes/L200xH150/arton7-ab39c.jpg` (12 KB)
  - `local/cache-vignettes/L400xH218/fandangueiros-3-b4593-c30cd.jpg` (22 KB)
  - `local/cache-vignettes/L57xH100/P1030163-e889e.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/P1030166-39e2a.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/P1030168-46956.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/P1030170-307f1.jpg` (3 KB)
  - `local/cache-vignettes/L57xH100/P1030235-74393.jpg` (3 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Fandangueiros e Puxirão premiados!!!

- **Slug:** `Apresentacao-da-Katya-Teixeira-e`
- **URL original:** <https://www.fandangoemcananeia.art.br/Apresentacao-da-Katya-Teixeira-e>
- **Arquivo local:** `site/Apresentacao-da-Katya-Teixeira-e.html` (20 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH108/arton70-2df87.png` (55 KB)
  - `local/cache-vignettes/L473xH313/mazzaropi-3899d-c8e5e.jpg` (26 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Fernando Oliveira (autor)

- **Slug:** `Fernando-Oliveira`
- **URL original:** <https://www.fandangoemcananeia.art.br/Fernando-Oliveira>
- **Arquivo local:** `site/Fernando-Oliveira.html` (20 KB)
- **Status:** **OK**
- **Página pai:** `Puxirao`
- **Assets referenciados:** 22

  **Imagens (3):**

  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Festa caiçara em Pedrinhas

- **Slug:** `Festa-caicara-em-Pedrinhas`
- **URL original:** <https://www.fandangoemcananeia.art.br/Festa-caicara-em-Pedrinhas>
- **Arquivo local:** `site/Festa-caicara-em-Pedrinhas.html` (22 KB)
- **Status:** **OK**
- **Página pai:** `Agenda`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L300xH207/festa_caicara_pedrinhas-14242-4819e.png` (95 KB)
  - `local/cache-vignettes/L94xH100/arton79-f005e.jpg` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Festa de Santo André

- **Slug:** `Festa-da-Tainha`
- **URL original:** <https://www.fandangoemcananeia.art.br/Festa-da-Tainha>
- **Arquivo local:** `site/Festa-da-Tainha.html` (19 KB)
- **Status:** **OK**
- **Página pai:** `Agenda`
- **Assets referenciados:** 25

  **Imagens (6):**

  - `local/cache-vignettes/L150xH161/arton50-4d40e.jpg` (9 KB)
  - `local/cache-vignettes/L300xH225/capa_1-42eb2-73e49.jpg` (41 KB)
  - `local/cache-vignettes/L500xH268/itacuruca_festa_cataia_pag_principal-633f8.png` (200 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Filme

- **Slug:** `Filme`
- **URL original:** <https://www.fandangoemcananeia.art.br/Filme>
- **Arquivo local:** `site/Filme.html` (42 KB)
- **Status:** **OK**
- **Página pai:** `Produtos-sociais`
- **Assets referenciados:** 71

  **Imagens (52):**

  - `local/cache-vignettes/L134xH100/330474_314501391904506_1197615073_o-941f4.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_5066-688ba.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/IMG_5093-694f6.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/IMG_5095-55042.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_5130-608b1.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/IMG_5167-36f02.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/IMG_6893-849a8.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_6900-21e1e.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/IMG_6902-04051.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/IMG_6992-424ee.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_7025-af3b0.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_7095-c6317.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/IMG_7099-84ece.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/IMG_7136-4b9e7.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_7164-5aee0.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/IMG_7203-720c7.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_7251-e5db4.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/IMG_7273-11a21.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_7285-afc53.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_7286-d3a3f.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_7335-af316.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/IMG_7390-d8564.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/P1010224-26ad6.jpg` (6 KB)
  - `local/cache-vignettes/L151xH100/Rafael_Xavier_3005-a2aac.jpg` (6 KB)
  - `local/cache-vignettes/L151xH100/Rafael_Xavier_3029-d5ebc.jpg` (5 KB)
  - `local/cache-vignettes/L151xH100/Rafael_Xavier_3040-2-a04d5.jpg` (4 KB)
  - `local/cache-vignettes/L151xH100/Rafael_Xavier_3054-3797c.jpg` (5 KB)
  - `local/cache-vignettes/L151xH100/Rafael_Xavier_3124-3d34c.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/P1010265-7efaf.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/P1010302-82431.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/capa-ca55f.jpg` (8 KB)
  - `local/cache-vignettes/L400xH225/assista_baixe_filme_puxirao-b9a6b-7fb74.png` (62 KB)
  - `local/cache-vignettes/L500xH375/IMG_5054-20198-826fa.jpg` (66 KB)
  - `local/cache-vignettes/L57xH100/P1010276-6f3f3.jpg` (3 KB)
  - `local/cache-vignettes/L65xH66/arton17-9ce6c.png` (3 KB)
  - `local/cache-vignettes/L76xH100/IMG_5052-7b650.jpg` (3 KB)
  - `local/cache-vignettes/L76xH100/IMG_5056-49f52.jpg` (3 KB)
  - `local/cache-vignettes/L76xH100/IMG_5060-c7d47.jpg` (3 KB)
  - `local/cache-vignettes/L76xH100/IMG_5091-c1303.jpg` (4 KB)
  - `local/cache-vignettes/L76xH100/IMG_5096-b5084.jpg` (3 KB)
  - `local/cache-vignettes/L76xH100/IMG_7007-62935.jpg` (4 KB)
  - `local/cache-vignettes/L76xH100/IMG_7056-b9766.jpg` (3 KB)
  - `local/cache-vignettes/L76xH100/IMG_7209-622b9.jpg` (3 KB)
  - `local/cache-vignettes/L76xH100/IMG_7295-e8cbc.jpg` (3 KB)
  - `local/cache-vignettes/L76xH100/IMG_7301-345b3.jpg` (4 KB)
  - `local/cache-vignettes/L76xH100/IMG_7319-60eee.jpg` (4 KB)
  - `local/cache-vignettes/L76xH100/IMG_7359-3ec84.jpg` (3 KB)
  - `local/cache-vignettes/L76xH100/P1010175-1bb79.jpg` (4 KB)
  - `local/cache-vignettes/L8xH11/puce-32883.gif` (0 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Grupo Esperança lançará CD na Ilha

- **Slug:** `Grupo-Esperanca-lancara-CD-na-Ilha`
- **URL original:** <https://www.fandangoemcananeia.art.br/Grupo-Esperanca-lancara-CD-na-Ilha>
- **Arquivo local:** `site/Grupo-Esperanca-lancara-CD-na-Ilha.html` (23 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 26

  **Imagens (7):**

  - `IMG/png/esperanca_capa_cd.png` (286 KB)
  - `IMG/png/esperanca_gravacao_estudio.png` (288 KB)
  - `local/cache-vignettes/L200xH108/arton86-d9dec.png` (52 KB)
  - `local/cache-vignettes/L500xH565/cartaz_festa_santo_andre-7dadf.jpg` (83 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Grupo Esperança na estrada e finalizando seu disco

- **Slug:** `Grupo-Esperanca-circulara-pelo`
- **URL original:** <https://www.fandangoemcananeia.art.br/Grupo-Esperanca-circulara-pelo>
- **Arquivo local:** `site/Grupo-Esperanca-circulara-pelo.html` (25 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 28

  **Imagens (9):**

  - `local/cache-vignettes/L188xH100/Fandango-Apresentacao_do_Grupo_Esperanca_no_Arraia_da_Tiduca_Cananeia_FOTO_Rodolfo_Monteiro_capa-3-5fe0c.jpg` (9 KB)
  - `local/cache-vignettes/L200xH107/arton85-9f159.jpg` (10 KB)
  - `local/cache-vignettes/L400xH225/GrupoEsperanca3_Rodolfo_Istvanffy-c8d75-3734a.jpg` (86 KB)
  - `local/cache-vignettes/L400xH265/GrupoEsperanca1_Rodolfo_Monteiro_baixa-c2a30-4ffb0.jpg` (174 KB)
  - `local/cache-vignettes/L400xH300/GrupoEsperanca2_Rodolfo_Monteiro_baixa-80fcd-8277b.jpg` (53 KB)
  - `local/cache-vignettes/L429xH500/GrupoEsperanca4_Aldrin_Klimke-0908e-f5b65.jpg` (63 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Grupos

- **Slug:** `Grupos`
- **URL original:** <https://www.fandangoemcananeia.art.br/Grupos>
- **Arquivo local:** `site/Grupos.html` (23 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 27

  **Imagens (8):**

  - `IMG/jpg/IMG_7364-2.jpg` (37 KB)
  - `local/cache-vignettes/L125xH100/arton6-99609.png` (29 KB)
  - `local/cache-vignettes/L127xH100/arton8-1e9d8.jpg` (5 KB)
  - `local/cache-vignettes/L150xH100/arton67-52a71.jpg` (4 KB)
  - `local/cache-vignettes/L150xH85/arton4-a340d.jpg` (6 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### HQ

- **Slug:** `article18`
- **URL original:** <https://www.fandangoemcananeia.art.br/article18>
- **Arquivo local:** `site/article18.html` (23 KB)
- **Status:** **OK**
- **Página pai:** `Produtos-sociais`
- **Assets referenciados:** 25

  **Imagens (6):**

  - `local/cache-vignettes/L326xH500/baixe_hq_puxirao_pdf-00df3-fdfb7.png` (346 KB)
  - `local/cache-vignettes/L500xH375/tela_hq_1-4ffc4-dda54.jpg` (139 KB)
  - `local/cache-vignettes/L65xH66/arton18-c32d1.png` (3 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### História

- **Slug:** `Natureza`
- **URL original:** <https://www.fandangoemcananeia.art.br/Natureza>
- **Arquivo local:** `site/Natureza.html` (27 KB)
- **Status:** **OK**
- **Página pai:** `Cananeia`
- **Assets referenciados:** 28

  **Imagens (9):**

  - `local/cache-vignettes/L150xH101/arton53-c518a.png` (31 KB)
  - `local/cache-vignettes/L300xH200/mapa_cananeia_1502-f42da-15f32.png` (149 KB)
  - `local/cache-vignettes/L380xH214/cananeia2-cfd97-7baec.png` (130 KB)
  - `local/cache-vignettes/L400xH252/marco_itacuruca_ilhadocardoso_wordpress-2-a4752-98220.png` (175 KB)
  - `local/cache-vignettes/L400xH277/maruja-14d12-ae907.png` (183 KB)
  - `local/cache-vignettes/L500xH342/homem_do_sambaqui-d15ea.png` (365 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Hugo Emiliano

- **Slug:** `Seu-Hugo`
- **URL original:** <https://www.fandangoemcananeia.art.br/Seu-Hugo>
- **Arquivo local:** `site/Seu-Hugo.html` (19 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 23

  **Imagens (4):**

  - `local/cache-vignettes/L200xH170/arton11-39dc6.jpg` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Início

- **Slug:** `index`
- **URL original:** <https://www.fandangoemcananeia.art.br/>
- **Arquivo local:** `site/index.html` (24 KB)
- **Status:** **OK**
- **Assets referenciados:** 42

  **Imagens (23):**

  - `local/cache-gd2/043b682c3dfff6ba56184370fc32fda8.jpg` (17 KB)
  - `local/cache-gd2/57043a760677d4df6886f61ffbe01389.png` (100 KB)
  - `local/cache-gd2/643214e946ba5bd0f9ddbf3d5a668048.jpg` (15 KB)
  - `local/cache-gd2/720cdb5f6b7b6cc6ff1a5147b3e7be14.png` (79 KB)
  - `local/cache-gd2/8d11473f7c9bcf2f24838328db0dabe7.png` (80 KB)
  - `local/cache-gd2/c284ed93972ef4439ae69ca5ee81cc0a.png` (100 KB)
  - `local/cache-gd2/c93912f82f965ed132b907270c91517b.png` (104 KB)
  - `local/cache-gd2/f03453b390a6dd9af7bbe179dbf49eec.jpg` (12 KB)
  - `local/cache-gd2/fbc5dbc8656d2bdd80066a3f84397355.jpg` (22 KB)
  - `local/cache-gd2/febfc7f2d4c54615e926e51766092fa0.png` (105 KB)
  - `local/cache-vignettes/L65xH65/arton16-35041.png` (4 KB)
  - `local/cache-vignettes/L65xH65/arton17-3ee95.png` (4 KB)
  - `local/cache-vignettes/L65xH65/arton18-ab1f9.png` (3 KB)
  - `local/cache-vignettes/L65xH65/arton19-83651.png` (5 KB)
  - `local/cache-vignettes/L660xH389/arton69-81cfa.jpg` (116 KB)
  - `local/cache-vignettes/L727xH388/arton88-580f0.png` (492 KB)
  - `local/cache-vignettes/L727xH388/arton89-632e7.png` (380 KB)
  - `local/cache-vignettes/L727xH388/arton90-51f30.png` (478 KB)
  - `local/cache-vignettes/L727xH389/arton28-a01bb.png` (482 KB)
  - `local/cache-vignettes/L727xH389/arton91-9f356.png` (558 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Jovens Fandangueiros do Itacuruçá

- **Slug:** `Fandangueiros-do-Itacuruca`
- **URL original:** <https://www.fandangoemcananeia.art.br/Fandangueiros-do-Itacuruca>
- **Arquivo local:** `site/Fandangueiros-do-Itacuruca.html` (25 KB)
- **Status:** **OK**
- **Página pai:** `Grupos`
- **Assets referenciados:** 40

  **Imagens (21):**

  - `local/cache-vignettes/L150xH100/Dico-7d085.jpg` (5 KB)
  - `local/cache-vignettes/L150xH100/F1000003-79a03.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/F1000009-dd275.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/F1000020-78813.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/F1000021-29801.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/F1000025-571e4.jpg` (5 KB)
  - `local/cache-vignettes/L150xH100/Filpo-550b8.jpg` (5 KB)
  - `local/cache-vignettes/L150xH100/Todos-e0482.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/Vadico-79ef1.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/filpo1-86837.jpg` (5 KB)
  - `local/cache-vignettes/L200xH100/6-a584c.jpg` (8 KB)
  - `local/cache-vignettes/L200xH105/arton9-7edb4.jpg` (8 KB)
  - `local/cache-vignettes/L209xH100/5-3ce7e.jpg` (8 KB)
  - `local/cache-vignettes/L400xH267/4-2-9ab64-23cc7.jpg` (42 KB)
  - `local/cache-vignettes/L67xH100/Elvaristo-088d2.jpg` (2 KB)
  - `local/cache-vignettes/L67xH100/F1000027-4401f.jpg` (3 KB)
  - `local/cache-vignettes/L67xH100/Tambores-c2110.jpg` (2 KB)
  - `local/cache-vignettes/L8xH11/puce-32883.gif` (0 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### João Alves

- **Slug:** `Joao-Alves`
- **URL original:** <https://www.fandangoemcananeia.art.br/Joao-Alves>
- **Arquivo local:** `site/Joao-Alves.html` (20 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH150/arton51-bc949.jpg` (8 KB)
  - `local/cache-vignettes/L300xH225/Joao_Alves-7e642.png` (105 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### João Firmino

- **Slug:** `Joao-Firmino`
- **URL original:** <https://www.fandangoemcananeia.art.br/Joao-Firmino>
- **Arquivo local:** `site/Joao-Firmino.html` (20 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH150/arton35-08fe3.jpg` (9 KB)
  - `local/cache-vignettes/L301xH448/joao_firmino-27ca6.jpg` (27 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### João da Toca (In memorian)

- **Slug:** `Joao-da-Toca-In-memorian`
- **URL original:** <https://www.fandangoemcananeia.art.br/Joao-da-Toca-In-memorian>
- **Arquivo local:** `site/Joao-da-Toca-In-memorian.html` (23 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L150xH113/arton77-c96d1.png` (30 KB)
  - `local/cache-vignettes/L360xH270/joao_da_toca-9ad2d-dbdc6.png` (132 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Kátya Teixeira e fandango caiçara: encontro perfeito

- **Slug:** `Katya-Teixeira-no-SESC-Belenzinho`
- **URL original:** <https://www.fandangoemcananeia.art.br/Katya-Teixeira-no-SESC-Belenzinho>
- **Arquivo local:** `site/Katya-Teixeira-no-SESC-Belenzinho.html` (22 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH108/arton29-eb237.jpg` (9 KB)
  - `local/cache-vignettes/L500xH268/arton29-a84e8-a19a7-82466.jpg` (32 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Lembranças de um fandango caiçara...

- **Slug:** `Lembrancas-de-um-fandango-caicara`
- **URL original:** <https://www.fandangoemcananeia.art.br/Lembrancas-de-um-fandango-caicara>
- **Arquivo local:** `site/Lembrancas-de-um-fandango-caicara.html` (27 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 47

  **Imagens (28):**

  - `local/cache-vignettes/L134xH100/WhatsApp_Image_2018-05-02_at_16-06-21-bd9be.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/WhatsApp_Image_2018-05-02_at_16-06-35-a8134.jpg` (2 KB)
  - `local/cache-vignettes/L134xH100/WhatsApp_Image_2018-05-02_at_16-06-37-99d74.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/WhatsApp_Image_2018-05-02_at_16-06-38-21a25.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/WhatsApp_Image_2018-05-02_at_16-06-39-7e889.jpg` (5 KB)
  - `local/cache-vignettes/L150xH100/IMG_0854-redimensionado-dad51.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/IMG_0860-redimensionado-112db.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/IMG_0863-redimensionado-1ef63.jpg` (5 KB)
  - `local/cache-vignettes/L150xH100/IMG_0866-redimensionado-35027.jpg` (5 KB)
  - `local/cache-vignettes/L150xH100/IMG_0896-redimensionado-4e26f.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/IMG_0898-redimensionado-b8277.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/IMG_0914-redimensionado-39828.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/IMG_1015-redimensionado-f6b93.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/IMG_1018-redimensionado-7f8f5.jpg` (6 KB)
  - `local/cache-vignettes/L151xH100/WhatsApp_Image_2018-05-03_at_00-25-52-ac147.jpg` (2 KB)
  - `local/cache-vignettes/L151xH100/WhatsApp_Image_2018-05-03_at_00-25-53-ab2bd.jpg` (3 KB)
  - `local/cache-vignettes/L178xH100/expo_fandango_panoramica_baixa-f86f3.jpg` (6 KB)
  - `local/cache-vignettes/L200xH107/arton90-f4748.png` (44 KB)
  - `local/cache-vignettes/L500xH334/IMG_0843-redimensionado-4a5e2-2ffda.jpg` (45 KB)
  - `local/cache-vignettes/L67xH100/IMG_0844-redimensionado-5063b.jpg` (3 KB)
  - `local/cache-vignettes/L67xH100/IMG_0846-redimensionado-85c01.jpg` (3 KB)
  - `local/cache-vignettes/L67xH100/IMG_0847-redimensionado-8ad3f.jpg` (3 KB)
  - `local/cache-vignettes/L67xH100/IMG_0848-redimensionado-ea506.jpg` (3 KB)
  - `local/cache-vignettes/L67xH100/WhatsApp_Image_2018-05-03_at_00-25-50_1_-c3c60.jpg` (3 KB)
  - `local/cache-vignettes/L67xH100/WhatsApp_Image_2018-05-03_at_00-25-51_1_-12d6a.jpg` (3 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Leonildo Pereira

- **Slug:** `Arnaldo-Pereira`
- **URL original:** <https://www.fandangoemcananeia.art.br/Arnaldo-Pereira>
- **Arquivo local:** `site/Arnaldo-Pereira.html` (23 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L150xH200/arton55-29f4e.jpg` (5 KB)
  - `local/cache-vignettes/L299xH448/seu_arnaldo-d4a3c.jpg` (20 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Mestre Zé Pereira em Cuba

- **Slug:** `Mestre-Ze-Pereira-em-Cuba`
- **URL original:** <https://www.fandangoemcananeia.art.br/Mestre-Ze-Pereira-em-Cuba>
- **Arquivo local:** `site/Mestre-Ze-Pereira-em-Cuba.html` (55 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 168

  **Imagens (149):**

  - `local/cache-vignettes/L134xH100/cuba012-d8e09.png` (34 KB)
  - `local/cache-vignettes/L134xH100/cuba018-55a73.png` (27 KB)
  - `local/cache-vignettes/L134xH100/cuba039-a1c29.png` (31 KB)
  - `local/cache-vignettes/L134xH100/cuba074-0ceb2.png` (28 KB)
  - `local/cache-vignettes/L134xH100/cuba084-cae54.png` (16 KB)
  - `local/cache-vignettes/L134xH100/cuba090-d00c4.png` (32 KB)
  - `local/cache-vignettes/L134xH100/cuba095-a8ced.png` (33 KB)
  - `local/cache-vignettes/L134xH100/cuba113-b7f94.png` (29 KB)
  - `local/cache-vignettes/L134xH100/cuba135-de637.png` (27 KB)
  - `local/cache-vignettes/L178xH100/cuba002-983aa.png` (42 KB)
  - `local/cache-vignettes/L178xH100/cuba003-c7fb0.png` (34 KB)
  - `local/cache-vignettes/L178xH100/cuba004-881b3.png` (42 KB)
  - `local/cache-vignettes/L178xH100/cuba005-e2102.png` (41 KB)
  - `local/cache-vignettes/L178xH100/cuba006-a0f45.png` (26 KB)
  - `local/cache-vignettes/L178xH100/cuba008-a56cb.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba009-ee98b.png` (29 KB)
  - `local/cache-vignettes/L178xH100/cuba010-17948.png` (32 KB)
  - `local/cache-vignettes/L178xH100/cuba014-20c88.png` (29 KB)
  - `local/cache-vignettes/L178xH100/cuba015-00c16.png` (32 KB)
  - `local/cache-vignettes/L178xH100/cuba016-32e5e.png` (33 KB)
  - `local/cache-vignettes/L178xH100/cuba019-c52c4.png` (36 KB)
  - `local/cache-vignettes/L178xH100/cuba021-eda2f.png` (35 KB)
  - `local/cache-vignettes/L178xH100/cuba022-5c4b1.png` (42 KB)
  - `local/cache-vignettes/L178xH100/cuba023-7ec2a.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba025-97aad.png` (27 KB)
  - `local/cache-vignettes/L178xH100/cuba026-c64d5.png` (37 KB)
  - `local/cache-vignettes/L178xH100/cuba027-d4ad4.png` (41 KB)
  - `local/cache-vignettes/L178xH100/cuba029-b33b5.png` (36 KB)
  - `local/cache-vignettes/L178xH100/cuba030-3c00e.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba031-9492c.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba032-2feed.png` (42 KB)
  - `local/cache-vignettes/L178xH100/cuba033-45bee.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba034-de9f6.png` (25 KB)
  - `local/cache-vignettes/L178xH100/cuba035-5deb4.png` (32 KB)
  - `local/cache-vignettes/L178xH100/cuba036-09633.png` (41 KB)
  - `local/cache-vignettes/L178xH100/cuba037-f5480.png` (34 KB)
  - `local/cache-vignettes/L178xH100/cuba038-eb454.png` (37 KB)
  - `local/cache-vignettes/L178xH100/cuba041-94d9f.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba042-2-01f2a.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba043-f0749.png` (32 KB)
  - `local/cache-vignettes/L178xH100/cuba044-f7370.png` (31 KB)
  - `local/cache-vignettes/L178xH100/cuba045-c8c7d.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba047-3577c.png` (36 KB)
  - `local/cache-vignettes/L178xH100/cuba048-6a138.png` (34 KB)
  - `local/cache-vignettes/L178xH100/cuba049-c2725.png` (42 KB)
  - `local/cache-vignettes/L178xH100/cuba050-cc9b6.png` (32 KB)
  - `local/cache-vignettes/L178xH100/cuba051-960d1.png` (30 KB)
  - `local/cache-vignettes/L178xH100/cuba052-5a41d.png` (35 KB)
  - `local/cache-vignettes/L178xH100/cuba053-880f7.png` (45 KB)
  - `local/cache-vignettes/L178xH100/cuba054-036c6.png` (33 KB)
  - `local/cache-vignettes/L178xH100/cuba055-ea3fb.png` (42 KB)
  - `local/cache-vignettes/L178xH100/cuba056-8739a.png` (42 KB)
  - `local/cache-vignettes/L178xH100/cuba057-5dbae.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba058-30586.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba059-05dfa.png` (39 KB)
  - `local/cache-vignettes/L178xH100/cuba060-2e5f5.png` (42 KB)
  - `local/cache-vignettes/L178xH100/cuba061-59f7d.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba062-c7968.png` (32 KB)
  - `local/cache-vignettes/L178xH100/cuba063-e64a3.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba064-4f999.png` (31 KB)
  - `local/cache-vignettes/L178xH100/cuba065-b2871.png` (36 KB)
  - `local/cache-vignettes/L178xH100/cuba066-64d9c.png` (43 KB)
  - `local/cache-vignettes/L178xH100/cuba067-5d6ad.png` (36 KB)
  - `local/cache-vignettes/L178xH100/cuba068-93a13.png` (33 KB)
  - `local/cache-vignettes/L178xH100/cuba069-201a6.png` (41 KB)
  - `local/cache-vignettes/L178xH100/cuba070-dcaf7.png` (32 KB)
  - `local/cache-vignettes/L178xH100/cuba071-36db0.png` (39 KB)
  - `local/cache-vignettes/L178xH100/cuba072-d3408.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba075-e4052.png` (39 KB)
  - `local/cache-vignettes/L178xH100/cuba076-e8f62.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba080-14128.png` (42 KB)
  - `local/cache-vignettes/L178xH100/cuba081-73a45.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba082-8d186.png` (36 KB)
  - `local/cache-vignettes/L178xH100/cuba083-bb065.png` (28 KB)
  - `local/cache-vignettes/L178xH100/cuba085-dbd13.png` (44 KB)
  - `local/cache-vignettes/L178xH100/cuba086-f3ae0.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba087-2aa5c.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba088-cf436.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba089-dad79.png` (37 KB)
  - `local/cache-vignettes/L178xH100/cuba091-68852.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba092-554f9.png` (30 KB)
  - `local/cache-vignettes/L178xH100/cuba094-1b62d.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba097-3bd5a.png` (39 KB)
  - `local/cache-vignettes/L178xH100/cuba098-10cb4.png` (28 KB)
  - `local/cache-vignettes/L178xH100/cuba099-d8550.png` (35 KB)
  - `local/cache-vignettes/L178xH100/cuba100-c0dba.png` (39 KB)
  - `local/cache-vignettes/L178xH100/cuba101-e1c96.png` (31 KB)
  - `local/cache-vignettes/L178xH100/cuba102-79e37.png` (35 KB)
  - `local/cache-vignettes/L178xH100/cuba104-d1fa9.png` (35 KB)
  - `local/cache-vignettes/L178xH100/cuba105-13882.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba106-b7e46.png` (37 KB)
  - `local/cache-vignettes/L178xH100/cuba108-fe007.png` (35 KB)
  - `local/cache-vignettes/L178xH100/cuba109-501a8.png` (27 KB)
  - `local/cache-vignettes/L178xH100/cuba110-df940.png` (28 KB)
  - `local/cache-vignettes/L178xH100/cuba111-f7a66.png` (28 KB)
  - `local/cache-vignettes/L178xH100/cuba112-2-cc6eb.png` (25 KB)
  - `local/cache-vignettes/L178xH100/cuba112-8bdac.png` (25 KB)
  - `local/cache-vignettes/L178xH100/cuba114-2fef9.png` (41 KB)
  - `local/cache-vignettes/L178xH100/cuba115-78d5e.png` (29 KB)
  - `local/cache-vignettes/L178xH100/cuba116-86610.png` (30 KB)
  - `local/cache-vignettes/L178xH100/cuba117-ae663.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba119-2f0f5.png` (36 KB)
  - `local/cache-vignettes/L178xH100/cuba120-6dbd9.png` (40 KB)
  - `local/cache-vignettes/L178xH100/cuba121-9e272.png` (27 KB)
  - `local/cache-vignettes/L178xH100/cuba122-222fc.png` (41 KB)
  - `local/cache-vignettes/L178xH100/cuba123-93ecf.png` (33 KB)
  - `local/cache-vignettes/L178xH100/cuba124-01bfe.png` (44 KB)
  - `local/cache-vignettes/L178xH100/cuba124-2-97d8d.png` (44 KB)
  - `local/cache-vignettes/L178xH100/cuba126-15421.png` (41 KB)
  - `local/cache-vignettes/L178xH100/cuba127-4099d.png` (43 KB)
  - `local/cache-vignettes/L178xH100/cuba128-0be43.png` (28 KB)
  - `local/cache-vignettes/L178xH100/cuba129-d5c1e.png` (33 KB)
  - `local/cache-vignettes/L178xH100/cuba130-ded08.png` (37 KB)
  - `local/cache-vignettes/L178xH100/cuba132-496cd.png` (37 KB)
  - `local/cache-vignettes/L178xH100/cuba133-0b531.png` (38 KB)
  - `local/cache-vignettes/L178xH100/cuba134-53a72.png` (31 KB)
  - `local/cache-vignettes/L178xH100/cuba136-1e4c8.png` (30 KB)
  - `local/cache-vignettes/L178xH100/cuba137-657c3.png` (30 KB)
  - `local/cache-vignettes/L178xH100/cuba139-3f212.png` (32 KB)
  - `local/cache-vignettes/L178xH100/cuba140-01833.png` (34 KB)
  - `local/cache-vignettes/L178xH100/cuba141-5b181.png` (27 KB)
  - `local/cache-vignettes/L178xH100/cuba142-90bfc.png` (24 KB)
  - `local/cache-vignettes/L178xH100/cuba143-014a6.png` (41 KB)
  - `local/cache-vignettes/L200xH113/arton73-494cd.jpg` (7 KB)
  - `local/cache-vignettes/L400xH225/cuba_texto_01-73489.png` (151 KB)
  - `local/cache-vignettes/L400xH225/cuba_texto_02-2972d-3a8c5.png` (118 KB)
  - `local/cache-vignettes/L400xH225/cuba_texto_03-f414a-b5579.png` (158 KB)
  - `local/cache-vignettes/L400xH225/cuba_texto_04-a6321-61e7b.png` (151 KB)
  - `local/cache-vignettes/L400xH225/ze_pereira_em_cuba-a7837-545cd.png` (168 KB)
  - `local/cache-vignettes/L57xH100/cuba011-10ac2.png` (14 KB)
  - `local/cache-vignettes/L57xH100/cuba013-ac4d6.png` (14 KB)
  - `local/cache-vignettes/L57xH100/cuba017-08ce3.png` (13 KB)
  - `local/cache-vignettes/L57xH100/cuba020-6e88a.png` (12 KB)
  - `local/cache-vignettes/L57xH100/cuba024-862e4.png` (10 KB)
  - `local/cache-vignettes/L57xH100/cuba028-45ea0.png` (11 KB)
  - `local/cache-vignettes/L57xH100/cuba073-23185.png` (14 KB)
  - `local/cache-vignettes/L57xH100/cuba078-93395.png` (12 KB)
  - `local/cache-vignettes/L57xH100/cuba079-98777.png` (14 KB)
  - `local/cache-vignettes/L57xH100/cuba096-2-aaaed.png` (11 KB)
  - `local/cache-vignettes/L57xH100/cuba103-7deae.png` (10 KB)
  - `local/cache-vignettes/L57xH100/cuba118-325fc.png` (9 KB)
  - `local/cache-vignettes/L57xH100/cuba125-083d4.png` (11 KB)
  - `local/cache-vignettes/L57xH100/cuba131-97d22.png` (12 KB)
  - `local/cache-vignettes/L57xH100/cuba138-22bcb.png` (14 KB)
  - `local/cache-vignettes/L57xH100/cuba144-d86bc.png` (11 KB)
  - `local/cache-vignettes/L57xH100/cuba145-5fe94.png` (13 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Mutirão colheita de arroz na Comunidade do Varadouro

- **Slug:** `Cruzeiro-EducArte-visita-a-cidade`
- **URL original:** <https://www.fandangoemcananeia.art.br/Cruzeiro-EducArte-visita-a-cidade>
- **Arquivo local:** `site/Cruzeiro-EducArte-visita-a-cidade.html` (24 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 23

  **Imagens (4):**

  - `local/cache-vignettes/L200xH108/arton26-f5780.jpg` (11 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Música, dança e instrumentos

- **Slug:** `Ontem-e-hoje`
- **URL original:** <https://www.fandangoemcananeia.art.br/Ontem-e-hoje>
- **Arquivo local:** `site/Ontem-e-hoje.html` (27 KB)
- **Status:** **OK**
- **Página pai:** `Fandango`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH134/arton10-5c5ce.png` (50 KB)
  - `local/cache-vignettes/L400xH267/fandango_musica_danca_instrumentos-40586.png` (149 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Músicas

- **Slug:** `Musicas`
- **URL original:** <https://www.fandangoemcananeia.art.br/Musicas>
- **Arquivo local:** `site/Musicas.html` (25 KB)
- **Status:** **OK**
- **Página pai:** `Produtos-sociais`
- **Assets referenciados:** 40

  **Imagens (21):**

  - `local/cache-vignettes/L100xH100/bolacha_rotulo_SMD_1-2-b9afc.png` (12 KB)
  - `local/cache-vignettes/L100xH100/bolacha_rotulo_SMD_1-f59b7.png` (12 KB)
  - `local/cache-vignettes/L100xH100/bolacha_rotulo_SMD_2-3b4fc.png` (12 KB)
  - `local/cache-vignettes/L134xH100/IMG_7214-b7a19.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/IMG_7392-b5a4e.jpg` (5 KB)
  - `local/cache-vignettes/L178xH100/DSC01513-e11b5.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSC01514-60418.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSC01537-f8005.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/P1030155-37992.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/P1030176-59983.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/P1030191-fe6ff.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/P1030217-03641.jpg` (6 KB)
  - `local/cache-vignettes/L300xH104/baixe_puxirao_ogg-b05f3-a9e2f.png` (15 KB)
  - `local/cache-vignettes/L300xH109/baixe_mp3_puxirao-4bf80-331f9.png` (15 KB)
  - `local/cache-vignettes/L300xH169/ouca_smd_sound_clound-508d3-570fa.png` (45 KB)
  - `local/cache-vignettes/L500xH376/IMG_7370-0a2d4-22e35.jpg` (46 KB)
  - `local/cache-vignettes/L65xH66/arton16-a4ec9.png` (3 KB)
  - `local/cache-vignettes/L76xH100/IMG_7364-adb4c.jpg` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Natureza

- **Slug:** `Natureza-80`
- **URL original:** <https://www.fandangoemcananeia.art.br/Natureza,80>
- **Arquivo local:** `site/Natureza-80.html` (26 KB)
- **Status:** **OK**
- **Página pai:** `Cananeia`
- **Assets referenciados:** 29

  **Imagens (10):**

  - `local/cache-vignettes/L150xH100/arton80-ffea8.png` (31 KB)
  - `local/cache-vignettes/L390xH252/cachoeira_rio_das_minas-fa3e7-5591e.png` (228 KB)
  - `local/cache-vignettes/L400xH225/ilha_cardoso_cercos-351ad-d6e42.png` (128 KB)
  - `local/cache-vignettes/L400xH268/valo_grande_aerea-1c9d7-12666.jpg` (43 KB)
  - `local/cache-vignettes/L431xH244/ponta_da_trincheira-55a68-989b0.png` (162 KB)
  - `local/cache-vignettes/L450xH316/boto_cinza-a26ca.png` (305 KB)
  - `local/cache-vignettes/L450xH338/terrasimbarragemnao-1de07-727d8.jpg` (73 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Natália Latansio (autora)

- **Slug:** `Natalia-Latansio`
- **URL original:** <https://www.fandangoemcananeia.art.br/Natalia-Latansio>
- **Arquivo local:** `site/Natalia-Latansio.html` (19 KB)
- **Status:** **OK**
- **Página pai:** `Puxirao`
- **Assets referenciados:** 22

  **Imagens (3):**

  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Navegue

- **Slug:** `Na-Web`
- **URL original:** <https://www.fandangoemcananeia.art.br/Na-Web>
- **Arquivo local:** `site/Na-Web.html` (25 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 25

  **Imagens (6):**

  - `local/cache-vignettes/L113xH150/rubon19-1831f.png` (25 KB)
  - `local/cache-vignettes/L76xH100/arton74-b9e2a.png` (13 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/puce.gif` (0 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Nelson Franco (Pica-pau)

- **Slug:** `Nelson-Franco-Pica-pau`
- **URL original:** <https://www.fandangoemcananeia.art.br/Nelson-Franco-Pica-pau>
- **Arquivo local:** `site/Nelson-Franco-Pica-pau.html` (20 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH131/arton57-176c0.jpg` (8 KB)
  - `local/cache-vignettes/L350xH240/Sem_titulo-2-9ccf4-577ea.jpg` (39 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Notícias

- **Slug:** `Noticias`
- **URL original:** <https://www.fandangoemcananeia.art.br/Noticias>
- **Arquivo local:** `site/Noticias.html` (24 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 27

  **Imagens (8):**

  - `local/cache-vignettes/L150xH81/arton87-b3fd8.png` (24 KB)
  - `local/cache-vignettes/L150xH81/arton88-9be65.png` (30 KB)
  - `local/cache-vignettes/L150xH81/arton89-84b86.png` (22 KB)
  - `local/cache-vignettes/L150xH81/arton90-b6baf.png` (26 KB)
  - `local/cache-vignettes/L150xH81/arton91-b197d.png` (28 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### O galo canta...

- **Slug:** `O-galo-canta`
- **URL original:** <https://www.fandangoemcananeia.art.br/O-galo-canta>
- **Arquivo local:** `site/O-galo-canta.html` (25 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 37

  **Imagens (18):**

  - `local/cache-vignettes/L178xH100/DSCN0006-ed00f.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/DSCN0007-322dc.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN0009-9eeab.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN0011-2c68f.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/DSCN0018-5c857.jpg` (8 KB)
  - `local/cache-vignettes/L178xH100/DSCN9926-ccf43.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN9936-06e1b.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN9939-2d713.jpg` (4 KB)
  - `local/cache-vignettes/L178xH100/DSCN9948-9fb33.jpg` (7 KB)
  - `local/cache-vignettes/L178xH100/DSCN9952-8d3d1.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN9987-7ea3e.jpg` (6 KB)
  - `local/cache-vignettes/L178xH100/DSCN9991-c14b2.jpg` (6 KB)
  - `local/cache-vignettes/L200xH108/arton76-f4af0.png` (38 KB)
  - `local/cache-vignettes/L500xH282/DSCN0005-dedda-2e1bc.jpg` (36 KB)
  - `local/cache-vignettes/L57xH100/DSCN0016-aa5f4.jpg` (3 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### O projeto Puxirão participou da 12ª OID

- **Slug:** `O-projeto-Puxirao-participou-da`
- **URL original:** <https://www.fandangoemcananeia.art.br/O-projeto-Puxirao-participou-da>
- **Arquivo local:** `site/O-projeto-Puxirao-participou-da.html` (21 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH108/arton81-410e3.png` (39 KB)
  - `local/cache-vignettes/L500xH267/noticia_participacao_oid-d1085-e0191.png` (231 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Objetivos

- **Slug:** `Objetivos`
- **URL original:** <https://www.fandangoemcananeia.art.br/Objetivos>
- **Arquivo local:** `site/Objetivos.html` (21 KB)
- **Status:** **OK**
- **Página pai:** `Puxirao`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L150xH120/arton2-70c11.png` (12 KB)
  - `local/cache-vignettes/L400xH300/mariano_seu_ze_pereira-8a813-c1581.png` (224 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Parceiros

- **Slug:** `Parceiros`
- **URL original:** <https://www.fandangoemcananeia.art.br/Parceiros>
- **Arquivo local:** `site/Parceiros.html` (24 KB)
- **Status:** **OK**
- **Página pai:** `Puxirao`
- **Assets referenciados:** 25

  **Imagens (6):**

  - `local/cache-vignettes/L150xH120/arton48-aae3a.jpg` (5 KB)
  - `local/cache-vignettes/L400xH267/mandicuera_EscunaHacker-01-06-13-CamCaco_011-508ea-2a089.png` (231 KB)
  - `local/cache-vignettes/L8xH11/puce-32883.gif` (0 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Patrimônio Cultural

- **Slug:** `Patrimonio-Cultural`
- **URL original:** <https://www.fandangoemcananeia.art.br/Patrimonio-Cultural>
- **Arquivo local:** `site/Patrimonio-Cultural.html` (19 KB)
- **Status:** **OK**
- **Página pai:** `Fandango`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH151/arton12-0c195.png` (50 KB)
  - `local/cache-vignettes/L350xH263/fandango_patrimonio_cultural-06c6d.png` (130 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Paulinho Pereira

- **Slug:** `Paulinho-Pereira`
- **URL original:** <https://www.fandangoemcananeia.art.br/Paulinho-Pereira>
- **Arquivo local:** `site/Paulinho-Pereira.html` (19 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `IMG/jpg/DSCN9178.jpg` (398 KB)
  - `local/cache-vignettes/L150xH200/arton34-5a4b7.jpg` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Portal Web

- **Slug:** `Portal-Web`
- **URL original:** <https://www.fandangoemcananeia.art.br/Portal-Web>
- **Arquivo local:** `site/Portal-Web.html` (21 KB)
- **Status:** **OK**
- **Página pai:** `Produtos-sociais`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L500xH282/tela_spip-509af-14e7a.png` (136 KB)
  - `local/cache-vignettes/L65xH66/arton19-f80c6.png` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Produtos sociais

- **Slug:** `Produtos-sociais`
- **URL original:** <https://www.fandangoemcananeia.art.br/Produtos-sociais>
- **Arquivo local:** `site/Produtos-sociais.html` (22 KB)
- **Status:** **OK**
- **Página pai:** `Puxirao`
- **Assets referenciados:** 26

  **Imagens (7):**

  - `local/cache-vignettes/L65xH66/arton16-a4ec9.png` (3 KB)
  - `local/cache-vignettes/L65xH66/arton17-9ce6c.png` (3 KB)
  - `local/cache-vignettes/L65xH66/arton18-c32d1.png` (3 KB)
  - `local/cache-vignettes/L65xH66/arton19-f80c6.png` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Programa Puxirão: fandango caiçara e software livre

- **Slug:** `Cultura-Digital`
- **URL original:** <https://www.fandangoemcananeia.art.br/Cultura-Digital>
- **Arquivo local:** `site/Cultura-Digital.html` (20 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 23

  **Imagens (4):**

  - `local/cache-vignettes/L200xH118/arton71-e0485.png` (52 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Projeto

- **Slug:** `Projeto`
- **URL original:** <https://www.fandangoemcananeia.art.br/Projeto>
- **Arquivo local:** `site/Projeto.html` (19 KB)
- **Status:** **OK**
- **Página pai:** `Puxirao`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH188/arton37-753e8.jpg` (54 KB)
  - `local/cache-vignettes/L500xH375/DSC00221-e63af.jpg` (32 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Prêmio Fandango Caiçara

- **Slug:** `Premio-Fandango-Caicara`
- **URL original:** <https://www.fandangoemcananeia.art.br/Premio-Fandango-Caicara>
- **Arquivo local:** `site/Premio-Fandango-Caicara.html` (21 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `IMG/jpg/fotos_dia2_1a_festa_do_fandango_caicara_cananeia_2016_48.jpg` (145 KB)
  - `local/cache-vignettes/L200xH107/arton89-191c8.png` (37 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Puxirão

- **Slug:** `Puxirao`
- **URL original:** <https://www.fandangoemcananeia.art.br/Puxirao>
- **Arquivo local:** `site/Puxirao.html` (22 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 27

  **Imagens (8):**

  - `IMG/jpg/jornal_varacao.jpg` (24 KB)
  - `local/cache-vignettes/L107xH100/arton37-e708a.jpg` (3 KB)
  - `local/cache-vignettes/L125xH100/arton2-be848.png` (12 KB)
  - `local/cache-vignettes/L125xH100/arton48-f7b80.jpg` (3 KB)
  - `local/cache-vignettes/L150xH85/arton39-d0790.png` (20 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Terra Firme

- **Slug:** `Terra-Firme`
- **URL original:** <https://www.fandangoemcananeia.art.br/Terra-Firme>
- **Arquivo local:** `site/Terra-Firme.html` (22 KB)
- **Status:** **OK**
- **Página pai:** `Grupos`
- **Assets referenciados:** 32

  **Imagens (13):**

  - `local/cache-vignettes/L134xH100/1371479_10200854699551862_1292306187_n-cd6c0.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/1373458_10200854699231854_476849454_n-0d69b.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/1376165_10200854698111826_839247305_n-50f3b.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/1395001_10200854700071875_434073326_n-be0c3.jpg` (6 KB)
  - `local/cache-vignettes/L143xH100/cananeia_especial1-abca6.jpg` (6 KB)
  - `local/cache-vignettes/L200xH134/arton67-a5bba.jpg` (6 KB)
  - `local/cache-vignettes/L300xH225/cananeia_especial2-1976c-31352.jpg` (24 KB)
  - `local/cache-vignettes/L75xH100/1369113_10200854699031849_355675094_n-c3c00.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/1388003_10200854698831844_33680991_n-fd018.jpg` (4 KB)
  - `local/cache-vignettes/L75xH100/962852_10200854698591838_483982108_n-dee15.jpg` (3 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Tá chegando a hora...

- **Slug:** `Ta-chegando-a-hora`
- **URL original:** <https://www.fandangoemcananeia.art.br/Ta-chegando-a-hora>
- **Arquivo local:** `site/Ta-chegando-a-hora.html` (21 KB)
- **Status:** **OK**
- **Página pai:** `index`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH108/arton91-fae60.png` (50 KB)
  - `local/cache-vignettes/L500xH268/arte_festadofandango2018_noticias_fandangoemcananeia-6e4b1.png` (277 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Violas de Ouro São Paulo Bagre

- **Slug:** `Violas-de-Ouro-Sao-Paulo-Bagre`
- **URL original:** <https://www.fandangoemcananeia.art.br/Violas-de-Ouro-Sao-Paulo-Bagre>
- **Arquivo local:** `site/Violas-de-Ouro-Sao-Paulo-Bagre.html` (25 KB)
- **Status:** **OK**
- **Página pai:** `Grupos`
- **Assets referenciados:** 33

  **Imagens (14):**

  - `IMG/jpg/Rafael_Xavier_3004.jpg` (5.1 MB)
  - `IMG/jpg/Rafael_Xavier_3040.jpg` (5.3 MB)
  - `IMG/jpg/Rafael_Xavier_3050.jpg` (5.5 MB)
  - `IMG/jpg/Rafael_Xavier_3051.jpg` (5.5 MB)
  - `IMG/jpg/Rafael_Xavier_3053.jpg` (5.6 MB)
  - `IMG/jpg/Rafael_Xavier_3063.jpg` (5.1 MB)
  - `IMG/jpg/Rafael_Xavier_3064.jpg` (5.1 MB)
  - `IMG/jpg/Rafael_Xavier_3067.jpg` (5.1 MB)
  - `local/cache-vignettes/L200xH130/arton31-ed845.jpg` (9 KB)
  - `local/cache-vignettes/L360xH270/u_100-14710-42104.jpg` (91 KB)
  - `local/cache-vignettes/L8xH11/puce-32883.gif` (0 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Vídeos e fotos

- **Slug:** `Videos-e-fotos`
- **URL original:** <https://www.fandangoemcananeia.art.br/Videos-e-fotos>
- **Arquivo local:** `site/Videos-e-fotos.html` (24 KB)
- **Status:** **OK**
- **Página pai:** `Fandango`
- **Assets referenciados:** 42

  **Imagens (23):**

  - `IMG/jpg/DSC02579.jpg` (810 KB)
  - `IMG/jpg/DSC05113.jpg` (1.2 MB)
  - `IMG/jpg/DSC05876.jpg` (1.3 MB)
  - `local/cache-vignettes/L134xH100/04-921b4.jpg` (7 KB)
  - `local/cache-vignettes/L134xH100/25-8d13d.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/32-96f2d.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/35-b0f26.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/37-15e68.jpg` (6 KB)
  - `local/cache-vignettes/L134xH100/8-f3c2c.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/DSC02838-b04f0.jpg` (4 KB)
  - `local/cache-vignettes/L134xH100/dsc00104-7e2cc.jpg` (5 KB)
  - `local/cache-vignettes/L134xH100/dsc00106-42d78.jpg` (5 KB)
  - `local/cache-vignettes/L150xH100/Galeria_Lagamar-c14d6.jpg` (7 KB)
  - `local/cache-vignettes/L150xH100/OAAAALgywqzFEt9BI1WQj_bHkP6q2UfX0vriAhZ51QHJpOBFPw5VNgIak2NZPoAptc0yRSnBG8q7H9h8sH5BnKcokdYAm1T1UAmM287NQ6QJykRJHYolN6eojuQH-b5ef2.jpg` (6 KB)
  - `local/cache-vignettes/L150xH100/OgAAAMPk3KeF6Sm1XkCb5vooV6n33exCQ6EeWjWsF5ML3d6DHVhOXDLVMtqPkuVFtbUHDREqCjtgWaaQW-b3Vsz0REUAm1T1ULAPl2EVdLB_pKeU-J3lWIB2JIkl-dfa9b.jpg` (4 KB)
  - `local/cache-vignettes/L175xH100/OgAAADFj29hvjRaq2juVW2d440cwZr8WZB1ePI-b8KgvSRYVYUOEZLIhfutOAvyuzZHQ6eWngghaCy6c4N2Dl2BaJZoAm1T1UHXt1MNOvCMcAiUaUfItJxkrLMv5-0f6d3.jpg` (7 KB)
  - `local/cache-vignettes/L68xH100/OAAAAGQyUm9tcU9sMIkkakQxjH2Xj2fyjmsfV2dDutvqOeqRLA6VIr0lLEb2mFNNrJlBVrnl2_BrlNzw7ldux8cvSbYAm1T1UMnw50S6eikIIc4V0a36vcIIa7cm-cede4.jpg` (4 KB)
  - `local/cache-vignettes/L68xH100/OgAAADVEm5kVpGwbpbwQHFrghTdKsSXXPTT8LTlads44mf_w6DqhrFRvL1DyDtzubHQCKpNaY1p-iDizi519MnLtWTYAm1T1UBQ0V1L75lj7F4lLP7lAGQ5SKode-77344.jpg` (4 KB)
  - `local/cache-vignettes/L76xH100/10-70023.jpg` (4 KB)
  - `local/cache-vignettes/L76xH100/9-1ec43.jpg` (3 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Zé Pereira

- **Slug:** `Ze-Pereira`
- **URL original:** <https://www.fandangoemcananeia.art.br/Ze-Pereira>
- **Arquivo local:** `site/Ze-Pereira.html` (20 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L150xH200/arton15-81c69.jpg` (6 KB)
  - `local/cache-vignettes/L349xH472/rc-27685-a7039.jpg` (163 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


### Ângelo Ramos

- **Slug:** `Angelo-Ramos`
- **URL original:** <https://www.fandangoemcananeia.art.br/Angelo-Ramos>
- **Arquivo local:** `site/Angelo-Ramos.html` (19 KB)
- **Status:** **OK**
- **Página pai:** `Mestres`
- **Assets referenciados:** 24

  **Imagens (5):**

  - `local/cache-vignettes/L200xH134/arton61-bfa0b.jpg` (7 KB)
  - `local/cache-vignettes/L287xH456/seu_angelo-febcf.png` (237 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
  - `squelettes-dist/spip.png` (2 KB)

  **CSS (7):**

  - `extensions/porte_plume/css/barre_outils.css` (4 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
  - `plugins/auto/theme_californiumite/habillage.css` (10 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
  - `plugins/auto/zpip_v1/spip_style.css` (3 KB)
  - `squelettes-dist/impression.css` (3 KB)
  - `squelettes-dist/spip_formulaires.css` (5 KB)

  **JavaScript (12):**

  - `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
  - `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
  - `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)
  - `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
  - `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
  - `prive/javascript/ajaxCallback.js` (11 KB)
  - `prive/javascript/jquery.cookie.js` (4 KB)
  - `prive/javascript/jquery.form.js` (28 KB)
  - `prive/javascript/jquery.js` (179 KB)


---


---

---

## 🔀 Redirects 301 (preservação de SEO)

Lista de redirecionamentos do URL antigo (SPIP) para o URL novo (estático limpo).
Aplicado automaticamente pelo `.htaccess` no servidor Apache.

### URLs que mudaram de slug

| URL antigo (SPIP) | URL novo (estático limpo) | Página |
|---|---|---|
| `/` | `/` | Início |
| `/1ª-Festa-do-Fandango-Caicara-de` | `/1-Festa-do-Fandango-Caicara-de/` | 1ª Festa do Fandango Caiçara de Cananeia |
| `/2ª-Festa-do-Fandango-Caicara-de` | `/2-Festa-do-Fandango-Caicara-de/` | 2ª Festa do Fandango Caiçara de Cananeia |
| `/Natureza,80` | `/Natureza-80/` | Natureza (artigo 80) |

### Páginas removidas (vão para `/`)

| URL removido | Motivo |
|---|---|
| `/slider1` | Slide 1 do SPIP (placeholder) |
| `/slider2` | Slide 2 do SPIP (placeholder) |
| `/Nova-materia` | Página vazia de exemplo do SPIP |
| `/icone` | Página vazia de ícone |
| `?debut_articles=*` | Paginação antiga do SPIP |
| `/spip.php?page=login` | Login do admin (removido) |
| `/spip.php?page=plan` | Mapa do site antigo (substituído por sitemap.xml) |
| `/spip.php?page=backend` | Feed RSS (removido - site estático) |
| `/spip.php?action=cron` | Tarefa agendada SPIP (removida) |
| `/spip.php?page=barre_outils_*` | CSS da barra de edição admin (removido) |
| `/favicon.ico` | Favicon (arquivo original vazio, removido) |

### Regra geral de rewrite

Todas as URLs do tipo `/Nome.html` são reescritas para `/Nome/` (sem extensão).
Exemplo: `/Ze-Pereira.html` → `/Ze-Pereira/`

### Configuração HTTPS

O `.htaccess` força HTTPS. Todas as requisições HTTP são redirecionadas (301) para HTTPS.



## Lista consolidada de todos os assets

Total de assets únicos: **1076**

### `IMG/` (281 arquivos)

- `IMG/jpg/12232699_1075508925839028_5605818588108382832_o.jpg` (228 KB)
- `IMG/jpg/12322609_1076250022431585_3327245267137528295_o_1_.jpg` (103 KB)
- `IMG/jpg/12322617_1076249762431611_6554320287414218485_o.jpg` (183 KB)
- `IMG/jpg/13115950_1076250862431501_2214173033235536381_o.jpg` (268 KB)
- `IMG/jpg/13115950_1076251335764787_2187071644458492560_o.jpg` (206 KB)
- `IMG/jpg/13227655_1076251132431474_3297021200732566116_o.jpg` (280 KB)
- `IMG/jpg/13227655_1076251132431474_3297021200732566116_o_1_.jpg` (280 KB)
- `IMG/jpg/13227661_1075507055839215_3375345727391640019_o.jpg` (272 KB)
- `IMG/jpg/13227812_1076250242431563_8735647375495910503_o.jpg` (228 KB)
- `IMG/jpg/13243969_1076250365764884_203265086870310951_o.jpg` (311 KB)
- `IMG/jpg/13247866_1075513949171859_6672840712381833689_o.jpg` (326 KB)
- `IMG/jpg/13248398_1075506249172629_8789655659657964287_o.jpg` (281 KB)
- `IMG/jpg/13248399_1075505549172699_7845213277083426642_o.jpg` (265 KB)
- `IMG/jpg/13254664_1075513179171936_8381867252378284812_o.jpg` (267 KB)
- `IMG/jpg/13254670_1075507589172495_3345273443506609490_o.jpg` (306 KB)
- `IMG/jpg/13254738_1075512429172011_3300565288310940985_o.jpg` (340 KB)
- `IMG/jpg/13254760_1075511689172085_5153974210411206731_o.jpg` (225 KB)
- `IMG/jpg/13267998_1075512232505364_2055320635613483972_o.jpg` (291 KB)
- `IMG/jpg/13268016_1075511585838762_5599236152025617550_o.jpg` (266 KB)
- `IMG/jpg/13268055_1075506905839230_7412188209502901435_o.jpg` (428 KB)
- `IMG/jpg/13268135_1075511629172091_8064686998844360395_o.jpg` (199 KB)
- `IMG/jpg/13268229_1076251589098095_9142089765239863972_o.jpg` (335 KB)
- `IMG/jpg/13268250_1075506549172599_8005272368799160650_o.jpg` (290 KB)
- `IMG/jpg/13268262_1076250185764902_5235453477401747154_o.jpg` (255 KB)
- `IMG/jpg/13268288_1076250809098173_7417392197269641431_o.jpg` (341 KB)
- `IMG/jpg/13268421_1076251059098148_8285972990412760086_o.jpg` (320 KB)
- `IMG/jpg/13268428_1076249889098265_7391958302521835022_o.jpg` (209 KB)
- `IMG/jpg/13301232_1079306192125968_6565624680067977961_o.jpg` (214 KB)
- `IMG/jpg/13301243_1079233045466616_1012719379065694745_o.jpg` (153 KB)
- `IMG/jpg/13301251_1076249872431600_7001801613887811405_o_1_.jpg` (363 KB)
- `IMG/jpg/13301337_1076250462431541_792534431475515374_o.jpg` (292 KB)
- `IMG/jpg/13301364_1079272848795969_6466149809670572416_o.jpg` (293 KB)
- `IMG/jpg/13301403_1079264832130104_7880301696929559403_o.jpg` (172 KB)
- `IMG/jpg/13301434_1079258775464043_556841763103857873_o.jpg` (224 KB)
- `IMG/jpg/13301445_1079241702132417_8599050701711931169_o.jpg` (286 KB)
- `IMG/jpg/13301460_1075506435839277_4472644495761402809_o.jpg` (504 KB)
- `IMG/jpg/13301467_1079235882132999_7115892130661602507_o-2.jpg` (164 KB)
- `IMG/jpg/13301467_1079235882132999_7115892130661602507_o.jpg` (164 KB)
- `IMG/jpg/13301477_1079237918799462_1150778034860330981_o.jpg` (207 KB)
- `IMG/jpg/13301482_1079306335459287_4564108995514419407_o.jpg` (203 KB)
- `IMG/jpg/13301508_1079273075462613_5191430013365146921_o.jpg` (239 KB)
- `IMG/jpg/13301525_1079237702132817_4650437282204768244_o.jpg` (282 KB)
- `IMG/jpg/13301526_1079233382133249_2244378613599543582_o.jpg` (146 KB)
- `IMG/jpg/13301549_1079271878796066_8725811155358072905_o.jpg` (345 KB)
- `IMG/jpg/13304991_1079238615466059_343727537094328064_o.jpg` (228 KB)
- `IMG/jpg/13304998_1075505622506025_5307362293781662973_o.jpg` (286 KB)
- `IMG/jpg/13305031_1079232242133363_6383484558218265512_o.jpg` (190 KB)
- `IMG/jpg/13305046_1079236825466238_2995937111962437851_o-2-r90.jpg` (348 KB)
- `IMG/jpg/13305046_1079236825466238_2995937111962437851_o.jpg` (317 KB)
- `IMG/jpg/13305078_1076250372431550_6060155569853427574_o_1_.jpg` (325 KB)
- `IMG/jpg/13305085_1076249649098289_6732477892388314606_o.jpg` (209 KB)
- `IMG/jpg/13305111_1079266912129896_7465233908329698137_o.jpg` (263 KB)
- `IMG/jpg/13305114_1075512685838652_416112188580598250_o.jpg` (261 KB)
- `IMG/jpg/13305121_1076250189098235_47026192685506384_o.jpg` (223 KB)
- `IMG/jpg/13305152_1076249805764940_5472514652783038420_o.jpg` (198 KB)
- `IMG/jpg/13305159_1076249652431622_7859957590042090335_o.jpg` (183 KB)
- `IMG/jpg/13305194_1079277302128857_28012014208633729_o.jpg` (278 KB)
- `IMG/jpg/13305198_1076250439098210_3091114935182458091_o.jpg` (290 KB)
- `IMG/jpg/13305211_1075506185839302_1521389449692546432_o.jpg` (314 KB)
- `IMG/jpg/13308143_1075505475839373_8617823150311030811_o.jpg` (304 KB)
- `IMG/jpg/13308167_1079272602129327_8179316623690420645_o.jpg` (293 KB)
- `IMG/jpg/13308189_1079243678798886_7846421594724192257_o.jpg` (348 KB)
- `IMG/jpg/13308192_1079261288797125_1857638973285448691_o.jpg` (195 KB)
- `IMG/jpg/13308242_1076250495764871_2861905761117262623_o_1_.jpg` (171 KB)
- `IMG/jpg/13308244_1079232088800045_4492478252374015322_o.jpg` (192 KB)
- `IMG/jpg/13308267_1079294985460422_8870735566719178576_o.jpg` (272 KB)
- `IMG/jpg/13308276_1076250749098179_77881283741477945_o.jpg` (327 KB)
- `IMG/jpg/13308282_1079278155462105_6282167973235583479_o-2.jpg` (299 KB)
- `IMG/jpg/13308282_1079278155462105_6282167973235583479_o.jpg` (299 KB)
- `IMG/jpg/13308367_1079244018798852_6374241505280355498_o-2.jpg` (232 KB)
- `IMG/jpg/13308367_1079244018798852_6374241505280355498_o.jpg` (232 KB)
- `IMG/jpg/13308375_1076250619098192_2515131669200408875_o.jpg` (249 KB)
- `IMG/jpg/13308428_1079239662132621_4859702617482708345_o.jpg` (274 KB)
- `IMG/jpg/13308442_1079253068797947_422123339998009295_o.jpg` (151 KB)
- `IMG/jpg/13308444_1079304242126163_89161860595507219_o.jpg` (279 KB)
- `IMG/jpg/13308488_1075509422505645_3949798281796077254_o.jpg` (204 KB)
- `IMG/jpg/13308525_1076251439098110_6036076940515550509_o.jpg` (289 KB)
- `IMG/jpg/13308550_1076249839098270_4883271374426646217_o_1_.jpg` (200 KB)
- `IMG/jpg/13308609_1075511315838789_9107661089301342425_o.jpg` (222 KB)
- `IMG/jpg/13308664_1076249709098283_4497695605271564645_o.jpg` (216 KB)
- `IMG/jpg/13308675_1075514019171852_872171814626111930_o.jpg` (255 KB)
- `IMG/jpg/13308736_1079233612133226_2211869573122895716_o.jpg` (131 KB)
- `IMG/jpg/13308751_1079232422133345_7610360886389425605_o.jpg` (224 KB)
- `IMG/jpg/13316834_1075509515838969_3345581327743928567_o.jpg` (217 KB)
- `IMG/jpg/13316860_1079232325466688_8121208129251000448_o.jpg` (133 KB)
- `IMG/jpg/13316865_1076250572431530_8341961384569737897_o.jpg` (227 KB)
- `IMG/jpg/13316875_1076250565764864_7595415614020473374_o.jpg` (303 KB)
- `IMG/jpg/13316937_1076251382431449_1200765745638391308_o.jpg` (266 KB)
- `IMG/jpg/13316943_1076250795764841_4976588736733272852_o.jpg` (309 KB)
- `IMG/jpg/13316947_1079254925464428_8715288332263052867_o.jpg` (317 KB)
- `IMG/jpg/13316948_1079271605462760_8109040740058883396_o.jpg` (252 KB)
- `IMG/jpg/13317023_1076251112431476_4749254368697072911_o.jpg` (268 KB)
- `IMG/jpg/13320348_1079279955461925_4867954174403044922_o.jpg` (334 KB)
- `IMG/jpg/13320358_1076250925764828_37028684721144178_o.jpg` (177 KB)
- `IMG/jpg/13320407_1075513119171942_1014275378221738098_o_1_.jpg` (248 KB)
- `IMG/jpg/13320476_1075514459171808_3483452810028514506_o.jpg` (288 KB)
- `IMG/jpg/13320490_1079240085465912_2959664574583776144_o.jpg` (264 KB)
- `IMG/jpg/13320499_1076249962431591_1375855808743073815_o_3_.jpg` (200 KB)
- `IMG/jpg/13320542_1076251249098129_705318032552765465_o.jpg` (280 KB)
- `IMG/jpg/13320709_1075507742505813_34628559811846009_o.jpg` (345 KB)
- `IMG/jpg/13320729_1075507232505864_4363841272373930180_o.jpg` (190 KB)
- `IMG/jpg/13320754_1075504435839477_7176507828282414998_o_1_.jpg` (239 KB)
- `IMG/jpg/13320760_1079304715459449_7618488717471688342_o.jpg` (297 KB)
- `IMG/jpg/13320767_1076250919098162_6582619854785036928_o.jpg` (356 KB)
- `IMG/jpg/13320777_1076250032431584_4479185856217378334_o_1_.jpg` (172 KB)
- `IMG/jpg/13320816_1079276868795567_9205606441263106793_o.jpg` (320 KB)
- `IMG/jpg/13320854_1076249745764946_5496917782587217267_o.jpg` (218 KB)
- `IMG/jpg/13320867_1079242912132296_4438057938149345807_o.jpg` (353 KB)
- `IMG/jpg/13320879_1076251649098089_1687675040997717623_o.jpg` (336 KB)
- `IMG/jpg/13320906_1079235438799710_5545362728803112078_o.jpg` (216 KB)
- `IMG/jpg/13320973_1075514092505178_4817456437684159328_o.jpg` (179 KB)
- `IMG/jpg/13323173_1079240728799181_5456903316701449326_o.jpg` (225 KB)
- `IMG/jpg/13323214_1076250739098180_7818444116089433764_o.jpg` (307 KB)
- `IMG/jpg/13323214_1076251422431445_3628475376404757073_o.jpg` (293 KB)
- `IMG/jpg/13323228_1079297942126793_1003010045703220272_o.jpg` (219 KB)
- `IMG/jpg/13323292_1079234662133121_5741200735555498133_o.jpg` (245 KB)
- `IMG/jpg/13323298_1076249949098259_7943128451828005492_o_1_.jpg` (145 KB)
- `IMG/jpg/13323355_1075512855838635_5684821247787901961_o.jpg` (295 KB)
- `IMG/jpg/13323363_1076250359098218_2108330255088768358_o.jpg` (206 KB)
- `IMG/jpg/13323367_1079275145462406_2431876237795502921_o.jpg` (225 KB)
- `IMG/jpg/13323512_1079237082132879_2109532908944007723_o.jpg` (259 KB)
- `IMG/jpg/13323513_1075512742505313_3610228213969166353_o.jpg` (274 KB)
- `IMG/jpg/13323515_1075507169172537_899579967073891021_o-2.jpg` (220 KB)
- `IMG/jpg/13323515_1075507169172537_899579967073891021_o.jpg` (220 KB)
- `IMG/jpg/13323518_1079249105465010_6065675660289938105_o.jpg` (351 KB)
- `IMG/jpg/13323529_1079233258799928_2522938225843835991_o.jpg` (215 KB)
- `IMG/jpg/13323536_1075514259171828_6666236013877437924_o.jpg` (223 KB)
- `IMG/jpg/13323537_1079239388799315_3602114513997349223_o.jpg` (298 KB)
- `IMG/jpg/13323538_1076250685764852_8692891093287953061_o.jpg` (228 KB)
- `IMG/jpg/13323585_1076250025764918_2761057211110763737_o_1_.jpg` (212 KB)
- `IMG/jpg/13323603_1079268938796360_7132876966533624969_o.jpg` (272 KB)
- `IMG/jpg/13323610_1079305225459398_5028620080807722668_o.jpg` (275 KB)
- `IMG/jpg/13323628_1075514385838482_1964458915442237795_o.jpg` (260 KB)
- `IMG/jpg/13323641_1076250072431580_3752937062430742132_o_1_.jpg` (306 KB)
- `IMG/jpg/13323687_1079274712129116_4295417798424027501_o.jpg` (272 KB)
- `IMG/jpg/13323712_1075507475839173_7175475575790670072_o.jpg` (357 KB)
- `IMG/jpg/13323736_1079239042132683_4741258295288530791_o.jpg` (257 KB)
- `IMG/jpg/13323738_1079263418796912_3366045151531122098_o.jpg` (213 KB)
- `IMG/jpg/13323751_1079232828799971_1483253728786985874_o.jpg` (181 KB)
- `IMG/jpg/13329382_1079274112129176_477610579421611231_o.jpg` (235 KB)
- `IMG/jpg/13329437_1076250962431491_1529321515998963446_o.jpg` (340 KB)
- `IMG/jpg/13329448_1079237332132854_8325931793984816528_o.jpg` (238 KB)
- `IMG/jpg/13329502_1079234112133176_3043627520102021015_o.jpg` (144 KB)
- `IMG/jpg/13329545_1079273645462556_329071289408680213_o.jpg` (225 KB)
- `IMG/jpg/13340199_1079291628794091_7815085642707368623_o.jpg` (289 KB)
- `IMG/jpg/13340286_1079233472133240_2829268272314942789_o.jpg` (133 KB)
- `IMG/jpg/13346178_1079276595462261_3746320459417203682_o.jpg` (313 KB)
- `IMG/jpg/13346244_1079244942132093_2020174106766753234_o.jpg` (123 KB)
- `IMG/jpg/13346261_1079238348799419_3491593152137267775_o.jpg` (206 KB)
- `IMG/jpg/13350241_1079306008792653_7912740921889825177_o.jpg` (191 KB)
- `IMG/jpg/13350271_1079271422129445_9088097380591210485_o.jpg` (260 KB)
- `IMG/jpg/13350306_1079274318795822_581816325619813363_o.jpg` (278 KB)
- `IMG/jpg/13350348_1079280088795245_5300275541746692761_o.jpg` (305 KB)
- `IMG/jpg/13350394_1079284695461451_2897359321383756457_o.jpg` (316 KB)
- `IMG/jpg/13350414_1079240398799214_3600787127841262977_o.jpg` (228 KB)
- `IMG/jpg/13350428_1079275845462336_3326696110935394754_o.jpg` (273 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_01.jpg` (270 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_02.jpg` (244 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_03.jpg` (202 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_04.jpg` (297 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_05.jpg` (330 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_06.jpg` (304 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_07.jpg` (366 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_08.jpg` (259 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_09.jpg` (302 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_10.jpg` (237 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_11.jpg` (179 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_12.jpg` (321 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_13.jpg` (246 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_14.jpg` (266 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_15.jpg` (342 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_16.jpg` (329 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_17.jpg` (369 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_18.jpg` (355 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_19.jpg` (216 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_20.jpg` (335 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_21.jpg` (361 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_22.jpg` (269 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_23.jpg` (213 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_24.jpg` (236 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_25.jpg` (282 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_26.jpg` (191 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_27.jpg` (312 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_28.jpg` (283 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_29.jpg` (248 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_30.jpg` (309 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_31.jpg` (202 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_32.jpg` (164 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_33.jpg` (261 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_34.jpg` (220 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia1_35.jpg` (299 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_01.jpg` (170 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_02.jpg` (175 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_03.jpg` (228 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_04.jpg` (238 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_05.jpg` (227 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_06.jpg` (217 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_07.jpg` (146 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_08.jpg` (145 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_09.jpg` (152 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_10.jpg` (165 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_11.jpg` (233 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_12.jpg` (210 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_13.jpg` (240 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_14.jpg` (236 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_15.jpg` (214 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_16.jpg` (219 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_17.jpg` (215 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_18.jpg` (226 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_19.jpg` (276 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_20.jpg` (181 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_21.jpg` (225 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_22.jpg` (272 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_23.jpg` (219 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_24.jpg` (195 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_25.jpg` (307 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_26.jpg` (267 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia2_28.jpg` (385 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_01.jpg` (188 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_02.jpg` (283 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_04.jpg` (179 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_05.jpg` (247 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_07.jpg` (238 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_08.jpg` (196 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_09.jpg` (236 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_10.jpg` (187 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_16.jpg` (210 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_17.jpg` (149 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_18.jpg` (224 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_20.jpg` (303 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_21.jpg` (158 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_22.jpg` (147 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_23.jpg` (247 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_24.jpg` (287 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_25.jpg` (243 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_26.jpg` (203 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_27.jpg` (189 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_28.jpg` (207 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_29.jpg` (278 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_30.jpg` (235 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_31.jpg` (170 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_32.jpg` (178 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_34.jpg` (116 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_35.jpg` (241 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_36.jpg` (183 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_37.jpg` (236 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_38.jpg` (222 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_39.jpg` (238 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_41.jpg` (260 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_42.jpg` (238 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_45.jpg` (227 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_46.jpg` (280 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_47.jpg` (286 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_48.jpg` (344 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_49.jpg` (320 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_50.jpg` (332 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_51.jpg` (193 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_52.jpg` (352 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_53.jpg` (342 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_54.jpg` (247 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_55.jpg` (367 KB)
- `IMG/jpg/2a_Festa_do_Fandango_Caicara_2018_dia3_56.jpg` (268 KB)
- `IMG/jpg/DSC02579.jpg` (810 KB)
- `IMG/jpg/DSC05113.jpg` (1.2 MB)
- `IMG/jpg/DSC05876.jpg` (1.3 MB)
- `IMG/jpg/DSCN9178.jpg` (398 KB)
- `IMG/jpg/IMG_7364-2.jpg` (37 KB)
- `IMG/jpg/P1070433.jpg` (30 KB)
- `IMG/jpg/Rafael_Xavier_3004.jpg` (5.1 MB)
- `IMG/jpg/Rafael_Xavier_3040.jpg` (5.3 MB)
- `IMG/jpg/Rafael_Xavier_3050.jpg` (5.5 MB)
- `IMG/jpg/Rafael_Xavier_3051.jpg` (5.5 MB)
- `IMG/jpg/Rafael_Xavier_3053.jpg` (5.6 MB)
- `IMG/jpg/Rafael_Xavier_3063.jpg` (5.1 MB)
- `IMG/jpg/Rafael_Xavier_3064.jpg` (5.1 MB)
- `IMG/jpg/Rafael_Xavier_3067.jpg` (5.1 MB)
- `IMG/jpg/dsc00114.jpg` (64 KB)
- `IMG/jpg/fotos_dia2_1a_festa_do_fandango_caicara_cananeia_2016_48.jpg` (145 KB)
- `IMG/jpg/jornal_varacao.jpg` (24 KB)
- `IMG/png/esperanca_capa_cd.png` (286 KB)
- `IMG/png/esperanca_gravacao_estudio.png` (288 KB)

### `extensions/` (4 arquivos)

- `extensions/porte_plume/css/barre_outils.css` (4 KB)
- `extensions/porte_plume/javascript/jquery.markitup_pour_spip.js` (22 KB)
- `extensions/porte_plume/javascript/jquery.previsu_spip.js` (3 KB)
- `extensions/porte_plume/javascript/xregexp-min.js` (7 KB)

### `lib/` (2 arquivos)

- `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.css` (9 KB)
- `lib/jquery.fancybox-1.3.4/fancybox/jquery.fancybox-1.3.4.js` (29 KB)

### `local/` (772 arquivos)

- `local/cache-gd2/043b682c3dfff6ba56184370fc32fda8.jpg` (17 KB)
- `local/cache-gd2/57043a760677d4df6886f61ffbe01389.png` (100 KB)
- `local/cache-gd2/643214e946ba5bd0f9ddbf3d5a668048.jpg` (15 KB)
- `local/cache-gd2/720cdb5f6b7b6cc6ff1a5147b3e7be14.png` (79 KB)
- `local/cache-gd2/8d11473f7c9bcf2f24838328db0dabe7.png` (80 KB)
- `local/cache-gd2/c284ed93972ef4439ae69ca5ee81cc0a.png` (100 KB)
- `local/cache-gd2/c93912f82f965ed132b907270c91517b.png` (104 KB)
- `local/cache-gd2/f03453b390a6dd9af7bbe179dbf49eec.jpg` (12 KB)
- `local/cache-gd2/fbc5dbc8656d2bdd80066a3f84397355.jpg` (22 KB)
- `local/cache-gd2/febfc7f2d4c54615e926e51766092fa0.png` (105 KB)
- `local/cache-vignettes/L100xH100/bolacha_rotulo_SMD_1-2-b9afc.png` (12 KB)
- `local/cache-vignettes/L100xH100/bolacha_rotulo_SMD_1-f59b7.png` (12 KB)
- `local/cache-vignettes/L100xH100/bolacha_rotulo_SMD_2-3b4fc.png` (12 KB)
- `local/cache-vignettes/L107xH100/arton37-e708a.jpg` (3 KB)
- `local/cache-vignettes/L113xH150/rubon19-1831f.png` (25 KB)
- `local/cache-vignettes/L116xH104/image8886-d43cd.png` (20 KB)
- `local/cache-vignettes/L120xH113/Sergio-204cc.png` (23 KB)
- `local/cache-vignettes/L120xH114/Aldrin-fa415.png` (26 KB)
- `local/cache-vignettes/L120xH114/Avena-0b69d.png` (24 KB)
- `local/cache-vignettes/L120xH114/Banto-b7e74-1e0f7.png` (26 KB)
- `local/cache-vignettes/L120xH114/Bruno-b60aa.png` (23 KB)
- `local/cache-vignettes/L120xH114/Fernando-caa2a.png` (21 KB)
- `local/cache-vignettes/L120xH114/Gabriel-01587.png` (26 KB)
- `local/cache-vignettes/L120xH114/Luana-2-785f9.png` (25 KB)
- `local/cache-vignettes/L120xH114/Luana1-a5ff3.png` (26 KB)
- `local/cache-vignettes/L120xH114/Luana2-fe3ed.png` (25 KB)
- `local/cache-vignettes/L120xH114/Luiz-0a006.png` (25 KB)
- `local/cache-vignettes/L120xH114/Luma-a2a96.png` (25 KB)
- `local/cache-vignettes/L120xH114/Mexicano-99b53.png` (23 KB)
- `local/cache-vignettes/L120xH114/Natalia-93e3a.png` (25 KB)
- `local/cache-vignettes/L120xH114/Solange-c52dc.png` (23 KB)
- `local/cache-vignettes/L120xH114/Vitor-0e129-6843c.png` (23 KB)
- `local/cache-vignettes/L120xH115/Cleber-6f234-bec67.png` (26 KB)
- `local/cache-vignettes/L120xH115/Helo-5e01c.png` (25 KB)
- `local/cache-vignettes/L120xH115/Ricardo-7cc56-b4cd0.png` (28 KB)
- `local/cache-vignettes/L120xH94/Enrico-3d2cb.png` (21 KB)
- `local/cache-vignettes/L120xH94/Will-0ffcf.png` (22 KB)
- `local/cache-vignettes/L120xH95/Cacule-a4c20.png` (23 KB)
- `local/cache-vignettes/L125xH100/arton2-be848.png` (12 KB)
- `local/cache-vignettes/L125xH100/arton48-f7b80.jpg` (3 KB)
- `local/cache-vignettes/L125xH100/arton6-99609.png` (29 KB)
- `local/cache-vignettes/L127xH100/arton8-1e9d8.jpg` (5 KB)
- `local/cache-vignettes/L127xH100/p7140136-6a816.jpg` (5 KB)
- `local/cache-vignettes/L133xH100/arton77-15840.png` (26 KB)
- `local/cache-vignettes/L133xH100/p7140141-15622.jpg` (6 KB)
- `local/cache-vignettes/L133xH100/programacao_festa_fandango-e1905.png` (31 KB)
- `local/cache-vignettes/L134xH100/04-921b4.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/101_0243-60990.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/101_0248-c81d2.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/101_0249-1c60b.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/1371479_10200854699551862_1292306187_n-cd6c0.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/1373458_10200854699231854_476849454_n-0d69b.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/1376165_10200854698111826_839247305_n-50f3b.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/1395001_10200854700071875_434073326_n-be0c3.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/25-8d13d.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/29-48aa3.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_36-3e9f9.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_38-94916.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_39-1e108.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_32-f08cd.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_33-02da7.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_11-b7116.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_12-26dd9.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_15-b16b6.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_19-3be2d.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/30-86ba6.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/31-386bc.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/32-2-6e20f.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/32-96f2d.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/33-503ef.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/330474_314501391904506_1197615073_o-941f4.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/34-6964f.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/35-2-f1414.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/35-b0f26.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/36-53cad.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/37-15e68.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/37-2-c3846.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/38-2ba1a.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/8-f3c2c.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/DSC02838-b04f0.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/DSC04613-67a22.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_0428-1e09c.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_0946-57396.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_2310-c9542.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_5066-688ba.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/IMG_5093-694f6.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_5095-55042.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_5130-608b1.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_5167-36f02.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/IMG_6893-849a8.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_6900-21e1e.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_6902-04051.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/IMG_6992-424ee.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_7025-af3b0.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_7095-c6317.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_7099-84ece.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/IMG_7136-2-4cba3.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_7136-4b9e7.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_7164-5aee0.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_7203-720c7.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_7212-56458.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_7214-2-5102a.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_7214-b7a19.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_7251-e5db4.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_7273-11a21.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_7285-afc53.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_7286-d3a3f.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_7335-af316.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/IMG_7390-d8564.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_7391-3c96e.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_7392-2-fe20a.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/IMG_7392-b5a4e.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/P1010224-26ad6.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/P1030265-754ff.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/WhatsApp_Image_2018-05-02_at_16-06-21-bd9be.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/WhatsApp_Image_2018-05-02_at_16-06-35-a8134.jpg` (2 KB)
- `local/cache-vignettes/L134xH100/WhatsApp_Image_2018-05-02_at_16-06-37-99d74.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/WhatsApp_Image_2018-05-02_at_16-06-38-21a25.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/WhatsApp_Image_2018-05-02_at_16-06-39-7e889.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/arton12-b7554.png` (25 KB)
- `local/cache-vignettes/L134xH100/cuba012-d8e09.png` (34 KB)
- `local/cache-vignettes/L134xH100/cuba018-55a73.png` (27 KB)
- `local/cache-vignettes/L134xH100/cuba039-a1c29.png` (31 KB)
- `local/cache-vignettes/L134xH100/cuba074-0ceb2.png` (28 KB)
- `local/cache-vignettes/L134xH100/cuba084-cae54.png` (16 KB)
- `local/cache-vignettes/L134xH100/cuba090-d00c4.png` (32 KB)
- `local/cache-vignettes/L134xH100/cuba095-a8ced.png` (33 KB)
- `local/cache-vignettes/L134xH100/cuba113-b7f94.png` (29 KB)
- `local/cache-vignettes/L134xH100/cuba135-de637.png` (27 KB)
- `local/cache-vignettes/L134xH100/dia_folclore_sao_goncalo-6d091.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/domingueira_esperanca-ebbe3.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/dsc00104-7e2cc.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/dsc00106-42d78.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/dsc01162-2-f7b80.jpg` (3 KB)
- `local/cache-vignettes/L134xH100/dsc01172-fcc86.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/dsc01179-5fabd.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/dsc01182-4f52c.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/dsc01184-360a2.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/dsc01186-dd120.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/dsc01191-2eaea.jpg` (3 KB)
- `local/cache-vignettes/L134xH100/dsc01202-54041.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/dsc01229-34e3b.jpg` (3 KB)
- `local/cache-vignettes/L134xH100/dsc01232-bfc37.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/dsc01245-e7089.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/dsc01253-c1b8a.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/dsc01258-9657f.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/dsc01271-83903.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/dsc01292-3a984.jpg` (3 KB)
- `local/cache-vignettes/L134xH100/dsc01293-8bd3c.jpg` (3 KB)
- `local/cache-vignettes/L134xH100/dsc01295-15321.jpg` (3 KB)
- `local/cache-vignettes/L134xH100/dsc01298-35b0c.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/dsc01299-ac173.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/dsc01310-ea1d2.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/dsc01320-3bea9.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/dsc01331-943f7.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/dsc01333-2d171.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/dsc01335-f6be9.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/dsc01336-03aae.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/dsc01343-dec80.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/dsc01345-3aa10.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/dsc01348-7d0dd.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/dsc01354-6131c.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/dsc01359-70013.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/dsc01363-fb19a.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/dsc01367-14f18.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/dsc01368-8236b.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/dsc01371-4ba78.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/dsc01373-2de03.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/grupo-de-fandango-familia-neves-683e1.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/saogoncalo-6cd3f.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/sdc11536-6d9fb.jpg` (3 KB)
- `local/cache-vignettes/L134xH100/sdc11553-909f8.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/sdc11559-24973.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/sdc11560-a1185.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/sdc11566-fab31.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/sdc11578-18c90.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/sdc11582-3a08e.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/sdc11591-e5510.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/sdc11601-cf3d7.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/sdc11628-e821a.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/sdc11632-82915.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/sdc11639-2-2b755.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/sdc11654-58694.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/sdc11659-afe82.jpg` (3 KB)
- `local/cache-vignettes/L134xH100/sdc11668-b2513.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/sdc11669-7f223.jpg` (4 KB)
- `local/cache-vignettes/L134xH100/sdc11672-037ae.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/sdc11675-d5c2e.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/sdc11676-be4a9.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/sdc11694-c0aee.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/sdc11706-b98cc.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/sdc11715-19d44.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/sdc11732-d5114.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/sdc11744-77fe0.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/sdc11762-7d36c.jpg` (5 KB)
- `local/cache-vignettes/L134xH100/sdc11764-53b16.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/sdc11765-db3c9.jpg` (7 KB)
- `local/cache-vignettes/L134xH100/sdc11772-2-9c79d.jpg` (6 KB)
- `local/cache-vignettes/L134xH100/sdc11772-4279f.jpg` (6 KB)
- `local/cache-vignettes/L137xH100/cartaz_festa_fandango-2-3e9da.png` (27 KB)
- `local/cache-vignettes/L143xH100/cananeia_especial1-abca6.jpg` (6 KB)
- `local/cache-vignettes/L147xH100/convite-10842.png` (17 KB)
- `local/cache-vignettes/L149xH100/arton53-9e41d.png` (32 KB)
- `local/cache-vignettes/L150xH100/Canoa-56e83.jpg` (5 KB)
- `local/cache-vignettes/L150xH100/Dico-7d085.jpg` (5 KB)
- `local/cache-vignettes/L150xH100/F1000003-79a03.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/F1000009-dd275.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/F1000020-78813.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/F1000021-29801.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/F1000025-571e4.jpg` (5 KB)
- `local/cache-vignettes/L150xH100/Filpo-550b8.jpg` (5 KB)
- `local/cache-vignettes/L150xH100/Galeria_Lagamar-c14d6.jpg` (7 KB)
- `local/cache-vignettes/L150xH100/IMG_0854-redimensionado-dad51.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/IMG_0860-redimensionado-112db.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/IMG_0863-redimensionado-1ef63.jpg` (5 KB)
- `local/cache-vignettes/L150xH100/IMG_0866-redimensionado-35027.jpg` (5 KB)
- `local/cache-vignettes/L150xH100/IMG_0896-redimensionado-4e26f.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/IMG_0898-redimensionado-b8277.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/IMG_0914-redimensionado-39828.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/IMG_1015-redimensionado-f6b93.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/IMG_1018-redimensionado-7f8f5.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/OAAAALgywqzFEt9BI1WQj_bHkP6q2UfX0vriAhZ51QHJpOBFPw5VNgIak2NZPoAptc0yRSnBG8q7H9h8sH5BnKcokdYAm1T1UAmM287NQ6QJykRJHYolN6eojuQH-b5ef2.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/OgAAAMPk3KeF6Sm1XkCb5vooV6n33exCQ6EeWjWsF5ML3d6DHVhOXDLVMtqPkuVFtbUHDREqCjtgWaaQW-b3Vsz0REUAm1T1ULAPl2EVdLB_pKeU-J3lWIB2JIkl-dfa9b.jpg` (4 KB)
- `local/cache-vignettes/L150xH100/Todos-e0482.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/Vadico-79ef1.jpg` (6 KB)
- `local/cache-vignettes/L150xH100/arton1-a1650.png` (30 KB)
- `local/cache-vignettes/L150xH100/arton10-34a95.png` (30 KB)
- `local/cache-vignettes/L150xH100/arton54-a2dc1.png` (25 KB)
- `local/cache-vignettes/L150xH100/arton61-2f9eb.jpg` (5 KB)
- `local/cache-vignettes/L150xH100/arton62-ac108.jpg` (14 KB)
- `local/cache-vignettes/L150xH100/arton67-52a71.jpg` (4 KB)
- `local/cache-vignettes/L150xH100/arton80-ffea8.png` (31 KB)
- `local/cache-vignettes/L150xH100/filpo1-86837.jpg` (5 KB)
- `local/cache-vignettes/L150xH101/arton53-c518a.png` (31 KB)
- `local/cache-vignettes/L150xH113/arton77-c96d1.png` (30 KB)
- `local/cache-vignettes/L150xH120/arton2-70c11.png` (12 KB)
- `local/cache-vignettes/L150xH120/arton48-aae3a.jpg` (5 KB)
- `local/cache-vignettes/L150xH161/arton30-4c1b2.jpg` (9 KB)
- `local/cache-vignettes/L150xH161/arton50-4d40e.jpg` (9 KB)
- `local/cache-vignettes/L150xH200/arton15-81c69.jpg` (6 KB)
- `local/cache-vignettes/L150xH200/arton34-5a4b7.jpg` (4 KB)
- `local/cache-vignettes/L150xH200/arton55-29f4e.jpg` (5 KB)
- `local/cache-vignettes/L150xH200/arton56-d0013.jpg` (7 KB)
- `local/cache-vignettes/L150xH81/arton87-b3fd8.png` (24 KB)
- `local/cache-vignettes/L150xH81/arton88-9be65.png` (30 KB)
- `local/cache-vignettes/L150xH81/arton89-84b86.png` (22 KB)
- `local/cache-vignettes/L150xH81/arton90-b6baf.png` (26 KB)
- `local/cache-vignettes/L150xH81/arton91-b197d.png` (28 KB)
- `local/cache-vignettes/L150xH85/arton39-d0790.png` (20 KB)
- `local/cache-vignettes/L150xH85/arton4-a340d.jpg` (6 KB)
- `local/cache-vignettes/L150xH98/arton57-4a034.jpg` (5 KB)
- `local/cache-vignettes/L151xH100/DSC052451-300x199-5bda7.jpg` (6 KB)
- `local/cache-vignettes/L151xH100/IMG_6421-73739.jpg` (4 KB)
- `local/cache-vignettes/L151xH100/IMG_6436-d316f.jpg` (6 KB)
- `local/cache-vignettes/L151xH100/IMG_6453-0b7c7.jpg` (7 KB)
- `local/cache-vignettes/L151xH100/IMG_6454-2-75442.jpg` (7 KB)
- `local/cache-vignettes/L151xH100/IMG_6488-c60dd.jpg` (6 KB)
- `local/cache-vignettes/L151xH100/IMG_6489-32a2b.jpg` (7 KB)
- `local/cache-vignettes/L151xH100/Rafael_Xavier_3005-a2aac.jpg` (6 KB)
- `local/cache-vignettes/L151xH100/Rafael_Xavier_3029-d5ebc.jpg` (5 KB)
- `local/cache-vignettes/L151xH100/Rafael_Xavier_3040-2-a04d5.jpg` (4 KB)
- `local/cache-vignettes/L151xH100/Rafael_Xavier_3054-3797c.jpg` (5 KB)
- `local/cache-vignettes/L151xH100/Rafael_Xavier_3124-3d34c.jpg` (6 KB)
- `local/cache-vignettes/L151xH100/WhatsApp_Image_2018-05-03_at_00-25-52-ac147.jpg` (2 KB)
- `local/cache-vignettes/L151xH100/WhatsApp_Image_2018-05-03_at_00-25-53-ab2bd.jpg` (3 KB)
- `local/cache-vignettes/L151xH100/_DSC0237-0e7ff.jpg` (6 KB)
- `local/cache-vignettes/L152xH250/enciclopedia_caicara-7017c-9e1a7.png` (63 KB)
- `local/cache-vignettes/L155xH100/Sem_titulo-34150.png` (36 KB)
- `local/cache-vignettes/L159xH100/marco_itacuruca_ilhadocardoso_wordpress-edc03.png` (29 KB)
- `local/cache-vignettes/L175xH100/OgAAADFj29hvjRaq2juVW2d440cwZr8WZB1ePI-b8KgvSRYVYUOEZLIhfutOAvyuzZHQ6eWngghaCy6c4N2Dl2BaJZoAm1T1UHXt1MNOvCMcAiUaUfItJxkrLMv5-0f6d3.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_29-1a3fa.jpg` (9 KB)
- `local/cache-vignettes/L178xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_30-689e1.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_03-9963b.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSC01513-e11b5.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSC01514-60418.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSC01525-79c59.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSC01528-7b039.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSC01534-2f0dd.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSC01537-f8005.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSC01540-8fead.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSC01544-43291.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSC02557-defe4.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSC02560-497c2.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSC02577-e5ad3.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSC02579-2-c8d06.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSC02590-0bbc7.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSCN0006-ed00f.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSCN0007-322dc.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN0009-9eeab.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN0011-2c68f.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSCN0018-5c857.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSCN6479-222c1.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN6482-e23aa.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN8709-f035a.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSCN8715-092e4.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN8724-ac279.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSCN8728-1dd49.jpg` (5 KB)
- `local/cache-vignettes/L178xH100/DSCN8748-5dd9b.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSCN8753-c41fb.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8759-a3630.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSCN8763-29ba9.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN8772-29725.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSCN8786-39bf7.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSCN8787-a8a5a.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN8795-33708.jpg` (5 KB)
- `local/cache-vignettes/L178xH100/DSCN8799-33afa.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8817-06472.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8818-f8a0d.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8819-daf7e.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8820-e9af0.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN8822-8162b.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8823-03d71.jpg` (5 KB)
- `local/cache-vignettes/L178xH100/DSCN8826-346de.jpg` (5 KB)
- `local/cache-vignettes/L178xH100/DSCN8828-2acb0.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8832-08c78.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8836-12faf.jpg` (5 KB)
- `local/cache-vignettes/L178xH100/DSCN8837-518b5.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN8838-970e5.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN8847-b8f3e.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/DSCN8856-37ea2.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN8857-77f23.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8858-3fe58.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8876-3fc6d.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8879-a4fb1.jpg` (4 KB)
- `local/cache-vignettes/L178xH100/DSCN8884-fc4d8.jpg` (5 KB)
- `local/cache-vignettes/L178xH100/DSCN8900-d3b49.jpg` (5 KB)
- `local/cache-vignettes/L178xH100/DSCN8908-b4063.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8918-36575.jpg` (4 KB)
- `local/cache-vignettes/L178xH100/DSCN8925-61cea.jpg` (9 KB)
- `local/cache-vignettes/L178xH100/DSCN8929-f4748.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8936-fd26c.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8941-075d5.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN8947-8fc6f.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8949-15f17.jpg` (5 KB)
- `local/cache-vignettes/L178xH100/DSCN8953-a2cdf.jpg` (4 KB)
- `local/cache-vignettes/L178xH100/DSCN8955-e2c14.jpg` (3 KB)
- `local/cache-vignettes/L178xH100/DSCN8957-343b5.jpg` (3 KB)
- `local/cache-vignettes/L178xH100/DSCN8961-52055.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN8998-2cdd9.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN9048-cc4f2.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN9926-ccf43.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN9936-06e1b.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN9939-2d713.jpg` (4 KB)
- `local/cache-vignettes/L178xH100/DSCN9948-9fb33.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/DSCN9952-8d3d1.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN9987-7ea3e.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/DSCN9991-c14b2.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/P1010265-7efaf.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/P1010302-82431.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/P1030155-2-b8a5f.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/P1030155-37992.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/P1030176-2-50b98.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/P1030176-59983.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/P1030191-fe6ff.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/P1030217-03641.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/P1030252-aee89.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/P1030307-b1417.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/capa-ca55f.jpg` (8 KB)
- `local/cache-vignettes/L178xH100/cuba002-983aa.png` (42 KB)
- `local/cache-vignettes/L178xH100/cuba003-c7fb0.png` (34 KB)
- `local/cache-vignettes/L178xH100/cuba004-881b3.png` (42 KB)
- `local/cache-vignettes/L178xH100/cuba005-e2102.png` (41 KB)
- `local/cache-vignettes/L178xH100/cuba006-a0f45.png` (26 KB)
- `local/cache-vignettes/L178xH100/cuba008-a56cb.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba009-ee98b.png` (29 KB)
- `local/cache-vignettes/L178xH100/cuba010-17948.png` (32 KB)
- `local/cache-vignettes/L178xH100/cuba014-20c88.png` (29 KB)
- `local/cache-vignettes/L178xH100/cuba015-00c16.png` (32 KB)
- `local/cache-vignettes/L178xH100/cuba016-32e5e.png` (33 KB)
- `local/cache-vignettes/L178xH100/cuba019-c52c4.png` (36 KB)
- `local/cache-vignettes/L178xH100/cuba021-eda2f.png` (35 KB)
- `local/cache-vignettes/L178xH100/cuba022-5c4b1.png` (42 KB)
- `local/cache-vignettes/L178xH100/cuba023-7ec2a.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba025-97aad.png` (27 KB)
- `local/cache-vignettes/L178xH100/cuba026-c64d5.png` (37 KB)
- `local/cache-vignettes/L178xH100/cuba027-d4ad4.png` (41 KB)
- `local/cache-vignettes/L178xH100/cuba029-b33b5.png` (36 KB)
- `local/cache-vignettes/L178xH100/cuba030-3c00e.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba031-9492c.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba032-2feed.png` (42 KB)
- `local/cache-vignettes/L178xH100/cuba033-45bee.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba034-de9f6.png` (25 KB)
- `local/cache-vignettes/L178xH100/cuba035-5deb4.png` (32 KB)
- `local/cache-vignettes/L178xH100/cuba036-09633.png` (41 KB)
- `local/cache-vignettes/L178xH100/cuba037-f5480.png` (34 KB)
- `local/cache-vignettes/L178xH100/cuba038-eb454.png` (37 KB)
- `local/cache-vignettes/L178xH100/cuba041-94d9f.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba042-2-01f2a.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba043-f0749.png` (32 KB)
- `local/cache-vignettes/L178xH100/cuba044-f7370.png` (31 KB)
- `local/cache-vignettes/L178xH100/cuba045-c8c7d.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba047-3577c.png` (36 KB)
- `local/cache-vignettes/L178xH100/cuba048-6a138.png` (34 KB)
- `local/cache-vignettes/L178xH100/cuba049-c2725.png` (42 KB)
- `local/cache-vignettes/L178xH100/cuba050-cc9b6.png` (32 KB)
- `local/cache-vignettes/L178xH100/cuba051-960d1.png` (30 KB)
- `local/cache-vignettes/L178xH100/cuba052-5a41d.png` (35 KB)
- `local/cache-vignettes/L178xH100/cuba053-880f7.png` (45 KB)
- `local/cache-vignettes/L178xH100/cuba054-036c6.png` (33 KB)
- `local/cache-vignettes/L178xH100/cuba055-ea3fb.png` (42 KB)
- `local/cache-vignettes/L178xH100/cuba056-8739a.png` (42 KB)
- `local/cache-vignettes/L178xH100/cuba057-5dbae.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba058-30586.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba059-05dfa.png` (39 KB)
- `local/cache-vignettes/L178xH100/cuba060-2e5f5.png` (42 KB)
- `local/cache-vignettes/L178xH100/cuba061-59f7d.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba062-c7968.png` (32 KB)
- `local/cache-vignettes/L178xH100/cuba063-e64a3.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba064-4f999.png` (31 KB)
- `local/cache-vignettes/L178xH100/cuba065-b2871.png` (36 KB)
- `local/cache-vignettes/L178xH100/cuba066-64d9c.png` (43 KB)
- `local/cache-vignettes/L178xH100/cuba067-5d6ad.png` (36 KB)
- `local/cache-vignettes/L178xH100/cuba068-93a13.png` (33 KB)
- `local/cache-vignettes/L178xH100/cuba069-201a6.png` (41 KB)
- `local/cache-vignettes/L178xH100/cuba070-dcaf7.png` (32 KB)
- `local/cache-vignettes/L178xH100/cuba071-36db0.png` (39 KB)
- `local/cache-vignettes/L178xH100/cuba072-d3408.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba075-e4052.png` (39 KB)
- `local/cache-vignettes/L178xH100/cuba076-e8f62.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba080-14128.png` (42 KB)
- `local/cache-vignettes/L178xH100/cuba081-73a45.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba082-8d186.png` (36 KB)
- `local/cache-vignettes/L178xH100/cuba083-bb065.png` (28 KB)
- `local/cache-vignettes/L178xH100/cuba085-dbd13.png` (44 KB)
- `local/cache-vignettes/L178xH100/cuba086-f3ae0.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba087-2aa5c.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba088-cf436.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba089-dad79.png` (37 KB)
- `local/cache-vignettes/L178xH100/cuba091-68852.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba092-554f9.png` (30 KB)
- `local/cache-vignettes/L178xH100/cuba094-1b62d.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba097-3bd5a.png` (39 KB)
- `local/cache-vignettes/L178xH100/cuba098-10cb4.png` (28 KB)
- `local/cache-vignettes/L178xH100/cuba099-d8550.png` (35 KB)
- `local/cache-vignettes/L178xH100/cuba100-c0dba.png` (39 KB)
- `local/cache-vignettes/L178xH100/cuba101-e1c96.png` (31 KB)
- `local/cache-vignettes/L178xH100/cuba102-79e37.png` (35 KB)
- `local/cache-vignettes/L178xH100/cuba104-d1fa9.png` (35 KB)
- `local/cache-vignettes/L178xH100/cuba105-13882.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba106-b7e46.png` (37 KB)
- `local/cache-vignettes/L178xH100/cuba108-fe007.png` (35 KB)
- `local/cache-vignettes/L178xH100/cuba109-501a8.png` (27 KB)
- `local/cache-vignettes/L178xH100/cuba110-df940.png` (28 KB)
- `local/cache-vignettes/L178xH100/cuba111-f7a66.png` (28 KB)
- `local/cache-vignettes/L178xH100/cuba112-2-cc6eb.png` (25 KB)
- `local/cache-vignettes/L178xH100/cuba112-8bdac.png` (25 KB)
- `local/cache-vignettes/L178xH100/cuba114-2fef9.png` (41 KB)
- `local/cache-vignettes/L178xH100/cuba115-78d5e.png` (29 KB)
- `local/cache-vignettes/L178xH100/cuba116-86610.png` (30 KB)
- `local/cache-vignettes/L178xH100/cuba117-ae663.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba119-2f0f5.png` (36 KB)
- `local/cache-vignettes/L178xH100/cuba120-6dbd9.png` (40 KB)
- `local/cache-vignettes/L178xH100/cuba121-9e272.png` (27 KB)
- `local/cache-vignettes/L178xH100/cuba122-222fc.png` (41 KB)
- `local/cache-vignettes/L178xH100/cuba123-93ecf.png` (33 KB)
- `local/cache-vignettes/L178xH100/cuba124-01bfe.png` (44 KB)
- `local/cache-vignettes/L178xH100/cuba124-2-97d8d.png` (44 KB)
- `local/cache-vignettes/L178xH100/cuba126-15421.png` (41 KB)
- `local/cache-vignettes/L178xH100/cuba127-4099d.png` (43 KB)
- `local/cache-vignettes/L178xH100/cuba128-0be43.png` (28 KB)
- `local/cache-vignettes/L178xH100/cuba129-d5c1e.png` (33 KB)
- `local/cache-vignettes/L178xH100/cuba130-ded08.png` (37 KB)
- `local/cache-vignettes/L178xH100/cuba132-496cd.png` (37 KB)
- `local/cache-vignettes/L178xH100/cuba133-0b531.png` (38 KB)
- `local/cache-vignettes/L178xH100/cuba134-53a72.png` (31 KB)
- `local/cache-vignettes/L178xH100/cuba136-1e4c8.png` (30 KB)
- `local/cache-vignettes/L178xH100/cuba137-657c3.png` (30 KB)
- `local/cache-vignettes/L178xH100/cuba139-3f212.png` (32 KB)
- `local/cache-vignettes/L178xH100/cuba140-01833.png` (34 KB)
- `local/cache-vignettes/L178xH100/cuba141-5b181.png` (27 KB)
- `local/cache-vignettes/L178xH100/cuba142-90bfc.png` (24 KB)
- `local/cache-vignettes/L178xH100/cuba143-014a6.png` (41 KB)
- `local/cache-vignettes/L178xH100/dsc02190-f4e49.jpg` (7 KB)
- `local/cache-vignettes/L178xH100/expo_fandango_panoramica_baixa-f86f3.jpg` (6 KB)
- `local/cache-vignettes/L178xH100/maxresdefault-ee575.jpg` (8 KB)
- `local/cache-vignettes/L182xH100/1-199fd.jpg` (5 KB)
- `local/cache-vignettes/L186xH100/rc-25535-d91fa.jpg` (7 KB)
- `local/cache-vignettes/L187xH100/arton28-a01bb-68055.png` (45 KB)
- `local/cache-vignettes/L188xH100/Fandango-Apresentacao_do_Grupo_Esperanca_no_Arraia_da_Tiduca_Cananeia_FOTO_Rodolfo_Monteiro_capa-3-5fe0c.jpg` (9 KB)
- `local/cache-vignettes/L200xH100/4-0515d.jpg` (6 KB)
- `local/cache-vignettes/L200xH100/6-a584c.jpg` (8 KB)
- `local/cache-vignettes/L200xH100/7-b184a.jpg` (9 KB)
- `local/cache-vignettes/L200xH105/arton9-7edb4.jpg` (8 KB)
- `local/cache-vignettes/L200xH107/arton85-9f159.jpg` (10 KB)
- `local/cache-vignettes/L200xH107/arton87-99058.png` (40 KB)
- `local/cache-vignettes/L200xH107/arton88-b7848.png` (50 KB)
- `local/cache-vignettes/L200xH107/arton89-191c8.png` (37 KB)
- `local/cache-vignettes/L200xH107/arton90-f4748.png` (44 KB)
- `local/cache-vignettes/L200xH108/arton26-f5780.jpg` (11 KB)
- `local/cache-vignettes/L200xH108/arton28-69df8.png` (52 KB)
- `local/cache-vignettes/L200xH108/arton29-eb237.jpg` (9 KB)
- `local/cache-vignettes/L200xH108/arton65-2aa53.png` (44 KB)
- `local/cache-vignettes/L200xH108/arton66-6f07a.jpg` (7 KB)
- `local/cache-vignettes/L200xH108/arton70-2df87.png` (55 KB)
- `local/cache-vignettes/L200xH108/arton75-b46aa.png` (50 KB)
- `local/cache-vignettes/L200xH108/arton76-f4af0.png` (38 KB)
- `local/cache-vignettes/L200xH108/arton81-410e3.png` (39 KB)
- `local/cache-vignettes/L200xH108/arton86-d9dec.png` (52 KB)
- `local/cache-vignettes/L200xH108/arton91-fae60.png` (50 KB)
- `local/cache-vignettes/L200xH113/arton39-81639.png` (34 KB)
- `local/cache-vignettes/L200xH113/arton4-15fcc.jpg` (9 KB)
- `local/cache-vignettes/L200xH113/arton73-494cd.jpg` (7 KB)
- `local/cache-vignettes/L200xH118/arton69-dcc0f.jpg` (6 KB)
- `local/cache-vignettes/L200xH118/arton71-e0485.png` (52 KB)
- `local/cache-vignettes/L200xH130/arton31-ed845.jpg` (9 KB)
- `local/cache-vignettes/L200xH131/arton57-176c0.jpg` (8 KB)
- `local/cache-vignettes/L200xH134/arton1-9aaa2.png` (49 KB)
- `local/cache-vignettes/L200xH134/arton10-5c5ce.png` (50 KB)
- `local/cache-vignettes/L200xH134/arton61-bfa0b.jpg` (7 KB)
- `local/cache-vignettes/L200xH134/arton67-a5bba.jpg` (6 KB)
- `local/cache-vignettes/L200xH150/arton35-08fe3.jpg` (9 KB)
- `local/cache-vignettes/L200xH150/arton51-bc949.jpg` (8 KB)
- `local/cache-vignettes/L200xH150/arton7-ab39c.jpg` (12 KB)
- `local/cache-vignettes/L200xH151/arton12-0c195.png` (50 KB)
- `local/cache-vignettes/L200xH151/arton32-b0cb0.jpg` (9 KB)
- `local/cache-vignettes/L200xH159/arton8-c5668.jpg` (9 KB)
- `local/cache-vignettes/L200xH160/arton6-db64c.png` (64 KB)
- `local/cache-vignettes/L200xH170/arton11-39dc6.jpg` (10 KB)
- `local/cache-vignettes/L200xH188/arton37-753e8.jpg` (54 KB)
- `local/cache-vignettes/L209xH100/5-3ce7e.jpg` (8 KB)
- `local/cache-vignettes/L287xH456/seu_angelo-febcf.png` (237 KB)
- `local/cache-vignettes/L299xH448/seu_arnaldo-d4a3c.jpg` (20 KB)
- `local/cache-vignettes/L300xH104/baixe_puxirao_ogg-b05f3-a9e2f.png` (15 KB)
- `local/cache-vignettes/L300xH109/baixe_mp3_puxirao-4bf80-331f9.png` (15 KB)
- `local/cache-vignettes/L300xH169/ouca_smd_sound_clound-508d3-570fa.png` (45 KB)
- `local/cache-vignettes/L300xH200/fandango_o_que_e_itacuruca-38737.png` (89 KB)
- `local/cache-vignettes/L300xH200/mapa_cananeia_1502-f42da-15f32.png` (149 KB)
- `local/cache-vignettes/L300xH207/festa_caicara_pedrinhas-14242-4819e.png` (95 KB)
- `local/cache-vignettes/L300xH225/Joao_Alves-7e642.png` (105 KB)
- `local/cache-vignettes/L300xH225/cananeia_especial2-1976c-31352.jpg` (24 KB)
- `local/cache-vignettes/L300xH225/capa_1-42eb2-73e49.jpg` (41 KB)
- `local/cache-vignettes/L300xH242/seu_ezequiel-d01dc.png` (154 KB)
- `local/cache-vignettes/L300xH400/ze_pereira_servindo_bebida-42019-86844.png` (196 KB)
- `local/cache-vignettes/L301xH448/joao_firmino-27ca6.jpg` (27 KB)
- `local/cache-vignettes/L320xH213/IMG_6454-7b620-3ac31.jpg` (39 KB)
- `local/cache-vignettes/L326xH500/baixe_hq_puxirao_pdf-00df3-fdfb7.png` (346 KB)
- `local/cache-vignettes/L349xH472/rc-27685-a7039.jpg` (163 KB)
- `local/cache-vignettes/L350xH221/festa_enseada-27f9b-20900.png` (166 KB)
- `local/cache-vignettes/L350xH230/pereirinha-5a6d6-5c754.png` (177 KB)
- `local/cache-vignettes/L350xH233/beto_pereira-0602c-034d3.png` (143 KB)
- `local/cache-vignettes/L350xH240/Sem_titulo-2-9ccf4-577ea.jpg` (39 KB)
- `local/cache-vignettes/L350xH263/cerco_tainha_pereirinha-8a333-a800d.png` (146 KB)
- `local/cache-vignettes/L350xH263/fandango_patrimonio_cultural-06c6d.png` (130 KB)
- `local/cache-vignettes/L350xH263/peixe_seco_enseada-60b3e-8929a.png` (187 KB)
- `local/cache-vignettes/L360xH270/joao_da_toca-9ad2d-dbdc6.png` (132 KB)
- `local/cache-vignettes/L360xH270/u_100-14710-42104.jpg` (91 KB)
- `local/cache-vignettes/L360xH270/u_13-3dc7c-5e932.jpg` (123 KB)
- `local/cache-vignettes/L360xH270/u_23-1fd4b-fd240.jpg` (81 KB)
- `local/cache-vignettes/L360xH270/u_95-7d202-acf66.jpg` (165 KB)
- `local/cache-vignettes/L367xH223/canoa_motor_ilha_comprida-0e9eb-f64f4.png` (134 KB)
- `local/cache-vignettes/L380xH214/cananeia-f225b.png` (120 KB)
- `local/cache-vignettes/L380xH214/cananeia2-cfd97-7baec.png` (130 KB)
- `local/cache-vignettes/L380xH285/chamada_fandango_jureia_agenda-2877f-68ca7.png` (158 KB)
- `local/cache-vignettes/L390xH252/cachoeira_rio_das_minas-fa3e7-5591e.png` (228 KB)
- `local/cache-vignettes/L400xH207/cerco_pesca-fe77c-98dfe.png` (156 KB)
- `local/cache-vignettes/L400xH218/fandangueiros-3-b4593-c30cd.jpg` (22 KB)
- `local/cache-vignettes/L400xH225/GrupoEsperanca3_Rodolfo_Istvanffy-c8d75-3734a.jpg` (86 KB)
- `local/cache-vignettes/L400xH225/assista_baixe_filme_puxirao-b9a6b-7fb74.png` (62 KB)
- `local/cache-vignettes/L400xH225/cuba_texto_01-73489.png` (151 KB)
- `local/cache-vignettes/L400xH225/cuba_texto_02-2972d-3a8c5.png` (118 KB)
- `local/cache-vignettes/L400xH225/cuba_texto_03-f414a-b5579.png` (158 KB)
- `local/cache-vignettes/L400xH225/cuba_texto_04-a6321-61e7b.png` (151 KB)
- `local/cache-vignettes/L400xH225/ilha_cardoso_cercos-351ad-d6e42.png` (128 KB)
- `local/cache-vignettes/L400xH225/ze_pereira_em_cuba-a7837-545cd.png` (168 KB)
- `local/cache-vignettes/L400xH244/nascer_do_sol-e71df-4ab8d.png` (158 KB)
- `local/cache-vignettes/L400xH252/marco_itacuruca_ilhadocardoso_wordpress-2-a4752-98220.png` (175 KB)
- `local/cache-vignettes/L400xH265/GrupoEsperanca1_Rodolfo_Monteiro_baixa-c2a30-4ffb0.jpg` (174 KB)
- `local/cache-vignettes/L400xH265/casa_caicara_andrea_damato-19902-38654.png` (224 KB)
- `local/cache-vignettes/L400xH267/4-2-9ab64-23cc7.jpg` (42 KB)
- `local/cache-vignettes/L400xH267/fandango_musica_danca_instrumentos-40586.png` (149 KB)
- `local/cache-vignettes/L400xH267/fandangueiros-2-4077b-c896b.jpg` (30 KB)
- `local/cache-vignettes/L400xH267/mandicuera_EscunaHacker-01-06-13-CamCaco_011-508ea-2a089.png` (231 KB)
- `local/cache-vignettes/L400xH268/valo_grande_aerea-1c9d7-12666.jpg` (43 KB)
- `local/cache-vignettes/L400xH275/ariri-7aa78-0627b.png` (157 KB)
- `local/cache-vignettes/L400xH275/baile-dd3e7-3ed1f.png` (176 KB)
- `local/cache-vignettes/L400xH275/causos-b9253-63970.png` (180 KB)
- `local/cache-vignettes/L400xH275/cavacao-5e9cc-e0475.png` (260 KB)
- `local/cache-vignettes/L400xH275/mutirao_colheita_arroz-a4159-57d83.png` (248 KB)
- `local/cache-vignettes/L400xH275/varadouro-ee7b2-1efe0.png` (187 KB)
- `local/cache-vignettes/L400xH275/ze_pereira_orientando-cbe23-2c9ad.png` (216 KB)
- `local/cache-vignettes/L400xH277/maruja-14d12-ae907.png` (183 KB)
- `local/cache-vignettes/L400xH298/fandangueiro-2-34e5e-9257f.jpg` (36 KB)
- `local/cache-vignettes/L400xH300/GrupoEsperanca2_Rodolfo_Monteiro_baixa-80fcd-8277b.jpg` (53 KB)
- `local/cache-vignettes/L400xH300/descerramento_da_placa_de_inauguracao-4468a.jpg` (59 KB)
- `local/cache-vignettes/L400xH300/mariano_seu_ze_pereira-8a813-c1581.png` (224 KB)
- `local/cache-vignettes/L429xH500/GrupoEsperanca4_Aldrin_Klimke-0908e-f5b65.jpg` (63 KB)
- `local/cache-vignettes/L431xH244/ponta_da_trincheira-55a68-989b0.png` (162 KB)
- `local/cache-vignettes/L450xH316/boto_cinza-a26ca.png` (305 KB)
- `local/cache-vignettes/L450xH338/terrasimbarragemnao-1de07-727d8.jpg` (73 KB)
- `local/cache-vignettes/L473xH313/mazzaropi-3899d-c8e5e.jpg` (26 KB)
- `local/cache-vignettes/L500xH249/esquema_mapa-2-1257b.png` (142 KB)
- `local/cache-vignettes/L500xH267/noticia_participacao_oid-d1085-e0191.png` (231 KB)
- `local/cache-vignettes/L500xH268/arte_festadofandango2018_noticias_fandangoemcananeia-6e4b1.png` (277 KB)
- `local/cache-vignettes/L500xH268/arton29-a84e8-a19a7-82466.jpg` (32 KB)
- `local/cache-vignettes/L500xH268/arton65-a141a-0886d-a8a37.png` (221 KB)
- `local/cache-vignettes/L500xH268/chamada_festa_santo_andre_2013_agenda-1f997-5a4f5.png` (191 KB)
- `local/cache-vignettes/L500xH268/itacuruca_festa_cataia_pag_principal-633f8.png` (200 KB)
- `local/cache-vignettes/L500xH282/DSCN0005-dedda-2e1bc.jpg` (36 KB)
- `local/cache-vignettes/L500xH282/tela_spip-509af-14e7a.png` (136 KB)
- `local/cache-vignettes/L500xH334/IMG_0843-redimensionado-4a5e2-2ffda.jpg` (45 KB)
- `local/cache-vignettes/L500xH342/homem_do_sambaqui-d15ea.png` (365 KB)
- `local/cache-vignettes/L500xH375/2a_Festa_do_Fandango_Caicara_2018_dia2_35-18c2b-765e1.jpg` (48 KB)
- `local/cache-vignettes/L500xH375/2a_Festa_do_Fandango_Caicara_2018_dia3_13-3516e-a7e3a.jpg` (47 KB)
- `local/cache-vignettes/L500xH375/DSC00221-e63af.jpg` (32 KB)
- `local/cache-vignettes/L500xH375/IMG_5054-20198-826fa.jpg` (66 KB)
- `local/cache-vignettes/L500xH375/tela_hq_1-4ffc4-dda54.jpg` (139 KB)
- `local/cache-vignettes/L500xH376/IMG_7370-0a2d4-22e35.jpg` (46 KB)
- `local/cache-vignettes/L500xH565/cartaz_festa_santo_andre-7dadf.jpg` (83 KB)
- `local/cache-vignettes/L572xH100/DSCN8781-cd4be.jpg` (14 KB)
- `local/cache-vignettes/L57xH100/DSC01526-48b14.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSC01527-3c54c.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSC01529-32e24.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSC01531-21953.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSC01532-bbab3.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSC01533-421dd.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN0016-aa5f4.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8711-6753c.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8713-4f8fa.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8716-bfab8.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8717-6a627.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8718-85ca3.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8721-4eaed.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8722-5d8cb.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8729-ca679.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8734-27182.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8735-a8fc8.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8736-ff543.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8738-0838e.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8739-94837.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8740-61da5.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8742-e20af.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8743-f94e7.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8744-d0dd1.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8745-4b934.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8747-9e93e.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8751-19874.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8755-39913.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8775-aa3d2.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8778-dc648.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8784-41252.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8791-abc83.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8792-22c70.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8793-54027.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8805-be49f.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8806-a0317.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8807-2f5b1.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8808-d36b0.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8809-93fe1.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8810-459a9.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8812-304ae.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8813-9667a.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8814-bc883.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8815-e0cb3.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8824-d785a.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8825-507e4.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8829-39266.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8844-520ad.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8845-104b4.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8846-19966.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8849-7e3e3.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8915-19364.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8917-r90-143a3.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8965-e590f.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN8967-0bfc9.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN8988-bed87.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/DSCN9004-404c7.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN9012-19505.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/DSCN9143-9cb27.jpg` (2 KB)
- `local/cache-vignettes/L57xH100/P1010276-6f3f3.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/P1030163-e889e.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/P1030166-39e2a.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/P1030168-46956.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/P1030170-307f1.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/P1030235-74393.jpg` (3 KB)
- `local/cache-vignettes/L57xH100/cuba011-10ac2.png` (14 KB)
- `local/cache-vignettes/L57xH100/cuba013-ac4d6.png` (14 KB)
- `local/cache-vignettes/L57xH100/cuba017-08ce3.png` (13 KB)
- `local/cache-vignettes/L57xH100/cuba020-6e88a.png` (12 KB)
- `local/cache-vignettes/L57xH100/cuba024-862e4.png` (10 KB)
- `local/cache-vignettes/L57xH100/cuba028-45ea0.png` (11 KB)
- `local/cache-vignettes/L57xH100/cuba073-23185.png` (14 KB)
- `local/cache-vignettes/L57xH100/cuba078-93395.png` (12 KB)
- `local/cache-vignettes/L57xH100/cuba079-98777.png` (14 KB)
- `local/cache-vignettes/L57xH100/cuba096-2-aaaed.png` (11 KB)
- `local/cache-vignettes/L57xH100/cuba103-7deae.png` (10 KB)
- `local/cache-vignettes/L57xH100/cuba118-325fc.png` (9 KB)
- `local/cache-vignettes/L57xH100/cuba125-083d4.png` (11 KB)
- `local/cache-vignettes/L57xH100/cuba131-97d22.png` (12 KB)
- `local/cache-vignettes/L57xH100/cuba138-22bcb.png` (14 KB)
- `local/cache-vignettes/L57xH100/cuba144-d86bc.png` (11 KB)
- `local/cache-vignettes/L57xH100/cuba145-5fe94.png` (13 KB)
- `local/cache-vignettes/L57xH100/dsc02196-a23bd.jpg` (3 KB)
- `local/cache-vignettes/L65xH65/arton16-35041.png` (4 KB)
- `local/cache-vignettes/L65xH65/arton17-3ee95.png` (4 KB)
- `local/cache-vignettes/L65xH65/arton18-ab1f9.png` (3 KB)
- `local/cache-vignettes/L65xH65/arton19-83651.png` (5 KB)
- `local/cache-vignettes/L65xH66/arton16-a4ec9.png` (3 KB)
- `local/cache-vignettes/L65xH66/arton17-9ce6c.png` (3 KB)
- `local/cache-vignettes/L65xH66/arton18-c32d1.png` (3 KB)
- `local/cache-vignettes/L65xH66/arton19-f80c6.png` (4 KB)
- `local/cache-vignettes/L660xH389/arton69-81cfa.jpg` (116 KB)
- `local/cache-vignettes/L67xH100/Elvaristo-088d2.jpg` (2 KB)
- `local/cache-vignettes/L67xH100/F1000027-4401f.jpg` (3 KB)
- `local/cache-vignettes/L67xH100/IMG_0844-redimensionado-5063b.jpg` (3 KB)
- `local/cache-vignettes/L67xH100/IMG_0846-redimensionado-85c01.jpg` (3 KB)
- `local/cache-vignettes/L67xH100/IMG_0847-redimensionado-8ad3f.jpg` (3 KB)
- `local/cache-vignettes/L67xH100/IMG_0848-redimensionado-ea506.jpg` (3 KB)
- `local/cache-vignettes/L67xH100/Tambores-c2110.jpg` (2 KB)
- `local/cache-vignettes/L67xH100/WhatsApp_Image_2018-05-03_at_00-25-50_1_-c3c60.jpg` (3 KB)
- `local/cache-vignettes/L67xH100/WhatsApp_Image_2018-05-03_at_00-25-51_1_-12d6a.jpg` (3 KB)
- `local/cache-vignettes/L67xH100/naty_414_-3ba61.jpg` (2 KB)
- `local/cache-vignettes/L68xH100/OAAAAGQyUm9tcU9sMIkkakQxjH2Xj2fyjmsfV2dDutvqOeqRLA6VIr0lLEb2mFNNrJlBVrnl2_BrlNzw7ldux8cvSbYAm1T1UMnw50S6eikIIc4V0a36vcIIa7cm-cede4.jpg` (4 KB)
- `local/cache-vignettes/L68xH100/OgAAADVEm5kVpGwbpbwQHFrghTdKsSXXPTT8LTlads44mf_w6DqhrFRvL1DyDtzubHQCKpNaY1p-iDizi519MnLtWTYAm1T1UBQ0V1L75lj7F4lLP7lAGQ5SKode-77344.jpg` (4 KB)
- `local/cache-vignettes/L727xH388/arton88-580f0.png` (492 KB)
- `local/cache-vignettes/L727xH388/arton89-632e7.png` (380 KB)
- `local/cache-vignettes/L727xH388/arton90-51f30.png` (478 KB)
- `local/cache-vignettes/L727xH389/arton28-a01bb.png` (482 KB)
- `local/cache-vignettes/L727xH389/arton91-9f356.png` (558 KB)
- `local/cache-vignettes/L73xH100/3-cc70c.jpg` (3 KB)
- `local/cache-vignettes/L75xH100/101_0245-74d8f.jpg` (3 KB)
- `local/cache-vignettes/L75xH100/1369113_10200854699031849_355675094_n-c3c00.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/1388003_10200854698831844_33680991_n-fd018.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_37-4d603.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_40-72fdd.jpg` (3 KB)
- `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia1_41-81431.jpg` (3 KB)
- `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_31-328ae.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia2_34-2cefe.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/2a_Festa_do_Fandango_Caicara_2018_dia3_14-240d1.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/962852_10200854698591838_483982108_n-dee15.jpg` (3 KB)
- `local/cache-vignettes/L75xH100/IMG_7387-9a35a.jpg` (3 KB)
- `local/cache-vignettes/L75xH100/P1010266-c6023.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/P1010272-06ad7.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/arton78-0bc8b.png` (13 KB)
- `local/cache-vignettes/L75xH100/dsc01209-r270-197be.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/dsc01237-r270-4a546.jpg` (3 KB)
- `local/cache-vignettes/L75xH100/dsc01248-a564f.jpg` (3 KB)
- `local/cache-vignettes/L75xH100/dsc01276-b95ec.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/dsc01307-r270-0f7fa.jpg` (3 KB)
- `local/cache-vignettes/L75xH100/dsc01352-r270-30837.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/dsc01366-r270-aa52b.jpg` (3 KB)
- `local/cache-vignettes/L75xH100/sdc11583-r270-78804.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/sdc11670-r90-ff29c.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/sdc11699-88433.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/sdc11703-3294d.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/sdc11716-b8fb5.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/sdc11718-7e6bf.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/sdc11729-35bd0.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/sdc11733-97933.jpg` (3 KB)
- `local/cache-vignettes/L75xH100/sdc11737-3d846.jpg` (4 KB)
- `local/cache-vignettes/L75xH100/sdc11739-4af3e.jpg` (4 KB)
- `local/cache-vignettes/L76xH100/10-70023.jpg` (4 KB)
- `local/cache-vignettes/L76xH100/9-1ec43.jpg` (3 KB)
- `local/cache-vignettes/L76xH100/IMG_5052-7b650.jpg` (3 KB)
- `local/cache-vignettes/L76xH100/IMG_5056-49f52.jpg` (3 KB)
- `local/cache-vignettes/L76xH100/IMG_5060-c7d47.jpg` (3 KB)
- `local/cache-vignettes/L76xH100/IMG_5091-c1303.jpg` (4 KB)
- `local/cache-vignettes/L76xH100/IMG_5096-b5084.jpg` (3 KB)
- `local/cache-vignettes/L76xH100/IMG_7007-62935.jpg` (4 KB)
- `local/cache-vignettes/L76xH100/IMG_7056-b9766.jpg` (3 KB)
- `local/cache-vignettes/L76xH100/IMG_7209-622b9.jpg` (3 KB)
- `local/cache-vignettes/L76xH100/IMG_7295-e8cbc.jpg` (3 KB)
- `local/cache-vignettes/L76xH100/IMG_7301-345b3.jpg` (4 KB)
- `local/cache-vignettes/L76xH100/IMG_7319-60eee.jpg` (4 KB)
- `local/cache-vignettes/L76xH100/IMG_7359-3ec84.jpg` (3 KB)
- `local/cache-vignettes/L76xH100/IMG_7364-adb4c.jpg` (2 KB)
- `local/cache-vignettes/L76xH100/P1010175-1bb79.jpg` (4 KB)
- `local/cache-vignettes/L76xH100/arton74-b9e2a.png` (13 KB)
- `local/cache-vignettes/L77xH100/9-2-2d6b9.jpg` (4 KB)
- `local/cache-vignettes/L8xH11/puce-32883.gif` (0 KB)
- `local/cache-vignettes/L94xH100/arton30-00ddb.jpg` (4 KB)
- `local/cache-vignettes/L94xH100/arton50-7111d.jpg` (4 KB)
- `local/cache-vignettes/L94xH100/arton79-f005e.jpg` (4 KB)

### `plugins/` (9 arquivos)

- `plugins/auto/theme_californiumite/habillage.css` (10 KB)
- `plugins/auto/theme_californiumite/squelette_californiumite/creative.png` (9 KB)
- `plugins/auto/theme_californiumite/squelette_californiumite/css/style_californiumite.css` (6 KB)
- `plugins/auto/theme_californiumite/squelette_californiumite/js/jcarousellite.min.js` (2 KB)
- `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.cycle.js` (30 KB)
- `plugins/auto/theme_californiumite/squelette_californiumite/js/jquery.superfish.js` (4 KB)
- `plugins/auto/theme_californiumite/squelette_californiumite/js/sliders.js` (1 KB)
- `plugins/auto/theme_californiumite/squelette_californiumite/regua.png` (92 KB)
- `plugins/auto/zpip_v1/spip_style.css` (3 KB)

### `prive/` (4 arquivos)

- `prive/javascript/ajaxCallback.js` (11 KB)
- `prive/javascript/jquery.cookie.js` (4 KB)
- `prive/javascript/jquery.form.js` (28 KB)
- `prive/javascript/jquery.js` (179 KB)

### `squelettes-dist/` (4 arquivos)

- `squelettes-dist/impression.css` (3 KB)
- `squelettes-dist/puce.gif` (0 KB)
- `squelettes-dist/spip.png` (2 KB)
- `squelettes-dist/spip_formulaires.css` (5 KB)
