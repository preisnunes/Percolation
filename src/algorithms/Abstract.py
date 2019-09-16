class Abstract:

    def connected(self, p :int, q :int):
        raise NotImplementedError()

    def union(self, p :int, q :int):
        raise NotImplementedError()

    def setNumberOfItems(self, numberOfItems :int = 0):
        raise NotImplementedError()