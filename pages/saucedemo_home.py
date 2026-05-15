class HomePage:
    def __init__(self, page):
        self.page = page
        self.product_banner= page.get_by_text("Products")
        self.backpack=page.get_by_role("img", name="Sauce Labs Backpack")
        self.bikelight=page.get_by_role("img", name="Sauce Labs Bike Light")
        self.sortby_dropdown=page.get_by_role("combobox")

      
    def is_product_banner_visible(self):
        return self.product_banner.is_visible()
    
    def is_backpack_visible(self):
        return self.backpack.is_visible()

    
    def validate_dropdown_sortby_options(self, expected_options):
        options = self.sortby_dropdown.all_text_contents()
        print("Dropdown options:", options)
        return options == expected_options