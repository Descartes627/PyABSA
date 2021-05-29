# -*- coding: utf-8 -*-
# file: run_apc.py
# time: 2021/5/26 0026
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.

########################################################################################################################
#                                  fine-tuning on custom dataset (w/o test dataset)                                    #
########################################################################################################################


from pyabsa import train_apc

param_dict = {'model_name': 'slide_lcfs_bert',  # {slide_lcfs_bert, slide_lcf_bert lcf_bert, lcfs_bert, bert_spc, bert_base}
              'batch_size': 16,
              'seed': 1,                        # you can use a set of random seeds to train multiple rounds
              # 'seed': 996,                    # or use one seed only
              'device': 'cuda',
              'num_epoch': 6,
              'optimizer': "adam",              # {adam, adamw}
              'learning_rate': 0.00002,
              'pretrained_bert_name': "bert-base-uncased",
              'use_dual_bert': False,           # modeling the local and global context using different BERTs
              'use_bert_spc': True,             # Enable to enhance APC, do not use this parameter in ATE or joint task of APC and APC
              'max_seq_len': 80,
              'log_step': 3,                    # Evaluate per steps
              'SRD': 3,                         # Distance threshold to calculate local context
              'eta': -1,                        # Eta is valid in [0,1]
              'sigma': 0.3,                     # Sigma is valid in [0,1]
              'lcf': "cdw",                     # {cdm, cdw}
              'window': "lr",                   # {lr, l, r}
              'dropout': 0,
              'l2reg': 0.00001,
              }

# see hyper-parameters in pyabsa/main/training_configs.py
param_dict = {'model_name': 'bert_base', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}
train_set_path = 'sum_train.dat'
# train_set_path = 'datasets/restaurant15'

save_path = 'state_dict'
sent_classifier = train_apc(parameter_dict=param_dict,  # set param_dict=None to use default model
                            dataset_path=train_set_path,  # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,  # evaluate model while training if test set is available
                            auto_device=True  # Auto choose CUDA or CPU
                            )

param_dict = {'model_name': 'bert_spc', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}
train_set_path = 'sum_train.dat'
save_path = 'state_dict'

sent_classifier = train_apc(parameter_dict=param_dict,  # set param_dict=None to use default model
                            dataset_path=train_set_path,  # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,  # evaluate model while training if test set is available
                            auto_device=True  # Auto choose CUDA or CPU
                            )

param_dict = {'model_name': 'lcf_bert', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}
train_set_path = 'sum_train.dat'
save_path = 'state_dict'

sent_classifier = train_apc(parameter_dict=param_dict,  # set param_dict=None to use default model
                            dataset_path=train_set_path,  # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,  # evaluate model while training if test set is available
                            auto_device=True  # Auto choose CUDA or CPU
                            )

param_dict = {'model_name': 'lcfs_bert', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}
train_set_path = 'sum_train.dat'
model_path_to_save = save_path

sent_classifier = train_apc(parameter_dict=param_dict,  # set param_dict=None to use default model
                            dataset_path=train_set_path,  # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,  # evaluate model while training if test set is available
                            auto_device=True  # Auto choose CUDA or CPU
                            )

param_dict = {'model_name': 'slide_lcf_bert', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}
train_set_path = 'sum_train.dat'
model_path_to_save = save_path

sent_classifier = train_apc(parameter_dict=param_dict,  # set param_dict=None to use default model
                            dataset_path=train_set_path,  # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,  # evaluate model while training if test set is available
                            auto_device=True  # Auto choose CUDA or CPU
                            )

param_dict = {'model_name': 'slide_lcfs_bert', 'batch_size': 16, 'device': 'cuda', 'num_epoch': 5}
train_set_path = 'datasets/restaurant15'
train_set_path = 'sum_train.dat'
model_path_to_save = save_path

sent_classifier = train_apc(parameter_dict=param_dict,  # set param_dict=None to use default model
                            dataset_path=train_set_path,  # file or dir, dataset(s) will be automatically detected
                            model_path_to_save=save_path,  # set model_path_to_save=None to avoid save model
                            auto_evaluate=False,  # evaluate model while training if test set is available
                            auto_device=True  # Auto choose CUDA or CPU
                            )