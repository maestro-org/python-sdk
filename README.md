<p align="center">
  <a href="https://www.gomaestro.org/">
    <img src="https://www.gomaestro.org/logos/LandingLogos/DarkLogo.svg" alt="Maestro Logo" width="425" />
  </a>
  <h2 align="center">Python SDK for the <a href="https://www.gomaestro.org/">Maestro</a> Dapp Platform</h2>
  <p align="center">
    <a href="https://python-sdk.gomaestro.org/">
      <img src="https://img.shields.io/badge/-RTD-5E5184?style=flat-square&logo=python&logoColor=white" />
    </a>
    <a href="https://docs.gomaestro.org/docs/intro">
      <img src="https://img.shields.io/badge/-Docs-blue?style=flat-square&logo=semantic-scholar&logoColor=white" />
    </a>
    <a href="https://github.com/maestro-org/python-sdk/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/maestro-org/python-sdk?style=flat-square&label=License" />
    </a>
    <a href="https://github.com/maestro-org/python-sdk/actions/workflows/build.yml?query=branch%3Amain">
      <img src="https://img.shields.io/github/actions/workflow/status/maestro-org/python-sdk/build.yml?style=flat-square&branch=main&label=Build" />
    </a>
    <a href="./CONTRIBUTING.md">
      <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" />
    </a>
    <a href="https://twitter.com/GoMaestroOrg">
      <img src="https://img.shields.io/badge/-%40GoMaestroOrg-F3F1EF?style=flat-square&logo=twitter&logoColor=1D9BF0" />
    </a>
    <a href="https://discord.gg/ES2rDhBJt3">
      <img src="https://img.shields.io/badge/-Discord-414EEC?style=flat-square&logo=discord&logoColor=white" />
    </a>
  </p>
</p>

# Getting Started
1. [TODO] Install `maestro-sdk` package
```
# pip
pip install maestro-sdk

# poetry
poetry add maestro-sdk
```

2. Create a [Maestro API key](https://docs.gomaestro.org/Getting-started/Sign-up-login).
3. [TODO] Import the package
```python
from maestro_sdk import MaestroSession
```

## Local Development
1. Get [poetry](https://python-poetry.org/docs/#installation)
2. Install package: `poetry install`
3. Lock dependencies: `poetry lock`
4. Run Python shell: `poetry run python`
```bash
>>> from maestro_sdk import MaestroSession
>>> maestro = MaestroSession("mainnet", "<API_KEY>")
>>> chain_tip = maestro.general.chain_tip(maestro)
>>> chain_tip
ChainTip(block_hash='7ed2439755445de6c42984de49c15b0a13326da8a5666e8050cf39fbfd295a7c', slot=94249308, height=8857750)
```

# Documentation
* [Maestro public docs](https://docs.gomaestro.org/)
* [Maestro API reference](https://docs.gomaestro.org/maestro-api-introduction)

# Contributing

Meastro welcomes all contributors! Please see our [contributing guidelines](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md).
