import scrapy
import re


re0=r"(\n|\t|\r)" #Regex matching non SP WhiteSpace characters

def dV(LIST):
    """A simple pretty printer to eliminate some ugly values of fields, like CR LF Tabs... \
            and return "-" as a printable placeholder for the empty value"""
    if LIST == []:
        return "-"
    else:
        return re.sub(re0,"",LIST[-1])

class QuotesSpider(scrapy.Spider):
    name = "ebay"

    def start_requests(self):
        urls = [
                'file:///home/arthur/scrapy/EBAY/ebay/inputs/index.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


#    def parse(self, response):
#        """ method that reads ebay pages, searching for item descriptions"""
#        for article in response.xpath("//li[@id][@_sp]"):
#            print ""
#            print "DESCRIPTION:  ", dV(article.xpath('.//a/text()').extract() )
#            print "LIEN:         ", dV(article.xpath('.//h3/a/@href').extract() )
#            print "LIENIMAGE:    ", dV(article.xpath('.//div[@class="lvpicinner full-width picW"]//@imgurl').extract() )
#            print "PRICE:        ", dV(article.xpath('.//li[@class="lvprice prc"]').xpath('.//span[@class="prRange"]|.//span[@class="bold"]').extract() )
#            print "SHIPPING:     ", dV(article.xpath('.//li[@class="lvshipping"]/span[@class="ship"]').xpath('.//span/span/text()|.//span/text()').extract() )
#            print "RETURNS:      ", dV(article.xpath('.//div[@class="lvreturns"]/span[@class="bfsp"]/text()').extract())
#            print "SPECIAL OFFER:", dV(article.xpath('.//div[@class="hotness-signal black"]/text()').extract())

    def parse(self, response):
        """ method that reads ebay pages, searching for item descriptions"""
        for article in response.xpath("//li[@id][@_sp]"):
            print ""
            print "DESCRIPTION:  ", article.xpath('.//a/text()').extract() 
            print "LIEN:         ", article.xpath('.//h3/a/@href').extract() 
            print "LIENIMAGE:    ", article.xpath('.//div[@class="lvpicinner full-width picW"]//@imgurl').extract() 
            print "PRICE:        ", article.xpath('.//li[@class="lvprice prc"]').xpath('.//span[@class="prRange"]|.//span[@class="bold"]').extract() 
            print "SHIPPING:     ", article.xpath('.//li[@class="lvshipping"]/span[@class="ship"]').xpath('.//span/span/text()|.//span/text()').extract() 
            print "RETURNS:      ", article.xpath('.//div[@class="lvreturns"]/span[@class="bfsp"]/text()').extract()
            print "SPECIAL OFFER:", article.xpath('.//div[@class="hotness-signal black"]/text()').extract()

