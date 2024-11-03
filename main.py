import requests
from bs4 import BeautifulSoup
import os
import shutil
from datetime import datetime
import urllib.parse
import speedtest


def get_v2ray_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        divs = soup.find_all('div', class_='tgme_widget_message_text')
        divs2 = soup.find_all('div', class_='tgme_widget_message_text js-message_text before_footer')
        spans = soup.find_all('span', class_='tgme_widget_message_text')
        codes = soup.find_all('code')
        span = soup.find_all('span')
        main = soup.find_all('div')
        
        all_tags = divs + spans + codes + divs2 + span + main

        v2ray_configs = []
        for tag in all_tags:
            text = tag.get_text()
            if text.startswith('vless://') or text.startswith ('vmess://') or  text.startswith('ss://') or text.startswith('trojan://') or text.startswith('tuic://'):
                v2ray_configs.append(text)

        return v2ray_configs
    else:
        print(f"Failed to fetch URL (Status Code: {response.status_code})")
        return None

def get_region_from_ip(ip):
    api_endpoints = [
        f'https://ipapi.co/{ip}/json/',
        f'http://ipwho.is/{ip}?output=json',
        f'http://www.geoplugin.net/json.gp?ip={ip}',
        f'https://api.ipbase.com/v1/json/{ip}'
    ]

    for endpoint in api_endpoints:
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                data = response.json()
                if 'country' in data:
                    return data['country']
        except Exception as e:
            print(f"Error retrieving region from {endpoint}: {e}")
    return None

def test_speed():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    return st.results.download / 1_000_000, st.results.upload / 1_000_000  # Convert to Mbps

def save_configs_by_region(configs):
    config_folder = "sub"
    if os.path.exists(config_folder):
        for folder in os.listdir(config_folder):
            folder_path = os.path.join(config_folder, folder)
            if os.path.isdir(folder_path):
                shutil.rmtree(folder_path)

    if not os.path.exists(config_folder):
        os.makedirs(config_folder)

    for config in configs:
        ip = config.split('//')[1].split('/')[0]
        region = get_region_from_ip(ip)
        if region:
            region_folder = os.path.join(config_folder, region)
            if not os.path.exists(region_folder):
                os.makedirs(region_folder)

            download_speed, upload_speed = test_speed()
            with open(os.path.join(region_folder, 'config.txt'), 'a', encoding='utf-8') as file:
                file.write(f"{config} | Download Speed: {download_speed:.2f} Mbps | Upload Speed: {upload_speed:.2f} Mbps\n")

    all_configs_folder = "all_configs"
    if not os.path.exists(all_configs_folder):
        os.makedirs(all_configs_folder)

    with open(os.path.join(all_configs_folder, 'all_configs.txt'), 'a', encoding='utf-8') as file:
        for config in configs:
            file.write(config + '\n')

def send_file_to_telegram_channel(file_path, token, channel_id):
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    with open(file_path, 'rb') as file:
        response = requests.post(url, data={'chat_id': channel_id}, files={'document': file})
        
    if response.status_code == 200:
        print("File sent successfully.")
    else:
        print(f"Failed to send file. Error: {response.text}")

