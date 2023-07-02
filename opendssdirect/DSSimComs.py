from ._utils import api_util, Base


class IDSSimComs(Base):
    __slots__ = []
    __name__ = "DSSimComs"
    _api_prefix = "DSSimComs"
    _columns = []

    def BusVoltage(self, Index):
        return self.CheckForError(
            self._get_float64_array(self._lib.DSSimComs_BusVoltage, Index)
        )

    def BusVoltagepu(self, Index):
        return self.CheckForError(
            self._get_float64_array(self._lib.DSSimComs_BusVoltagepu, Index)
        )


_DSSimComs = IDSSimComs(api_util)

# For backwards compatibility, bind to the default instance
BusVoltage = _DSSimComs.BusVoltage
BusVoltagepu = _DSSimComs.BusVoltagepu
_columns = _DSSimComs._columns
__all__ = ["BusVoltage", "BusVoltagepu"]
