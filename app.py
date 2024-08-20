from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
from time import sleep
import csv
import datetime
import csv
import os
import random
import uuid
import pandas as pd
from lxml import etree
import time 
import requests
import ast
import threading
cookie = 'shshshfpa=09a241cf-2b35-148f-a467-608a6ffd9c9a-1724124209; shshshfpx=09a241cf-2b35-148f-a467-608a6ffd9c9a-1724124209; jcap_dvzw_fp=r5W74EFsEizNPWU0u5xAD1WVVPreE63xBXUoHJ0QyqKGfYTpGey8QGltMBeC4dvwkqmkeBjdEdOeBITKFmWUKw==; pt_key=AAJmxAxHADBW7OIrZeKz6uFXZMdpqh1PRvU3Y-JMcvjpieXHX85J77jhedjj-0O0zekFtuzvJws; pt_pin=jobsofferings; pt_token=yc6lzw1t; pwdt_id=jobsofferings; sfstoken=tk01mee981d42a8sMXgyKzIrMiszUpLq8cSL359vgLYvzLNLAmlIlQfuMPxtAVqusy/jZ0V/eF1g3DWuo7gAqq9bTcJD; wxa_level=1; retina=1; cid=9; jxsid=17241242316955022428; appCode=ms0ca95114; webp=1; visitkey=7620598431207933762; cd_eid=jdd03MM775SDVJOGZQWJDSUMN6JZF5SZO4BJ4H3GI75ZIU277DWZ72JC42EFTV26IJSMOED5NNOGMF77WXFRTOCGVWOAHLQAAAAMRNXH7RQAAAAAACBFFX4Q7QIM3UQX; PPRD_P=UUID.17241242094781745442924; jxsid_s_u=https%3A//my.m.jd.com/index.html; sc_width=1512; [object Object]=undefined; wqmnx1=MDEyNjM5OG1vaGV1czU5aShDZSAgcC8gbG9uYjQvMjctNFJIISk%3D; __wga=1724124235287.1724124232125.1724124232125.1724124232125.2.1; jxsid_s_t=1724124235303; x-rp-evtoken=N-nAb5Oj6OS1u8hkvixIgPcyLM1v2d3k-1bk0VT5ufEW02UoSaf9YGxsxWROImJOOmT1sy52-a2i3F1QEgW5rwm2S7wulc0rVRi5ijigitbrQKrAAyFflZT3YJ2R9B67kdidFOVI4CHVIfynZQpY5e_u-8td_pQTOci6CLWN8EH4ZflW8bLBm9J13tkdbjG4tANhiDp3b9xiwsyPKqgP_1RYt9y9ojybZWMmtsazF68%3D; ipLoc-djd=15-1213-0-0; jsavif=1; 3AB9D23F7A4B3CSS=jdd03MM775SDVJOGZQWJDSUMN6JZF5SZO4BJ4H3GI75ZIU277DWZ72JC42EFTV26IJSMOED5NNOGMF77WXFRTOCGVWOAHLQAAAAMRNXSJB3YAAAAACBSZOQOOVLBZOUX; __jdu=17241242094781745442924; shshshfpb=BApXSagTsbvRAVO_f2XL6OxauCf3UOy1ABmZTRSZo9xJ1P9ZUf5XZlBzuniL0NJUrHxFe1g; mba_sid=17241242096813854832132323122.7; __jda=95931165.17241242094781745442924.1724124209.1724124209.1724124209.1; __jdb=95931165.9.17241242094781745442924|1.1724124209; __jdc=95931165; 3AB9D23F7A4B3C9B=MM775SDVJOGZQWJDSUMN6JZF5SZO4BJ4H3GI75ZIU277DWZ72JC42EFTV26IJSMOED5NNOGMF77WXFRTOCGVWOAHLQ'

app = Flask(__name__)

CORS(app)

headers = [
    {
    'User-Agent': "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "cookie": cookie
    },
    {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "cookie": cookie
    },
    {
        'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "cookie": cookie
    },
    {
        'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
        "cookie": cookie
    },
    {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
         "cookie": cookie
    },
    {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        "cookie": cookie
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',

        "cookie": cookie

    },

]

def getip():  # 随机ip

    with open("ipdaili.txt") as f:
        iplist = f.readlines()
    proxy = iplist[random.randint(0, len(iplist) - 1)]
    proxy = proxy.replace("\n", "")
    proxies = {
        'http': 'http://' + str(proxy)
    }
    return proxies


