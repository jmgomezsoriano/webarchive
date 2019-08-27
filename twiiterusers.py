from typing import List, Any, Union

users: List[str] = ['@100cerosblog','@13whispers','@14Pulid','@1_5707','@1anaisaespinosa','@1cada8h','@1twroll',
                    '@23Sergiotm','@2_aristoteles','@2carrizos','@314ShowOficial','@35thigc','@411emilio',
                    '@42cintas','@55enrique','@5minuts_ciencia','@74Arenal','@7Gargamel','@8d4e5cdc5cd94d7','@aaovx',
                    '@abadphd','@abel_eiras','@Abel_Fisio','@abogadobsr','@AboGuzmanCubero','@Abroparaguas',
                    '@acarmonacampo','@Acebron','@AcevAsociacion','@achiquitere','@acienciacierta_',
                    '@AcosoInstituci1','@Acr9610','@acualquierotra1','@acualquierotraparte','@ACuruxa','@adabelardo',
                    '@AdamarelOscuro','@aDarPeroBien','@adcalicante','@ADCMurcia','@AdelFiume','@AdictosEqInvest',
                    '@Adonaiviene','@Adria_Molet','@Adrics02','@Adriix182','@adserias_tot','@aeac_science',
                    '@Afayaivos1','@aflojalacuerda','@afotoquimico','@agaragorn','@AgathaCantero','@agathapj',
                    '@AgrariasRepro','@agriculturamex','@agroalimentando','@aguadocarrasco','@aguedindin',
                    '@Agustin17751846','@AHdeRojas','@aida2santos','@aida_gross','@aidaivars','@AIIAP',
                    '@aingeru_mlg666','@aingeru_salceda','@ainharan80','@Aintza__Ne','@airiberri','@AitorEscu',
                    '@aitzibergh','@Alb3rTor','@albasenve','@albert_batista','@Albertigno','@albertofersie',
                    '@AlbertoGC1986','@AlbertVilella1','@albgasvil','@albpro','@AldeaCiencia','@aldoresp',
                    '@alecarlacarril2','@AleHerEDU','@AlejandroRecas','@alejoficial','@alemurilloh','@aleshammah',
                    '@Alex1907wiki','@Alex8990','@alexandrocerva5','@alexanlouisc','@AlexDoFe','@Alexmp766',
                    '@alexmurphys','@Alexny_85','@AlfaHelice','@alfonferfer','@AlfonsoHiguera2','@Alfonso___Lopez',
                    '@alfredoaranda','@AlfredoBaster6','@AlfredoEcharri','@alfredo_reyes20','@AlicanTuno',
                    '@AliciaLpezGmez','@Al_Iks','@Aliorsum','@alisonkathe8','@allepuzalejandr','@All_Kano',
                    '@alma_palau','@almejavz','@Almumellaman','@Altamirula','@Alvaro__AA','@AlvaroM92147969',
                    '@AlvaroPR_','@alvarord','@Amacahe','@amatxoki','@amcliment','@amenaortiz76','@amfauru',
                    '@amloii','@Amonterodel','@Amparo_san','@amrugar','@AnaAliciaBr','@AnaBelnMP1',
                    '@anacastanopsico','@anahas_1','@analectico','@ana_rdlf','@Ana_Rosae','@ANASAYEK','@anas_ckd',
                    '@AnaSublimada','@anaxandra31','@andersonlegald2','@andersonortiz3','@AndresMedranoRU',
                    '@AndresWiggin','@AnesCreativo','@Anestesi_Art','@angelaisgro','@Angel_Escozio','@angelicajmora',
                    '@Angelitagherard','@Angie_MC83','@anitaperez76','@AnnaCassanye','@AnnaManyes','@annamarinaz',
                    '@Antiescepticos','@antitodo_TV','@antlarr','@antoloppi','@Antonio0jimenez','@antonio211065',
                    '@antonioantunez','@antoniojhb','@antoniomonfor','@AntonioNautilo','@AntonioPulido72',
                    '@AntonioRSierra','@AoiNekoBcn','@A_Pellin','@apetp_','@ApgbaezPsi','@aplazab','@Aprendiendo33',
                    '@aprobandomates','@ApuntesCiencia','@AraAyora','@araferzd','@ArbLui','@ar_chapal','@A_R_Cid',
                    '@ArcPiluki','@argo816','@ArgoffTV','@aribego','@arkoiris_es','@aroha_coronado','@aro_illo_aro',
                    '@Arpin','@ArtesaniaDavid','@aryxael','@asborlaff','@ASDEN_Soria','@aseasyaspie2017',
                    '@AsidoCartagena','@Assurdobot','@Astillytas','@Astro__Comics','@astro_duque','@astrofisicamode',
                    '@astrometeoro','@_atanas_','@Ateo_Andaluz','@ateocracia','@atina200605','@atiurRkhan',
                    '@atmancode','@AtticusGu','@ATuin','@aubeva','@Audiosdeciencia','@aulacodi','@auroragb66',
                    '@avachemtrail','@avatarneyc','@avatarneyc','@avispamulticolo','@Awesome_World_','@AXASegurosEs',
                    '@Axiomagazine','@AytusMamadas','@AyVeva','@Azeriak77','@AzucenaMS','@Azuquahe','@baima_t',
                    '@ballesterada','@BankofWords','@barbarroja_jose','@Bari_Barria','@Baronesa_B','@BaronesaRoja',
                    '@Baron_Holbach','@barra_coma','@Barragan_JM','@BarroyLoto','@Basileia62','@Bastet_La_Diosa',
                    '@BBarragan_','@BCrespoRuiz','@bdiazmesa','@Bea_TIC','@beatrizcalidad','@BegoMaFe','@bego_nita',
                    '@bells_ruthe','@bena_l','@Benatprofe','@Benjami57888698','@Benjaminam96','@benzuria',
                    '@BermeFer','@BesbassiA','@BethSolsona','@bettercallraul','@bettina_colos','@biogeocarlos',
                    '@Bionica_sm','@Biotectista','@bisonfou','@BlackberryReina','@BlemcomM','@BluePaleDot_',
                    '@bombadeodio','@Bonhamled2','@Book_75','@Boolture','@BoschBarrera','@BoseCano','@Boticarios',
                    '@bpagricolas','@BrainDevourer','@BraisCedeira','@brakingthe1st','@brandmil9','@Briseida9528',
                    '@BruceGraysonTod','@brucknerite','@BSABadalona','@_buenprovecho_','@Burro_Benjamin',
                    '@BuzonYucatan','@bynzelman','@byribosoma','@caguenpiterpan','@CAguiler2','@Caja_R3',
                    '@calamar61','@calcagaf','@Callawarra','@Calvuno','@CamaradaMeliton','@CambridgeLi','@Cammgi',
                    '@Campestremente','@campilloscapuz','@canal_divul','@Canal_Sexo','@cancerdepulmone',
                    '@Cancionexx','@Candelaenlaluna','@CandorumRey','@caordas','@CaosAzucarado','@capadociados',
                    '@capellum','@CapitanoNerdBoy','@capolanda','@carbonlump','@Carlitos_Darwin','@CarloCorinto7',
                    '@carloscasabona','@CarlosChNav','@carlosmoya47','@Carlosmunozescu','@CarloSotoAipis',
                    '@CarlosPrego1','@Carlosrfk','@Carlosval63','@carmenbarcovdc','@CarmenBioRi','@Carmenchc',
                    '@carmengr','@__CarmenLopez','@carmenrrodrgue2','@carmenrrodrguez','@carmininn','@Carnaina',
                    '@carolinakease','@CarolinaLopezll','@Carol_MMorales','@CarRobDar','@Carsan_z','@carteraaaaas',
                    '@CashClyde7','@cat312014','@Catedra_GO','@cateterdoblej','@CazadorEscptico','@cazahoax',
                    '@CBermudoA','@cboullo','@CCsParaNormales','@CdCienciaUV','@cdurlan','@cealdie','@cecirondon',
                    '@celada1947','@celerin7','@celtaindomita1','@censurometro','@cerdeiros','@cerebromonoblog',
                    '@cerumenx','@Cerverella','@CervusL','@cesarandreschg','@CesarBritoGlez','@CesarDuarte',
                    '@cesarmagala','@cesbean','@cescept','@c_gremlin','@ChangingVending','@Charlo77ita',
                    '@charro1968','@cheek00','@Chemicracia','@ChemistredPuck','@chensan77','@chepe_comic','@cherja1',
                    '@Chicopanchito','@chochosan63','@chorizo_picante','@Chris_malhechor','@cicerogas3000',
                    '@ciencia5arradio','@Cienciabajolupa','@cienciacional','@CienciaCorrupta','@CienciaIntrusa',
                    '@cienciajornadas','@ciencialacarta','@CienciaLeon','@CienciaMas','@Cienciamento',
                    '@CiencianoFiccio','@cienciascenio','@Ciencia_Vaga','@cienciaycon','@cienncia',
                    '@cientifico_rojo','@CientificosNo','@cienviva','@cinnamondolly13','@ciprianoderore8',
                    '@citrusuc','@CJ_CM','@claubustam','@ClavedeSole','@CLinde9','@clinicanebot','@clopuche',
                    '@cmorenopirineu','@CNIOandTheCity','@Cognomada','@colinas26','@CollapseCuantum','@COMAlicante',
                    '@comunaholituri1','@comunicaCiencia','@ComunicandoUA','@concha_bru','@ConchiLillo',
                    '@ConcienciaAsoc','@concisate','@conciti','@conradogarcia','@Consalud_es','@ConValSegLocal',
                    '@convivirconmig1','@convivirconmigraña','@coraliuuus','@CordeiroLope','@cosmosfullhd','@CPFCYL',
                    '@cprietoandPT','@cptn_pastanaga','@craperro','@CrecerCiencia','@CrikyEspartero','@CrimiCarlota',
                    '@cripatia','@crisbed43','@CrisCulebbras','@crisjauregi','@Cris_Monteneg','@CristinaCasto',
                    '@cristina_riv','@cristina_rssell','@Cristinjorquera','@crisvipu','@Critheann','@CrodrigoCarlos',
                    '@_crs94_','@CrysaniaV','@CSanzAndrea','@csogorb','@CuadernodeLuis','@Cuquita72','@curious_geo7',
                    '@currelos','@curtnollarg','@cvamarosa','@Dagafo','@daianaee','@Damarysorissa','@DaniCoronado12',
                    '@DanielaBarico','@Daniel_Arbos','@danielcormar','@DanielJCalero','@DanielP61220543',
                    '@DanielPrat6','@danielquimic','@danielturienzo','@DaniEPAP','@Danny_CanoT','@DannyIbarra_',
                    '@danprietog','@danygmartin','@danzando_mp','@dapuchmas','@darexxi21','@DarkSlaayz',
                    '@darthgrande','@DarthTer','@Daurmith','@David08334527','@David_Aideti','@davidcabrerabcn',
                    '@DavidCrzG','@DavidFdezRemen','@davidgarmen','@DavidGNavas','@DavidGuerrero_A','@DavidPalomas',
                    '@davidsojodiego','@DavMorMat','@dazanes','@Dcastroarg','@dcienciablog','@deaadandburied',
                    '@Deawer_87','@Deberiaserseda','@Declaracion','@deibitbanon','@Deino_13','@dekelmaho',
                    '@dekuwaka','@delnabla','@delostuderiver','@DelrealMariano','@DelRojerioMeFio','@Demi_300kmh',
                    '@denissovega','@denuncio_estafa','@dergoober','@DerlisaBlanco','@desdelmasalla','@DesireAlba1',
                    '@de_suicidio','@detrassuicidio','@devastator1977','@devri_es','@dferradans','@dfkfc1',
                    '@dhaslock','@diabbolo1959','@DianaDespacho','@Diana_Oliver','@dicultura_','@diegmunoz',
                    '@dietistarealist','@diezauberfloete','@DigitalCorsario','@digitaltouch78','@digodiegodin',
                    '@DimatesUA','@DimoniCent','@DineshKhokhri','@DinoMorant','@DiosEsMentira','@divulgacionscn',
                    '@DLSIUA','@dmatronas','@doblecortina','@Docta_guerrera','@DoctaIgn','@DocThor9','@DOCTORISPILU',
                    '@Doctor_Pardo','@doctrizmapache','@DocYeyo','@dolorlumbar','@dolorsmolca','@DominOrtega',
                    '@donvanchipotin','@DorarNoSella','@DPosmoderno','@dra_dixit','@DraFigueras','@dramariajose',
                    '@DraSilviaSaenz','@DraSofiBauer','@DraStitzman','@Drey_1','@DR_FLORES','@Dr_JMLV','@Dr_Luis',
                    '@DrLuisRZabalaH','@drmiguelmarcos','@drpanno','@drsmontes','@DrTinahones','@drunkmartian',
                    '@DrXaverius','@d_tomas','@dukoman','@DumuzidShepherd','@dvguirao','@EBaladia','@Ebevidencia',
                    '@Ecoborpa_ou','@ecothinktank','@e_cycni','@edesojorge','@edgardrgc','@EdiSal12468','@ednaSed',
                    '@EdoardoMelilli','@Eduardjp','@educacion_papps','@edumonasterio','@eeep_valencia',
                    '@EfectoMcguffin','@EGuivernau','@ej_molina_c','@EJorgeGlez','@el9planeta','@elABCdlasflores',
                    '@EladaChen','@eladdio','@elandivar','@_Elara_','@elbetito10','@elbrotemoderno',
                    '@el_coto_monchis','@ElenaC_S','@ElenaGon17','@Elenamastroeni','@ElenaMolinaVega',
                    '@elfisicobarbudo','@Elgabidrscience','@elGendo87','@elisa_beneit','@eljaviel','@ELlaveria',
                    '@elmoide','@Elmundodeivan2','@elnazareno123','@elnocturno','@Elo_N','@eloycam2012',
                    '@elsibarita27','@eltabo_','@elvaquerourbano','@elvoldicar','@eMeCanillas','@EMEphotografy',
                    '@emilcr81','@EmiliojosFR','@emiliollbb','@EmmaCastillo_00','@EmmanuelCampoy','@Emmanuelcient',
                    '@emocionpositiva','@emonroye','@emotellon','@EmOtraNo','@emulenews','@EncarnaAmoros',
                    '@EncuestaDinamic','@endegal','@EnfermeraMonete','@enjiruiz','@enlopezbu','@EnnaSwan',
                    '@enri_m42','@EnriqueGallar12','@EnriqueJoven','@enriqueros','@entropiacaos','@entropiagallega',
                    '@epicur013','@Epicureo64','@episteme98','@epsiloom','@EqInvestigacion','@Eratonada',
                    '@erdrick2003','@ermurse78','@ErnestoLopezRey','@eroyuela','@ErratumUniversi','@errorrelativo',
                    '@Ervagco','@esanmarti','@escepticos','@esegatovengador','@EspeciesIsidre','@EsperanzaC_L',
                    '@EspinosaBosch','@espitagorgorita','@es_Schopenhauer','@EstanislaoLem','@EstefanoMobili',
                    '@estejoli','@estherkimpark','@esthersanz4','@EstrellaMoyaR','@eugendrastignac','@EugeniAIemany',
                    '@EugeniAlemany','@EugenioManuel','@EuroComunismo','@EuroParental','@eurostia','@EustoMolina',
                    '@EuzkalZombi','@evaanyon','@evafrabla','@EvaGalanMoya','@EvaVidal4','@evildemon27',
                    '@exogeneidad','@exoplaneto','@falcaldeolivera','@fali_mz','@family_autism','@fanfrikan',
                    '@Farmacarlos','@Farma_Ciencia','@farmatornero','@fasciencia','@favilaramirez','@fbernaus',
                    '@fblascoxyz','@FBpsy','@FcoJSanchez','@FCorregidor','@fcuartero','@FCuencaMartinez','@_FdMQ',
                    '@Federico_R_','@FEEF_SPAIN','@fefonteboa','@felipe63ap','@FelipeBarberia','@FelipeSerantes',
                    '@FemeninoMiramar','@FenixIgnifugo','@FerFrias','@fermalcol','@fermar666','@fermincruzmata',
                    '@fermont_','@fernan113','@Fernan_boti','@FernandoCervera','@fernandollopis','@Fernando_Tala',
                    '@ferqtpo','@FerranPoma','@FeVaDiC','@ffauben','@ffmargo','@Fgparr','@fibromialgianot',
                    '@fidernesto','@FilosofoRikardo','@fir_bot','@Firefly_fan','@fisio1958','@fisiobobesponja',
                    '@fisionines','@Fisio_Rt','@fitnesspowerr','@FJMoyano','@fjresal','@flapendo','@Flatuslowly',
                    '@flyerLPA','@FMeritxell','@fojuelosdotcom','@fonso','@fontanagallego','@Fosilera9','@fpplantas',
                    '@fragonib','@frame100fuegos','@Fran5121975','@fran_75','@FranciscaLis','@francisconz84',
                    '@franfg1981','@frank900t','@FranPedia','@fransanchezbe','@fredegar_bolger','@FridaSiKahlo',
                    '@FRIKINGEEKNIERO','@frikiscience','@frikiteacher','@FriSanCam','@FSanzGarcia','@FtimaV',
                    '@FTorrecilla','@fuchoreal','@FuenteApolo','@fulianSP','@fum0bajoelagua','@gaban55','@Gabi_tdf',
                    '@gabobelmar21','@GaboTuitero','@gabridominguez','@gabrielrossi123','@Gabrigortiz','@Galateaal',
                    '@galeodea','@galera_fina','@GalindoDentista','@GanaderiayAgro','@gangai19','@Gaphelion',
                    '@GARAITEZIN','@garcialpa','@GarcPalomar','@Garlfield_79','@GarzaNoite','@Gataqueladra',
                    '@GatitaBohemia','@gatodellic','@gatosconbatas','@Gatoweb','@Geckocenter','@GEldeanita',
                    '@gemagoldie','@gemagomezolmos','@generacionX1978','@geologoenapuros','@GEPAC_','@gerardhll',
                    '@GerardoCostea','@germanbosque','@GermanLianez','@GeyRivers','@gfmburgos','@ghost_h141',
                    '@gildelatorre1','@Gilvernet','@GLandaburo','@gloryreq','@gluonconleche','@gmt_iccp',
                    '@GonzalocqFT','@Goyinsa','@gplsi','@Gracia_Moreno','@gracianoflecha','@GracielaOjeda',
                    '@gradalamar','@gradc','@granadaabandono','@Granizadoo','@GranjeroVerde','@GrardNoo',
                    '@Grupo_Arbio','@gsaracibar','@guardiolajavi','@GubCop','@guimencen','@hakyre','@Hal14112',
                    '@Hannah02002077','@hannita_vet','@Hardgore_Annie','@HARROW_h','@HctorCaraballo','@hdelosrios2',
                    '@hecaidi','@hecatonchiro','@hecgigar','@HectorCerezoH','@HelenaGluconeo1','@HelenaMatute',
                    '@HelenaSYN','@HelenEsteve','@hermeneutah','@hernan_0xff','@Herraiz_MJ','@hescolar','@heseloni',
                    '@heuropo','@hgtranshumanist','@Hielo80Maria','@Hill_Chars','@HipoIncognito','@HiponaProyecto',
                    '@hipopede','@Hj50019','@Hjorvik','@Homeo_Patinho','@HomepataSincero','@homografix',
                    '@Hondoncity','@honey_eyes1405','@hrrosem','@HugClin','@HumanistesVlc','@humano404','@hwkpnr',
                    '@IagoGonzalezB','@IAmDekow','@IamSilviaAlonso','@iballesza','@icalles','@ichocrates',
                    '@iclerigues','@idoibiza','@IdunnFreyja','@iescriva','@IEVallAlbaida','@ifbayo',
                    '@IgnacioEnriquez','@IgnaEsc_Oficial','@IgorZarranz','@ihpeco','@iigoperalesbarr','@ikiro7',
                    '@Ikortega','@iksfc1','@ildefonde','@illborregos','@imaccyl','@ImJohn_Ray','@ImpulSalud',
                    '@ImpulSaludMad','@inakiaguirrezab','@Inconformista22','@InfoManip','@InfoMedicodon',
                    '@InfoTextual','@ING_1975','@inma164','@inmacoruna','@InmaLeonC','@inmatrola','@InsArrieta2',
                    '@insurrectoblog','@intrepidojones','@Investigalicia','@ippotis11','@IQM_CSIC','@irengonzi',
                    '@Ireul_Renfield','@irisgmoyano','@irsva','@isaacgonz','@Isabelalor2015','@isabel_bres',
                    '@isabelmorenobuj','@isabelperis23','@isabel_p_riera','@isabelsolerg','@isefran79','@isetapm',
                    '@ishmajl','@isidroaguillo','@israsoiyo','@Issa30797634','@itoclonina','@itrquotes','@ivamoscid',
                    '@ivan_1273','@ivelindimitrov1','@IzanAznar99','@jaalechig','@JAAMochon','@JabierGS',
                    '@jacgbilbao','@JacoboCabanas','@JacoboMendioroz','@jagabaldo','@JaimeCReven','@JaimeEspinozaR',
                    '@JaimePrimeroR','@JALGUERRERO','@jalvamore','@janribbon','@japer3z','@JaumeFlexas73',
                    '@javcasta','@javdagnesses','@javi_AlexM','@javibuhardilla','@javiddt','@javierarmentia',
                    '@javiercadima','@JavierDiazOrue','@javierg131531','@_javiergp','@javiermacho65','@javiermolto',
                    '@javierparrazu','@javisarr','@Javi_sien','@javi_sociologia','@j_borre','@JCarcinogMutage',
                    '@JCBguez','@jchecarius','@jcrprojectsllc','@JDupuytren','@jeffreyovc','@jennifermyc',
                    '@jennifersorri17','@jeojavi','@JessLongway','@jesus714000','@jesusazulay','@jesusfe61867926',
                    '@jesuspurroy','@JesusTDuque','@jfontich','@JGilMunoz','@JGzlezz','@JHG_','@JhonJTarros',
                    '@jhonpineda97','@JhonyLaPongo','@jizhe74','@jjserpe','@JLCiencia','@JL_Ferr','@jmartinezDN',
                    '@JMBiurrun','@jmcampsss','@jmcuevasb','@JMEspinolaE','@jmgomezsoriano','@jmmulet',
                    '@JMPerezFlor','@jmreyruiz','@JMSepulcre','@jmsolerinsa','@jmzueco','@JoanGalve','@joanplanas',
                    '@JohnathanLaird','@jolliffe71','@jomanaba','@jonanmg_1976','@JonKalada','@jonsulve','@_JoPiVi_',
                    '@jordi_31416','@jordicuesta_dn','@JordiPuente','@JorgeB222','@jorgecampos1972','@JorgeGarBas',
                    '@jorgegrip','@jorgejfrias','@jorgekoruna','@JorgeMTamayo','@jorgeordonezcar','@JorgePlaGarcia',
                    '@jorgeruiz45','@jornadas_gandia','@jorsandur','@josealca','@JoseAng99765561','@joseanjauregui',
                    '@josef_ramirez','@JoseJVeraG','@joselitok70','@joseluisderueda','@joseluissariego',
                    '@Joselusann','@josemabea','@josemanu_44','@josema_olvera','@Jose_Maria_100','@josemgarcig',
                    '@josepallas1','@josepalmalozano','@Josep_Falco','@Joseph_D_Tenka','@josete600','@joseuribeok',
                    '@josmanbul','@josoclliures','@josue_tinoco','@Josvill74306753','@JotaEle1978','@joxandonosti',
                    '@jragrelo','@jralonso3','@jramonfernandez','@JRivasSC','@jserranodf','@JSimoL','@jspm29',
                    '@jtpeces','@juaevpa','@jualej2','@juanaalemany','@juanalberto10','@Juanamariabio',
                    '@juanantcardenas','@JuanBa_Rem','@JuanCar30897708','@juanesdean','@juanfisicahr','@juanfrans_',
                    '@juangilopez','@JuanjoLoMe','@JuanMaConsuegra','@Juanmalucky','@JuanMan61300689',
                    '@juanmapinana','@juanmazaORL','@Juanmconde1','@JuanMNavarroP','@juan_musik','@juanpa_epull',
                    '@juan_revenga','@JuanSoler_3333','@JuanViUanKenobi','@judascartoonist','@juliacerrillo_',
                    '@Juliadietista','@juliana0426','@julinkyvideos','@JulioBasulto_DN','@JulioGSoriano',
                    '@juli_ojanguren','@Julipascualc','@JulitaMorgunova','@juremaorg','@JustFuckSci','@jvasquez1612',
                    '@jvicenteprieto','@jzhlhp','@kafurz','@kaihocuspocus','@Kaiindai','@kailashkora','@kain24',
                    '@kalandrakas','@kallahant','@KarenRokaz','@Karina_Joao89','@KarinaRogers271','@KarmaROVA',
                    '@kellylu29','@Kemaman_','@kennedh_ghoul','@kerkhoff','@kevincl02','@keyeoh','@keysoftt',
                    '@kikealmeida','@Kike__GM','@Kike_MH','@KikeXtra','@kitiaraCronopio','@Kitidin','@KITTA44',
                    '@kix2902','@klodco','@KoldoSobaco','@kpitel','@krbaa','@KropTor','@Krtkon1','@KSuleng',
                    '@KublaiKhan17','@L9Ringo','@Labestia3','@labotikacien','@lacaiguda','@ladelho',
                    '@ladronaqueladra','@lafsanig','@lagamez','@lakasama','@lal36laia','@lalb85','@LaMarijuanaMx',
                    '@lamiskis','@LaMoriano','@Landecraft','@laquerol','@larjartito','@LaRutnikova','@lasariera',
                    '@Lastriff','@LaTiadelaLejia','@LauMarJi','@Laura331ac','@LauraAsensi1','@LauraCCsXraNorm',
                    '@lauramorron','@Laurapvq','@LauraSofaEnrqu2','@Lauricg83','@LaurichiTrasgu','@LBaconsdottir',
                    '@LBPA','@lcapote1973','@LCFC','@lcienciamaa','@lema_de_zorn','@LenHerrera17','@lennyelblanco',
                    '@lennyespañolista','@leonisdeniquea','@lerneo','@LeticiaGoimil','@Letraherido_','@LibreCritico',
                    '@LibresOpinamos','@Librodelprofe','@Librosalaula','@libroscuriosos','@licilook',
                    '@LiedEsperanza','@LierClaudio','@ligero999','@Ligre100','@Liliana_PULP','@Lilith00666',
                    '@Lily42__','@limariposa','@lipido','@Lirenere','@LisandroFisio','@LittlelionmanJP',
                    '@live__untamed','@livimarian','@ljorozco','@llaveypuerta','@llazzar','@LlompartLm',
                    '@LluisSoteras','@lmerinogo','@lmescu','@Lola_Lolilla','@LolesBerlin','@Lomber9','@lo_mestre',
                    '@lonar2','@lopezborgonoz','@Loquequedademi3','@Loreneando','@LorenzoFisio78','@LoriMalijna',
                    '@Lorosinfuturo','@LozanoDuffman','@lramosneira','@lriveroweber','@LrsCrwn','@Lsegoviamiranda',
                    '@lualnu10','@lucenae','@LuceroJuarez27','@LuciaVelilla','@luckytras','@LuiBar','@luifer294',
                    '@Luigy_Moon','@Luis314159','@Luisaguilar_es','@LuisAPunto','@LuisIrazusta','@luisjarj',
                    '@LuisJorgeAlloza','@LuisLuisnavarro','@LuisMartin222','@luismijimenezz','@luispereabcn',
                    '@luis_quevedo','@luisrodero','@LuisSoftail','@LuisSuso_','@LUJOMORO','@luzbel19',
                    '@Luzmaria1989','@lvdislexica','@lveale96','@lvgap','@macgondar','@machotesur','@MadiDinu',
                    '@MadreDeTragonas','@madridvk','@madTere','@Maebdira','@Maestro_Cosmico','@mafaldasevilla',
                    '@magelesmedina','@maicamero1','@maisbet23','@maitecicleta','@maituti','@MalcolmPerez12',
                    '@MalkyaT','@mamamaruja92','@MaMii_DesdeCDMX','@Manelillolop','@manelmorillo','@manuelapr05',
                    '@ManuelCorroza','@manueldiazn2','@ManuelRosello1','@manuelsorian1','@ManuEsteban1990','@manyez',
                    '@manzanasada','@mapepecl','@Maranhe','@Maras70','@marcasycompras','@MarcelinoBlanco',
                    '@marchenina','@Marco_Erebus','@marcosuch','@MarcRuizDeMinte','@marcvfons','@marga39637546',
                    '@margaritatm','@margonzac','@margonzalvez','@Margonzy','@Maria_cvna','@MariaEsp19',
                    '@marialopzc','@MariaMarquesDN','@mariamoes_rock','@marianetake','@MarianoCollante',
                    '@mariapalomeras','@mariita_al','@MarinaNy5','@Marine82815656','@MARIOESTVEZ','@mariomzn',
                    '@MarisaI70501001','@mark55136828','@markcha','@MarMarejadilla','@maroor','@marsmenn',
                    '@Marta51970','@Marta_dalvarado','@martafcerrada','@martinfabreg','@martinfd78','@martona_to',
                    '@MarvinHarris76','@masendocrino','@MastroAndrea1','@matiascamilo13','@MatiMatarredona',
                    '@M_A_VAL','@MaximoFlorin','@MayaOpinando','@mayerri','@mayka212','@mcapdepon','@mcarmen_n',
                    '@mcris1116','@mcris1611','@medejas_helada','@MeDicenBerlanga','@medicinaiesport',
                    '@MedTechpreneur','@mefmontiel','@Melocoya','@merc_CARACENA','@merece_saberlo','@merifrai',
                    '@merisalmenis','@Messcobar_','@MestryneJorge','@MetalTrooper','@MeteoBetera','@meteolp',
                    '@mfherrador','@mfuentesdaras','@MGGGuz','@MGutEspinosa','@Miangabu','@MICAELA95100',
                    '@michaellusty','@michelsamperio','@michiwini','@Midazolam24h','@mightyfalcon__',
                    '@miguelcrispin','@_miguelmc','@miguelmediavill','@Miguel_Mollar','@mikelc88','@milagroslg',
                    '@milco81','@mimenusingluten','@mimesica','@minaharker20_12','@minimalist_unix','@minipunk',
                    '@MintPennyroyal','@mipuntodevistaa','@Mir11003126','@miriam_chic','@MiriamQ17','@Miri_Rouch',
                    '@Mir_M_Marquez','@MischaBerger1','@Missingduke','@MisterDBunker','@mithralda','@MitosComer',
                    '@miwebdesalud','@mjg_mj','@mjkayto','@mjlvmjlv','@MJoseGomezFdez','@m_joseruiz',
                    '@mmartinloeches','@mmitadiel','@mmrtnzluna','@mnasin','@MnicaCrespo10','@mogrosso78',
                    '@moigaren','@MonfortRaul','@mongegemon','@mongologuista','@monicafuster','@MonikaSalgueiro',
                    '@Monstergumis','@monstuiterito','@Montalvo22Luis','@MonteCarles','@monteror32','@MoriartyProfe',
                    '@movidas_raras','@MPAlonso','@mperezcast','@mpml8','@mr___cooper','@Mr_dobe','@m_redondoc',
                    '@Mrevildrporkchp','@Mr_Marlom','@mrosastw','@mrsrosaperez','@MuchoMochuelo','@mufuva',
                    '@MundoAnimalTv4','@muyenforma','@myfreedom14','@myriamarin','@myrkna','@_Mywonderfulife',
                    '@nabi_onandia','@nachinpascual','@Nachobacter','@nachoguerreros','@Nadiehabladora',
                    '@najera2000','@najuca2010','@Nancypotillo','@nanopc','@nataliacani','@NatxoBCN','@Natymuj',
                    '@navarro_fm','@navarrolucia12','@Nefaro90','@Neferchitty','@negraco1980','@neidau','@nekane__',
                    '@nemesis_online','@NerdOrgulloso','@neur0nid','@neuralhacker','@neuronacher','@newilustracion',
                    '@NicoCristiani_','@nieto_de_zeus','@Nievedechicle','@Nieves11681156','@NievesSalinas','@Niha',
                    '@NikyBenz','@nilsonbarios','@ninesfer','@nishetabcn','@Nitrotoluen0','@nlpzr','@noa_rey',
                    '@Nobodysferpect','@nochedluz','@NoemiRemesal','@NoInvisibles','@nomecreonadatv','@Noragueda',
                    '@norbertoramis','@NoriaEdward','@nosense_sonder','@NostromoADF','@Notanswer_','@Nuria_LG',
                    '@NuriaMartnezRa3','@NurietaMG','@NutriciaGarrido','@Nutri_Daniel','@Nutrisalvador',
                    '@nviglesias','@OAlonsoToledo','@Oberon_WolfCult','@ObeyJolinbo','@obreis','@Ocelote_Lanudo',
                    '@OctavioSandra','@OcupaTEA','@odi_camila','@oespejo','@OfeliaDiazIngel','@Ofendiditis',
                    '@ogarciaalzorriz','@Ohanarasuis','@OmaCroga','@Omar_Audicio','@Omargarfias','@omaro1428',
                    '@onafm','@oncomet_','@ordenauta','@OrgTecnopia','@OrientaCarpe','@Origen_Psico','@ortegamanoli',
                    '@osasunafarma','@OscarAlejo02','@Oscar_Arino','@OscarBonGon','@Oscar_Tagrend','@osdiol',
                    '@oso_loga','@Otroesceptico','@otrowalker','@ovemundo','@oyebartola1','@PabGMontero','@PablHdez',
                    '@Pabloblublu','@pablocervantes6','@Pablo_Deco','@PabloGsalum','@PabloGToral','@PabloHerreraJ',
                    '@pablo_jack','@pablovicensh','@Paco_Catala','@PacoVC1','@padegarma','@paleofreak',
                    '@palomamoreda','@Paloma_Sastron','@PalPakiyo','@panopower','@PaolaMalot','@papochette',
                    '@Paradigma60','@parador08','@para_lelopipedo','@ParalelUniverso','@ParaMicroBio',
                    '@ParlemDeCiencia','@pascuanotaria','@Pastranec','@Paterbubo','@PatLacruz','@patricia_adalil',
                    '@patriciadamiano','@PatriciaLargoB','@PatricioMBarco','@PatrickDeFlores','@patrimartinez11',
                    '@patti_ep','@pattymrendon','@PaulaGallego97','@PaulaGanitsky','@PaulaPepo_cheep',
                    '@Paulina100197','@pauperez','@Pau_Vega13','@pazcarmor','@PecoAz','@pedroabad','@Pedrodanielpg',
                    '@PedroGallego201','@PedroMargolles','@penanietobb','@penquero','@penssent','@pentamorfico',
                    '@pepecampostruji','@pepemagana_48','@PepitaPerezL','@PepoteCC','@PepRubio1','@pepxabiagen',
                    '@perejoanpons','@perepatongon','@Perguelofici','@perpetuocambio','@__Persefone__',
                    '@persianasvalenc','@persusanper','@pertindiscolo','@PEspain00','@peterrvergara','@PeterSlimmer',
                    '@PetraEsperanza','@PetriFabero','@petri_nets','@Piamonte','@picusmagnificus','@Pilar1207',
                    '@Pilarmadero','@pilarrmontalban','@pilarsanchezupv','@pilibustera','@pilila1','@pinabertoglia',
                    '@pinturaonline8','@PipeTatanVP','@pipicp','@pitiklinov','@pitiso14','@PitPenedes',
                    '@Pizzalandia','@PizzaWoow','@Plasmaideas','@plataformalife','@PlatInvestUCM','@Plaza_Bickle',
                    '@PlcboNet','@PLRSANI','@P_manel','@pmcolladoc','@podemosciencia','@polarharen','@Poliandrico',
                    '@ponmeeldesayuno','@PostalesDeAmor','@potiholic','@poximuz','@p_pandora','@ppoHeisenberg',
                    '@Pr3cog','@preguntacadadia','@preguntas_i','@prestamoweb','@Principia_io','@prmch73',
                    '@probandox2','@_ProfeAlfonso','@profesor10mates','@Profiterol500mg','@Prometheo567',
                    '@ProtectorSkept','@ProtonC1','@Pseudosanidad','@psico_diet','@psicojurix','@Psicologia2222',
                    '@psicomap','@PsicoMarilyaSB','@PsicoProfesor','@Psicorespuesta','@psicritica_','@psi_kyta',
                    '@Psiqetal','@psyconpsicologo','@PuenteEnya','@Pumukki','@PunkDeLaCiencia','@PURECHOKALATE',
                    '@QEDcon','@qmph_es','@QueliAGZ','@Quercus86954081','@querubeatle','@quieropruebas',
                    '@quijotuiter','@QuimicaAsturias','@QuimicaEuskadi','@QuimicaSociedad','@quimico_llopis',
                    '@quimidicesnews','@QuimiHeisenberg','@Quinonet_Madrid','@quinturicchio','@Quiquedmt','@qwa256',
                    '@QXXI_justoginer','@R11Adri','@r4y_j4y','@Ra_Alba','@raboso1980','@radiodelaUA',
                    '@RadioElcheSER','@RadioRho','@radupopa_nino','@rafaelfontan','@RafaelTimermans',
                    '@rafa_navarrog','@ragedroidnet','@Raicesyagua','@rainhavermella','@rakelises','@ralvar314',
                    '@ramedteroll','@ramirotwit','@RamonAlbanchez','@ramondeveciana','@ramonsincajal','@rantfer',
                    '@RaquelDeGamonal','@RaqueTEBA','@Raquiglam','@RArribasArnau','@raskub','@Ratber3',
                    '@raulcuencacoach','@RaulLazaro','@r_bernal109','@rcf7303','@rdemerce','@rdeviguri',
                    '@rebecaruee','@RebeccaCohenS','@ReconstrDe','@Recopla1','@RedCE_','@reduke','@redunecontacto',
                    '@Reflectora','@RendimientoMarg','@requenajamonero','@RequiroSlne','@resped','@Reyeselda95',
                    '@rgserapio','@Rialnurt','@ribap','@rilart_ru','@Rippenmolche','@ritalumbreras','@RiveroMariluz',
                    '@rmgtrad','@rmnmrgrd','@RNFinfo','@Robert_Drum','@RobertoAcunaEC','@rochetou70',
                    '@RodrigoLlarena','@rodrigoparola','@roentgen66','@roi_cal','@Romana8888','@rosagarciagar17',
                    '@Rosa_Hita','@Rosalind_Fr','@RosaMLazaro','@Rosasimancas','@RoseBush_Dawn','@rosenrod',
                    '@rotjetavila','@RSalviati','@rubenbaston','@rubendcm_98','@RubenFMat','@rubentxuplas',
                    '@Rubino83927379','@rubpd','@RuizdelPozo_M','@Rusbenito','@rutharenasm','@rvalencia_raul',
                    '@R_VelVa','@sabeletta','@saezatxa','@sagilca','@salasgar79','@SalmeronAlvaro','@saludgruiz',
                    '@saludonnet','@SaludsinBulos','@salveth','@SamFoxdoc','@samfrado','@sam__ggg','@samprojecteu',
                    '@samuel_ilitch','@SamuelJaneman','@SamuelMarCoe','@SancasDev','@SanmartinSa','@santi2141',
                    '@Santiag16094246','@Santiag98539926','@santiagorendon','@santifierrop','@SantiMelia',
                    '@SanzMata','@SapUcm','@SaraRC83','@sarateja','@SarayArVi','@SarayDubaVitha','@sarayzc92',
                    '@SarcomaSB92','@SarmaMalbec','@sarupy17','@satware','@S_Behizain','@scariosHR','@ScienceFlows',
                    '@scifo78','@ScottyPeople','@SCQuimico','@Scruzcampillo','@ScyKness','@SdeStendhal',
                    '@SEDUPoficial','@SefiFood','@segoviag969','@selanora','@seneca231','@SEnElistmo',
                    '@Senorita_Fook','@sensociencia','@sepsis_stop','@SerafinCuidando','@serbita7777moya',
                    '@Serendipiabravo','@SergiBoleda','@sergio203bio','@Sergio5zuelas','@sergiogarmor',
                    '@sergiviudes','@SerraSergi','@SeshatShop','@Seth_Tifon','@SettiEduardo','@sferrebenedicto',
                    '@SgtSagan','@Shora','@SilvanaCostales','@silvercius','@Silvia83043064','@SilviaGismera',
                    '@SILVIAMAGTZ','@Silvinsula','@SIMEFchile','@Simone820402','@SimonPerera','@SincroMktOnline',
                    '@sisifolibre','@Sisoyio','@Sitajux','@sixhundredsisty','@sizigia90','@Skepticendocrin',
                    '@SkepticJalisco2','@skoci2','@slararcos','@slumart','@SM_imma','@soap_mrs','@Sofichof',
                    '@SoldeSalamanca','@SolEnFlandes','@solers_m','@Solof1sincirco','@SoloMillennials','@SolPsim',
                    '@sombradoble','@SoNaVaquera','@soniasaezrojo','@son_ribas','@Sorgin','@sospatriciasos',
                    '@soyamp','@SoyMuySad','@SoyPediatra','@soyTanchus','@spagyriainsti','@_spalacios',
                    '@spidermanzano','@Sprayology','@sprovira','@SraPetrillo','@src_santiago','@SRDiogenes',
                    '@SrGarrote','@Srpapalord','@StardustLeila','@SteveMcPerro','@Stevia_','@stian_hernandez',
                    '@stop_ela','@StopPseudo','@StopSuicidiosGC','@Subeenpracticas','@Sucrot','@SUgayos',
                    '@Sunkissedglow3','@SuperCapuchita','@suplem_digital','@SusanaRo1','@SusoFePe','@sysadmit',
                    '@Tabernita','@TadeoScience','@TaesUa','@TallerDelSexo','@Tank_Girl111','@Tataray21','@TaTiuski',
                    '@TaTou230','@tdahvalles','@teamediterraneo','@Teatrero5','@TebaldoCapuleto','@tecnoenpunta',
                    '@TecnoNewsInfo','@TecNovedosos','@tehuacatl1','@teknahi','@___TeleKa___','@Tel_Esperanza',
                    '@Tellepizza','@telonnius','@tenazas_sr','@teoparamo','@teresaalarcos','@tetaaporter',
                    '@thaiselenags','@thecrow9111','@thejuniorsan','@THEMMEXCHANGE','@TheRealCiencia',
                    '@theTNutrition','@Thinktactil','@Thor_gin','@Thu_nenah_rubia','@Thyroiddamsel','@TiaRepelente',
                    '@timehugo','@TodasUnidasApp','@Todoestasofrito','@tomascarralero','@tomasdepor','@tonetete_xd',
                    '@TonyJimJr','@toolatetomend','@tornilloarqui','@torrado_leo','@Toufa53161397','@T_peligrosas',
                    '@tradumedic','@tranciela','@Transgenico9','@trasukoma','@trasywan','@trimmms','@triskelet13',
                    '@trisquelisabel','@Trolito_itoor','@trollsofico','@TSJosep','@tuchogc','@Tucubutense',
                    '@tuelo111','@Tu_Inclusion','@Tuiterricolas','@Turumi14','@Tusiquevales28','@tutuhelms',
                    '@tvindalerta','@TVWriting','@twalmar','@TWmnv','@twttEperez','@Txabolica','@Txamaris',
                    '@txe31416','@UAM_Madrid','@UA_Universidad','@ULM_75','@ultrabetstips','@unaiaso',
                    '@UnaMentePensate','@UnAntojoDe','@UnCastellsMes','@uningenieromas','@Ununcuadio','@UPA_Federal',
                    '@upermanente','@UPV','@Uraeus_Nefer','@UribeX','@urmore1','@Urtzain','@usuku','@vaiconDios',
                    '@ValentnIglesias','@VanBurencio','@vanturifox','@VanUgalde','@VarillasJean','@VaryIngweion',
                    '@vbaosv','@v_berrondo','@VDimension5','@vegapaco1','@VeideSantEdR','@veneciana1981',
                    '@Veneciavianey','@vengadoracad','@verkkossas','@VeroDeLaCueva','@veronicablancox',
                    '@Vero_Nica_Rg_25','@Vicente39385746','@VicentetG','@vicentoller','@vicman1707','@ViConejero',
                    '@Victagua','@victorguisado','@_victoriaim','@Victorpujales','@victtoro05','@vidabienestarsa',
                    '@vielbein','@vikigweto','@villafrades','@villamanuel','@VillaverdeJorge','@vinchur',
                    '@vinicioro','@VirSarabia','@Vitia_Hache','@VJacuinde','@Voice_clinical','@volland_cellia',
                    '@vonrdnz','@voro3492','@vosorioTICsalud','@vRawon','@VScienco','@Vtedavid','@waltzing_piglet',
                    '@wankel1981','@waytohell666','@Werdergast','@wildduckcluster','@WilmanBueno','@wnzzzjeje',
                    '@WottonKid','@Wyrlenne','@_Xacoal','@xandariano','@xavigranda','@xduran_e','@XeloJordan',
                    '@Xibarda','@Xikitxik','@xPaisMejor','@XpineteX','@XulioAntelo','@YayaCeravieja_',
                    '@Yeimschateau','@ygolonac','@ygrayne','@ykadir1306','@YoCasiopea','@yo_fosfolipido',
                    '@Yolanda94645054','@YouFisio','@y_tu_mas_','@yvanisevick','@Zaijuander','@ZaoM27','@zasjgc',
                    '@zazen71','@zelatari','@ZlinxWired','@zoe_lc','@ZoidbergSr','@zoltanpickman','@zubia_asun',
                    '@Zulydiazf','@zurielguitarro']

tweet = ''
for e in users:
    if len(tweet + e) > 280:
        print(tweet, end='\n\n')
        tweet = e
    else:
        tweet += ',' + e