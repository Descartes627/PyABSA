# -*- coding: utf-8 -*-
# file: train_apc_without_test_set.py
# time: 2021/5/26 0026
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.

########################################################################################################################
#                    train and evaluate on your own apc_datasets (need train and test apc_datasets)                    #
#              your custom dataset should have the continue polarity labels like [0,N-1] for N categories              #
########################################################################################################################

from pyabsa import train_apc

from pyabsa import ABSADatasetList

param_dict = {'model_name': 'bert_base', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}

multilingual = ABSADatasetList.Multilingual
save_path = 'state_dict'
sent_classifier = train_apc(parameter_dict=param_dict,     # set param_dict=None to use default model
                            dataset_path=multilingual,   # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,           # evaluate model while training_tutorials if test set is available
                            auto_device=True               # Auto choose CUDA or CPU
                            )

param_dict = {'model_name': 'bert_spc', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}

sent_classifier = train_apc(parameter_dict=param_dict,     # set param_dict=None to use default model
                            dataset_path=multilingual,   # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,           # evaluate model while training_tutorials if test set is available
                            auto_device=True               # Auto choose CUDA or CPU
                            )

param_dict = {'model_name': 'lcf_bert', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}

sent_classifier = train_apc(parameter_dict=param_dict,     # set param_dict=None to use default model
                            dataset_path=multilingual,   # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,           # evaluate model while training_tutorials if test set is available
                            auto_device=True               # Auto choose CUDA or CPU
                            )

param_dict = {'model_name': 'lcfs_bert', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}

sent_classifier = train_apc(parameter_dict=param_dict,     # set param_dict=None to use default model
                            dataset_path=multilingual,   # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,           # evaluate model while training_tutorials if test set is available
                            auto_device=True               # Auto choose CUDA or CPU
                            )

param_dict = {'model_name': 'slide_lcf_bert', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}

sent_classifier = train_apc(parameter_dict=param_dict,     # set param_dict=None to use default model
                            dataset_path=multilingual,   # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,           # evaluate model while training_tutorials if test set is available
                            auto_device=True               # Auto choose CUDA or CPU
                            )

param_dict = {'model_name': 'slide_lcfs_bert', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}

sent_classifier = train_apc(parameter_dict=param_dict,     # set param_dict=None to use default model
                            dataset_path=multilingual,   # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,           # evaluate model while training_tutorials if test set is available
                            auto_device=True               # Auto choose CUDA or CPU
                            )
