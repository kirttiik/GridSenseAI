from app.etl.base.base_pipeline import BasePipeline
from app.etl.extractors.generation_extractor import GenerationExtractor
from app.etl.loaders.generation_loader import GenerationLoader
from app.etl.registry import register_pipeline
from app.etl.transformers.generation_transformer import GenerationTransformer
from app.etl.validators.generation_validator import GenerationValidator

DATASET_NAME = "GRID_INDIA_GENERATION"


@register_pipeline(DATASET_NAME)
class GenerationPipeline(BasePipeline):
    def __init__(self):
        super().__init__(
            dataset_name=DATASET_NAME,
            extractor=GenerationExtractor(dataset_id=DATASET_NAME),
            validator=GenerationValidator(),
            transformer=GenerationTransformer(),
            loader=GenerationLoader(),
        )
