# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os

import numpy as np
import torch
import torch.distributed as dist
from torch.utils.data import Dataset, DistributedSampler

dist.init_process_group(backend="nccl")
rank = dist.get_rank()
torch.cuda.set_device(rank)


class RandomDataset(Dataset):
    def __init__(self, num_samples):
        self.num_samples = num_samples

    def __getitem__(self, idx):
        image = np.random.random([16]).astype("float32")
        label = np.random.randint(0, 9, (1,)).astype("int64")
        return image, label

    def __len__(self):
        return self.num_samples


dataset = RandomDataset(16)
sampler = DistributedSampler(
    dataset=dataset,
    num_replicas=None,
    rank=None,
    shuffle=False,
    seed=0,
    drop_last=False,
)

data = [i for i in sampler]
data = torch.tensor(data).squeeze()
if rank == 0:
    print(data)
    torch.save(data, os.environ["DUMP_FILE"])
