from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import RichTextBlock
from wagtail.core.fields import StreamField

from wagtail.core.models import Page


class HomePage(Page):
    introduction = StreamField([("rich_text", RichTextBlock())], blank=True)
    content_panels = Page.content_panels + [
        StreamFieldPanel("introduction")
    ]
