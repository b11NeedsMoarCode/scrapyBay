#Author : Arthur KIHM
#Author : Bastien Gouzerch
import scrapy
import re

#from scrapy.linkextractors import LinkExtractor

#re0=r"(\n|\t|\r)" #Regex matching non SP WhiteSpace characters
#def dV(LIST):
#    """A simple pretty printer to eliminate some ugly values of fields, like CR LF Tabs... \
#            and return "-" as a printable placeholder for the empty value"""
#    if LIST == []:
#        return "-"
#    else:
#        return re.sub(re0,"",LIST[-1])

def lastElement(L):
    """helper function to extract the last element of list L, or None if list is empty"""
    try:
        result = L[-1]
    except:
        result = None
    finally:
        return result


class QuotesSpider(scrapy.Spider):
    name = "ebay"

    def start_requests(self):
        urls = [
                'file:///home/arthur/scrapy/EBAY/ebay/inputs/index.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """ method that reads ebay pages, searching for item descriptions"""

        #We need only to extract the number of the page once, hence it is not in the loop.
        PAGENR = response.xpath('//td[@class="pages"]/a[@class="pg  curr"]/text()').extract_first()

        for article in response.xpath("//li[@id][@_sp]"):

            print {
             "PageNr"          : PAGENR, 
             "Description"     : lastElement(article.xpath('.//a/text()').extract()),
             "Lien"            : article.xpath('.//h3/a/@href').extract_first(),
             "LienImage"       : article.xpath('.//div[@class="lvpicinner full-width picW"]//@imgurl').extract_first() , 
             "Prix"            : article.xpath('.//li[@class="lvprice prc"]').xpath('.//span[@class="prRange"]|.//span[@class="bold"]').extract_first() ,
             "ShippingPolicy"  : lastElement(article.xpath('.//li[@class="lvshipping"]/span[@class="ship"]').xpath('.//span/span/text()|.//span/text()').extract()),
             "ReturnPolicy"    : article.xpath('.//div[@class="lvreturns"]/span[@class="bfsp"]/text()').extract_first(),
             "SpecialOffer"    : article.xpath('.//div[@class="hotness-signal black"]/text()').extract_first()
            }
        newlink = response.xpath('//td[@class="pagn-next"]/a/@href').extract_first() 
        if newlink is not None:
            print "!<-- page after  ",PAGENR," found-->"
            yield response.follow(newlink, callback=self.parse)


