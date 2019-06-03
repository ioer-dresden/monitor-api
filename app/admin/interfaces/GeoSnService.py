import abc


class GeoSnService(abc.ABC):
    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def create(self, indicator):
        pass

    @abc.abstractmethod
    def delete(self):
        pass
