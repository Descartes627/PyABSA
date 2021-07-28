# -*- coding: utf-8 -*-
# file: lcf_atepc_benchmark.py
# time: 2021/6/8 0008
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.

from pyabsa import train_atepc, atepc_config_handler

from pyabsa import ABSADatasetList
from pyabsa.model_utils import ATEPCModelList

import copy


def run_lcf_atepc_cdw(param_dict=None):
    if not param_dict:
        print('No optimal hyper-parameters are set, using default params...')
        _atepc_param_dict_english = copy.deepcopy(atepc_config_handler.get_atepc_param_dict_english())
        _atepc_param_dict_english['model'] = ATEPCModelList.LCF_ATEPC
        _atepc_param_dict_english['lcf'] = 'cdw'
        _atepc_param_dict_english['log_step'] = 10
        _atepc_param_dict_english['evaluate_begin'] = 2
    else:
        _atepc_param_dict_english = param_dict

    train_atepc(dataset_path=ABSADatasetList.Laptop14,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Restaurant14,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Restaurant15,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Restaurant16,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Phone,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Car,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Camera,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Notebook,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )


def run_lcf_atepc_cdm(param_dict=None):
    if not param_dict:
        print('No optimal hyper-parameters are set, using default params...')
        _atepc_param_dict_english = copy.deepcopy(atepc_config_handler.get_atepc_param_dict_english())
        _atepc_param_dict_english['model'] = ATEPCModelList.LCF_ATEPC
        _atepc_param_dict_english['lcf'] = 'cdm'
        _atepc_param_dict_english['log_step'] = 10
        _atepc_param_dict_english['evaluate_begin'] = 2
    else:
        _atepc_param_dict_english = param_dict

    train_atepc(dataset_path=ABSADatasetList.Laptop14,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Restaurant14,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Restaurant15,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Restaurant16,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Phone,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Car,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Camera,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )

    train_atepc(dataset_path=ABSADatasetList.Notebook,
                parameter_dict=_atepc_param_dict_english,  # set param_dict=None will use the apc_param_dict as well
                auto_evaluate=True,  # evaluate model while training_tutorials if test set is available
                auto_device=True  # automatic choose CUDA or CPU
                )
