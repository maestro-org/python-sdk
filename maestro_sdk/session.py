from .handlers.general import General

class MaestroSession():
    def __init__(self, network: str, api_key: str, version: str = "v0") -> None:
        if not network:
            raise Exception("Network not specified. Use 'preview', 'preprod, or 'mainnet'.")
        self.network = network
        self.api_key = api_key
        self.version = version
        self.base_url = f"https://{self.network}.gomaestro-api.org/{self.version}"

        self.general = General()

    def accounts(self):
        self

    def addresses(self):
        pass

    def assets(self):
        pass

    def datum(self):
        pass

    def epochs(self):
        pass

    def pools(self):
        pass

    def scripts(self):
        pass

    def transactions(self):
        pass

    def submit(self):
        pass

    def txmanager(self):
        pass

if __name__ == "__main__": 
    maestro = MaestroSession("mainnet", "opIqovS7Xdp4o876Ml7c4cbwvm7cETgV")
    chain_tip = maestro.general.chain_tip(maestro)
