# -*- coding: utf-8 -*-
# file: atepc_param_search.py
# time: 2021/6/13 0013
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.

import copy

from pyabsa import ABSADatasets, detect_dataset
from pyabsa.functional import init_config

from pyabsa.config.atepc_config import atepc_config_handler

from pyabsa.tasks.atepc.training.atepc_trainer import train4atepc

from pyabsa.utils.logger import get_logger


def atepc_param_search(parameter_dict=None,
                       dataset_path=None,
                       search_param: list = None,
                       auto_evaluate=True,
                       auto_device=True):
    logger = get_logger('param_search_logs', 'param_search_{}'.format(search_param[0]), 'optimal_param')

    if not isinstance(dataset_path, list):
        dataset_path = [dataset_path]
        logger.info('Search on Datasets: {}'.format(dataset_path))
        logger.info('Search with random seed: {1, 2, 3}')
        logger.info('Alternative param to test:')
        logger.info(search_param)

    optimal_param = 'None'
    max_score = 0
    for alternative in search_param[1]:
        parameter_dict[search_param[0]] = alternative
        logger.info('*********************** Set {} = {} ***********************'.format(search_param[0], alternative))
        score = 0
        for dataset in dataset_path:
            dataset_file = detect_dataset(dataset, auto_evaluate, task='atepc_benchmark')
            config = init_config(parameter_dict, atepc_config_handler.get_atepc_param_dict_base(), auto_device)
            config.logger = logger
            config.dataset_path = dataset
            config.model_path_to_save = None
            config.dataset_file = dataset_file
            config.dataset_path = dataset
            config.seed = [1, 2, 3]
            for _, s in enumerate(config.seed):
                t_config = copy.deepcopy(config)
                t_config.seed = s
                running_result = train4atepc(t_config, logger)
                score += (running_result[3] + running_result[4] + running_result[5])
        logger.info('{}: {} tested on dataset {} scored: {}'.format(search_param[0],
                                                                    alternative,
                                                                    ','.join(dataset_path),
                                                                    score))
        print()
        if score > max_score:
            max_score = score
            optimal_param = alternative
    logger.info('*' * 100)
    logger.info('Optimal {} tested on dataset(s) {} is {}'.format(search_param[0],
                                                                  ','.join(dataset_path),
                                                                  optimal_param))
    logger.info('*' * 100)
    print()

    return optimal_param
