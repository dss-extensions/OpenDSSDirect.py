from ._utils import api_util, Base


class IDSSimComs(Base):
    __slots__ = []
    __name__ = "DSSimComs"
    _api_prefix = "DSSimComs"
    _columns = []

    def BusVoltage(self, Index):
        self.CheckForError(self._lib.DSSimComs_BusVoltage_GR(Index))
        return self._get_float64_gr_array()

    def BusVoltagepu(self, Index):
        self.CheckForError(self._lib.DSSimComs_BusVoltagepu_GR(Index))
        return self._get_float64_gr_array()


_DSSimComs = IDSSimComs(api_util)

# For backwards compatibility, bind to the default instance
BusVoltage = _DSSimComs.BusVoltage
BusVoltagepu = _DSSimComs.BusVoltagepu
_columns = _DSSimComs._columns
__all__ = ["BusVoltage", "BusVoltagepu"]
