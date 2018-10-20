import requests
import re



url = 'https://www.pk.cn/portal-glossary'
response = requests.get(url)
response.encoding = 'utf-8'
html_txt = response.text
# print(html)
html_url = re.findall(r'/portal-glossary.*?.html', html_txt, re.S)
# print(html_url)
for html in html_url:

    html_urls = "https://www.pk.cn%s" % html
    # print(html_urls)
    html_response = requests.get(html_urls)
    html_response.encoding = 'utf-8'
    detail_html = html_response.text
    # html_content = re.findall(r'<div class="glossarySection--content">(.*?)<div style.*?', detail_html, re.S)

    html_content = re.findall(r'class="glossarySection--content-headline">(.*?)<div style.*?', detail_html, re.S)

# html_content = html_content.replace(' ', '')

    b = str(html_content)
    # print(b)
    # print(html_content)
    b = b.replace(' ', '')
    b = b.replace('</h2>', '')
    b = b.replace('<h2>', '')
    b = b.replace('\\n', '')
    b = b.replace('<br />', '')
    b = b.replace('<br/>', '')
    b = re.sub('<imgsrc="/themes/poker/glossary/images/.*?hspace="2"/>|相关主题', '', b)
    # b = re.sub('<spanstyle.*?|</span>', '', b)
    # b = re.sub('例子(德州扑克):.*?|\'', '', b)
    # b = re.sub('<tableborder.*?|相关主题', '相关主题', b)
    # b = re.sub('<imgsrc="/download/content/glossary/.*?|height=".*?"/>', '', b)
    b = re.sub('<tablewidth.*?相关主题|', '相关主题:', b)
    b = b.replace('</b>', '')
    b = b.replace('<b>', '')
    b = b.replace('<p>', '')
    b = b.replace('</p>', '')
    b = b.replace('\\t', '')
    b = b.replace('<td>', '')
    b = b.replace('</td>', '')
    b = b.replace('<tr>', '')
    b = b.replace('</tr>', '')
    b = b.replace('\\r', '')
    b = b.replace('<i>', '')
    b = b.replace('</i>', '')

    # print(html_content
    print(b)
    # exit()