def getdata(url):
    res = requests.get(url, headers=random.choice(headers))
    res.encoding = 'utf-8'
    text = res.text
    selector = etree.HTML(text)
    list = selector.xpath('//*[@id="J_goodsList"]/ul/li')

    rows = []
    for i in list:
        title = i.xpath('.//div[@class="p-name p-name-type-2"]/a/em/text()')
        price = i.xpath('.//div[@class="p-price"]//text()')
        price="".join(price)
        product_id = i.xpath('.//div[@class="p-commit"]/strong/a/@id')[0].replace("J_comment_", "")
        try:
            shop = i.xpath('.//div[@class="p-shop"]/span/a/text()')[0]
        except IndexError:
            shop = ''
        title = ' '.join(title)
        rows.append([product_id, title.replace('\n', '').replace('\t', ''), price.replace('\n', '').replace('\t', ''), shop.replace('\n', '').replace('\t', '')])
    return rows


def get_info1(sku):
    url = 'https://item.jd.com/{}.html'.format(sku)
    response = requests.get(url,  headers=random.choice(headers))
    parser = etree.HTMLParser()
    tree = etree.fromstring(response.content, parser)
    leixing = tree.xpath('//div[@class="crumb fl clearfix"]//text()')
    leixing = ''.join(leixing).replace(' ','').replace('\n','')


    pinlei = tree.xpath('//div[@class="item  selected  "]/@data-value')
    pinlei = ''.join(pinlei)



    guochang = '无'
    flag_list = tree.xpath('//ul[@class="parameter2 p-parameter-list"]//text()')
    for fl in flag_list:
        if '国产' in fl.split(':')[-1]:
            guochang = '国产'
        elif '进口' in fl.split(':')[-1]:
            guochang = '进口'
    img_list_ = tree.xpath('//*[@id="spec-list"]/ul/li/img/@src')
    img_list = []
    for il in img_list_:
        il = 'https:' + il.replace('/n5/','/n1/').replace('.avif','')
        img_list.append(il)
    return leixing,pinlei,guochang,img_list

from dotenv import load_dotenv
import os
from openai import OpenAI

def generate_content(img_urls, promt):
    #TODO: generate content based on the image_url
    content = [
        {
            "type": "text", 
            "text": promt
        },
    ]
    for img_url in img_urls:
        img_template = {
            "type": "image_url",
            "image_url": {
                'url': img_url},
        }
        content.append(img_template)

    return content

def askAI(img_url, base_url):

    promt = \
    """
    请结合所给图片进行分析，参照以下格式，提供产品详细信息需要包括：['Product volume/size(产品体积/尺寸)', 'Packageformat(包装形式)', 'Package material(包装材料)', 'Label(标签)', 'Numbers of printing color (印刷颜色数量）', 'Dimension(尺寸)', 'Company(公司)', 'Ingredient of product (产品成分)']
    回复内容按照以下形式组织，没有的元素标为不详，图片有的元素必须具体给出：
    {'Product volume/size(产品体积/尺寸)': '不详', 'Packageformat(包装形式)': '塑料瓶装', 'Package material(包装材料)': '高密度聚乙烯（HDPE）塑料', 'Label(标签)': '除菌除螨、99%除菌、72小时抑菌、新升级', 'Numbers of printing color (印刷颜色数量）': '四种颜色：红色、白色、蓝色和绿色', 'Dimension(尺寸)': '不详', 'Company(公司)': 'Procter & Gamble (宝洁公司)', 'Ingredient of product (产品成分)': '不详'}
    """
    client = OpenAI()
    client.base_url = base_url
    content = generate_content(img_url, promt)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content




# if not os.path.exists('data.csv'):
#     file1 = open(r'data.csv', mode='a', encoding='utf-8-sig', newline='')   #打开这个文件，没有则自动创建，以追加形式写入，’utf-8‘编码方法编码
#     write1 = csv.writer(file1)  #用csv写入
#     write1.writerow(['链接','Description(描述)','价格','店铺','Categories(类别)','Product format(产品规格)','Manufacturing location(生产地点)'
#                      ,'Product volume/size(产品体积/尺寸)','Packageformat(包装形式)','Package material(包装材料)','Label(标签)'
#                      ,'Numbers of printing color (印刷颜色数量）','Dimension(尺寸)','Company(公司)','Ingredient of product (产品成分)'])  #csv表格写入这些数据
#     file1.close()


# max_count = input("请输入要爬取的最大数量：")
# max_count = int(max_count)
# item = input('请输入关键词：')
# time111 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
# lujing = input("请输入要保存文件的路径(例如：D:\Desktop):")
# data_list=[]
# for i in range(1,5):
    
#     url = 'https://search.jd.com/Search?keyword={}&enc=utf-8&wq={}'.format(
#         item,item)
#     n = i*2-1
#     url = url+"&pvid=e028fd4d4ba34c848d58d1c1f46c0259&page={}".format(n)
#     data = getdata(url)
#     for d in data:
#         data_list.append(d)
#     print(len(data_list))
#     if len(data_list) > max_count:
#         data_list = data_list[:max_count]
#         break
#     time.sleep(2)

# count=0
# for data in data_list:
#     if 1:
#         count+=1
#         leixing,pinlei,guochang,img_list = get_info1(data[0])
#         load_dotenv()

