from django import template
import logging

logger = logging.getLogger(__name__)
register = template.Library()

@register.filter
def get_star_range(rating):
    logger.debug(f"Rating: {rating}")
    star_range = range(int(rating))
    logger.debug(f"Star Range: {star_range}")
    return star_range