class ServiceQuote:

    global tax_rate
    tax_rate = 0.0625

    def __init__(self):
        self.__parts_charges = float(input("Enter the parts charges: "))
        self.__labor_charges = float(input("Enter the labor charges: "))

    def set_parts_charges(pcharge):
        self.__parts_charges = pcharge

    def set_labor_charges(lcharge):
        self.__labor_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        self.__sales_tax = tax_rate * (self.__parts_charges + self.__labor_charges)
        return self.__sales_tax

    def get_total_charges(self):
        self.__total_charges = (
            self.__parts_charges
            + self.__labor_charges
            + (tax_rate * (self.__parts_charges + self.__labor_charges))
        )
        return self.__total_charges