#         img_urls = img_list
#         base_url = "https://one-api.bltcy.top/v1"
#         answer = askAI(img_urls, base_url)
#         data[0] = 'https://item.jd.com/{}.html'.format(data[0])
#         #print(data + [leixing,pinlei,guochang])
#         answer = answer.split('{')[-1].split('}')[0]
#         answer = '{' + answer + '}'
#         answer = ast.literal_eval(answer)
#         #print(answer['Product volume/size(产品体积/尺寸)'],answer['Packageformat(包装形式)'],answer['Package material(包装材料)'],answer['Label(标签)'],answer['Numbers of printing color (印刷颜色数量）'],answer['Dimension(尺寸)'],answer['Ingredient of product (产品成分)'])
#         input1 = data + [leixing,pinlei,guochang] + [answer['Product volume/size(产品体积/尺寸)'],answer['Packageformat(包装形式)'],answer['Package material(包装材料)'],answer['Label(标签)'],answer['Numbers of printing color (印刷颜色数量）'],answer['Dimension(尺寸)'],answer['Company(公司)'],answer['Ingredient of product (产品成分)']]
#         time.sleep(2)
#         print("当前正在第{}条！！！".format(count),input1) 
            
#         # file1 = open(r'{}/{}_{}.csv'.format(lujing,item,time111), mode='a', encoding='utf-8-sig', newline='')   #打开这个文件，没有则自动创建，以追加形式写入，’utf-8‘编码方法编码
#         # write1 = csv.writer(file1)  #用csv写入
#         # write1.writerow(input1)  #csv表格写入这些数据
#         # file1.close()
#     else:
#         time.sleep(1)
#         pass
    
# 存储任务状态的字典
tasks = {}
tasks_lock = threading.Lock()

@app.route('/scrape', methods=['POST'])
def scrape_data():
    try:
        # 从请求体中获取参数
        data = request.json
        max_count = data.get('max_count')
        item = data.get('item')
        # 生成唯一的任务 ID
        task_id = str(uuid.uuid4())

        with tasks_lock:
          tasks[task_id] = {
              "status": "running",
              "max_count": max_count,
              "item": item,
              "task_list": [],
              "result": []
          }
        
        # 检查参数是否有效
        if not all([max_count, item]):
            return jsonify({"error": "Missing required parameters"}), 400
        
        # 启动后台任务
        def run_task(task_id):
            try:
                time111 = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
                data_list = []

                for i in range(1, 5):
                    try:
                        url = f'https://search.jd.com/Search?keyword={item}&enc=utf-8&wq={item}&page={(i*2)-1}'
                        data = getdata(url)
                        data_list.extend(data)
                        if len(data_list) > max_count:
                            data_list = data_list[:max_count]
                            break
                        time.sleep(2)
                    except OSError as e:
                        print(f"Failed to fix data: {e}")

                count = 0
                for data in data_list:
                    if 1:
                        try:
                            count += 1
                            leixing, pinlei, guochang, img_list = get_info1(data[0])
                            load_dotenv()
                            img_urls = img_list
                            base_url = "https://one-api.bltcy.top/v1"
                            answer = askAI(img_urls, base_url)
                            data[0] = f'https://item.jd.com/{data[0]}.html'
                            answer = answer.split('{')[-1].split('}')[0]
                            answer = '{' + answer + '}'
                            answer = ast.literal_eval(answer)
                            input1 = data + [leixing, pinlei, guochang] + [answer['Product volume/size(产品体积/尺寸)'], answer['Packageformat(包装形式)'], answer['Package material(包装材料)'], answer['Label(标签)'], answer['Numbers of printing color (印刷颜色数量）'], answer['Dimension(尺寸)'], answer['Company(公司)'], answer['Ingredient of product (产品成分)']]
                            time.sleep(2)
                            print(f"当前正在第{count}条！！！", input1)
                            with tasks_lock:
                              tasks[task_id]["result"].append(input1)
                              tasks[task_id]["task_list"].append('true')
                        except Exception as e:
                            with tasks_lock:
                              tasks[task_id]["task_list"].append('false')
                            print(f"Failed to fix data: {e}")
                with tasks_lock:
                  tasks[task_id]["status"] = "completed"
            except Exception as e:
                with tasks_lock:
                  tasks[task_id]["status"] = "failed"
                print(f"Task failed: {e}")

        # 启动任务处理线程
        import threading
        threading.Thread(target=run_task, args=(task_id,)).start()

        # 返回任务 ID
        return jsonify({"task_id": task_id}), 202

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status/<task_id>', methods=['GET'])
def get_status(task_id):
    with tasks_lock:
        if task_id not in tasks:
            print(tasks, '-----------------')
            return jsonify({"error": "Invalid task ID"}), 400
        task_data = tasks[task_id]
    return jsonify(task_data), 200

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)