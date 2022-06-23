from typing import Dict, Optional

from pydantic import BaseModel, validator


class Product(BaseModel):
    name: str
    description: str
    params: Optional[Dict[str, str]]

    class Config:
        min_anystr_length = 1
        max_anystr_length = 250
        error_msg_templates = {
            'value_error.any_str.min_length': 'min_length:{limit_value}',
            'value_error.any_str.max_length': 'max_length:{limit_value}',
        }

    @validator('name', 'description')
    def is_space_value(cls, value):
        if value.isspace():
            raise ValueError('Value must not be a space')
        return value

    @validator('params')
    def is_space_values(cls, value_dict):
        if value_dict:
            for key, value in value_dict.items():
                if key.isspace():
                    raise ValueError('Key must not be a space')
                if value.isspace():
                    raise ValueError('Value must not be a space')
        return value_dict
