class Scale:
    def check(self):
        if self.count_person > 500:
            return f"{self.name}是个大公司"
        else:
            return f"{self.name}是个小公司"

class Detail:
    def show(self, scale):
        print(f'{scale},公司有{self.count_person}名员工。')

class Company(Detail, Scale):
    def __init__(self, name, count):
        self.name = name
        self.count_person = count

if __name__ == '__main__':
    my_company = Company("Fuck You", 800)
    company_scale = my_company.check()
    my_company.show(company_scale)