from utils import sortlist

class Range(object):
    def __init__(self):
        self._ranges_min = sortlist([])
        self._ranges_max = sortlist([])


    def valueInRange(self, value, index):
        # print 'Value in range %d '%value
        if index != None and index <= len(self._ranges_min)-1:
            return self._ranges_min[index] <= value <= self._ranges_max[index]
        return False

    def range_data(self, start, stop):
        # print 'Searching range data (%d, %d)'%(start, stop)
        min_index = max(self._ranges_min.search(start), self._ranges_max.search(start))
        max_index = max(self._ranges_min.search(stop), self._ranges_max.search(stop))
        min_in_range = self.valueInRange(start, min_index)
        max_in_range = self.valueInRange(stop, max_index)
        return min_index, min_in_range, max_index, max_in_range

    def addRange(self, start, stop):
        min_index, min_in_range, max_index, max_in_range = self.range_data(start-1, stop+1)

        # print min_index, min_in_range, max_index, max_in_range
        delete_min = min_index if min_index != None else 0
        delete_max = max_index if max_index != None else delete_min

        if min_index == -1: 
            min_index = delete_min = 0
            delete_max += 1
        elif min_in_range or max_in_range:
            delete_max += 1
            if not min_in_range:
                delete_min += 1
        elif min_index != None:
            delete_min += 1
            delete_max +=1
        if min_in_range:
            start = min(self._ranges_min[min_index], start)
        if max_in_range:
            stop = max(self._ranges_max[max_index], stop)

        self.deleteRangeIndexes(xrange(delete_min, delete_max))
        self._ranges_min.insert(start)
        self._ranges_max.insert(stop)

    def addRangeBasic(self, start, stop):
        self._ranges_min.insert(start)
        self._ranges_max.insert(stop)

    def queryRange(self, start, stop):
        min_index, min_in_range, max_index, max_in_range = self.range_data(start, stop)
        return min_index == max_index and min_in_range and max_in_range

    def deleteRangeIndex(self, index):
        # print 'Deleting range (%d, %d)'%(self._ranges_min[index], self._ranges_max[index])
        self._ranges_min.delete(index)
        self._ranges_max.delete(index)

    def deleteRangeIndexes(self, indexes):
        # print 'deleting indexes %s'%indexes
        for i, r  in enumerate(indexes):
            self.deleteRangeIndex(r-i)

    def deleteRange(self, start, stop):
        min_index, min_in_range, max_index, max_in_range = self.range_data(start, stop)
        print min_index, min_in_range, max_index, max_in_range
        if min_index == -1:
            min_index = 0
            max_index = max_index
            if not max_in_range:
                max_index = max_index+1
        if min_in_range:
            self._ranges_max[min_index] = min(start-1, self._ranges_max[min_index])
        if max_in_range:
            self._ranges_min[max_index] = min(stop+1, self._ranges_min[max_index])
        if self._ranges_min[max_index] > self._ranges_max[max_index]:
            print self._ranges_min[max_index] , self._ranges_max[max_index]
            # max_index += 1
        if self._ranges_min[min_index] > self._ranges_max[min_index]:
            min_index -= 1
        # if not self._ranges_min[max_index] < self._ranges_max[max_index] < start:
        #     max_index += 1
            # min_index -= 1
        # if min_in_range and max_in_range:
        #     min_index += 1
        self.deleteRangeIndexes(xrange(min_index+1, max_index))

    @property
    def ranges(self):
        return [(self._ranges_min[i],self._ranges_max[i]) for i in xrange(len(self._ranges_min))]

