from .request import get_request
from dataclasses import dataclass
from dacite import from_dict


@dataclass
class ChainTip:
    block_hash: str
    slot: int
    height: int

class General():
    def chain_tip(self, maestro_session):
        resp = get_request(maestro_session, "chain-tip")
        return from_dict(data_class=ChainTip, data=resp)
        
    def era_history(self):
        pass

    def protocol_params(self):
        pass

    def system_start(self):
        pass
