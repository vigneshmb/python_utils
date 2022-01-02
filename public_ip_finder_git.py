from requests import get
import json
from datetime import datetime
from dotenv import load_dotenv
import os


def get_public_ip():

    ip = get('https://api.ipify.org').text
    # print('My public IP address is: {}'.format(ip))
    key = os.environ.get("api_key")

    api_url = 'https://geo.ipify.org/api/v1?'
    url = api_url + 'apiKey=' + key + '&ipAddress=' + ip
    resp = get(url).text
    resp_data = json.loads(resp)

   # print(resp_data)
    try:
        ip = str(resp_data['ip'])
    except KeyError:
        ip = "none"

    try:
        country = str(resp_data['location']['country'])
    except KeyError:
        country = "none"

    try:
        region = str(resp_data['location']['region'])
    except KeyError:
        region = "none"

    try:
        city = str(resp_data['location']['city'])
    except KeyError:
        city = "none"

    try:
        lati = str(resp_data['location']['lat'])
    except KeyError:
        lati = "none"

    try:
        longi = str(resp_data['location']['lng'])
    except KeyError:
        longi = "none"

    try:
        postal = str(resp_data['location']['postalCode'])
    except KeyError:
        postal = "none"

    try:
        timez = str(resp_data['location']['timezone'])
    except KeyError:
        timez = "none"

    try:
        geoname = str(resp_data['location']['geonameId'])
    except KeyError:
        geoname = "none"

    try:
        temp_list = resp_data['domains']
        domains = ','.join([str(i) for i in temp_list])

    except KeyError:
        domains = "none"

    try:
        num = str(resp_data['as']['asn'])
    except KeyError:
        num = "none"

    try:
        name = str(resp_data['as']['name'])
    except KeyError:
        name = "none"

    try:
        route = str(resp_data['as']['route'])
    except KeyError:
        route = "none"

    try:
        domain = str(resp_data['as']['domain'])
    except KeyError:
        domain = "none"

    try:
        type_val = str(resp_data['as']['type'])
    except KeyError:
        type_val = "none"

    try:
        isp = str(resp_data['isp'])
    except KeyError:
        isp = "none"

    try:
        proxy = str(resp_data['proxy']['proxy'])
    except KeyError:
        proxy = "none"

    try:
        vpn = str(resp_data['proxy']['vpn'])
    except KeyError:
        vpn = "none"

    try:
        tor = str(resp_data['proxy']['tor'])
    except KeyError:
        tor = "none"

    data_list = []
    data_list.append(ip)
    data_list.append(country)
    data_list.append(region)
    data_list.append(city)
    data_list.append(lati)
    data_list.append(longi)
    data_list.append(postal)
    data_list.append(timez)
    data_list.append(geoname)
    data_list.append(domains)
    data_list.append(num)
    data_list.append(name)
    data_list.append(route)
    data_list.append(domain)
    data_list.append(type_val)
    data_list.append(isp)
    data_list.append(proxy)
    data_list.append(vpn)
    data_list.append(tor)

    return(data_list)


if __name__ == "__main__":
    load_dotenv()
    data = get_public_ip()
    print(data)

#   ip_addr,country,region,city,lati,longi,postalcode,timezone,geonameId,domains,asn,name,route,domain,type,isp,proxy,vpn,tor
