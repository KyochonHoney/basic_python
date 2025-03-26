# day 09

class Page:
    def get_total_page(self, m, n):
        if(m % n == 0):
            return m // n
        else:
            return m // n + 1
    
page_instance = Page()

print(page_instance.get_total_page(5, 10))