import hashlib
import time
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# List of passwords
passwords = [
    "password123", "admin2024", "mypassword", "welcome2024", "somalia1446password123",
    "Cabdirashiid2017", "cabdiwalid2017", "Cabdiwalid2017", "cabdixamid2017", "Cabdixamid2017",
    "caydaruus2017", "Caydaruus2017", "caydarus2017", "Caydarus2017", "cabaas2017",
    "Cabaas2017", "cisman2017", "Cisman2017", "cismaan2017", "Cismaan2017", "ciise2017",
    "Ciise2017", "cimraan2017", "Cimraan2017", "cimraan2017", "Cimran2017", "ciiltire2017",
    "Ciiltire2017", "cusman2017", "Cusman2017", "cusmaan2017", "Cusmaan2017", "cumar2017",
    "Cumar2017", "cudoon2017", "Cudoon2017", "coldoon2017", "Coldoon2017", "colaad2017",
    "Colaad2017", "daauud2017", "Daauud2017", "Duraan2017", "durasn2017", "daud2017",
    "Daud2017", "daadir2017", "Daadir2017", "deeq2017", "Deeq2017", "deeqa2017",
    "Deeqa2017", "faarax2017", "Faarax2017", "farax2017", "Farax2017", "Farxaan2017",
    "farxaan2017", "farxan2017", "Farxan2017", "fahad2017", "Fahad2017", "Farduus2017",
    "farduus2017", "fardus2017", "Fardus2017", "faryaad2017", "Faryaad2017", "Faryad2017",
    "faryad2017", "fahiima2017", "Fahiima2017", "fahima2017", "Fahima2017", "fadumo2017",
    "Fadumo2017", "faadumo2017", "Faadumo2017", "faatuush2017", "Faatuush2017", "fatush2017",
    "Fatush2017", "fadxi2017", "Fadxi2017", "fadxa2017", "Fadxa2017", "faysal2017",
    "Faysal2017", "fuad2017", "Fuad2017", "fosiya2017", "Fosiya2017", "foosi2017",
    "Foosi2017", "filsan2017", "Filsan2017", "fiicane2017", "Fiicane2017", "garaad2017",
    "Garaad2017", "Garad2017", "garad2017", "ganey2017", "Ganey2017", "gaaxnuug2017",
    "Gaaxnuug2017", "gaxnug2017", "Gaxnug2017", "gacalo2017", "Gacalo2017", "guled2017",
    "Guled2017", "guuleed2017", "Guuleed2017", "guhaad2017", "Guhaad2017", "Geesi2017",
    "geesi2017", "geele2017", "Geele2017", "Geenyo2017", "geenyo2017", "gaari2017",
    "Gaari2017", "Gobaad2017", "gobaad2017", "gobaadsan2017", "Gobaadsan2017", "guulwade2017",
    "Guulwade2017", "gacalo2017", "Gacalo2017", "hanad2017", "Hanad2017", "hasan2017",
    "Hasan2017", "Hodan2017", "hodan2017", "haboon2017", "Haboon2017", "habon2017",
    "Habon2017", "haaruun2017", "Haaruun2017", "harun2017", "Harun2017", "hasna2017",
    "Hasna2017", "hibaaq2017", "Hibaaq2017", "hibaq2017", "Hibaq2017", "hibo2017",
    "Hibo2017", "hinda2017", "Hinda2017", "huda2017", "Huda2017", "haldoor2017",
    "Haldoor2017", "hoodo2017", "Hoodo2017", "Heego2017", "heego2017", "Ismaaciil2017",
    "ismaaciil2017", "ismacil2017", "Ismacil2017", "ismahan2017", "Ismahan2017", "ishwaaq2017",
    "Ishwaaq2017", "isra2017", "Isra2017", "isaxaaq2017", "Isaxaaq2017", "isaxaq2017",
    "Isaxaq2017", "ibtisam2017", "Ibtisam2017", "ibtisaan2017", "Ibtisaan2017", "ibrahim2017",
    "Ibrahim2017", "ibraahim2017", "Ibraahim2017", "iman2017", "Iman2017", "iiman2017",
    "Iiman2017", "ikran2017", "Ikran23", "ikraan2017", "Ikraan2017", "ilhan2017", "Ilhan2017"
]

