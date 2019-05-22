import abc


class GeoSnService(abc.ABC):
    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def create(self, indicator, file_path=None):
        pass

    @abc.abstractmethod
    def delete(self, file_path=None):
        pass
