Summary:	A program which will display a fortune
Summary(cs):	Program sušenka s věštbou (fortune cookie) s opravami chyb
Summary(da):	fortune-cookie program med mange fejl rettelser
Summary(de):	Glückskeks-Programm mit Bugfixes
Summary(fi):	Paranneltu fortnue-ohjelma
Summary(fr):	Programme fortune cookie avec correction de bugs
Summary(tr):	Rasgele, minik, sevimli mesajlar görüntüler
Name:		fortune-mod
Version:	1.99.1
Release:	29
License:	BSD
Group:		Toys
# Sources of the program
Url:		http://www.redellipse.net/code/fortune/
Source0:	http://www.redellipse.net/code/downloads/%{name}-%{version}.tar.bz2
# sources of fortune data files
# when no URL is given it is because the data files are not on the internet.
# they are either personal data I've collected myself trough the years;
# or data that people sent me in my quality of i18n coordinator of Mandriva
Source1:	http://crystal.u-strasbg.fr/glp.txt.bz2
Source2:	COPYING.glp
Source3:	http://crystal.u-strasbg.fr/cabale.txt.bz2
Source4:	ftp://sunsite.unc.edu/pub/Linux/games/amusement/fortune-fr.1138.tar.bz2
Source5:	ftp://sunsite.unc.edu/pub/Linux/games/amusement/fortune-it-1.51.tar.bz2
Source6:	ftp://ftp.startrek.eu.org/pub/linux/MS-FORTUNES.bz2
Source7:	http://sam.linuxfr.org/fortunes.txt.bz2
Source8:	COPYING.linuxfr
Source9:	http://www.multimania.com/fortune/ffr.tar.bz2
Source10:	azafra.txt.bz2
Source11:	deprimente.txt.bz2
Source12:	fortune-wa-spots.txt.bz2
Source13:	fortune-kotowaza.bz2
Source14:	fortune-kotowaza.README.bz2
Source15:	fortune-proverbs-gaeilge.bz2
Source16:	fortune-walon.txt.bz2
Source17:	fortune-msg-id.tar.bz2
Source18:	ftp://sunsite.unc.edu/pub/Linux/games/amusement/fortune-cs-1.2.4.tar.bz2
Source19:	ftp://sunsite.unc.edu/pub/Linux/games/amusement/fortunes-hu-0.1.tar.bz2
Patch0:		fortune-mod-1.99.1-LDFLAGS.diff
BuildRequires:	recode-devel recode

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's
your program. Fun-loving system administrators can add fortune to
users' .login files, so that the users get their dose of wisdom 
each time they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

Now it supports reading the LANG variable and choosing, if they exist,
fortunes in the user language, when no parameter is given.

%description -l cs
Toto je trvale oblíbený program věstící osud (fortune). Rád zobrazí
náhodnou věštbu, je-li spuštěn. Obvykle je legrace, když se umístí
do souboru .login pro uživatele vašeho systému, aby uviděli něco
nového pokaždé, když se přihlásí.

%description -l da
Dette er det altid populære 'fortune' program. Det vil gladeligt
udskrive en tilfældig besked når det køres. Det er sjovt at have i
.login filen for dine brugere, så de altid ser noget nyt når de
logger ind.

%description -l de
Dies ist das beliebte Glückskeks-Programm. Es druckt eine zufällige
Weisheit. Wenn Sie es in die .login-Datei Ihrer Benutzer schreiben,
erhalten diese bei jedem Anmelden einen neuen Spruch.

%description -l fi
Tämä on aina suosittu fortune-ohjelma. Se tulostaa satunnaisen mietelauseen
tai vitsin aina ajettaessa. Se yleensä laitetaan käynnistymään käyttäjien
.login-tiedoston kautta, jolloin käyttäjä näkee aina uuden lauseen
kirjautuessaan sisään.

%description -l fr
Le célèbre programme fortune. Il affiche joyeusement un dicton
aléatoire lorsqu'il est lancé. Il est généralement amusant de le
placer dans le .login des utilisateurs d'un système pour qu'ils
voient quelque chose de nouveau à chaque fois qu'ils se loggent.

Cette version supporte l'utilisation de la variable $LANG pour choisir
automatiquemment un sous répertoire adapté à la langue de l'utilisateur

%description -l it
Questo e' il popolare gioco fortune. Visualizza casualmente delle
frasi sul video. Gli utenti di solito lo aggiungono nel proprio .login
per vedere delle frasi divertenti ogni volta si collegano.

%description -l tr
Fortune, her çağrıldığında büyük bir kitaplıktan rasgele seçeceği,
eğlenceli bir metni görüntüleyecektir. Aşırı bilimsel ve yararlı bir
uygulama olmamasına karşın kullanıcıların her sisteme bağlanışında
değişik bir mesajla karşılaşmalarını sağlar.

