import time
import urllib
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup

sp500 = []

Russel_3000 = ['FLWS', 'FCCY', 'SRCE', 'FOXA', 'FOX', 'XXII', 'TWOU', 'DDD', 'MMM', 'EGHT', 'AVHI', 'ATEN', 'AAC', 'AAON', 'AIR', 'AAN', 'ABAX', 'ABT', 'ABBV', 'ABEO', 'ANF', 'ABMD', 'ABM', 'AXAS', 'ACIA', 'ACTG', 'ACHC', 'ACAD', 'AKR', 'AXDX', 'XLRN', 'ACN', 'ANCX', 'ACCO', 'ARAY', 'AKAO', 'ACHN', 'ACIW', 'ACRS', 'ACMR', 'ACNB', 'ACOR', 'ATVI', 'ATU', 'AYI', 'GOLF', 'ACXM', 'ADMS', 'AE', 'ADUS', 'IOTS', 'ADNT', 'ADMA', 'ADBE', 'ADT', 'ATGE', 'ADTN', 'ADRO', 'AAP', 'ADSW', 'WMS', 'ADES', 'AEIS', 'AMD', 'ASIX', 'ADVM', 'ACM', 'AEGN', 'AGLE', 'AERI', 'HIVE', 'AJRD', 'AVAV', 'AES', 'AET', 'AMG', 'AFL', 'MITT', 'AGCO', 'AGEN', 'A', 'AGYS', 'AGIO', 'AGNC', 'ADC', 'AGFS', 'AIMT', 'AL', 'APD', 'ATSG', 'AYR', 'AKS', 'AKAM', 'AKCA', 'AKBA', 'AKRX', 'ALG', 'ALRM', 'ALK', 'AIN', 'ALB', 'ALBO', 'AA', 'ALDR', 'ALDX', 'ALEX', 'ALX', 'ARE', 'ALXN', 'ALCO', 'ALGN', 'ALKS', 'Y', 'ATI', 'ABTX', 'ALGT', 'ALLE', 'ALNA', 'AGN', 'ALE', 'ADS', 'AOI', 'LNT', 'AMOT', 'ALSN', 'MDRX', 'ALL', 'ALLY', 'ALNY', 'AOSL', 'GOOGL', 'GOOG', 'AMR', 'ALTR', 'AYX', 'ASPS', 'AIMC', 'MO', 'AMAG', 'AMZN', 'AMBC', 'AMBA', 'AMBR', 'AMC', 'DOX', 'AMED', 'APEI', 'UHAL', 'AEE', 'AMRC', 'AAL', 'AAT', 'AXL', 'ACC', 'AEO', 'AEP', 'AEL', 'AXP', 'AFG', 'AMH', 'AIG', 'ANAT', 'AMNB', 'AOBC', 'ARII', 'ARA', 'ARL', 'AMSWA', 'AWR', 'AMT', 'AVD', 'AMWD', 'AWK', 'CRMT', 'COLD', 'AMP', 'ABCB', 'AMSF', 'ABC', 'ATLO', 'AME', 'AMGN', 'FOLD', 'AMKR', 'AMN', 'AMRX', 'AMPH', 'APH', 'AMPE', 'AFSI', 'AMRS', 'APC', 'AMCX', 'ANAB', 'ANDV', 'ANDE', 'ANGO', 'ANIP', 'ANIK', 'AXE', 'NLY', 'ANSS', 'ATRS', 'AR', 'ANTM', 'ANH', 'AON', 'APA', 'AIV', 'APLS', 'APY', 'APOG', 'ARI', 'AMEH', 'APPF', 'APLE', 'AAPL', 'AIT', 'AMAT', 'AAOI', 'AREX', 'APTI', 'ATR', 'APTV', 'WTR', 'AQ', 'WAAS', 'ARMK', 'PETX', 'ABR', 'ABUS', 'ARCB', 'ACGL', 'ARCH', 'ADM', 'AROC', 'ARNC', 'RCUS', 'ARD', 'ARDX', 'ADI', 'ACRE', 'AGX', 'ARGO', 'ANET', 'AI', 'AHH', 'ARR', 'AFI', 'AWI', 'ARQL', 'ARRY', 'ARRS', 'ARW', 'AROW', 'ARWR', 'ASNS', 'ARTNA', 'APAM', 'ABG', 'ASNA', 'ASGN', 'AHT', 'AINC', 'ASH', 'AHL', 'AZPN', 'ASMB', 'ASB', 'AC', 'AIZ', 'AGO', 'ASTE', 'ATRO', 'ASUR', 'HOME', 'T', 'ATRA', 'ATHN', 'ATH', 'ATNX', 'ATHX', 'ATKR', 'ACBI', 'AT', 'AAWW', 'TEAM', 'ATO', 'ASC', 'ARNA', 'ATRI', 'AUBN', 'BOLD', 'ADSK', 'ADP', 'AN', 'AZO', 'AVB', 'AGR', 'AVYA', 'AVEO', 'AVY', 'CDMO', 'AVID', 'CAR', 'AVA', 'AVT', 'AVX', 'EQH', 'AXTA', 'ACLS', 'AXS', 'AXGN', 'AAXN', 'AXTI', 'AZZ', 'BGS', 'RILY', 'BW', 'BMI', 'BHGE', 'BCPC', 'BWINB', 'BLL', 'BANC', 'BANF', 'BLX', 'TBBK', 'BXS', 'BOCH', 'BAC', 'BOH', 'BMRC', 'BK', 'NTB', 'BPRN', 'ATNI', 'ATRC', 'BWFG', 'BANR', 'BHB', 'BNED', 'BKS', 'B', 'BBSI', 'BAS', 'BSET', 'BAX', 'BCML', 'BBT', 'BBX', 'BCBP', 'BECN', 'BBGI', 'BZH', 'BDX', 'BBBY', 'BELFB', 'BDC', 'BLCM', 'BEL', 'BMS', 'BHE', 'BNCL', 'BNFT', 'WRB', 'BRK.B', 'BHLB', 'BERY', 'BBY', 'BGSF', 'BGCP', 'BGFV', 'BIG', 'BH.A', 'BH', 'BCRX', 'BIIB', 'BHVN', 'BMRN', 'BIO', 'BIOS', 'BSTC', 'TECH', 'OZRK', 'BFIN', 'BKU', 'BKH', 'BKI', 'BLKB', 'BL', 'BLK', 'BXMT', 'HRB', 'BLMN', 'BCOR', 'BLBD', 'BHBK', 'BLUE', 'BXG', 'BXC', 'BPMC', 'BRG', 'BMCH', 'BA', 'BOFI', 'WIFI', 'BCC', 'BOJA', 'BOKF', 'BCEI', 'BKNG', 'BOOT', 'BAH', 'BWA', 'SAM', 'BOMN', 'BPFH', 'BXP', 'BSX', 'EPAY', 'BOX', 'BYD', 'BRC', 'BHR', 'BDN', 'BDGE', 'BWB', 'BGG', 'BFAM', 'BCOV', 'BHF', 'BEAT', 'BTX', 'BJRI', 'BRS', 'BRX', 'AVGO', 'BR', 'BKD', 'BRKL', 'BRKS', 'BRO', 'BF.A', 'BF.B', 'BRT', 'BRKR', 'BC', 'BMTC', 'BLMT', 'BKE', 'BLDR', 'BG', 'BURL', 'BFST', 'BWXT', 'BY', 'CFFI', 'CHRW', 'CJ', 'CA', 'CABO', 'CBT', 'CCMP', 'COG', 'CACI', 'WHD', 'CADE', 'CDNS', 'CDZI', 'CZR', 'CSTE', 'CAI', 'CALM', 'CAMP', 'CVGW', 'CAL', 'CRC', 'CWT', 'CALA', '5', 'BSIG', 'EAT', 'BCO', 'BMY', 'ABCD', 'CBM', 'CATC', 'CAC', 'CPT', 'CPB', 'CWH', 'CNNE', 'CMD', 'CPLA', 'CCBG', 'COF', 'CSU', 'CFFN', 'CSTR', 'CMO', 'CARA', 'CRR', 'CBLK', 'CARB',
'CAH', 'CSII', 'CDLX', 'CATM', 'CRCM', 'CDNA', 'CECO', 'CTRE', 'CARG', 'CSL', 'KMX', 'CCL', 'CARO', 'CRS', 'CSV', 'CRZO', 'TAST', 'CARS', 'CRI', 'CVNA', 'CASA', 'CWST', 'CASY', 'CASI', 'CALX', 'ELY', 'CPE', 'CLXT', 'CPRX', 'CTT', 'CAT', 'CATY', 'CATO', 'CVCO', 'CAVM', 'CBFV', 'CBZ', 'CBL', 'CBOE', 'CBRE', 'CBS', 'CBTX', 'CDK', 'CDW', 'CECE', 'CDR', 'CE', 'CELC', 'CELG', 'CBMG', 'CELH', 'CNC', 'CDEV', 'CNP', 'CSFL', 'CETV', 'CENT', 'CENTA', 'CPF', 'CVCY', 'CENX', 'CNBKA', 'CNTY', 'CCS', 'CTL', 'CDAY', 'CERN', 'CERS', 'CEVA', 'CF', 'ECOM', 'CRL', '6', 'CASS', 'ROX', 'CSLT', 'CTLT', 'CBIO', 'CAKE', 'CHEF', 'CHGG', 'CHE', 'CHFC', 'CCXI', 'CHMG', 'LNG', 'CHMI', 'CHK', 'CHSP', 'CPK', 'CVX', 'CHS', 'PLCE', 'CIM', 'CMRX', 'CMG', 'CHH', 'CDXC', 'CB', 'CHD', 'CHDN', 'CHUY', 'CIEN', 'CI', 'XEC', 'CMPR', 'CBB', 'CINF', 'CNK', 'CTAS', 'CIR', 'CRUS', 'CSCO', 'CISN',
'CIT', 'CTRN', 'C', 'CZNC', 'CFG', 'CIA', 'CTXS', 'GTLS', 'CHTR', 'CHFN', 'CCF', 'CLDT', 'CLH', 'CCO', 'CLFD', 'CLSD', 'CLW', 'CLF', 'CLPR', 'CLX', 'CLD', 'CLDR', 'CLVS', 'CME', 'CMS', 'CNA', 'CCNE', 'CNO', 'CNX', 'COBZ', 'COKE', 'KO', 'CDXS', 'CVLY', 'CDE', 'CCOI', 'CGNX', 'CTSH', 'CWBR', 'CNS', 'COHR', 'CHRS', 'COHU', 'CFX', 'CL', 'COLL', 'CLNY', 'CLNC', 'COLB', 'CLBK', 'CXP', 'COLM', 'CMCO', 'CMCSA', 'CMA', '7', 'CHCO', 'CIO', 'CIVB', 'CIVI', 'CLAR', 'CLNE', 'ESXB', 'TCFC', 'CYH', 'CHCT', 'CTBI', 'CVLT', 'CMP', 'CPSI', 'CIX', 'CMTL', 'CAG', 'CNCE', 'CXO', 'CNDT', 'CNMD', 'CTWS', 'CNOB', 'CONN', 'COP', 'CEIX', 'CNSL', 'ED', 'CTO', 'CWCO', 'STZ', 'CBPX', 'CLR', 'CTRL', 'CVON', 'CVG', 'COO', 'CPS', 'CTB', 'CPA', 'CPRT', 'CRBP', 'CORT', 'CORE', 'CXW', 'CLGX', 'CORR', 'CPLG', 'FIX', 'CBSH', 'CMC', 'CVGI', 'COMM', 'CBU', 'CMRE', 'CSGP', 'COST', 'COTV', 'COTY', 'ICBK', 'COUP', 'CUZ', 'CVA', 'CVTI', 'CVIA', 'COWN', 'CRAI', 'CBRL', 'BREW', 'CR', 'CRD.B', 'CRAY', 'CACC', 'CREE', 'CROX', 'CCRN', 'CCI', 'CCK', 'CRY', 'CYRX', 'CSGS', 'CSWI', 'CSX', 'CTIC', 'CTS', 'CUBE', 'CUB', 'CUE', 'CFR', 'CULP', 'CMI', 'CURO', 'CW', 'CUBI', 'CUTR', 'CVBF', '8', 'COR', 'CORI', 'CSOD', 'GLW', 'OFC', 'CRVL', 'CRVS', 'CTMX', 'CTSO', 'DHI', 'DJCO', 'DAKT', 'DAN', 'DHR', 'DRI', 'DAR', 'DZSI', 'DSKE', 'PLAY', 'DVA', 'DWSN', 'DCT', 'DDR', 'DF', 'DCPH', 'DECK', 'DE', 'DFRG', 'TACO', 'DK', 'DVMT', 'DAL', 'DLX', 'DNLI', 'DNR', 'DENN', 'XRAY', 'DEPO', 'DERM', 'DVN', 'DXCM', 'DHT', 'DHIL', 'DO', 'FANG', 'DRH', 'DRNA', 'DKS', 'CVI', 'CVS', 'CBAY', 'CY', 'CONE', 'CYS', 'CYTK', 'DPLO', 'DFS', 'DISCA', 'DISCK', 'DISH', 'DIS', 'BOOM', 'DOCU', 'DLB', 'DG', 'DLTR', 'D', 'DPZ', 'UFS', 'DCI', 'DGICA', 'DFIN', 'RRD', 'LPG', 'DORM', 'PLOW', 'DEI', 'DOVA', 'DOV', 'DWDP', 'DPS', 'DRQ', 'DS', 'DSW', 'DTE', 'DCO', 'DUK', 'DRE', 'DLTH', 'DNB', 'DNKN', 'DRRX', 'DXC', 'DXPE', 'DY', 'DVAX', '9', 'DBD', 'DGII', 'DMRC', 'DLR', 'DDS', 'DCOM', 'DIN', 'DIOD', 'DEA', 'EML', 'EGP', 'EMN', 'KODK', 'ETN', 'EV', 'EBAY', 'EBIX', 'ECHO', 'SATS', 'ECR', 'ECL', 'EPC', 'EIX', 'EDIT', 'EDR', 'EW', 'EGAN', 'EHTH', 'EE', 'LOCO', 'ERI', 'ESIO', 'EA', 'EFII', 'ELVT', 'ELF', 'ELLI', 'PERY', 'ELOX', 'EMCI', 'EME', 'EEX', 'EBS', 'EMR', 'NYNY', 'ESRT', 'EIG', 'ENTA', 'DX', 'ETFC', 'EGBN', 'EGLE', 'EXP', 'EGRX', 'ESTE', 'EWBC', 'WATT', 'UUUU', 'ERII', 'EGC', 'ENS', 'EGL', 'EBF', 'ENVA', 'ENPH', 'NPO', 'ENSG', 'ESGR', 'ENFC', 'ENTG', 'ETM', 'ETR', 'EBTC', 'EFSC', 'EVC', 'ENV', 'EVI', 'EVHC', 'ENZ', 'EOG', 'EPE', 'EPAM', 'EPZM', 'PLUS', 'EPR', 'EQT', 'EFX', 'EQIX', 'EQBK', 'EQC', 'ELS', 'EQR', 'ERA', 'ERIE', 'EROS', 'ESCA', '10', 'EHC', 'ECPG', 'WIRE', 'ENDP', 'ECYT', 'ELGX', 'EIGI', 'EGN', 'ENR', 'ETH', 'ETSY', 'EEFT', 'EVBN', 'EVLO', 'EVBG', 'EVR', 'RE', 'EVRG', 'EVRI', 'ES', 'EVTC', 'EVH', 'EOLS', 'EPM', 'AQUA', 'EXAS', 'XAN', 'XELA', 'EXEL', 'EXC', 'EXLS', 'EXPE', 'EXPD', 'EXPO', 'EXPR', 'ESRX', 'STAY', 'EXTN', 'EXR', 'XOG', 'EXTR', 'XOM', 'EZPW', 'FFIV', 'FN', 'FB', 'FDS', 'FICO', 'ESE', 'ESPR', 'ESQ', 'ESSA', 'ESND', 'ESNT', 'ESS', 'EL', 'ESL', 'FCB', 'AGM', 'FRT', 'FSS', 'FII', 'FDX', 'FNHC', 'FENC', 'FOE', 'FG', 'FGEN', 'FDBC', 'FIS', 'LION', 'FRGI', 'FITB', 'FNGN', 'FISI', 'FNSR', 'FEYE', 'FAF', 'FNLC', 'FBNC', 'FBP', 'FBMS', 'FRBA', 'BUSE', 'FBIZ', 'FCBP', 'FCNCA', 'FCBC', 'FCCO', 'FCF', 'FBNK', 'FDC', 'FDEF', 'FFBC', 'THFF', 'FFIN', '11', 'FARM', 'FMAO', 'FFKT', 'FMNB', 'FPI', 'FARO', 'FAST', 'FATE', 'FBK', 'FFG', 'FMBH', 'FMBI', 'FNWB', 'FRC', 'FSFG', 'FSLR', 'FUNC', 'FCFS', 'FE', 'FISV', 'FIT', 'FIVE', 'FPRX', 'FIVN', 'FBC', 'FLT', 'FLXN', 'FLXS', 'FLIR', 'FND', 'FTK', 'FLO', 'FLS', 'FLNT', 'FLDM', 'FLR', 'FFIC', 'FMC', 'FNBG', 'FNB', 'FNF', 'FONR', 'FL', 'F', 'FSCT', 'FCE.A', 'FOR', 'FORM', 'FFNW', 'FFWM', 'FGBI', 'FHB', 'FHN', 'FR', 'INBK', 'FIBK', 'FLIC', 'FRME', 'FMI', 'FCPT', 'FOXF', 'FRAN', 'FC', 'FELE', 'FSB', 'BEN', 'FSP', 'FI', 'FCX', 'RAIL', 'FDP', 'FRPT', 'RESI', 'FTR', 'FRO', 'FRPH', 'FSBW', 'FCN', 'FTSI', 'FCEL', 'FULT', 'FNKO', 'FSNN', 'FF', 'GTHX', 'GAIA', 'GCAP', 'AJG', 'GBL', 'GME', 'GLPI', 'GCI', 'GPS', 'GDI', 'GRMN', 'IT', '12', 'FORR', 'FRTA', 'FTNT', 'FTV', 'FBIO', 'FBHS', 'FET', 'FWRD', 'FOSL', 'FSTR', 'FBM', 'GFN', 'GIS', 'GM', 'GCO', 'GWR', 'GEN', 'GNMK', 'GHDX', 'G', 'GNTX', 'THRM', 'GPC', 'GNW', 'GEO', 'GABC', 'GERN', 'GTY', 'GGP', 'ROCK', 'GILD', 'GBCI', 'GOOD', 'LAND', 'GLT', 'GKOS', 'GBT', 'BRSS', 'GBLI', 'GMRE', 'GNL', 'GPN', 'GWRS', 'GMED', 'GLUU', 'GLYC', 'GMS', 'GNC', 'GLOG', 'GTES', 'GATX', 'GLIBA', 'GCP', 'GNK', 'GENC', 'GNRC', 'GD', 'GE', 'GIII',
'GPX', 'GRA', 'GGG', 'EAF', 'GHM', 'GHC', 'GWW', 'GPT', 'LOPE', 'GVA', 'GPMT', 'GPK', 'GTN', 'AJX', 'GLDD', 'GSBC', 'GWB', 'GNBC', 'GRBK', 'GDOT', 'GPRE', 'GBX', 'GCBC', 'GHL', 'GLRE', 'GEF', 'GEF.B', 'GRIF', 'GFF', 'GPI', 'GRPN', 'GRUB', 'GTT', 'GTXI', 'GBNK', 'GNTY', 'GES', '13', 'GDDY', 'GOGO', 'GLNG', 'GORO', 'GDEN', 'GS', 'GDP', 'GT', 'GSHD', 'GPRO', 'GRC', 'GOV', 'HALO', 'HYH', 'HBB', 'HLNE', 'HWC', 'HBI', 'HAFC', 'HASI', 'THG', 'HONE', 'HOG', 'HLIT', 'HRS', 'HSC', 'HIG', 'HBIO', 'HAS', 'HVT', 'HE', 'HA', 'HCOM', 'HWKN', 'HAYN', 'FUL', 'HCHC', 'HCA', 'HCI', 'HCP', 'HDS', 'HIIQ', 'HR', 'HCSG', 'HTA', 'HQY', 'HSTM', 'HTLD', 'GWRE', 'GLF', 'GPOR', 'HEES', 'HABT', 'HCKT', 'HAE', 'HAIN', 'HK', 'HNRG', 'HAL', 'HALL', 'HTBK', 'HCCI', 'HFWA', 'HRTG', 'MLHR', 'HRTX', 'HT', 'HSY', 'HTZ', 'HSKA', 'HES', 'HPE', 'HXL', 'HF', 'HIBB', 'HPR', 'HIW', 'HIL', 'HI',
'HRC', 'HTH', 'HGV', 'HLT', 'HIFS', 'HMSY', 'HNI', 'HFC', 'HOLX', 'HBCP', 'HOMB', 'HD', 'HMST', 'HTBI', 'FIXX', 'HON', 'HOFT', '14', 'HTLF', 'HL', 'HEI.A', 'HEI', 'HSII', 'HELE', 'HSDT', 'HLX', 'HP', 'HMTV', 'JKHY', 'HLF', 'HRI', 'HHC', 'HPQ', 'HRG', 'HUBG', 'HUBB', 'HUBS', 'HUD', 'HPP', 'HUM', 'HBAN', 'HII', 'HUN', 'HURC', 'HURN', 'H', 'HY', 'IAC', 'IBKC', 'ICFI', 'ICHR', 'ICUI', 'IDA', 'IDRA', 'IEX', 'IDXX', 'IESC', 'INFO', 'IIVI', 'ILG', 'ITW', 'ILMN', 'IMAX', 'IMMR', 'IMDZ', 'IMGN', 'HOPE', 'HMN', 'HBNC', 'HZNP', 'HRL', 'HDP', 'HPT', 'HST', 'TWNK', 'HMHC', 'HLI', 'HOV', 'HBMD', 'III', 'HIFR', 'IEA', 'IR', 'NGVT', 'IMKTA', 'INGR', 'INWK', 'IPHS', 'IOSP', 'IIPR', 'INVA', 'INGN', 'INOV', 'INO', 'IPHI', 'NSIT', 'INSM', 'NSP', 'INSP', 'IBP', 'IIIN', 'INST', 'PODD', 'INSY', 'ITGR', 'IART', 'IDTI', 'INTC', 'NTLA', 'I', 'IPAR', 'IBKR', 'ICPT', 'ICE', '15',
'IMMU', 'IMH', 'IMPV', 'PI', 'INCY', 'ICD', 'IHC', 'IRT', 'IBCP', 'INDB', 'IBTX', 'ILPT', 'INFN', 'IPCC', 'IPI', 'XON', 'IIN', 'INTU', 'ISRG', 'IVC', 'IVZ', 'IVR', 'ISTR', 'ITG', 'ISBC', 'IRET', 'ITIC', 'NVTA', 'INVH', 'IO', 'IONS', 'IOVA', 'IPGP', 'IQV', 'IRMD', 'IRTC', 'IRDM', 'IRBT', 'IRM', 'IRWD', 'ISRL', 'STAR', 'ITI', 'ITRI', 'ITT', 'JJSF', 'JAX', 'JCOM', 'IDCC', 'TILE', 'INAP', 'IBOC', 'IGT', 'IP', 'INSW', 'ISCA', 'IPG', 'XENT', 'IBM', 'INTL', 'IFF', 'ITCI']

