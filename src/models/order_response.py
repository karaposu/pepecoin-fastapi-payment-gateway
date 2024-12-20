# coding: utf-8

"""
    Pepecoin Payment Gateway API

    An API for processing Pepecoin payments, including order creation, payment monitoring, and status retrieval. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from models.transaction import Transaction
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderResponse(BaseModel):
    """
    OrderResponse
    """ # noqa: E501
    order_id: Optional[StrictStr] = Field(default=None, description="Unique identifier for the order")
    payment_address: Optional[StrictStr] = Field(default=None, description="Unique Pepecoin address for this order")
    amount_due: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Amount due in Pepecoin")
    amount_paid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Amount paid by the customer")
    status: Optional[StrictStr] = Field(default=None, description="Current status of the order")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp when the order was created")
    expires_at: Optional[datetime] = Field(default=None, description="Timestamp when the order expires")
    transactions: Optional[List[Transaction]] = Field(default=None, description="List of transactions associated with the order")
    order_metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Additional data associated with the order")
    __properties: ClassVar[List[str]] = ["order_id", "payment_address", "amount_due", "amount_paid", "status", "created_at", "expires_at", "transactions", "order_metadata"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Pending', 'Paid', 'Underpaid', 'Overpaid', 'Expired', 'Cancelled',):
            raise ValueError("must be one of enum values ('Pending', 'Paid', 'Underpaid', 'Overpaid', 'Expired', 'Cancelled')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OrderResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item in self.transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transactions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "order_id": obj.get("order_id"),
            "payment_address": obj.get("payment_address"),
            "amount_due": obj.get("amount_due"),
            "amount_paid": obj.get("amount_paid"),
            "status": obj.get("status"),
            "created_at": obj.get("created_at"),
            "expires_at": obj.get("expires_at"),
            "transactions": [Transaction.from_dict(_item) for _item in obj.get("transactions")] if obj.get("transactions") is not None else None,
            "order_metadata": obj.get("order_metadata")
        })
        return _obj