if __name__ == "__main__":
    telegram_urls = [
                
"https://t.me/s/V2range",
"https://t.me/s/Outline_ir",
"https://t.me/s/outlinevpnir",
"https://t.me/s/ZibaNabz",
"https://t.me/s/beiten",
"https://t.me/s/hopev2ray",
"https://t.me/s/V2rayNGn",
"https://t.me/Messi_Serwers",
"https://t.me/manVPN",
"https://t.me/EuServer",
"https://t.me/vmess_vless_v2rayng",
"https://t.me/mtproxy_lists",
"https://t.me/v2rayngch",
"https://t.me/V2raymelody",
"https://t.me/v2Line",
"https://t.me/s/free4allVPN",
"https://t.me/s/PrivateVPNs",
"https://t.me/s/DirectVPN",
"https://t.me/s/v2ray_outlineir",
"https://t.me/s/NetAccount",
"https://t.me/s/oneclickvpnkeys",
"https://t.me/s/daorzadannet",
"https://t.me/s/Outline_Vpn",
"https://t.me/s/vpn_xw",
"https://t.me/s/prrofile_purple",
"https://t.me/s/ShadowSocks_s",
"https://t.me/s/azadi_az_inja_migzare",
"https://t.me/s/WomanLifeFreedomVPN",
"https://t.me/s/customv2ray",
"https://t.me/s/UnlimitedDev",
"https://t.me/s/vmessorg",
"https://t.me/s/v2rayNG_Matsuri",
"https://t.me/s/v2rayngvpn",
"https://t.me/s/vpn_ioss",
"https://t.me/s/FalconPolV2rayNG",
"https://t.me/s/v2rayNGNeT",
"https://t.me/s/ShadowProxy66",
"https://t.me/s/ipV2Ray",
"https://t.me/s/kiava",
"https://t.me/s/Helix_Servers",
"https://t.me/s/PAINB0Y",
"https://t.me/s/VpnProSec",
"https://t.me/s/VlessConfig",
"https://t.me/s/NIM_VPN_ir",
"https://t.me/s/hashmakvpn",
"https://t.me/s/iran_ray",
"https://t.me/s/INIT1984",
"https://t.me/s/ServerNett",
"https://t.me/s/Pinkpotatocloud",
"https://t.me/s/CloudCityy",
"https://t.me/s/Qv2raychannel",
"https://t.me/s/shopingv2ray",
"https://t.me/s/xrayproxy",
"https://t.me/s/Proxy_PJ",
"https://t.me/s/V2rayng_Fast",
"https://t.me/s/v2ray_swhil",
"https://t.me/s/LoRd_uL4mo",
"https://t.me/s/proxyymeliii",
"https://t.me/s/MsV2ray",
"https://t.me/s/free_v2rayyy",
"https://t.me/s/v2ray1_ng",
"https://t.me/s/vless_vmess",
"https://t.me/s/MTConfig",
"https://t.me/s/PNG_V2rayNG",
"https://t.me/s/v2rayNG_VPNN",
"https://t.me/s/vmess_vless_v2rayng",
"https://t.me/s/Cov2ray",
"https://t.me/s/V2RayTz",
"https://t.me/s/VmessProtocol",
"https://t.me/s/MehradLearn",
"https://t.me/s/SafeNet_Server",
"https://t.me/s/ovpn2",
"https://t.me/s/lrnbymaa",
"https://t.me/s/vpn_tehran",
"https://t.me/s/OutlineVpnOfficial",
"https://t.me/s/v2ray_vpn_ir",
"https://t.me/s/v2_team",
"https://t.me/s/ConfigsHUB",
"https://t.me/s/V2rayngninja",
"https://t.me/s/iSegaro",
"https://t.me/s/bright_vpn",
"https://t.me/s/talentvpn",
"https://t.me/s/proxystore11",
"https://t.me/s/yaney_01",
"https://t.me/s/rayvps",
"https://t.me/s/free1_vpn",
"https://t.me/s/Parsashonam",
"https://t.me/s/v2rayngvp",
"https://t.me/s/Hope_Net",
"https://t.me/s/VPNCLOP",
"https://t.me/s/fnet00",
"https://t.me/s/V2pedia",
"https://t.me/s/molovpn",
"https://t.me/s/melov2ray",
"https://t.me/s/polproxy",
"https://t.me/s/Outlinev2rayNG",
"https://t.me/s/iP_CF",
"https://t.me/s/VPNCUSTOMIZE",
"https://t.me/s/MoV2ray",
"https://t.me/s/Royalping_ir",
"https://t.me/s/v2rayng_vpnrog",
"https://t.me/s/v2rayng_config_amin",
"https://t.me/s/rxv2ray",
"https://t.me/s/Capital_NET",
"https://t.me/s/VpnFreeSec",
"https://t.me/s/lightning6",
"https://t.me/s/WebShecan",
"https://t.me/s/v2Line",
"https://t.me/s/vmessiran",
"https://t.me/s/Configforvpn01",
"https://t.me/s/God_CONFIG",
"https://t.me/s/Awlix_ir",
"https://t.me/s/FreakConfig",
"https://t.me/s/frev2ray",
"https://t.me/s/vpnmasi",
"https://t.me/s/BestV2rang",
"https://t.me/s/TPvpn_Official",
"https://t.me/s/AM_TEAMMM",
"https://t.me/s/Lockey_vpn",
"https://t.me/s/XsV2ray",
"https://t.me/s/shh_proxy",
"https://t.me/s/L_AGVPN13",
"https://t.me/s/iTV2RAY",
"https://t.me/s/V2rayNGmat",
"https://t.me/s/ARv2ray",
"https://t.me/s/V2parsin",
"https://t.me/s/reality_daily",
"https://t.me/s/IRN_VPN",
"https://t.me/s/daredevill_404",
"https://t.me/s/idigitalz",
"https://t.me/s/aspeedvpn",
"https://t.me/s/FoxNim",
"https://t.me/s/marambashi",
"https://t.me/s/V2Ray_FreedomIran",
"https://t.me/s/V2RAY_VMESS_free",
"https://t.me/s/bypass_filter",
"https://t.me/s/CUSTOMVPNSERVER",
"https://t.me/s/DarkTeam_VPN",
"https://t.me/s/proxy_kafee",
"https://t.me/s/V2raysFree",
"https://t.me/s/Awlix_V2RAY",
"https://t.me/s/liq_VPN",
"https://t.me/s/v2logy",
"https://t.me/s/Watashi_VPN",
"https://t.me/s/servermomo",
"https://t.me/s/irancpi_vpn",
"https://t.me/s/V2rayCollector",
"https://t.me/s/ProxyForOpeta",
"https://t.me/s/mftizi",
"https://t.me/s/DeamNet_Proxy",
"https://t.me/s/EUT_VPN",
"https://t.me/s/Qv2rayDONATED",
"https://t.me/s/hcv2ray",
"https://t.me/s/MrV2Ray",
"https://t.me/s/Capoit",
"https://t.me/s/flyv2ray",
"https://t.me/s/forwardv2ray",
"https://t.me/s/inikotesla",
"https://t.me/s/networknim",
"https://t.me/s/foxrayiran",
"https://t.me/s/DailyV2RY",
"https://t.me/s/EliV2ray",
"https://t.me/s/v2rayng_fa2",
"https://t.me/s/V2rayNGvpni",
"https://t.me/s/custom_14",
"https://t.me/s/v2_vmess",
"https://t.me/s/FreeVlessVpn",
"https://t.me/s/freeland8",
"https://t.me/s/vmessq",
"https://t.me/s/WeePeeN",
"https://t.me/s/V2rayNG3",
"https://t.me/s/ShadowsocksM",
"https://t.me/s/shadowsocksshop",
"https://t.me/s/v2rayan",
"https://t.me/s/napsternetv_config",
"https://t.me/s/Easy_Free_VPN",
"https://t.me/s/v2ray_for_free",
"https://t.me/s/V2rayN_Free",
"https://t.me/s/vpn_ocean",
"https://t.me/s/configV2rayForFree",
"https://t.me/s/FreeV2rays",
"https://t.me/s/DigiV2ray",
"https://t.me/s/v2rayNG_VPN",
"https://t.me/s/freev2rayssr",
"https://t.me/s/v2rayn_server",
"https://t.me/s/Shadowlinkserverr",
"https://t.me/s/iranvpnet",
"https://t.me/s/vmess_iran",
"https://t.me/s/mahsaamoon1",
"https://t.me/s/V2RAY_NEW",
"https://t.me/s/v2RayChannel",
"https://t.me/s/configV2rayNG",
"https://t.me/s/config_v2ray",
"https://t.me/s/vpn_proxy_custom",
"https://t.me/s/v2ray_custom",
"https://t.me/s/HTTPCustomLand",
"https://t.me/s/ViPVpn_v2ray",
"https://t.me/s/FreeNet1500",
"https://t.me/s/v2ray_ar",
"https://t.me/s/beta_v2ray",
"https://t.me/s/vip_vpn_2022",
"https://t.me/s/FOX_VPN66",
"https://t.me/s/VorTexIRN",
"https://t.me/s/YtTe3la",
"https://t.me/s/V2RayOxygen",
"https://t.me/s/Network_442",
"https://t.me/s/VPN_443",
"https://t.me/s/v2rayng_v",
"https://t.me/s/ultrasurf_12",
"https://t.me/s/iSeqaro",
"https://t.me/s/frev2rayng",
"https://t.me/s/v2rayfree1",
"https://t.me/s/freev2raygood",
"https://t.me/s/proxy_mtm",
"https://t.me/s/amookashani",
"https://t.me/s/v2rayng_org",
"https://t.me/s/proxy_shadosocks",
"https://t.me/s/v2ray_youtube",
"https://t.me/s/V2ray_Alpha"
    ]

    all_v2ray_configs = []
    for url in telegram_urls:
        v2ray_configs = get_v2ray_links(url)
        if v2ray_configs:
            all_v2ray_configs.extend(v2ray_configs)

    if all_v2ray_configs:
        save_configs_by_region(all_v2ray_configs)
        
        # ارسال فایل به کانال تلگرام
        token = '5390914661:AAFumx5d-Q7N3r3dpMkkGzlWnsRZ-ez_GXg'  # توکن ربات خود را در اینجا قرار دهید
        channel_id = '@xxx12dd'  # شناسه کانال خود را در اینجا قرار دهید

        # ارسال فایل‌های پیکربندی
        for region in os.listdir("sub"):
            region_folder = os.path.join("sub", region)
            if os.path.isdir(region_folder):
                file_path = os.path.join(region_folder, 'config.txt')
                send_file_to_telegram_channel(file_path, token, channel_id)

        print("Configs saved and sent successfully.")
    else:
        print("No V2Ray configs found.")
