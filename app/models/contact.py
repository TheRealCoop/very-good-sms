from app import DB


class Contact(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    first_name = DB.Column(DB.String(255), nullable=False)
    last_name = DB.Column(DB.String(255))
    number = DB.Column(DB.Integer, nullable=False)

    __table_args__ = (
        DB.UniqueConstraint('first_name', 'last_name', 'number'),
    )


    @classmethod
    def create(cls, **kwargs):
        kwargs['number'] = _clean_phone_number(kwargs['number'])
        contact = Contact(**kwargs)
        DB.session.add(contact)
        DB.session.commit()
        return contact


    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'number': _format_phone_number(self.number)
        }


    def delete(self):
        DB.session.delete(self)
        DB.session.commit()
        return {'success': True}


def _clean_phone_number(phone_number):
    return ''.join([x for x in phone_number if x.isdigit()])


def _format_phone_number(phone_number):
    first_three = str(phone_number)[:3]
    middle_three = str(phone_number)[3:6]
    last_four = str(phone_number)[-4:]
    return f'{first_three}-{middle_three}-{last_four}'
