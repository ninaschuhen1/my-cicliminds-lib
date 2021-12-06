from cicliminds_lib.query.datasets import get_datasets_for_block
from cicliminds_lib.unify.datasets.merge import get_merged_dataset
from cicliminds_lib.unify.model_weights import get_merged_model_weights


def get_merged_dataset_by_query(datasets_reg, query):
    filtered_datasets_reg = get_datasets_for_block(datasets_reg, query)
    dataset = get_merged_dataset(filtered_datasets_reg, query["scenario"])
    return dataset


def get_merged_model_weights_by_query(model_weights_reg, query):
    dataset = get_merged_model_weights(model_weights_reg, query.get("model_weights"))
    return dataset
