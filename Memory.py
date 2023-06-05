from pymem import Pymem

procID = Pymem("ac_client.exe")
module_base_address = procID.base_address
