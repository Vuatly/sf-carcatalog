from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.views.generic import ListView
from .models import Car

import logging

logger = logging.getLogger(__name__)


class CarsList(ListView):
    model = Car
    template_name = 'cars-list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        logger.debug(f"Request to CarsList from user: {self.request.user.id} with params: {self.request.GET}")
        logger.info("CarsList.get_queryset called")
        try:
            search_query = self.request.GET.get('search', '')
            qs = Car.objects.all()
            if search_query:
                qs = Car.objects.annotate(
                    search=SearchVector('model', 'manufacturer', 'color', 'release_year', 'transmission'),
                ).filter(search=search_query)
                if not qs:
                    logger.warning("Cars list is empty")
            return qs
        except Exception as exc:
            logger.error(str(exc))
            raise
