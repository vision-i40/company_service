def get_attribute_from_the_last_object_of(model, attribute):
    return model.objects.values(attribute).order_by('created').last()

def create_object_of(model, **kwargs):
    return model.objects.create(**kwargs)

def compare_attributes_of_the_last_object(first_model, first_attribute, second_model, second_attribute):
    return get_attribute_from_the_last_object_of(first_model, first_attribute) == get_attribute_from_the_last_object_of(second_model, second_attribute)