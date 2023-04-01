from selenium import webdriver
import os

# VPN istemcisini açın ve bağlanın
# VPN istemcisine özel talimatlar kullanmanız gerekebilir
# Bazı VPN sağlayıcılarının API'leri veya SDK'ları da mevcuttur
# Bu API veya SDK'ları kullanarak otomatik olarak VPN bağlantısı kurabilirsiniz

for i in range(10):
    # VPN bağlantısını kesin ve yeniden bağlanın
    os.system("sudo service openvpn stop")
    os.system("sudo service openvpn start")

    # Selenium WebDriver'ı yapılandırın ve VPN üzerinden web sayfalarına erişmek için proxy ayarlayın
    service_args = ['--proxy=localhost:8080', '--proxy-type=socks5']
    driver = webdriver.Firefox(service_args=service_args)

    # Web sayfasını yükleyin
    driver.get('http://www.example.com')

    # Sayfanın kaynağını yazdırın
    print(driver.page_source)

    # Tarayıcıyı kapatın
    driver.quit()