def scrape_sp500():
    data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    table = data[0]
    sliced_table = table[1:]
    header = table.iloc[0]
    corrected_table = sliced_table.rename(columns=header)
    tickers = corrected_table['Symbol'].tolist()
    return tickers

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata    

#scrape wanted statistics from yahoo finace and then compare them to desired numbers 
def yahooKeyStats(stock):        
    try:        
        soup = make_soup('https://finance.yahoo.com/quote/' + stock +'/key-statistics')
        rev_growth = soup('table')[4].findAll('tr')[2].findAll('td')[1].string
        rev_growth = float(rev_growth[:-1].replace(',','')) #truncate the % before typecasting to float
        earning_growth = soup('table')[4].findAll('tr')[7].findAll('td')[1].string
        earning_growth = float(earning_growth[:-1].replace(',',''))
        pe = soup('table')[0].findAll('tr')[2].findAll('td')[1].string
        pe = float(pe[:-1].replace(',',''))
        
        if earning_growth > 20 or rev_growth > 10:
            if pe < 45:
                soup = make_soup('https://finance.yahoo.com/quote/'+ stock + '/financials')
                rev_17 = soup('table')[0].findAll('tr')[1].findAll('td')[1].string
                rev_16 = soup('table')[0].findAll('tr')[1].findAll('td')[2].string
                if float(rev_17.replace(',',''))/float(rev_16.replace(',','')) > 1.25:
                    print(stock)
                    print('Revenue growth: ' + str(rev_growth))
                    print('Earning growth: ' + str(earning_growth))
                    print('PE: ' + str(pe))
                    print('rev_17: ' + str(rev_17))
                    print('rev_16: ' + str(rev_16) + '\n')                    
        
    except Exception as e: 
        #print(e)
        c=0              

answer = input("1.sp500\n2.Russel3000")
if int(answer) is 1:
    sp500 = scrape_sp500()
    print('searching..')
    for stock in sp500:
        yahooKeyStats(stock)
elif int(answer) is 2:
    print('searching..')
    for stock in Russel_3000:
        yahooKeyStats(stock)


