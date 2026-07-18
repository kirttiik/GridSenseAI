import enum


class EnvironmentType(str, enum.Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"

    @property
    def is_development(self) -> bool:
        return self == self.DEVELOPMENT

    @property
    def is_testing(self) -> bool:
        return self == self.TESTING

    @property
    def is_staging(self) -> bool:
        return self == self.STAGING

    @property
    def is_production(self) -> bool:
        return self == self.PRODUCTION