def crack_hash_from_list(password_hash, time_limit=300):
    start_time = time.time()
    for password in passwords:
        if time.time() - start_time > time_limit:
            print(Fore.RED + "Waqtiga baarista wuu dhammaaday (5 daqiiqo)!")
            return None
        if hashlib.sha256(password.encode()).hexdigest() == password_hash:
            return password
    return None

def print_ascii_art():
    print(Fore.BLUE + """
#######################################
               ******                
            ************             
          ****************           
        ********************         
      **********************         
    ***************************      
   **********         **********     
  ********              ********     
 ********                ********    
********                  ********   
********                  ********   
 ********                ********    
  ********              ********     
   **********         **********     
    ***************************      
      **********************         
        ********************         
          ****************           
            ************             
               ******                
#######################################
               SOMALIA               
#######################################
    CODED BY BLACK1446
#######################################
    """)

def main():
    print_ascii_art()
    print(Fore.YELLOW + "Xulo adeegga aad rabto:")
    print("1. TikTok")
    print("2. Facebook")
    print("3. YouTube")
    print("4. Instagram")
    print("5. PUBG")
    
    option = input("Dooro adeegga (1-5): ")
    
    if option in ['1', '2', '3', '4', '5']:
        username = input(Fore.YELLOW + "Gali username-ka: ")
        password_hash = input(Fore.YELLOW + "Gali SHA256 hash-ka password-ka: ")

        # Crack password using a list with a 5-minute limit
        print(Fore.YELLOW + f"Waxaan baarayaa hash-ka {password_hash}...")
        cracked_password = crack_hash_from_list(password_hash, time_limit=300)

        if cracked_password:
            print(Fore.GREEN + f"Password-ka {username} waa: {cracked_password}")
        else:
            print(Fore.RED + "Password lama helin liiska ereyada sirta ah ama waqtiga wuu dhammaaday!")
    else:
        print(Fore.YELLOW + "Doorasho aan sax ahayn!")

