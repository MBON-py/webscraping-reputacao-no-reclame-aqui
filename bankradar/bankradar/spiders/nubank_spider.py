import scrapy


class NubankSpiderSpider(scrapy.Spider):
    name = "nubank_spider"
    allowed_domains = ["www.reclameaqui.com.br"]
    start_urls = ["https://www.reclameaqui.com.br/empresa/nubank/lista-reclamacoes/"]

    def parse(self, response):
        pass
