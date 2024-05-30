from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from .blocks import BannerBlock, AboutSectionBlock, TeamCarouselBlock, CallToActionBlock, AltCallToActionBlock, UpcomingEventsBlock

class HomePage(Page):
    body = StreamField([
        ('banner', BannerBlock()),
        ('about_section', AboutSectionBlock()),
        ('team_carousel', TeamCarouselBlock()),
        ('call_to_action', CallToActionBlock()),
        ('alternate_call_to_action', AltCallToActionBlock()),
        ('upcoming_events', UpcomingEventsBlock()),
        # Add other blocks here
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
