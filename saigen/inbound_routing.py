#!/usr/bin/python3

import sys

from saigen.confbase import *
from saigen.confutils import *


class InboundRouting(ConfBase):

    def __init__(self, params={}):
        super().__init__(params)

    def items(self):
        self.numYields = 0
        print('  Generating InboundRouting ...', file=sys.stderr)
        p = self.params
        cp = self.cooked_params
        vm_underlay_dip = ipaddress.ip_address(p.PAL)

        for eni_index, eni in enumerate(range(p.ENI_START, p.ENI_START + p.ENI_COUNT)):
            vm_underlay_dip = vm_underlay_dip + int(ipaddress.ip_address(p.IP_STEP1))

            self.numYields += 1
            vnet_data = {
                'name': 'vnet#%d' % eni_index,
                "type": "SAI_OBJECT_TYPE_VNET",
                "attributes": {
                    "SAI_VNET_ATTR_VNI": "DIR_LOOKUP_ENI",
                },
                "OP": "create",
            }

            yield vnet_data


if __name__ == '__main__':
    conf = InboundRouting()
    common_main(conf)
