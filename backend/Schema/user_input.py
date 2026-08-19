from pydantic import BaseModel, computed_field, Field
from typing import Annotated, Literal


class UserInput(BaseModel):

    company: Annotated[
        str,
        Field(
            ...,
            description='Enter the laptop company',
            example='Apple'
        )
    ]

    product: Annotated[
        str,
        Field(
            ...,
            description='Enter the laptop model/product name',
            example='MacBook Pro'
        )
    ]

    typename: Annotated[
        Literal[
            'Ultrabook',
            'Notebook',
            'Netbook',
            'Gaming',
            '2 in 1 Convertible',
            'Workstation'
        ],
        Field(
            ...,
            description='Enter the type of laptop',
            example='Notebook'
        )
    ]

    inches: Annotated[
        float,
        Field(
            ...,
            gt=10,
            lt=19,
            description='Enter the screen size in inches',
            example=15.6
        )
    ]

    ram_gb: Annotated[
        int,
        Field(
            ...,
            gt=0,
            le=64,
            description='Enter RAM in GB',
            example=8
        )
    ]

    opsys: Annotated[
        Literal[
            'macOS',
            'No OS',
            'Windows 10',
            'Mac OS X',
            'Linux',
            'Android',
            'Windows 10 S',
            'Chrome OS',
            'Windows 7'
        ],
        Field(
            ...,
            description='Enter Operating System',
            example='Windows 10'
        )
    ]

    # -------------------------
    # Storage
    # -------------------------

    ssd_gb: Annotated[
        float,
        Field(
            ...,
            ge=0,
            description='SSD capacity in GB',
            example=256
        )
    ]

    hdd_gb: Annotated[
        float,
        Field(
            ...,
            ge=0,
            description='HDD capacity in GB',
            example=1024
        )
    ]

    flash_gb: Annotated[
        float,
        Field(
            ...,
            ge=0,
            description='Flash storage capacity in GB',
            example=0
        )
    ]

    hybrid_gb: Annotated[
        float,
        Field(
            ...,
            ge=0,
            description='Hybrid storage capacity in GB',
            example=0
        )
    ]

    # -------------------------
    # CPU
    # -------------------------

    cpu_speed_ghz: Annotated[
        float,
        Field(
            ...,
            gt=0,
            lt=6,
            description='CPU clock speed in GHz',
            example=2.5
        )
    ]

    cpu_family: Annotated[
        str,
        Field(
            ...,
            description='CPU family',
            example='Core i5'
        )
    ]

    cpu_brand: Annotated[
        Literal[
            'Intel',
            'AMD',
            'Samsung'
        ],
        Field(
            ...,
            description='CPU manufacturer',
            example='Intel'
        )
    ]

    # -------------------------
    # GPU
    # -------------------------

    gpu_brand: Annotated[
        Literal[
            'Intel',
            'AMD',
            'Nvidia',
            'ARM'
        ],
        Field(
            ...,
            description='GPU manufacturer',
            example='Nvidia'
        )
    ]

    # -------------------------
    # Display
    # -------------------------

    resolution: Annotated[
        str,
        Field(
            ...,
            description='Screen resolution',
            example='1920x1080'
        )
    ]

    touchscreen: Annotated[
        bool,
        Field(
            ...,
            description='Whether the laptop has a touchscreen',
            example=False
        )
    ]

    # -------------------------
    # Computed features
    # -------------------------

    @computed_field
    @property
    def res_width(self) -> int:
        return int(self.resolution.split('x')[0])

    @computed_field
    @property
    def res_height(self) -> int:
        return int(self.resolution.split('x')[1])

    @computed_field
    @property
    def is_touchscreen(self) -> int:
        return int(self.touchscreen)