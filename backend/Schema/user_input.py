from pydantic import BaseModel, computed_field, Field, field_validator
from typing import Annotated, Literal

class UserInput(BaseModel):
    company : Annotated[str, Field(..., description='Enter the name of the Company of laptop', example='Apple')]
    typename : Annotated[Literal['Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible', 'Workstation'], Field(..., description='Enter the kind of laptop you want', example='Notebook')]
    inches : Annotated[float, Field(..., gt=10, lt=19, description='Enter the size of the laptop you want', example=18.4)]
    ram_gb : Annotated[str, Field(..., description='Enter the RAM', example='8GB')]
    opsys: Annotated[Literal['macOS', 'No OS', 'Windows 10', 'Mac OS X', 'Linux', 'Android', 'Windows 10 S', 'Chrome OS', 'Windows 7'], Field(..., description='Enter Operating System', example='Windows 10')]
    resolution : Annotated[str, Field(..., description='Enter screen size', example='1280x720')]
    touchscreen: Annotated[bool, Field(..., description='Enter if the laptop is touchscreen')]
    memory: Annotated[Literal['SSD', 'HDD', 'Flash Drive'], Field(..., description='Type of memory')]
    cpu_brand : Annotated[Literal['Intel', 'AMD', 'Samsung'], Field(..., description='Enter the brand of the CPU')]
    gpu_brand : Annotated[Literal['Intel', 'AMD', 'Nvidia', 'ARM'], Field(..., description='Enter the brand of GPU')]

    @computed_field
    @property
    def ram(self) -> int:
        ram = self.ram_gb.replace('GB', '')
        return int(ram)
    
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
        if self.touchscreen == True:
            return 1
        else:
            return 0
        
    @computed_field
    @property
    def has_ssd(self) -> int:
        if self.memory == 'SSD':
            return 1
        else:
            return 0
        
    @computed_field
    @property
    def has_hdd(self) -> int:
        if self.memory == 'HDD':
            return 1
        else:
            return 0
        
    @computed_field
    @property
    def has_flash(self) -> int:
        if self.memory == 'Flash Drive':
            return 1
        else:
            return 0