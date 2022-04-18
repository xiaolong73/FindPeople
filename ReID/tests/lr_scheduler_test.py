import sys
import unittest

import torch
from torch import nn

sys.path.append('.')
from ReID.solver.lr_scheduler import WarmupMultiStepLR
from ReID.solver.build import make_optimizer
from ReID.config import cfg


class MyTestCase(unittest.TestCase):
    def test_something(self):
        net = nn.Linear(10, 10)
        optimizer = make_optimizer(cfg, net)
        lr_scheduler = WarmupMultiStepLR(optimizer, [20, 40], warmup_iters=10)
        for i in range(50):
            lr_scheduler.step()
            for j in range(3):
                print(i, lr_scheduler.get_lr()[0])
                optimizer.step()


if __name__ == '__main__':
    unittest.main()
