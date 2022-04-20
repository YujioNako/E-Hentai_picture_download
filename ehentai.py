# coding=gbk
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
import time
import re
import os


indexUrl = input("Ոݔ����Ʒ�Wַ|Please Enter the Adress of the Artwork��") or 'https://e-hentai.org/g/928151/e8de7d62e1/'
option = FirefoxOptions()
driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver.implicitly_wait(10)




def getPage(pageNow):
    # ��ȡ��ǰURL��HTMLҳ��
    htmlNow = driver.page_source
    #print(htmlNow)
    # ʹ��lxml���xpath����scriptԪ�ص����ݣ���ǰ�۲�ǰ�������������ҳ��Դ����Ľṹ�����Է��ָ�λ�б���script�У�
    imgNow = re.search('<img id="img" src="(.+?)"', htmlNow)
    if(pageNow <=10):
        pageNow = '00' + str(pageNow)
    elif(pageNow <=100):
        pageNow = '0' + str(pageNow)
    print(imgNow[1])
    name = imgNow[1].split('/')[-1]
    print(name)
    driver.find_element_by_xpath('//body/div/div/a/img[1]').screenshot('%s%s_%s.png' % (filename, pageNow, name))
    #screen_shot(imgNow[1], filename + name + '.png')
    #a = requests.get(url=imgNow[1], headers=HEADERS, verify=False)
    #f = open('/image/'+name, 'wb')
    #f.write(a.content)
    #f.close()  # ��ͼƬ����Ϊname

def mkdir(s):  # �����ļ���
    isExists = os.path.exists(s)  # �ж��Ƿ񴴽����ļ���
    if not isExists:
        os.makedirs(s)  # �����ļ���
        print("�����ļ��A'%s'���ļ���������춴�|Have created '%s', pictures will be saved here." % (s, s))
    else:
        print("�ѽ���'%s'�ļ��A���ļ���������춴�|'%s' already exists, pictures will be saved here." % (s, s))

def screen_shot(url,name):
    # ʹ��webdirver.PhantomJS()�����½�һ��phantomjs�Ķ��������ʹ�õ�phantomjs.exe����������path���Ҳ���phantomjs.exe����ᱨ��

    # ʹ��get()��������ָ��ҳ�档ע��������phantomjs���޽���ģ����Բ������κ�ҳ����ʾ
    driver.get(url)
    # ����phantomjs�����ȫ����ʾ
    driver.maximize_window()
    # ʹ��save_screenshot����������Ĳ��ֽ�ͼ����ʹ���ı����޷�һҳ��ʾ��ȫ��save_screenshotҲ������ȫ��ͼ
    driver.find_element_by_xpath('//body/img[1]').screenshot(name)
    # �ر�phantomjs���������Ҫ��������һ�����������������������з����������
    driver.close()


# ��ת��Ŀ�������ҳ

driver.get(indexUrl)
# �����������ҳ��ת���������ҳ��
time.sleep(1)
mainhtml = driver.page_source
firstpage = re.search('no-repeat"><a href="(.+?)"><img alt=', mainhtml)
artwork = re.search('<h1 id="gn">(.+?)</h1>', mainhtml)
artworkName = artwork[1]
invalid_chars = '[\\\/:*?"<>|]'
replace_char = '-'
artworkName = re.sub(invalid_chars, replace_char, artworkName)
filename = "./"+ artworkName +"/"
mkdir(filename)
# �ȴ�1��
time.sleep(1)
print(firstpage[1])
driver.get(firstpage[1])


# �������ҳ���index��ȡҳ��ְλ�б�ĺ���

# ��ȡ��ǰURL��HTMLҳ��
time.sleep(1)
html = driver.page_source
#print(html)

total_page_str = re.search('/ <span>(.+?)</span>', html)
# ������ʽ��ȡ���������ҳ��,����ƥ��1λ������λ������λ������λ������λ�������Ժ������п�������
total_page = int(total_page_str[1])
print("�� %s ҳ" %total_page)

for pageNow in range(1,total_page+1):
#for pageNow in range(1, 501):
    print("������ȡ %s ҳ���� %s ҳ" %(pageNow, total_page))
    time.sleep(5)
    try:
        getPage(pageNow)
        driver.find_elements_by_tag_name('a')[2].click()
    except:
        print("ERR: %s ����ʧ��, ������" % pageNow)
        time.sleep(3)
        driver.refresh()
        total_page = total_page-1


driver.quit()