from mongoengine import fields, Document, EmbeddedDocument


class Salary(EmbeddedDocument):
    b2b = fields.DictField(default={'min': None, 'max': None})
    uop = fields.DictField(default={'min': None, 'max': None})


class Finances(EmbeddedDocument):
    contracts = fields.DictField(default={'b2b': False, 'uop': False})
    salary = fields.EmbeddedDocumentField(Salary)


class Location(EmbeddedDocument):
    address = fields.StringField()
    coordinates = fields.GeoPointField()
    

class JobPosition(Document):
    location = fields.EmbeddedDocumentField(Location)
    company_size = fields.IntField(min_value = 0)
    experience_level = fields.StringField(max_length=100)
    technologies = fields.ListField(fields.StringField())
    finances = fields.EmbeddedDocumentField(Finances)
    date = fields.StringField(max_length=100)

    meta = {'allow_inheritance': True}

    def __str__(self):
        return self.title


class JobOffer(JobPosition):
    title = fields.StringField()
    company = fields.StringField(max_length=100)
    languages = fields.ListField(fields.StringField())
    offer_link = fields.URLField()
    source_page = fields.StringField(max_length=100)
    active = fields.BooleanField(default=True)
    offer_hash = fields.StringField(max_length=62)