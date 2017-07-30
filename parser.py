

class Parser:
    def __init__(self, input_na_sign='?', output_na_sign='?'):
        self.input_na_sign = input_na_sign
        self.output_na_sign = output_na_sign

    def parse(self, data):
        lines = self._split_into_lines(data)
        objects_attributes = self._split_lines_into_attributes(lines)
        objects_attributes = self._convert_strings_into_unique_numbers(objects_attributes)
        objects_attributes = self._separate_class_attribute(objects_attributes)

        return objects_attributes

    def _split_into_lines(self, data):
        return [line for line in data.split('\n') if line]

    def _split_lines_into_attributes(self, lines):
        return [line.split(",") for line in lines]

    def _convert_strings_into_unique_numbers(self, instances):
        attributes_indices = range(len(instances[0]))

        for attribute_index in attributes_indices:
            unique_attributes = {}
            for instance in instances:
                attribute = instance[attribute_index]
                instance[attribute_index] = self._convert_attribute(attribute, unique_attributes)

        return instances

    def _convert_attribute(self, attribute, unique_attributes):
        if attribute == self.input_na_sign:
            return self.output_na_sign
        elif attribute.isnumeric():
            return float(attribute)
        else:
            if attribute not in unique_attributes:
                unique_attributes[attribute] = len(unique_attributes)
            return float(unique_attributes[attribute])

    def _separate_class_attribute(self, objects_attributes):
        result = []

        for attributes in objects_attributes:
            class_attribute = attributes.pop()
            result.append({"attributes": attributes, "class": class_attribute})

        return result

