from django import forms

from .models import ACTIVATION_STYLE, HIGH_ROLLER_STATUS, Enhancement, Drawback, CREATION_REASON, Power_Full


def set_field_html_name(cls, new_name):
    """
    This creates wrapper around the normal widget rendering,
    allowing for a custom field name (new_name).
    """
    old_render = cls.widget.render
    def _widget_render_wrapper(name, value, attrs=None, renderer=None):
        return old_render(new_name, value, attrs, renderer=None)

    cls.widget.render = _widget_render_wrapper

class EnhancementDrawbackPickerForm(forms.ModelForm):
    # used in the admin app for base_power
    def  __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['enhancements'].queryset = Enhancement.objects.order_by("-is_general").all()
        self.fields['drawbacks'].queryset = Drawback.objects.order_by("-is_general").all()
        self.fields['example_powers'].queryset = Power_Full.objects.order_by("-pub_date").all()

class DrawbackModelForm(forms.ModelForm):
    class Meta:
        model = Drawback
        exclude = []

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['drawbacks'].queryset = Drawback.objects.order_by("is_general").all()

def make_enhancement_form(enhancement, enhancement_instance=None):
    class EnhancementForm(forms.Form):
        def get_label(enhancement):
            requirements = ""
            required_status = {}
            for status in HIGH_ROLLER_STATUS: required_status[status[0]] = status[1]
            if enhancement.required_status in [HIGH_ROLLER_STATUS[2][0], HIGH_ROLLER_STATUS[3][0]]:
                requirements = "requires: {}".format(required_status[enhancement.required_status])
            return '{} ({}) {}'.format(enhancement.name, enhancement.description, requirements)

        label= get_label(enhancement)
        enhancement_slug=str(enhancement.slug)
        eratta = enhancement.eratta
        multiplicity_allowed=enhancement.multiplicity_allowed;
        is_selected = forms.BooleanField(required=True)
        if enhancement_instance:
            is_selected.initial=True
        set_field_html_name(is_selected, enhancement.form_name())
        if enhancement.detail_field_label is not "" and enhancement.detail_field_label is not None:
            detail_text = forms.CharField(required=False,
                                          label=enhancement.detail_field_label)
            set_field_html_name(detail_text, enhancement.form_detail_name())
            if enhancement_instance:
                detail_text.initial=enhancement_instance.detail

    return EnhancementForm

def make_drawback_form(drawback):
    class DrawbackForm(forms.Form):
        def get_label(drawback):
            requirements = ""
            required_status = {}
            for status in HIGH_ROLLER_STATUS: required_status[status[0]] = status[1]
            if drawback.required_status in [HIGH_ROLLER_STATUS[2][0], HIGH_ROLLER_STATUS[3][0]]:
                requirements = "requires: {}".format(required_status[drawback.required_status])
            return '{} ({}) {}'.format(drawback.name, drawback.description, requirements)

        label= get_label(drawback)
        eratta = drawback.eratta
        drawback_slug=str(drawback.slug)
        multiplicity_allowed=drawback.multiplicity_allowed;
        is_selected = forms.BooleanField(required=True)
        set_field_html_name(is_selected, drawback.form_name())
        if drawback.detail_field_label is not "" and drawback.detail_field_label is not None:
            detail_text = forms.CharField(required=False,
                                          label=drawback.detail_field_label)
            set_field_html_name(detail_text, drawback.form_detail_name())

    return DrawbackForm

def make_parameter_form(power_param):
    parameter = power_param.relevant_parameter
    class ParameterForm(forms.Form):
        param_choices = []
        for i in range(parameter.get_max_level()):
            param_choices.append((i, str(parameter.get_value_for_level(i) + power_param.get_status_tag(i))))
        label = parameter.name
        level_picker = forms.ChoiceField(choices=param_choices,
                                         initial=power_param.default)
        set_field_html_name(level_picker, parameter.slug)

    return ParameterForm

class CreatePowerForm(forms.Form):
    power_name = forms.CharField(label='Power Name', max_length=100)
    flavor = forms.CharField(label='Flavor Text',
                             widget=forms.Textarea,
                             help_text='A snippet of text that introduces the power in a flavorful way')
    description = forms.CharField(label='Description',
                                  widget=forms.Textarea,
                                  help_text='Describe what the power looks like when it is used, how it works, and its impact on the owner, target, and environment')
    system = forms.CharField(label='System', widget=forms.Textarea,
                             help_text='Describe the power\'s cost, associated roll(s), determination of outcome, conditions, etc')
    activation_style = forms.ChoiceField(choices=ACTIVATION_STYLE, disabled=True)


    def __init__(self, base_power, *args, **kwargs):
        super(CreatePowerForm, self).__init__(*args, **kwargs)
        #
        # base_power context sensitive field mutations go here.
        #
        self.fields['activation_style'].help_text='Choose whether the power is always on (passive) or activated manually (active). ' \
                                                  'Default is ' + base_power.default_activation_style + "."
        self.fields['activation_style'].initial=base_power.default_activation_style