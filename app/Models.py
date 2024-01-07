from pydantic import BaseModel


class House(BaseModel):
    location: str | None = None  #
    price: int | None = None  #
    zest: int | None = None  # zillow estimate
    beds: int | None = None  #
    baths: int | None = None  #
    area: int | None = None  #
    rent: int | None = None  # rent/month
    type_: str | None = None  # house type
    built: int | None = None  # year built
    lot: int | None = None  # lot area
    psqft: int | None = None  # price/squarefeet
    hoa: int | None = None  # house of association
    features: list[str] | None = None  #
    description: str | None = None  #
    live: int | None = None  # how long has a house been in zillow
    views: int | None = None  # how many viewers
    saves: int | None = None  # how many viewers has save this house
    zlastcheck: str | None = None  # how long has it been to zillow to check this item
    updated: str | None = None  # when this house has been recently updated
    lister: str | None = None  # who create this listing
    source: str | None = None  # source of the listing
    Origin_MLS: str | None = None  # Origin of the MLS
