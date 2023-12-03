import frappe
from frappe.model.document import Document


class Property(Document):
    def after_insert(self):
        frappe.msgprint(
            msg=f"Document {self.name} inserted Successfully",
        )


# def validate(self):
#     if self.property_type == "Condominium":
#         for amenity in self.amenities:
#             if amenity.amenity == "Deck":
#                 frappe.throw(
#                     title="Error",
#                     msg=f"Property of <b>Condominium</b> should not have amenity <b>{amenity.amenity}</b>",
#                 )

#         # SQL
#         amenity = frappe.db.sql(
#             f""" SELECT amenity FROM `tabProperty Amenity Detail` WHERE parent='{self.name}' AND parenttype='Property' AND amenity='Deck' """,
#             as_dict=True,
#         )
#         if amenity:
#             frappe.throw(
#                 title="Error",
#                 msg=f"Property of <b>Condominium</b> should not have amenity <b>{amenity[0].amenity}</b>",
#             )