%prep
%setup -q
%patch0 -p1

%build
%make RPM_OPT_FLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall_std prefix=%{buildroot}
mkdir -p %{buildroot}{%{_bindir}/,%{_sbindir}}
mv %{buildroot}%{_bindir}/*str* %{buildroot}%{_sbindir}/
cp util/rot %{buildroot}%{_bindir}

# extra english fortunes
mkdir -p en
mkdir -p doc/en
bzcat %{SOURCE6} > en/MS-FORTUNES

chmod -R a+rX en
cp en/* %{buildroot}%{_gamesdatadir}/fortunes/

# Czech fortunes
mkdir -p cs
mkdir -p doc/cs

tar xjf %{SOURCE18} && mv fortune-cs-1.2.4/{README,LICENSE,HISTORIE} doc/cs \
	&& rm fortune-cs-1.2.4/{fortune-cs.lsm,install.sh} \
	&& mv fortune-cs-1.2.4/* cs/
cd cs
for x in *;do recode l2..u8 $x;ln -s $x $x.u8; done
cd ..

chmod -R a+rX cs
cp -var cs %{buildroot}%{_gamesdatadir}/fortunes/

# Spanish fortunes
mkdir -p es
mkdir -p doc/es
bzcat %{SOURCE10} |recode l1..u8 > es/azafra
ln -s azafra es/azafra.u8
bzcat %{SOURCE11} |recode l1..u8 > es/deprimente
ln -s deprimente es/deprimente.u8

chmod -R a+rX es
cp -var es %{buildroot}%{_gamesdatadir}/fortunes/

# French fortunes
mkdir -p fr
mkdir -p doc/fr
tar xjf %{SOURCE4} -C fr/ && mkdir -p doc/fr/fortunes-fr && \
	mv fr/README fr/COPYING fr/INSTALL fr/*.lsm doc/fr/fortunes-fr
bzcat %{SOURCE1} | grep -v '^$' | sed 's/^-- /%/' > fr/glp \
	&& cp %{SOURCE2} doc/fr
bzcat %{SOURCE3} | grep -v '^$' | sed 's/^-- /%/' > fr/cabale
bzcat %{SOURCE7} > fr/linuxfr && cp %{SOURCE8} doc/fr
tar xjf %{SOURCE9} && mv ffr/data/* fr/ && rmdir ffr/data && \
	 mkdir -p doc/fr/ffr && mv ffr/* doc/fr/ffr/

recode l1..u8 fr/cabale
ln -s cabale fr/cabale.u8
recode l1..u8 fr/france
ln -s france fr/france.u8
recode l1..u8 fr/linuxfr
ln -s linuxfr fr/linuxfr.u8
recode l1..u8 fr/glp
ln -s glp fr/glp.u8
chmod -R a+rX fr
cp -var fr %{buildroot}%{_gamesdatadir}/fortunes/

# Gaeilge (Irish Gaelic) fortunes
mkdir -p ga
mkdir -p doc/ga
bzcat %{SOURCE15} > ga/proverbs && cat > doc/ga/proverbs << EOF
Gaeilge proverbs from Damian Lyons and GAELIC-L (mailing list)
EOF
recode l1..u8 ga/proverbs
ln -s proverbs ga/proverbs.u8
chmod -R a+rX ga
cp -var ga %{buildroot}%{_gamesdatadir}/fortunes/


# Hungarian fortunes
mkdir -p hu
mkdir -p doc/hu

tar xjvf %{SOURCE19} && mv fortunes-hu/{README,OLVASSEL} doc/hu \
	&& mv fortunes-hu/hu/magyar hu/
recode l1..u8 hu/magyar
ln -s magyar hu/magyar.u8

chmod -R a+rX hu
cp -var hu %{buildroot}%{_gamesdatadir}/fortunes/

# Indonesian fortunes
mkdir -p id
mkdir -p doc/id
tar xjf %{SOURCE17} && mv fortune-msg-id/README doc/id && \
	 mv fortune-msg-id/* id/

chmod -R a+rX id
cp -var id %{buildroot}%{_gamesdatadir}/fortunes/

# Italian fortunes
mkdir -p it
mkdir -p doc/it
tar xjf %{SOURCE5}
mv fortune.it-1.51/COPYING fortune.it-1.51/README doc/it
mv fortune.it-1.51/INSTALLAZIONE fortune.it-1.51/*.lsm doc/it
mv fortune.it-1.51/* it/

chmod -R a+rX it
cp -var it %{buildroot}%{_gamesdatadir}/fortunes/

# Japanese fortunes
mkdir -p ja
mkdir -p doc/ja
bzcat %{SOURCE13} > ja/kotowaza ; bzcat %{SOURCE14} > doc/ja/kotowaza.README

chmod -R a+rX ja
cp -var ja %{buildroot}%{_gamesdatadir}/fortunes/

# Walloon fortunes
mkdir -p wa
mkdir -p doc/wa
bzcat %{SOURCE12} > wa/spots
bzcat %{SOURCE16} > wa/walon
recode l1..u8 wa/spots
ln -s spots wa/spots.u8
recode l1..u8 wa/walon
ln -s walon wa/walon.u8

chmod -R a+rX wa
cp -var wa %{buildroot}%{_gamesdatadir}/fortunes/

rm -rf %{buildroot}%{_gamesdatadir}/fortunes/off

(
    cd %{buildroot}%{_gamesdatadir}/fortunes/
    find * -name "*.dat" | xargs rm
    for i in `find * -type f` ; do
        %{buildroot}%{_sbindir}/strfile $i
    done
)

ln -s strfile.1%_extension %{buildroot}%{_mandir}/man1/unstr.1%_extension
#wrong paths in the man page:
sed -i -e 's!%{buildroot}!!' %{buildroot}%{_mandir}/man6/*

%files
%doc README ChangeLog TODO 
#%doc doc/en/*
%lang(cs) %doc doc/cs
#%lang(es) %doc doc/es
%lang(fr) %doc doc/fr
%lang(ga) %doc doc/ga
%lang(hu) %doc doc/hu
#%lang(id) %doc doc/id
%lang(it) %doc doc/it
%lang(ja) %doc doc/ja
#%lang(wa) %doc doc/wa
%attr(755,root,root)%{_gamesbindir}/fortune
%attr(755,root,root)%{_sbindir}/strfile
%attr(755,root,root)%{_sbindir}/unstr
%attr(755,root,root)%{_bindir}/rot
%lang(cs) %{_gamesdatadir}/fortunes/cs
%lang(es) %{_gamesdatadir}/fortunes/es
%lang(fr) %{_gamesdatadir}/fortunes/fr
%lang(ga) %{_gamesdatadir}/fortunes/ga
%lang(hu) %{_gamesdatadir}/fortunes/hu
%lang(id) %{_gamesdatadir}/fortunes/id
%lang(it) %{_gamesdatadir}/fortunes/it
%lang(ja) %{_gamesdatadir}/fortunes/ja
%lang(wa) %{_gamesdatadir}/fortunes/wa

%dir %{_gamesdatadir}/fortunes
%{_gamesdatadir}/fortunes/MS-FORTUNES
%{_gamesdatadir}/fortunes/art
%{_gamesdatadir}/fortunes/ascii-art
%{_gamesdatadir}/fortunes/computers
%{_gamesdatadir}/fortunes/cookie
%{_gamesdatadir}/fortunes/debian
%{_gamesdatadir}/fortunes/definitions
%{_gamesdatadir}/fortunes/drugs
%{_gamesdatadir}/fortunes/education
%{_gamesdatadir}/fortunes/ethnic
%{_gamesdatadir}/fortunes/food
%{_gamesdatadir}/fortunes/fortunes
%{_gamesdatadir}/fortunes/goedel
%{_gamesdatadir}/fortunes/humorists
%{_gamesdatadir}/fortunes/kids
%{_gamesdatadir}/fortunes/knghtbrd
%{_gamesdatadir}/fortunes/law
%{_gamesdatadir}/fortunes/linux
%{_gamesdatadir}/fortunes/linuxcookie
%{_gamesdatadir}/fortunes/literature
%{_gamesdatadir}/fortunes/love
%{_gamesdatadir}/fortunes/magic
%{_gamesdatadir}/fortunes/medicine
%{_gamesdatadir}/fortunes/men-women
%{_gamesdatadir}/fortunes/miscellaneous
%{_gamesdatadir}/fortunes/news
%{_gamesdatadir}/fortunes/paradoxum
%{_gamesdatadir}/fortunes/people
%{_gamesdatadir}/fortunes/perl
%{_gamesdatadir}/fortunes/pets
%{_gamesdatadir}/fortunes/platitudes
%{_gamesdatadir}/fortunes/politics
%{_gamesdatadir}/fortunes/riddles
%{_gamesdatadir}/fortunes/science
%{_gamesdatadir}/fortunes/songs-poems
%{_gamesdatadir}/fortunes/sports
%{_gamesdatadir}/fortunes/startrek
%{_gamesdatadir}/fortunes/translate-me
%{_gamesdatadir}/fortunes/wisdom
%{_gamesdatadir}/fortunes/work
%{_gamesdatadir}/fortunes/zippy
%{_gamesdatadir}/fortunes/*.dat
%{_gamesdatadir}/fortunes/*.u8
%{_mandir}/man6/fortune.6*
%{_mandir}/man1/strfile.1*
%{_mandir}/man1/unstr.1*

