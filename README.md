# Waitress

## Overview

This repository serves as the code hub for the waitress package used within the Ultra Horizon launchpad PPAs.

This repository was built because the default waitress version on bionic is 1.0.1 which has severe Linux bugs.
To eliminate issues with UH VPN Server (uses waitress) we have compiled our own python3-waitress package to rectify issues.

If using outside UH VPN, please use at your own risk, we provide no guarantees about the stability of this software.

## Installation

Execute the commands below to install the package:

1. `sudo add-apt-repository ppa:ultrahorizon/ppa`
2. `sudo apt-get update`
3. `sudo apt-get install python3-waitress`
