from random import randint


class TimSort:
    """ A class to demonstrate Tim Sort """

    def __init__(self, array):
        self.array = array
        self.arrayLength = len(array)
        self.__RUN = 32

    def insertionSort(self, arr):
        """ Sorts the given array from given starting index to ending index """

        for i in range(1, len(arr)):
            currentElement = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > currentElement:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = currentElement

        return arr

    def mergeRuns(self, arr1, arr2):
        """ Merges the given two arrays: arr1 and arr2 """

        newArray = list()
        lengthOfArr1 = len(arr1)
        lengthOfArr2 = len(arr2)

        # The variable i is used to keep track of the indices of the first array
        # The variable j is used to keep track of the indices of the second array
        # The variable k is used to keep track of the indices of the newArray array which is to be returned
        i, j, k = 0, 0, 0

        while i < lengthOfArr1 and j < lengthOfArr2:
            if arr1[i] <= arr2[j]:
                newArray[k] = arr1[i]
                k += 1
                i += 1
            elif arr1[i] >= arr2[j]:
                newArray[k] = arr2[j]
                k += 1
                j += 1

            # The below two loops will append any remaining elements left in any of the two arrays.
            while i < lengthOfArr1:
                newArray.append(arr1[i])
                i += 1

            while j < lengthOfArr2:
                newArray.append(arr2[j])
                j += 1

        return newArray

    def changeRun(self, newRun):
        self.__RUN = newRun

    def algorithm(self):
        """ This function will perfom Tim Sort on the given array """

        # Breaking the array into chunks of subarray(RUNS) of size RUN and perfomring insertionSort on them.
        for i in range(0, self.arrayLength, self.__RUN):
            currentRunElements = self.array[i: i + self.__RUN]

            self.array[i: i +
                       self.__RUN] = self.insertionSort(currentRunElements)

        temp_runner = self.__RUN
        while temp_runner < self.arrayLength:
            for idx in range(0, self.arrayLength, temp_runner * 2):
                firstArray = self.array[idx: idx + temp_runner]
                secondArray = self.array[idx +
                                         temp_runner: idx + temp_runner * 2]
                self.array[idx: idx + temp_runner *
                           2] = self.mergeRuns(firstArray, secondArray)
            temp_runner = self.__RUN * 2

        print(f"The sorted array is : {self.array}")

    def __repr__(self):
        return f"Array: {self.array}\nRUN: {self.__RUN}"


myArray = [randint(1, 100) for i in range(15)]
demo = TimSort(myArray)
print(demo)
demo.algorithm()
