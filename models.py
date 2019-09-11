class DataCapture:
    data_values = []

    def add(self, elem):
        if elem < 0:
            return  # TODO: Error
        self.data_values.append(elem)

    def build_stats(self):
        total_elements = len(self.data_values)
        min_element = min(self.data_values)
        max_element = max(self.data_values)

        frequencies = {}
        for element in self.data_values:
            if element in frequencies:
                frequencies[element] += 1
            else:
                frequencies[element] = 1

        #  Create a dictionary of value: num_elements_less_than_value
        values_less = {}
        num_elements_less_than_current_num = frequencies[min_element]
        for current_num in range(min_element + 1, max_element + 1):
            values_less[current_num] = num_elements_less_than_current_num
            if current_num in frequencies:
                num_elements_less_than_current_num += frequencies[current_num]

        #  Create a dictionary of value: num_elements_greater_than_value
        values_greater = {}
        num_elements_greater_than_current_num = frequencies[max_element]
        for current_num in range(max_element - 1, min_element - 1, -1):
            values_greater[current_num] = num_elements_greater_than_current_num
            if current_num in frequencies:
                num_elements_greater_than_current_num += frequencies[current_num]

        return Stats(total_elements, min_element, max_element, frequencies, values_less, values_greater)


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
            return  # TODO: Error
        if lower_boundary == upper_boundary:
            return self.frequencies[lower_boundary]
        return self.total_elements - self.less(lower_boundary) - self.greater(upper_boundary)
