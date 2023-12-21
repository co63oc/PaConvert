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

import textwrap

from apibase import APIBase

obj = APIBase("torch.hub.help")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.hub.help('lyuwenyu/paddlehub_demo:main', model='MM')
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.hub.help('lyuwenyu/paddlehub_demo:main', model='MM', skip_validation=False)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.hub.help(github='lyuwenyu/paddlehub_demo:main', model='MM', force_reload=False, skip_validation=False, trust_repo=None)
        """
    )
    obj.run(pytorch_code, ["result"])


# generated by validate_unittest autofix, based on test_case_3
def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.hub.help('lyuwenyu/paddlehub_demo:main', 'MM', False, False, None)
        """
    )
    obj.run(pytorch_code, ["result"])


# generated by validate_unittest autofix, based on test_case_3
def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.hub.help(trust_repo=None, skip_validation=False, force_reload=False, model='MM', github='lyuwenyu/paddlehub_demo:main')
        """
    )
    obj.run(pytorch_code, ["result"])


# generated by validate_unittest autofix, based on test_case_3
def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.hub.help('lyuwenyu/paddlehub_demo:main', 'MM')
        """
    )
    obj.run(pytorch_code, ["result"])
