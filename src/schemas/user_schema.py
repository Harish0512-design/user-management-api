from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    firstname = fields.Str(
        required=True,
        validate=validate.Length(min=3)
    )
    lastname = fields.Str(
        required=True,
        validate=validate.Length(min=3)
    )
    dob = fields.Date(required=True)
    address = fields.Str(
        required=True,
        validate=validate.Length(min=5)
    )
    gender = fields.Str(
        required=True,
        validate=validate.OneOf(
            ["Male", "Female", "Other"]
        )
    )
    email = fields.Email(required=True)
    phone_number = fields.Str(
        required=True,
        validate=validate.Regexp(r'^\d{10}$')
    )  # 10 digits
