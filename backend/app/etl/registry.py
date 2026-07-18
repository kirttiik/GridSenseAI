import logging

from app.etl.base.base_pipeline import BasePipeline

logger = logging.getLogger(__name__)


class PipelineRegistry:
    """
    Registry linking dataset names to their respective ETL pipelines.
    """

    _registry: dict[str, type[BasePipeline]] = {}

    @classmethod
    def register(cls, dataset_name: str, pipeline_class: type[BasePipeline]) -> None:
        """Register a pipeline class for a dataset."""
        cls._registry[dataset_name] = pipeline_class
        logger.debug(f"Registered pipeline {pipeline_class.__name__} for dataset {dataset_name}")

    @classmethod
    def get_pipeline(cls, dataset_name: str) -> type[BasePipeline]:
        """Get the pipeline class for a dataset."""
        pipeline_class = cls._registry.get(dataset_name)
        if not pipeline_class:
            raise KeyError(f"No pipeline registered for dataset: {dataset_name}")
        return pipeline_class

    @classmethod
    def list_datasets(cls) -> list[str]:
        """List all registered dataset names."""
        return list(cls._registry.keys())


# Decorator for easy registration
def register_pipeline(dataset_name: str):
    def wrapper(pipeline_class: type[BasePipeline]):
        PipelineRegistry.register(dataset_name, pipeline_class)
        return pipeline_class

    return wrapper
