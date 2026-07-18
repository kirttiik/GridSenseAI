from app.etl.base.base_pipeline import BasePipeline
from app.etl.extractors.demand_extractor import DemandExtractor
from app.etl.loaders.demand_loader import DemandLoader
from app.etl.registry import register_pipeline
from app.etl.transformers.demand_transformer import DemandTransformer
from app.etl.validators.demand_validator import DemandValidator

DATASET_NAME = "GRID_INDIA_DEMAND"


@register_pipeline(DATASET_NAME)
class DemandPipeline(BasePipeline):
    def __init__(self):
        super().__init__(
            dataset_name=DATASET_NAME,
            extractor=DemandExtractor(dataset_id=DATASET_NAME),
            validator=DemandValidator(),
            transformer=DemandTransformer(),
            loader=DemandLoader(),
        )
