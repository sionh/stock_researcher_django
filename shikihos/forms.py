from django import forms

YEAR_CHOICES = (
    ('2020', '2020'),
    ('2019', '2019'),
    ('2018', '2018'),
    ('2017', '2017'),
)
QUARTER_CHOICES = (
    ('1', '春'),
    ('2', '夏'),
    ('3', '秋'),
    ('4', '冬'),
)

class SearchForm(forms.Form):
    year = forms.ChoiceField(
        label='発行年月',
        choices=YEAR_CHOICES,
        widget=forms.Select
    )

    quarter = forms.ChoiceField(
        label='発行時期',
        choices=QUARTER_CHOICES,
        widget=forms.Select
    )

    code = forms.CharField(
        label='銘柄コード',
        max_length=20,
        widget=forms.TextInput(),
        required=False,
    )

    comp_name = forms.CharField(
        label='企業名',
        max_length=20,
        widget=forms.TextInput(),
        required=False,
    )

    feature = forms.CharField(
        label='特徴',
        max_length=20,
        widget=forms.TextInput(),
        required=False,
    )

    topic = forms.CharField(
        label='トピック',
        max_length=20,
        widget=forms.TextInput(),
        required=False,
    )

    outlook = forms.CharField(
        label='見通し',
        max_length=20,
        widget=forms.TextInput(),
        required=False,
    )
