from app.models.assets.power_plant import PowerPlant
from app.repositories.base.unit_of_work import UnitOfWork
from app.seeders.base import BaseSeeder


class SampleAssetsSeeder(BaseSeeder):
    @property
    def name(self) -> str:
        return "Sample Assets Seeder"

    @property
    def priority(self) -> int:
        return 40

    @property
    def environments(self) -> list[str]:
        return ["development"]

    async def execute(self, uow: UnitOfWork) -> None:
        # Check if already seeded
        count = await uow.assets.power_plant.count()
        if count > 0:
            return  # Skip if already seeded

        # Fetch lookups
        states = await uow.reference.state.get_all()
        fuel_types = await uow.reference.fuel_type.get_all()
        operators = await uow.reference.operator.get_all()

        state_map = {s.name: s.id for s in states}
        fuel_map = {f.name: f.id for f in fuel_types}
        op_map = {o.name: o.id for o in operators}

        plants_data = [
            {
                "name": "Vindhyachal Super Thermal Power Station",
                "state_id": state_map.get("Madhya Pradesh"),
                "fuel_type_id": fuel_map.get("Coal"),
                "operator_id": op_map.get("NTPC Limited"),
                "installed_capacity_mw": 4760.00,
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Mundra Thermal Power Station",
                "state_id": state_map.get("Gujarat"),
                "fuel_type_id": fuel_map.get("Coal"),
                "operator_id": op_map.get("Adani Power"),
                "installed_capacity_mw": 4620.00,
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Bhadla Solar Park",
                "state_id": state_map.get("Rajasthan"),
                "fuel_type_id": fuel_map.get("Solar"),
                "operator_id": op_map.get("NTPC Limited"),  # Simplified
                "installed_capacity_mw": 2245.00,
                "created_by": "system",
                "updated_by": "system",
            },
        ]

        plants = []
        for p in plants_data:
            if p["state_id"] and p["fuel_type_id"] and p["operator_id"]:
                plants.append(PowerPlant(**p))

        if plants:
            await uow.assets.power_plant.bulk_create(plants)
