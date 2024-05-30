from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class BannerSlideBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=True, max_length=255)
    text = blocks.TextBlock(required=True)
    button_text = blocks.CharBlock(required=False, max_length=50)
    button_link = blocks.URLBlock(required=False)

    class Meta:
        icon = "image"
        label = "Banner Slide"
        template = "home/blocks/banner_slide_block.html"

class BannerBlock(blocks.StructBlock):
    slides = blocks.ListBlock(BannerSlideBlock())

    class Meta:
        icon = "image"
        label = "Banner Section"
        template = "home/blocks/banner_block.html"


class AboutFeatureBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    icon = blocks.CharBlock(required=True, max_length=50)
    title = blocks.CharBlock(required=True, max_length=255)
    text = blocks.TextBlock(required=True)

    class Meta:
        icon = "image"
        label = "About Feature"

class AboutSectionBlock(blocks.StructBlock):
    features = blocks.ListBlock(AboutFeatureBlock())
    main_title = blocks.CharBlock(required=True, max_length=255)
    main_text = blocks.RichTextBlock()
    main_image_1 = ImageChooserBlock(required=True)
    main_image_2 = ImageChooserBlock(required=True)

    class Meta:
        icon = "doc-full"
        label = "About Section"

class TeamMemberBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    name = blocks.CharBlock(required=True, max_length=255)
    designation = blocks.CharBlock(required=True, max_length=255)
    facebook_link = blocks.URLBlock(required=False)
    twitter_link = blocks.URLBlock(required=False)
    linkedin_link = blocks.URLBlock(required=False)

    class Meta:
        icon = "user"
        label = "Team Member"

class TeamCarouselBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255)
    subtitle = blocks.CharBlock(required=True, max_length=255)
    description = blocks.TextBlock(required=True)
    members = blocks.ListBlock(TeamMemberBlock())

    class Meta:
        icon = "group"
        label = "Team Carousel"

class CallToActionBlock(blocks.StructBlock):
    background_image = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=True, max_length=255)
    text = blocks.RichTextBlock()
    button_1_text = blocks.CharBlock(required=True, max_length=50)
    button_1_link = blocks.URLBlock(required=True)
    button_2_text = blocks.CharBlock(required=True, max_length=50)
    button_2_link = blocks.URLBlock(required=True)

    class Meta:
        icon = "link"
        label = "Call to Action"

class AltCallToActionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255)
    button_text = blocks.CharBlock(required=True, max_length=50)
    button_link = blocks.URLBlock(required=True)

    class Meta:
        icon = "link"
        label = "Alternate Call to Action"

class EventBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=True, max_length=255)
    description = blocks.TextBlock(required=True)
    time = blocks.CharBlock(required=True, max_length=50)
    location = blocks.CharBlock(required=True, max_length=255)
    link_text = blocks.CharBlock(required=True, max_length=50)
    link_url = blocks.URLBlock(required=True)

    class Meta:
        icon = "date"
        label = "Event"

class UpcomingEventsBlock(blocks.StructBlock):
    subtitle = blocks.CharBlock(required=True, max_length=255)
    title = blocks.CharBlock(required=True, max_length=255)
    description = blocks.TextBlock(required=True)
    events = blocks.ListBlock(EventBlock())

    class Meta:
        icon = "date"
        label = "Upcoming Events"
