import scrapy


class BusinessSpider(scrapy.Spider):
    name = 'business'
    start_urls = ['https://web.raleighchamber.org/allcategories']

    def parse(self, response):
        business_links = response.css('li.ListingCategories_AllCategories_CATEGORY a')[0:10]
        yield from response.follow_all(business_links, self.parse_biz)

    def parse_biz(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()
        try:
            all_biz_det = response.css("div.tabber")
            if all_biz_det.css('h2 span a'):
                yield {
                    "biz_name": extract_with_css("h2 span a::text")
                }
            elif all_biz_det.css('h2 span span'):
                yield {
                    "biz_name": extract_with_css("h2 span span::text")
                }
            else:
                biz_links = all_biz_det.css('a.level1_footer_left_box_a.friendly')[0:2]
                yield from response.follow_all(biz_links,  self.parse_biz)
        except Exception as err:
            self.logger.exception(err)
