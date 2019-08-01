from urllib import request
import re

class Spider():
    ''' 实现功能：爬出主播以及对应的人气值，并按人气从高到低排列
    '''
    url = "https://www.huya.com/g/wzry"
    root_pattern = '<span class="avatar fl">[\s\S]*?</span>[\w\W]*?</span>'  
    name_pattern = '<i class="nick" title=.*>(.*)</i>'
    number_pattern = '<i class="js-num">(.*)</i>'

    def __fetch_html(self):
        '''获取当前页面的html
        '''
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
    
    def __analysis(self, htmls):
        ''' 解析htmls，得到主播名称以及人气值
        '''
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        # print(anchors[0])
        return anchors
    
    def __refine(self, anchors):
        ''' 对集合中的元素进行精炼处理，去除多余的内容
        '''
        l = lambda anchor: {
            'name': anchor['name'][0],
            'number': anchor['number'][0]
            }
        return list(map(l, anchors))
    
    def __sort(self, anchors):
        ''' 对列表anchors进行排序
        '''
        # anchors = sorted(anchors, key=lambda anchor:anchor['number'])
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors
    
    def __sort_seed(self, anchor):
        ''' 排序种子
        '''
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number
    
    def __show(self, anchors):
        for rank in range(len(anchors)):
            print('rank '+str(rank + 1) 
                 + ': ' + anchors[rank]['name']
                 + '    ' + anchors[rank]['number'])
    
    def go(self):
        htmls = self.__fetch_html()
        anchors = self.__analysis(htmls)
        anchors = self.__refine(anchors)
        anchors = self.__sort(anchors)
        self.__show(anchors)

if __name__ == '__main__':
    spider = Spider()
    spider.go()