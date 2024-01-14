from django.db.models import CharField, IntegerField, Model, BigIntegerField


class Posting(Model):
    id = BigIntegerField(primary_key=True)
    name = CharField()
    location = CharField()
    image_link = CharField()
    insertion_order = IntegerField(unique=True)

    class Meta:
        db_table = 'postings'
        ordering = ['insertion_order']
