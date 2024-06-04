from wagtail.core import blocks

from wagtail.images.blocks import ImageChooserBlock

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel

from django.db import models
class AboutPage(Page):
    template = "home/about_page.html"
    
    banner_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )
    about_section = StreamField([
        ('content', blocks.StructBlock([
            ('subtitle', blocks.CharBlock(required=True)),
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
            ('button_text', blocks.CharBlock(required=False, null=True, blank=True)),
            ('button_link', blocks.URLBlock(required=False, null=True, blank=True)),
            ('image_1', ImageChooserBlock(required=True)),
            ('image_2', ImageChooserBlock(required=True)),
        ]))
    ], null=True, blank=True)

    about_section_features = StreamField([
        ('feature', blocks.StructBlock([
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
        ]))
    ], null=True, blank=True)

    what_we_do_section = StreamField([
        ('content', blocks.StructBlock([
            ('background_image', ImageChooserBlock(required=True)),
            ('subtitle', blocks.CharBlock(required=True)),
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
        ])),
        ('services', blocks.ListBlock(blocks.StructBlock([
            ('icon', blocks.CharBlock(required=True)),
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
        ])))
    ], null=True, blank=True)

    team_section = StreamField([
        ('content', blocks.StructBlock([
            ('subtitle', blocks.CharBlock(required=True)),
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
        ])),
        ('team_members', blocks.ListBlock(blocks.StructBlock([
            ('name', blocks.CharBlock(required=True)),
            ('designation', blocks.CharBlock(required=True)),
            ('image', ImageChooserBlock(required=True)),
            ('facebook', blocks.URLBlock(required=False)),
            ('twitter', blocks.URLBlock(required=False)),
            ('linkedin', blocks.URLBlock(required=False)),
        ])))
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('banner_image'),
        StreamFieldPanel('about_section'),
        StreamFieldPanel('about_section_features'),
        StreamFieldPanel('what_we_do_section'),
        StreamFieldPanel('team_section'),
    ]

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"


class HomePage(Page):
    template = "home/home_page.html"

    banner_section = StreamField([
        ('banner', blocks.StructBlock([
            ('background_image', ImageChooserBlock(required=True)),
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
            ('button_text', blocks.CharBlock(required=True)),
            ('button_link', blocks.URLBlock(required=True))
        ]))
    ], null=True, blank=True)

    about_section_feature = StreamField([
        ('feature', blocks.StructBlock([
            ('icon', blocks.CharBlock(required=True)),
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
            ('background_image', ImageChooserBlock(required=True)),
        ])),
    ], null=True, blank=True)

    about_section_content = StreamField([
            ('about_content', blocks.StructBlock([
            ('title', blocks.CharBlock(required=True)),
            ('subtitle', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
            ('button_text', blocks.CharBlock(required=True)),
            ('button_link', blocks.URLBlock(required=True)),
            ('image_1', ImageChooserBlock(required=True)),
            ('image_2', ImageChooserBlock(required=True))
        ]))], null=True, blank=True)

    what_we_do_section = StreamField([
        ('content', blocks.StructBlock([
            ('background_image', ImageChooserBlock(required=True)),
            ('subtitle', blocks.CharBlock(required=True)),
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
        ]))
    ], null=True, blank=True)

    services = StreamField([
        ('service', blocks.StructBlock([
            ('icon', blocks.CharBlock(required=True)),
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True))
        ]))
    ], null=True, blank=True)

    how_it_works_subtitle = models.CharField(max_length=255, blank=True, null=True)
    how_it_works_title = models.CharField(max_length=255, blank=True, null=True)
    how_it_works_description = models.TextField(blank=True, null=True)
    
    how_it_works_processes = StreamField([
        ('process', blocks.StructBlock([
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
            ('link_text', blocks.CharBlock(required=True)),
            ('link_url', blocks.URLBlock(required=True)),
            ('image', ImageChooserBlock(required=True)),
        ])),
    ], null=True, blank=True)

    team_section = StreamField([
        ('content', blocks.StructBlock([
            ('subtitle', blocks.CharBlock(required=True)),
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True))
        ])),
        ('team_members', blocks.ListBlock(blocks.StructBlock([
            ('name', blocks.CharBlock(required=True)),
            ('designation', blocks.CharBlock(required=True)),
            ('image', ImageChooserBlock(required=True)),
            ('facebook', blocks.URLBlock(required=False)),
            ('twitter', blocks.URLBlock(required=False)),
            ('linkedin', blocks.URLBlock(required=False))
        ])))
    ], null=True, blank=True)

    call_to_action = StreamField([
        ('content', blocks.StructBlock([
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
            ('button_text', blocks.CharBlock(required=True)),
            ('button_link', blocks.URLBlock(required=True)),
            ('background_image', ImageChooserBlock(required=True))
        ]))
    ], null=True, blank=True)

    upcoming_events = StreamField([
        ('content', blocks.StructBlock([
            ('subtitle', blocks.CharBlock(required=True)),
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
        ])),
        ('event', blocks.StructBlock([
            ('title', blocks.CharBlock(required=True)),
            ('image', ImageChooserBlock(required=True)),
            ('time', blocks.CharBlock(required=True)),
            ('location', blocks.CharBlock(required=True)),
            ('button_text', blocks.CharBlock(required=True)),
            ('button_link', blocks.URLBlock(required=True)),
        ]))
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('banner_section'),
        StreamFieldPanel('about_section_feature'),
        StreamFieldPanel('about_section_content'),
        StreamFieldPanel('what_we_do_section'),
        StreamFieldPanel('services'),
        FieldPanel('how_it_works_subtitle'),
        FieldPanel('how_it_works_title'),
        FieldPanel('how_it_works_description'),
        StreamFieldPanel('how_it_works_processes'),
        StreamFieldPanel('team_section'),
        StreamFieldPanel('call_to_action'),
        StreamFieldPanel('upcoming_events'),
    ]

    class Meta:
        verbose_name = "Home Page"