from django.conf import settings


def tienda_context(_request):
    """Provide site-wide store metadata."""
    tienda = getattr(settings, 'STORE_NAME', 'TecnoPunto')
    descripcion = getattr(
        settings,
        'STORE_DESCRIPTION',
        'TecnoPunto es tu aliado en soluciones tecnológicas para el aula y la oficina.'
    )
    return {
        'tienda': tienda,
        'descripcion': descripcion,
    }
