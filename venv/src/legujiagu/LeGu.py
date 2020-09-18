#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2019/9/10

__author__ = 'zzh'

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ms.v20180408 import ms_client, models

try:
    cred = credential.Credential("AKIDjTGsJapdq8QH8uqq56uSlpjWm0DPrTCn", "qY8nQvVGpwxoXMDvduAYkXCi50icK0TK")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ms.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ms_client.MsClient(cred, "13624", clientProfile)

    req = models.CreateResourceInstancesRequest()
    params = '{}'
    req.from_json_string(params)

    resp = client.CreateResourceInstances(req)
    print("成功了", resp.to_json_string())

except TencentCloudSDKException as err:
    print("失败了", err)
