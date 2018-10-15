from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ftw.simplelayout.contenttypes.browser.textblock import TextBlockView


class FaqBlockView(TextBlockView):
    template = ViewPageTemplateFile('faqblock.pt')