if __name__ == "__main__":
    main()passwords = [
    "password123", "admin2024", "mypassword", "welcome2024", "somalia1446password123",
    "Cabdirashiid2017", "cabdiwalid2017", "Cabdiwalid2017", "cabdixamid2017", "Cabdixamid2017",
    "caydaruus2017", "Caydaruus2017", "caydarus2017", "Caydarus2017", "cabaas2017",
    "Cabaas2017", "cisman2017", "Cisman2017", "cismaan2017", "Cismaan2017", "ciise2017",
    "Ciise2017", "cimraan2017", "Cimraan2017", "cimraan2017", "Cimran2017", "ciiltire2017",
    "Ciiltire2017", "cusman2017", "Cusman2017", "cusmaan2017", "Cusmaan2017", "cumar2017",
    "Cumar2017", "cudoon2017", "Cudoon2017", "coldoon2017", "Coldoon2017", "colaad2017",
    "Colaad2017", "daauud2017", "Daauud2017", "Duraan2017", "durasn2017", "daud2017",
    "Daud2017", "daadir2017", "Daadir2017", "deeq2017", "Deeq2017", "deeqa2017",
    "Deeqa2017", "faarax2017", "Faarax2017", "farax2017", "Farax2017", "Farxaan2017",
    "farxaan2017", "farxan2017", "Farxan2017", "fahad2017", "Fahad2017", "Farduus2017",
    "farduus2017", "fardus2017", "Fardus2017", "faryaad2017", "Faryaad2017", "Faryad2017",
    "faryad2017", "fahiima2017", "Fahiima2017", "fahima2017", "Fahima2017", "fadumo2017",
    "Fadumo2017", "faadumo2017", "Faadumo2017", "faatuush2017", "Faatuush2017", "fatush2017",
    "Fatush2017", "fadxi2017", "Fadxi2017", "fadxa2017", "Fadxa2017", "faysal2017",
    "Faysal2017", "fuad2017", "Fuad2017", "fosiya2017", "Fosiya2017", "foosi2017",
    "Foosi2017", "filsan2017", "Filsan2017", "fiicane2017", "Fiicane2017", "garaad2017",
    "Garaad2017", "Garad2017", "garad2017", "ganey2017", "Ganey2017", "gaaxnuug2017",
    "Gaaxnuug2017", "gaxnug2017", "Gaxnug2017", "gacalo2017", "Gacalo2017", "guled2017",
    "Guled2017", "guuleed2017", "Guuleed2017", "guhaad2017", "Guhaad2017", "Geesi2017",
    "geesi2017", "geele2017", "Geele2017", "Geenyo2017", "geenyo2017", "gaari2017",
    "Gaari2017", "Gobaad2017", "gobaad2017", "gobaadsan2017", "Gobaadsan2017", "guulwade2017",
    "Guulwade2017", "gacalo2017", "Gacalo2017", "hanad2017", "Hanad2017", "hasan2017",
    "Hasan2017", "Hodan2017", "hodan2017", "haboon2017", "Haboon2017", "habon2017",
    "Habon2017", "haaruun2017", "Haaruun2017", "harun2017", "Harun2017", "hasna2017",
    "Hasna2017", "hibaaq2017", "Hibaaq2017", "hibaq2017", "Hibaq2017", "hibo2017",
    "Hibo2017", "hinda2017", "Hinda2017", "huda2017", "Huda2017", "haldoor2017",
    "Haldoor2017", "hoodo2017", "Hoodo2017", "Heego2017", "heego2017", "Ismaaciil2017",
    "ismaaciil2017", "ismacil2017", "Ismacil2017", "ismahan2017", "Ismahan2017", "ishwaaq2017",
    "Ishwaaq2017", "isra2017", "Isra2017", "isaxaaq2017", "Isaxaaq2017", "isaxaq2017",
    "Isaxaq2017", "ibtisam2017", "Ibtisam2017", "ibtisaan2017", "Ibtisaan2017", "ibrahim2017",
    "Ibrahim2017", "ibraahim2017", "Ibraahim2017", "iman2017", "Iman2017", "iiman2017",
    "Iiman2017", "ikran2017", "Ikran23", "ikraan2017", "Ikraan2017", "ilhan2017", "Ilhan2017",
    # Add your new passwords here
    "password123", "admin2024", "mypassword", "welcome2024", "somalia1446"
]passwords = [
    "password123", "admin2024", "mypassword", "welcome2024", "somalia1446password123",
    "Cabdirashiid2017", "cabdiwalid2017", "Cabdiwalid2017", "cabdixamid2017", "Cabdixamid2017",
    "caydaruus2017", "Caydaruus2017", "caydarus2017", "Caydarus2017", "cabaas2017",
    "Cabaas2017", "cisman2017", "Cisman2017", "cismaan2017", "Cismaan2017", "ciise2017",
    "Ciise2017", "cimraan2017", "Cimraan2017", "cimraan2017", "Cimran2017", "ciiltire2017",
    "Ciiltire2017", "cusman2017", "Cusman2017", "cusmaan2017", "Cusmaan2017", "cumar2017",
    "Cumar2017", "cudoon2017", "Cudoon2017", "coldoon2017", "Coldoon2017", "colaad2017",
    "Colaad2017", "daauud2017", "Daauud2017", "Duraan2017", "durasn2017", "daud2017",
    "Daud2017", "daadir2017", "Daadir2017", "deeq2017", "Deeq2017", "deeqa2017",
    "Deeqa2017", "faarax2017", "Faarax2017", "farax2017", "Farax2017", "Farxaan2017",
    "farxaan2017", "farxan2017", "Farxan2017", "fahad2017", "Fahad2017", "Farduus2017",
    "farduus2017", "fardus2017", "Fardus2017", "faryaad2017", "Faryaad2017", "Faryad2017",
    "faryad2017", "fahiima2017", "Fahiima2017", "fahima2017", "Fahima2017", "fadumo2017",
    "Fadumo2017", "faadumo2017", "Faadumo2017", "faatuush2017", "Faatuush2017", "fatush2017",
    "Fatush2017", "fadxi2017", "Fadxi2017", "fadxa2017", "Fadxa2017", "faysal2017",
    "Faysal2017", "fuad2017", "Fuad2017", "fosiya2017", "Fosiya2017", "foosi2017",
    "Foosi2017", "filsan2017", "Filsan2017", "fiicane2017", "Fiicane2017", "garaad2017",
    "Garaad2017", "Garad2017", "garad2017", "ganey2017", "Ganey2017", "gaaxnuug2017",
    "Gaaxnuug2017", "gaxnug2017", "Gaxnug2017", "gacalo2017", "Gacalo2017", "guled2017",
    "Guled2017", "guuleed2017", "Guuleed2017", "guhaad2017", "Guhaad2017", "Geesi2017",
    "geesi2017", "geele2017", "Geele2017", "Geenyo2017", "geenyo2017", "gaari2017",
    "Gaari2017", "Gobaad2017", "gobaad2017", "gobaadsan2017", "Gobaadsan2017", "guulwade2017",
    "Guulwade2017", "gacalo2017", "Gacalo2017", "hanad2017", "Hanad2017", "hasan2017",
    "Hasan2017", "Hodan2017", "hodan2017", "haboon2017", "Haboon2017", "habon2017",
    "Habon2017", "haaruun2017", "Haaruun2017", "harun2017", "Harun2017", "hasna2017",
    "Hasna2017", "hibaaq2017", "Hibaaq2017", "hibaq2017", "Hibaq2017", "hibo2017",
    "Hibo2017", "hinda2017", "Hinda2017", "huda2017", "Huda2017", "haldoor2017",
    "Haldoor2017", "hoodo2017", "Hoodo2017", "Heego2017", "heego2017", "Ismaaciil2017",
    "ismaaciil2017", "ismacil2017", "Ismacil2017", "ismahan2017", "Ismahan2017", "ishwaaq2017",
    "Ishwaaq2017", "isra2017", "Isra2017", "isaxaaq2017", "Isaxaaq2017", "isaxaq2017",
    "Isaxaq2017", "ibtisam2017", "Ibtisam2017", "ibtisaan2017", "Ibtisaan2017", "ibrahim2017",
    "Ibrahim2017", "ibraahim2017", "Ibraahim2017", "iman2017", "Iman2017", "iiman2017",
    "Iiman2017", "ikran2017", "Ikran23", "ikraan2017", "Ikraan2017", "ilhan2017", "Ilhan2017",
    # Add your new passwords here
    "password123", "admin2024", "mypassword", "welcome2024", "somalia1446"
  ]passwords = [
    "password123", "admin2024", "mypassword", "welcome2024", "somalia1446password123",
    "Cabdirashiid2017", "cabdiwalid2017", "Cabdiwalid2017", "cabdixamid2017", "Cabdixamid2017",
    "caydaruus2017", "Caydaruus2017", "caydarus2017", "Caydarus2017", "cabaas2017",
    "Cabaas2017", "cisman2017", "Cisman2017", "cismaan2017", "Cismaan2017", "ciise2017",
    "Ciise2017", "cimraan2017", "Cimraan2017", "cimraan2017", "Cimran2017", "ciiltire2017",
    "Ciiltire2017", "cusman2017", "Cusman2017", "cusmaan2017", "Cusmaan2017", "cumar2017",
    "Cumar2017", "cudoon2017", "Cudoon2017", "coldoon2017", "Coldoon2017", "colaad2017",
    "Colaad2017", "daauud2017", "Daauud2017", "Duraan2017", "durasn2017", "daud2017",
    "Daud2017", "daadir2017", "Daadir2017", "deeq2017", "Deeq2017", "deeqa2017",
    "Deeqa2017", "faarax2017", "Faarax2017", "farax2017", "Farax2017", "Farxaan2017",
    "farxaan2017", "farxan2017", "Farxan2017", "fahad2017", "Fahad2017", "Farduus2017",
    "farduus2017", "fardus2017", "Fardus2017", "faryaad2017", "Faryaad2017", "Faryad2017",
    "faryad2017", "fahiima2017", "Fahiima2017", "fahima2017", "Fahima2017", "fadumo2017",
    "Fadumo2017", "faadumo2017", "Faadumo2017", "faatuush2017", "Faatuush2017", "fatush2017",
    "Fatush2017", "fadxi2017", "Fadxi2017", "fadxa2017", "Fadxa2017", "faysal2017",
    "Faysal2017", "fuad2017", "Fuad2017", "fosiya2017", "Fosiya2017", "foosi2017",
    "Foosi2017", "filsan2017", "Filsan2017", "fiicane2017", "Fiicane2017", "garaad2017",
    "Garaad2017", "Garad2017", "garad2017", "ganey2017", "Ganey2017", "gaaxnuug2017",
    "Gaaxnuug2017", "gaxnug2017", "Gaxnug2017", "gacalo2017", "Gacalo2017", "guled2017",
    "Guled2017", "guuleed2017", "Guuleed2017", "guhaad2017", "Guhaad2017", "Geesi2017",
    "geesi2017", "geele2017", "Geele2017", "Geenyo2017", "geenyo2017", "gaari2017",
    "Gaari2017", "Gobaad2017", "gobaad2017", "gobaadsan2017", "Gobaadsan2017", "guulwade2017",
    "Guulwade2017", "gacalo2017", "Gacalo2017", "hanad2017", "Hanad2017", "hasan2017",
    "Hasan2017", "Hodan2017", "hodan2017", "haboon2017", "Haboon2017", "habon2017",
    "Habon2017", "haaruun2017", "Haaruun2017", "harun2017", "Harun2017", "hasna2017",
    "Hasna2017", "hibaaq2017", "Hibaaq2017", "hibaq2017", "Hibaq2017", "hibo2017",
    "Hibo2017", "hinda2017", "Hinda2017", "huda2017", "Huda2017", "haldoor2017",
    "Haldoor2017", "hoodo2017", "Hoodo2017", "Heego2017", "heego2017", "Ismaaciil2017",
    "ismaaciil2017", "ismacil2017", "Ismacil2017", "ismahan2017", "Ismahan2017", "ishwaaq2017",
    "Ishwaaq2017", "isra2017", "Isra2017", "isaxaaq2017", "Isaxaaq2017", "isaxaq2017",
    "Isaxaq2017", "ibtisam2017", "Ibtisam2017", "ibtisaan2017", "Ibtisaan2017", "ibrahim2017",
    "Ibrahim2017", "ibraahim2017", "Ibraahim2017", "iman2017", "Iman2017", "iiman2017",
    "Iiman2017", "ikran2017", "Ikran23", "ikraan2017", "Ikraan2017", "ilhan2017", "Ilhan2017",
    # Add your new passwords here
    "password123", "admin2024", "mypassword", "welcome2024", "somalia1446"
    ]passwords = [
    "password123", "admin2024", "mypassword", "welcome2024", "somalia1446password123",
    "Cabdirashiid2017", "cabdiwalid2017", "Cabdiwalid2017", "cabdixamid2017", "Cabdixamid2017",
    "caydaruus2017", "Caydaruus2017", "caydarus2017", "Caydarus2017", "cabaas2017",
    "Cabaas2017", "cisman2017", "Cisman2017", "cismaan2017", "Cismaan2017", "ciise2017",
    "Ciise2017", "cimraan2017", "Cimraan2017", "cimraan2017", "Cimran2017", "ciiltire2017",
    "Ciiltire2017", "cusman2017", "Cusman2017", "cusmaan2017", "Cusmaan2017", "cumar2017",
    "Cumar2017", "cudoon2017", "Cudoon2017", "coldoon2017", "Coldoon2017", "colaad2017",
    "Colaad2017", "daauud2017", "Daauud2017", "Duraan2017", "durasn2017", "daud2017",
    "Daud2017", "daadir2017", "Daadir2017", "deeq2017", "Deeq2017", "deeqa2017",
    "Deeqa2017", "faarax2017", "Faarax2017", "farax2017", "Farax2017", "Farxaan2017",
    "farxaan2017", "farxan2017", "Farxan2017", "fahad2017", "Fahad2017", "Farduus2017",
    "farduus2017", "fardus2017", "Fardus2017", "faryaad2017", "Faryaad2017", "Faryad2017",
    "faryad2017", "fahiima2017", "Fahiima2017", "fahima2017", "Fahima2017", "fadumo2017",
    "Fadumo2017", "faadumo2017", "Faadumo2017", "faatuush2017", "Faatuush2017", "fatush2017",
    "Fatush2017", "fadxi2017", "Fadxi2017", "fadxa2017", "Fadxa2017", "faysal2017",
    "Faysal2017", "fuad2017", "Fuad2017", "fosiya2017", "Fosiya2017", "foosi2017",
    "Foosi2017", "filsan2017", "Filsan2017", "fiicane2017", "Fiicane2017", "garaad2017",
    "Garaad2017", "Garad2017", "garad2017", "ganey2017", "Ganey2017", "gaaxnuug2017",
    "Gaaxnuug2017", "gaxnug2017", "Gaxnug2017", "gacalo2017", "Gacalo2017", "guled2017",
    "Guled2017", "guuleed2017", "Guuleed2017", "guhaad2017", "Guhaad2017", "Geesi2017",
    "geesi2017", "geele2017", "Geele2017", "Geenyo2017", "geenyo2017", "gaari2017",
    "Gaari2017", "Gobaad2017", "gobaad2017", "gobaadsan2017", "Gobaadsan2017", "guulwade2017",
    "Guulwade2017", "gacalo2017", "Gacalo2017", "hanad2017", "Hanad2017", "hasan2017",
    "Hasan2017", "Hodan2017", "hodan2017", "haboon2017", "Haboon2017", "habon2017",
    "Habon2017", "haaruun2017", "Haaruun2017", "harun2017", "Harun2017", "hasna2017",
    "Hasna2017", "hibaaq2017", "Hibaaq2017", "hibaq2017", "Hibaq2017", "hibo2017",
    "Hibo2017", "hinda2017", "Hinda2017", "huda2017", "Huda2017", "haldoor2017",
    "Haldoor2017", "hoodo2017", "Hoodo2017", "Heego2017", "heego2017", "Ismaaciil2017",
    "ismaaciil2017", "ismacil2017", "Ismacil2017", "ismahan2017", "Ismahan2017", "ishwaaq2017",
    "Ishwaaq2017", "isra2017", "Isra2017", "isaxaaq2017", "Isaxaaq2017", "isaxaq2017",
    "Isaxaq2017", "ibtisam2017", "Ibtisam2017", "ibtisaan2017", "Ibtisaan2017", "ibrahim2017",
    "Ibrahim2017", "ibraahim2017", "Ibraahim2017", "iman2017", "Iman2017", "iiman2017",
    "Iiman2017", "ikran2017", "Ikran23", "ikraan2017", "Ikraan2017", "ilhan2017", "Ilhan2017",
    # Add your new passwords here
    "password123", "admin2024", "mypassword", "welcome2024", "somalia1446"
    ]passwords = [
    "password123", "admin2024", "mypassword", "welcome2024", "somalia1446password123",
    "Cabdirashiid2017", "cabdiwalid2017", "Cabdiwalid2017", "cabdixamid2017", "Cabdixamid2017",
    "caydaruus2017", "Caydaruus2017", "caydarus2017", "Caydarus2017", "cabaas2017",
    "Cabaas2017", "cisman2017", "Cisman2017", "cismaan2017", "Cismaan2017", "ciise2017",
    "Ciise2017", "cimraan2017", "Cimraan2017", "cimraan2017", "Cimran2017", "ciiltire2017",
    "Ciiltire2017", "cusman2017", "Cusman2017", "cusmaan2017", "Cusmaan2017", "cumar2017",
    "Cumar2017", "cudoon2017", "Cudoon2017", "coldoon2017", "Coldoon2017", "colaad2017",
    "Colaad2017", "daauud2017", "Daauud2017", "Duraan2017", "durasn2017", "daud2017",
    "Daud2017", "daadir2017", "Daadir2017", "deeq2017", "Deeq2017", "deeqa2017",
    "Deeqa2017", "faarax2017", "Faarax2017", "farax2017", "Farax2017", "Farxaan2017",
    "farxaan2017", "farxan2017", "Farxan2017", "fahad2017", "Fahad2017", "Farduus2017",
    "farduus2017", "fardus2017", "Fardus2017", "faryaad2017", "Faryaad2017", "Faryad2017",
    "faryad2017", "fahiima2017", "Fahiima2017", "fahima2017", "Fahima2017", "fadumo2017",
    "Fadumo2017", "faadumo2017", "Faadumo2017", "faatuush2017", "Faatuush2017", "fatush2017",
    "Fatush2017", "fadxi2017", "Fadxi2017", "fadxa2017", "Fadxa2017", "faysal2017",
    "Faysal2017", "fuad2017", "Fuad2017", "fosiya2017", "Fosiya2017", "foosi2017",
    "Foosi2017", "filsan2017", "Filsan2017", "fiicane2017", "Fiicane2017", "garaad2017",
    "Garaad2017", "Garad2017", "garad2017", "ganey2017", "Ganey2017", "gaaxnuug2017",
    "Gaaxnuug2017", "gaxnug2017", "Gaxnug2017", "gacalo2017", "Gacalo2017", "guled2017",
    "Guled2017", "guuleed2017", "Guuleed2017", "guhaad2017", "Guhaad2017", "Geesi2017",
    "geesi2017", "geele2017", "Geele2017", "Geenyo2017", "geenyo2017", "gaari2017",
    "Gaari2017", "Gobaad2017", "gobaad2017", "gobaadsan2017", "Gobaadsan2017", "guulwade2017",
    "Guulwade2017", "gacalo2017", "Gacalo2017", "hanad2017", "Hanad2017", "hasan2017",
    "Hasan2017", "Hodan2017", "hodan2017", "haboon2017", "Haboon2017", "habon2017",
    "Habon2017", "haaruun2017", "Haaruun2017", "harun2017", "Harun2017", "hasna2017",
    "Hasna2017", "hibaaq2017", "Hibaaq2017", "hibaq2017", "Hibaq2017", "hibo2017",
    "Hibo2017", "hinda2017", "Hinda2017", "huda2017", "Huda2017", "haldoor2017",
    "Haldoor2017", "hoodo2017", "Hoodo2017", "Heego2017", "heego2017", "Ismaaciil2017",
    "ismaaciil2017", "ismacil2017", "Ismacil2017", "ismahan2017", "Ismahan2017", "ishwaaq2017",
    "Ishwaaq2017", "isra2017", "Isra2017", "isaxaaq2017", "Isaxaaq2017", "isaxaq2017",
    "Isaxaq2017", "ibtisam2017", "Ibtisam2017", "ibtisaan2017", "Ibtisaan2017", "ibrahim2017",
    "Ibrahim2017", "ibraahim2017", "Ibraahim2017", "iman2017", "Iman2017", "iiman2017",
    "Iiman2017", "ikran2017", "Ikran23", "ikraan2017", "Ikraan2017", "ilhan2017", "Ilhan2017",
    # Add your new passwords here
    "password123", "admin2024", "mypassword", "welcome2024", "somalia1446"
    ]
