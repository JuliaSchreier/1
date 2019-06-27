from django.forms import CheckboxSelectMultiple

class ImageCheckboxSelectMultiple(CheckboxSelectMultiple):
    template_name = 'widgets/image_checkbox_select.html'
    option_template_name = 'widgets/image_checkbox_option.html'

    def __init__(self, images, attrs=None, choices=(), ):
        assert len(images)==len(choices), 'The number of images should be the same as number of choices'
        self.images = images

        return super().__init__(attrs, choices)

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        ret = super().create_option(name, value, label, selected, index, subindex, attrs)
        image_index = int(ret['index'])
        ret['image'] = self.images[image_index]
        return ret


