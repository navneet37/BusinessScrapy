import urllib.parse
from scrapy.loader import ItemLoader
import scrapy
from business.items import BusinessItem


class BusinessSpider(scrapy.Spider):
    name = 'business'
    start_urls = ['https://web.raleighchamber.org/allcategories']

    def parse(self, response):
        business_links = response.css('li.ListingCategories_AllCategories_CATEGORY a')[0:10]
        yield from response.follow_all(business_links, self.parse_biz)

    def parse_biz(self, response):
        # item = BusinessItem()
        def extract_with_get(query):
            return response.css(query).get(default='').strip()

        def extract_with_getall(query):
            _list = response.css(query).getall()
            return " ".join(_list)

        try:
            # from scrapy.shell import inspect_response
            # inspect_response(response, self)
            all_biz_det = response.css("div.tabber")
            if all_biz_det.css("h2 span a"):
                my_loader = ItemLoader(item=BusinessItem(), selector=all_biz_det)
                my_loader.add_css("biz_name", "h2 span a")
                my_loader.add_css("address", "span[itemprop]")
            # my_loader.add_css("contact_name", "span.ListingDetails_Level5_MAINCONTACT a")
            # my_loader.add_css("contact", "span.ListingDetails_Level5_MAINCONTACT")
            # my_loader.add_css("site", "a.ListingDetails_Level5_SITELINK::attr(href)")
            # my_loader.add_css("social_links", "div.ListingDetails_Level5_SOCIALMEDIA a::attr(href)")
            # my_loader.add_css("description", "div.ListingDetails_Level5_DESCRIPTION p")
            # social_list = all_biz_det.css("div.ListingDetails_Level5_SOCIALMEDIA a::attr(href)").getall()
            # social_list = [urllib.parse.unquote(each_link.split("?URL=")[-1]) for each_link in social_list]
            # item["biz_name"] = extract_with_get("h2 span a::text")
            # item["address"] = extract_with_getall("span[itemprop]::text")
            # item["contact_name"] = extract_with_get("span.ListingDetails_Level5_MAINCONTACT a::text")
            # item["contact"] = all_biz_det.css("span.ListingDetails_Level5_MAINCONTACT::text").getall()[-1]
            # item["site"] = extract_with_get("a.ListingDetails_Level5_SITELINK::attr(href)")
            # item["social_links"] = social_list
            # item["description"] = extract_with_get("div.ListingDetails_Level5_DESCRIPTION p::text")
                yield my_loader.load_item()
            # elif all_biz_det.css('h2 span span'):
            #     social_list = all_biz_det.css("div.ListingDetails_Level5_SOCIALMEDIA a::attr(href)").getall()
            #     social_list = [urllib.parse.unquote(each_link.split("?URL=")[-1]) for each_link in social_list]
            #     yield {
            #         "biz_name": extract_with_get("h2 span span::text"),
            #         "address": extract_with_getall("span[itemprop]::text"),
            #         "contact_name": extract_with_get("span.ListingDetails_Level5_MAINCONTACT a::text"),
            #         "contact": all_biz_det.css("span.ListingDetails_Level5_MAINCONTACT::text").getall()[-1],
            #         "site": extract_with_get("a.ListingDetails_Level5_SITELINK::attr(href)"),
            #         "social_links": social_list,
            #         "description": extract_with_get("div.ListingDetails_Level5_DESCRIPTION p::text")
            #     }
            biz_links = all_biz_det.css('a.level1_footer_left_box_a.friendly')[0:2]
            yield from response.follow_all(biz_links, self.parse_biz)
        except Exception as err:
            self.logger.exception(err)
