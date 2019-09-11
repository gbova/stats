from errors import NegativeInputException, MinLargerThanMaxException


class DataCapture:
    data_values = []

    def add(self, elem):
        if elem < 0:
            raise NegativeInputException
        self.data_values.append(elem)

    def build_stats(self):
        total_elements = len(self.data_values)
        min_element = min(self.data_values)
        max_element = max(self.data_values)
        frequency_map = self.calculate_frequency_map()
        values_less = self.create_values_less_dict(frequency_map, min_element, max_element)
        values_greater = self.create_values_greater_dict(frequency_map, min_element, max_element)

        return Stats(total_elements, min_element, max_element, frequency_map, values_less, values_greater)

    def calculate_frequency_map(self):
        frequency_map = {}
        for element in self.data_values:
            if element in frequency_map:
                frequency_map[element] += 1
            else:
                frequency_map[element] = 1
        return frequency_map

    @staticmethod
    def create_values_less_dict(frequency_map, min_element, max_element):
        values_less = {}
        num_elements_less_than_current_num = frequency_map[min_element]
        for current_num in range(min_element + 1, max_element + 1):
            values_less[current_num] = num_elements_less_than_current_num
            if current_num in frequency_map:
                num_elements_less_than_current_num += frequency_map[current_num]
        return values_less

    @staticmethod
    def create_values_greater_dict(frequency_map, min_element, max_element):
        values_greater = {}
        num_elements_greater_than_current_num = frequency_map[max_element]
        for current_num in range(max_element - 1, min_element - 1, -1):
            values_greater[current_num] = num_elements_greater_than_current_num
            if current_num in frequency_map:
                num_elements_greater_than_current_num += frequency_map[current_num]
        return values_greater


class Stats:
    def __init__(self, total_elements, min, max, frequencies, values_less, values_greater):
        self.total_elements = total_elements
        self.min = min
        self.max = max
        self.frequencies = frequencies
        self.values_less = values_less
        self.values_greater = values_greater

    #  Return the number of elements that are less than the given value
    def less(self, value):
        if value <= self.min:
            return 0
        if value > self.max:
            return self.total_elements
        return self.values_less[value]

    #  Return the number of elements that are greater than the given value
    def greater(self, value):
        if value >= self.max:
            return 0
        if value < self.min:
            return self.total_elements
        return self.values_greater[value]

    def between(self, lower_boundary, upper_boundary):
        if lower_boundary > upper_boundary:
            raise MinLargerThanMaxException
        if lower_boundary == upper_boundary:
            return self.frequencies[lower_boundary]
        return self.total_elements - self.less(lower_boundary) - self.greater(upper_boundary)
