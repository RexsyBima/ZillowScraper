def rent(p_bed_baths_sqft_loc_rent):
    try:
        item = p_bed_baths_sqft_loc_rent.find(
            "div", class_="styles__StyledPersonalizedPaymentWrapper-sc-t2ntu2-1"
        ).div.span.getText()
        return item
    except AttributeError:
        return None
