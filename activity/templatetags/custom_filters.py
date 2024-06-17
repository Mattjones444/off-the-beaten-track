from django import template
import logging

logger = logging.getLogger(__name__)
register = template.Library()

@register.filter
def get_star_range(rating):
    try:
        logger.debug(f"Rating: {rating}")
        star_range = range(int(rating) if rating is not None else 0)
        logger.debug(f"Star Range: {star_range}")
        return star_range
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid rating value: {rating} - {e}")
        return range(0)