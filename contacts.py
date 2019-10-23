class Simple:
    def __init__(self, name, tel):
        self.name = name
        self.telephone = tel

    def last_name(self):
        if len(self.name) > 1:
            return self.name.split()[-1]

    def __str__(self):
        return ' '.join(['{value}'.format(value=self.__dict__.get(key)) for key in self.__dict__])


class Family(Simple):
    def __init__(self, name, tel, dateofbirth):
        Simple.__init__(self, name, tel)
        self.dateOfBirth = dateofbirth


class Company(Simple):
    def __init__(self, name, tel, email=None):
        Simple.__init__(self, name, tel)
        self.email = email

    def __str__(self):
        self.name = '"' + self.name.upper() + '"'
        return ' '.join(['{value}'.format(value=self.__dict__.get(key)) for key in self.__dict__])


Anna = Simple('Anna Smith', '+1(408)785-9933')
BB = Company('BeautyBar', '+1(408)785-9959', 'appointment@bb.com')
Mom = Family('Julia', '+1(408)785-9962', '26-04-1957')
Dad = Family('Jhon', '+1(408)785-9967', '5-03-1956')
Paola = Simple('Paola', '+1(408)785-9971')


import shelve
db = shelve.open('contactsDB')

for rec in (Anna, BB, Mom, Dad, Paola):
    db[rec.name] = rec

for key in db:
    print(db[key])
db.close()
