import datetime

from django.forms import Field
from django.utils.translation import ugettext_lazy

from hrms.models import *
from django import forms
from search_views.filters import BaseFilter


# Sử dụng date input html5
class DateInput(forms.DateInput):
    input_type = "date"


# Sử dụng time input html5
class TimeInput(forms.TimeInput):
    input_type = "time"


# Thông báo lỗi mặc định
Field.default_error_messages = {
    'required': ugettext_lazy("Dữ liệu này không được bỏ trống!"),
    'invalid': ugettext_lazy('Giá trị nhập vào chưa hợp lý!')
}


# Giới tính
##############################################################################################################
# Thêm mới Gender
class GenderForm(forms.ModelForm):
    class Meta:
        model = Gender
        fields = ('gender_id', 'gender_name')
        labels = {
            'gender_id': "Mã giới tính",
            'gender_name': "Giới tính"
        }

    def __init__(self, *args, **kwargs):
        super(GenderForm, self).__init__(*args, **kwargs)
        self.fields['gender_id'].widget.attrs.update({'autofocus': 'autofocus'})

    def clean_gender_id(self, *args, **kwargs):
        gender_id = self.cleaned_data.get('gender_id')
        if Gender.objects.exclude(pk=self.instance.pk).filter(gender_id=gender_id).exists():
            # Unable to find a user, this is fine
            # A user was found with this as a username, raise an error.
            raise forms.ValidationError('Mã giới tính này đã có!')
        return gender_id


# Điều chỉnh Gender
class GenderUpdateForm(GenderForm):
    def __init__(self, *args, **kwargs):
        super(GenderUpdateForm, self).__init__(*args, **kwargs)
        self.fields['gender_id'].disabled = True


# Tiền tệ
##############################################################################################################
# Thêm mới Currency
class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ('currency_id', 'currency_name')
        labels = {
            'currency_id': "Mã tiền tệ",
            'currency_name': "Loại tiền"
        }

    def __init__(self, *args, **kwargs):
        super(CurrencyForm, self).__init__(*args, **kwargs)
        self.fields['currency_id'].widget.attrs.update({'autofocus': 'autofocus'})

    def clean_currency_id(self, *args, **kwargs):
        currency_id = self.cleaned_data.get('currency_id')
        if Currency.objects.exclude(pk=self.instance.pk).filter(currency_id=currency_id).exists():
            raise forms.ValidationError('Mã tiền tệ này đã có!')
        return currency_id


# Cập nhật Currency
class CurrencyUpdateForm(CurrencyForm):
    def __init__(self, *args, **kwargs):
        super(CurrencyForm, self).__init__(*args, **kwargs)
        self.fields['currency_name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['currency_id'].disabled = True


# Tìm kiếm
class CurrencySearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


# Fill data
class CurrencyFilter(BaseFilter):
    search_fields = {'search_text': ['currency_name'], }


# Nơi cấp CMND/ Hộ chiếu
##############################################################################################################
# Thêm mới PlaceOfIdentification
class PlaceOfIdentificationForm(forms.ModelForm):
    class Meta:
        model = PlaceOfIdentification
        fields = ('place_id', 'place_of_identification')
        labels = {
            'place_id': "Mã nơi cấp",
            'place_of_identification': "Nơi cấp"
        }

    def __init__(self, *args, **kwargs):
        super(PlaceOfIdentificationForm, self).__init__(*args, **kwargs)
        self.fields['place_id'].widget.attrs.update({'autofocus': 'autofocus'})

    def clean_place_id(self, *args, **kwargs):
        place_id = self.cleaned_data.get('place_id')
        if PlaceOfIdentification.objects.exclude(pk=self.instance.pk).filter(place_id=place_id).exists():
            raise forms.ValidationError('Mã nơi cấp này đã có!')
        if len(place_id) != 4:
            raise forms.ValidationError('Mã nơi cấp phải có 4 ký tự!')
        return place_id


# cập nhật PlaceOfIdentification
class PlaceOfIdentificationUpdateForm(PlaceOfIdentificationForm):
    def __init__(self, *args, **kwargs):
        super(PlaceOfIdentificationForm, self).__init__(*args, **kwargs)
        self.fields['place_of_identification'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['place_id'].disabled = True  # readonly id_name_code


class PlaceOfIdentificationSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class PlaceOfIdentificationFilter(BaseFilter):
    search_fields = {'search_text': ['place_of_identification'], }


# Loại giấy tờ tùy thân
##############################################################################################################
# Thêm mới IdNameForm
class IdNameForm(forms.ModelForm):
    class Meta:
        model = IdName
        fields = ('id_name_code', 'name_of_identification')
        labels = {
            'id_name_code': "Mã loại",
            'name_of_identification': "Tên loại"
        }

    def __init__(self, *args, **kwargs):
        super(IdNameForm, self).__init__(*args, **kwargs)
        self.fields['id_name_code'].widget.attrs.update({'autofocus': 'autofocus'})

    def clean_id_name_code(self, *args, **kwargs):
        id_name_code = self.cleaned_data.get('id_name_code')
        if IdName.objects.exclude(pk=self.instance.pk).filter(id_name_code=id_name_code).exists():
            raise forms.ValidationError('Mã nơi cấp này đã có!')
        return id_name_code


# Tìm kiếm
class IdNameSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


# Fill data
class IdNameFilter(BaseFilter):
    search_fields = {'search_text': ['name_of_identification'], }


# Cập nhật IdNameForm
class IdNameUpdateForm(IdNameForm):
    def __init__(self, *args, **kwargs):
        super(IdNameForm, self).__init__(*args, **kwargs)
        self.fields['name_of_identification'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['id_name_code'].disabled = True  # readonly id_name_code


# Dân tộc
##############################################################################################################
# Thêm mới People
class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('people_name',)
        labels = {
            'people_name': "Dân tộc",
        }

    def __init__(self, *args, **kwargs):
        super(PeopleForm, self).__init__(*args, **kwargs)
        self.fields['people_name'].widget.attrs.update({'autofocus': 'autofocus'})


class PeopleSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class PeopleFilter(BaseFilter):
    search_fields = {'search_text': ['people_name'], }


# Quốc tịch
##############################################################################################################
# Thêm mới Nation
class NationForm(forms.ModelForm):
    class Meta:
        model = Nation
        fields = ('nation_id', 'nation_name')
        labels = {
            'nation_id': "Mã quốc gia",
            'nation_name': "Tên quốc gia"
        }

    def __init__(self, *args, **kwargs):
        super(NationForm, self).__init__(*args, **kwargs)
        self.fields['nation_id'].widget.attrs.update({'autofocus': 'autofocus'})

    def clean_nation_id(self, *args, **kwargs):
        nation_id = self.cleaned_data.get('nation_id')
        if Nation.objects.exclude(pk=self.instance.pk).filter(nation_id=nation_id).exists():
            raise forms.ValidationError('Mã quốc gia này đã có!')
        return nation_id


class NationSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class NationFilter(BaseFilter):
    search_fields = {'search_text': ['nation_name'], }


# Cập nhật IdNameForm
class NationUpdateForm(NationForm):
    def __init__(self, *args, **kwargs):
        super(NationForm, self).__init__(*args, **kwargs)
        self.fields['nation_name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['nation_id'].disabled = True  # readonly id_name_code


# Đơn giá tiền ăn trưa
##############################################################################################################
# Thêm mới MealMoney
class MealMoneyForm(forms.ModelForm):
    class Meta:
        model = MealMoney
        fields = ('amount', 'currency', 'startday', 'endday')
        labels = {
            'amount': "Số tiền",
            'currency': 'Loại tiền',
            'startday': "Từ ngày",
            'endday': 'Đến ngày',
        }
        widgets = {
            'startday': DateInput,
            'endday': DateInput,
        }
        # Valid() accept number 1,000,000,000
        localized_fields = ('amount', 'startday', 'endday', )

    def __init__(self, *args, **kwargs):
        super(MealMoneyForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update(
            {'autofocus': 'autofocus',
             'class': 'amount',
             'style': 'text-align: right'})

    def clean_amount(self, *args, **kwargs):
        amount = self.cleaned_data.get('amount')
        if amount < 0:
            raise forms.ValidationError('Tiền ăn không được nhỏ hơn không (0)!')
        return amount

    def save(self, commit=True):
        m = super(MealMoneyForm, self).save(commit=False)
        # do custom stuff

        if commit:
            cert_day = self.cleaned_data.get('startday') - datetime.timedelta(1)
            if MealMoney.objects.all().exists():
                id_last = MealMoney.objects.values('mealmoney_id').all().last()['mealmoney_id']
                MealMoney.objects.filter(mealmoney_id=id_last).update(endday=cert_day)
            m.save()
        return m


class MealMoneySearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class MealMoneyFilter(BaseFilter):
    search_fields = {'search_text': ['amount'], }


# Cập nhật MealMoney
class MealMoneyUpdateForm(MealMoneyForm):
    def __init__(self, *args, **kwargs):
        super(MealMoneyForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update(
            {'autofocus': 'autofocus',
             'class': 'amount',
             'style': 'text-align: right'})


# Tiền lương tối thiểu
##############################################################################################################
# Thêm mới SalaryBasic
class SalaryBasicForm(forms.ModelForm):
    class Meta:
        model = SalaryBasic
        fields = ('name', 'amount', 'currency', 'startday', 'endday', 'designation', )
        labels = {
            'name': 'Tên vùng',
            'amount': "Số tiền",
            'currency': 'Loại tiền',
            'startday': "Từ ngày",
            'endday': 'Đến ngày',
            'designation': 'Theo văn bản',
        }
        widgets = {
            'startday': DateInput,
            'endday': DateInput,
        }
        # Valid() accept number 1,000,000,000
        localized_fields = ('amount', 'startday', 'endday', )

    def __init__(self, *args, **kwargs):
        super(SalaryBasicForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update(
            {'autofocus': 'autofocus',
             'class': 'amount',
             'style': 'text-align: right'})

    def clean_salary_basic_amount(self, *args, **kwargs):
        amount = self.cleaned_data.get('amount')
        if amount < 0:
            raise forms.ValidationError('Tiền không được nhỏ hơn không (0)!')
        return amount

    def save(self, commit=True):
        m = super(SalaryBasicForm, self).save(commit=False)
        # do custom stuff
        if commit:
            # Nếu chưa có phần tử nào thì save record đầu tiên
            if SalaryBasic.objects.all().exists():
                cert_day = self.cleaned_data.get('startday') - datetime.timedelta(1)
                id_last = SalaryBasic.objects.values('salary_basic_id').all().last()['salary_basic_id']
                SalaryBasic.objects.filter(salary_basic_id=id_last).update(endday=cert_day)
            m.save()
        return m


class SalaryBasicSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class SalaryBasicFilter(BaseFilter):
    search_fields = {'search_text': ['salary_basic_id', 'designation'], }


# Cập nhật SalaryBasic
class SalaryBasicUpdateForm(SalaryBasicForm):
    def __init__(self, *args, **kwargs):
        super(SalaryBasicForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({'autofocus': 'autofocus', 'class': 'amount', 'style': 'text-align: right'})


# Tỷ lệ Tiền lương tối thiểu tăng thêm
##############################################################################################################
# Thêm mới SalaryBasic
class SalaryBasicPlusForm(forms.ModelForm):
    class Meta:
        model = SalaryBasicPlus
        fields = ('ratio', 'startday', 'endday', )
        labels = {
            'ratio': "Tỷ lệ (%)",
            'startday': "Từ ngày",
            'endday': 'Đến ngày',
        }
        widgets = {'startday': DateInput, 'endday': DateInput, }
        # Valid() accept number 1,000,000,000
        localized_fields = ('ratio', 'startday', 'endday', )

    def __init__(self, *args, **kwargs):
        super(SalaryBasicPlusForm, self).__init__(*args, **kwargs)
        self.fields['ratio'].widget.attrs.update(
            {'autofocus': 'autofocus', 'class': 'ratio', 'style': 'text-align: right', 'placeholder': '', })

    def clean_ratio(self, *args, **kwargs):
        ratio = self.cleaned_data.get('ratio')
        if ratio < 0:
            raise forms.ValidationError('Tỷ lệ không được nhỏ hơn không (0)!')
        return ratio

    def save(self, commit=True):
        m = super(SalaryBasicPlusForm, self).save(commit=False)
        # do custom stuff
        if commit:
            # Nếu chưa có phần tử nào thì save record đầu tiên
            if SalaryBasicPlus.objects.all().exists():
                cert_day = self.cleaned_data.get('startday') - datetime.timedelta(1)
                id_last = SalaryBasicPlus.objects.values('salary_basic_plus_id').all().last()['salary_basic_plus_id']
                SalaryBasicPlus.objects.filter(salary_basic_plus_id=id_last).update(endday=cert_day)
            m.save()
        return m


class SalaryBasicPlusSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class SalaryBasicPlusFilter(BaseFilter):
    search_fields = {'search_text': ['ratio'], }


# Cập nhật SalaryBasic
class SalaryBasicPlusUpdateForm(SalaryBasicPlusForm):
    def __init__(self, *args, **kwargs):
        super(SalaryBasicPlusForm, self).__init__(*args, **kwargs)
        self.fields['ratio'].widget.attrs.update(
            {'autofocus': 'autofocus', 'class': 'ratio', 'style': 'text-align: right', })


# Hệ số lương
##############################################################################################################
# Thêm mới SalaryScale
class SalaryScaleForm(forms.ModelForm):
    class Meta:
        model = SalaryScale
        fields = ('name', 'scale', 'startday', 'endday', )
        labels = {
            'name': 'Tên bậc lương',
            'scale': "Tỷ lệ (%)",
            'startday': "Từ ngày",
            'endday': 'Đến ngày',
        }
        widgets = {'startday': DateInput, 'endday': DateInput, }
        # Valid() accept number 1,000,000,000
        localized_fields = ('scale', 'startday', 'endday', )

    def __init__(self, *args, **kwargs):
        super(SalaryScaleForm, self).__init__(*args, **kwargs)
        self.fields['scale'].widget.attrs.update({'class': 'scale', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus', })

    def clean_scale(self, *args, **kwargs):
        scale = self.cleaned_data.get('scale')
        if scale < 0:
            raise forms.ValidationError('Tỷ lệ không được nhỏ hơn không (0)!')
        return scale


# Cập nhật SalaryScale
class SalaryScaleUpdateForm(SalaryScaleForm):
    def __init__(self, *args, **kwargs):
        super(SalaryScaleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus', })


class SalaryScaleSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class SalaryScaleFilter(BaseFilter):
    search_fields = {'search_text': ['scale', 'name'], }


# BHXH, BHYT, BHTN
##############################################################################################################
# Thêm mới Insurance
class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ('social_company', 'social_employee', 'social_tnld_bnn',
                  'health_company', 'health_employee',
                  'unemployment_company', 'unemployment_employee',
                  'startday', 'endday', 'designation')
        labels = {
            'social_company': 'BHXH (%)',
            'social_employee': "BHXH (%)",
            'social_tnld_bnn': "BHTNLĐ-BNN (%)",
            'health_company': "BHYT (%)",
            'health_employee': "BHYT (%)",
            'unemployment_company': "BHTN (%)",
            'unemployment_employee': "BHTN (%)",
            'startday': "Từ ngày",
            'endday': 'Đến ngày',
            'designation': "Theo văn bản",
        }
        widgets = {'startday': DateInput, 'endday': DateInput,
                   'designation': forms.TextInput(), }
        # Valid() accept number 1,000,000,000.00
        localized_fields = ('social_company', 'social_employee', 'social_tnld_bnn',
                            'health_company', 'health_employee',
                            'unemployment_company', 'unemployment_employee',
                            'startday', 'endday', )

    def __init__(self, *args, **kwargs):
        super(InsuranceForm, self).__init__(*args, **kwargs)
        self.fields['social_company'].widget.attrs\
            .update({'autofocus': 'autofocus', 'class': 'social_company', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['social_employee'].widget.attrs\
            .update({'class': 'social_employee', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['social_tnld_bnn'].widget.attrs\
            .update({'class': 'social_tnld_bnn', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['health_company'].widget.attrs\
            .update({'class': 'health_company', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['health_employee'].widget.attrs\
            .update({'class': 'health_employee', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['unemployment_company'].widget.attrs\
            .update({'class': 'unemployment_company', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['unemployment_employee'].widget.attrs\
            .update({'class': 'unemployment_employee', 'style': 'text-align: right', 'placeholder': '', })

    def clean_social_company(self, *args, **kwargs):
        social_company = self.cleaned_data.get('social_company')
        if social_company < 0:
            raise forms.ValidationError('Tỷ lệ không được nhỏ hơn không (0)!')
        return social_company


# Cập nhật Insurance
class InsuranceUpdateForm(InsuranceForm):
    def __init__(self, *args, **kwargs):
        super(InsuranceForm, self).__init__(*args, **kwargs)
        self.fields['social_company'].widget.attrs \
            .update({'autofocus': 'autofocus', 'class': 'social_company', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['social_employee'].widget.attrs \
            .update({'class': 'social_employee', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['social_tnld_bnn'].widget.attrs \
            .update({'class': 'social_tnld_bnn', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['health_company'].widget.attrs \
            .update({'class': 'health_company', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['health_employee'].widget.attrs \
            .update({'class': 'health_employee', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['unemployment_company'].widget.attrs \
            .update({'class': 'unemployment_company', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['unemployment_employee'].widget.attrs \
            .update({'class': 'unemployment_employee', 'style': 'text-align: right', 'placeholder': '', })


class InsuranceSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class InsuranceFilter(BaseFilter):
    search_fields = {'search_text': ['designation'], }


# Công đoàn
##############################################################################################################
# Thêm mới Union
class UnionForm(forms.ModelForm):
    class Meta:
        model = Union
        fields = ('ratio_company', 'ratio_employee', 'startday', 'endday', 'designation')
        labels = {
            'ratio_company': 'Người sử dụng lao động', 'ratio_employee': "Người lao động",
            'startday': "Từ ngày", 'endday': 'Đến ngày', 'designation': "Theo văn bản",
        }
        widgets = {'startday': DateInput, 'endday': DateInput, 'designation': forms.TextInput(), }
        # Valid() accept number 1,000,000,000.00
        localized_fields = ('ratio_company', 'ratio_employee', 'startday', 'endday', )

    def __init__(self, *args, **kwargs):
        super(UnionForm, self).__init__(*args, **kwargs)
        self.fields['ratio_company'].widget.attrs\
            .update({'autofocus': 'autofocus', 'class': 'ratio_company', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['ratio_employee'].widget.attrs\
            .update({'class': 'ratio_employee', 'style': 'text-align: right', 'placeholder': '', })

    def clean_ratio_company(self, *args, **kwargs):
        ratio_company = self.cleaned_data.get('ratio_company')
        if ratio_company < 0:
            raise forms.ValidationError('Tỷ lệ không được nhỏ hơn không (0)!')
        return ratio_company

    def save(self, commit=True):
        m = super(UnionForm, self).save(commit=False)
        # do custom stuff
        if commit:
            # Nếu chưa có phần tử nào thì save record đầu tiên
            if Union.objects.all().exists():
                cert_day = self.cleaned_data.get('startday') - datetime.timedelta(1)
                id_last = Union.objects.values('union_id').all().last()['union_id']
                Union.objects.filter(union_id=id_last).update(endday=cert_day)
            m.save()
        return m


# Cập nhật Union
class UnionUpdateForm(UnionForm):
    def __init__(self, *args, **kwargs):
        super(UnionForm, self).__init__(*args, **kwargs)
        self.fields['ratio_company'].widget.attrs \
            .update({'autofocus': 'autofocus', 'class': 'ratio_company', 'style': 'text-align: right', 'placeholder': '', })
        self.fields['ratio_employee'].widget.attrs \
            .update({'class': 'ratio_employee', 'style': 'text-align: right', 'placeholder': '', })


class UnionSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class UnionFilter(BaseFilter):
    search_fields = {'search_text': ['designation'], }


##############################################################################################################
# Thời gian làm việc
# --------------------------------------------------------------------------
# Thêm mới WorkingTime
class WorkingTimeForm(forms.ModelForm):
    class Meta:
        model = WorkingTime
        fields = ('name', 'starttime', 'endtime', 'description', )
        labels = {'name': 'Loại giờ làm', 'starttime': 'Giờ bắt đầu', 'endtime': 'Giờ kết thúc', 'description': 'Diễn giải', }
        widgets = {'starttime': TimeInput, 'endtime': TimeInput, }

    def __init__(self, *args, **kwargs):
        super(WorkingTimeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus', })


# Cập nhật WorkingTime
class WorkingTimeUpdateForm(WorkingTimeForm):
    def __init__(self, *args, **kwargs):
        super(WorkingTimeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus', })


class WorkingTimeSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class WorkingTimeFilter(BaseFilter):
    search_fields = {'search_text': ['name', 'description'], }


# --------------------------------------------------------------------------
# Các ngày trong tuần
# Thêm mới DaysOfWeek
class DaysOfWeekForm(forms.ModelForm):
    class Meta:
        model = DaysOfWeek
        fields = ('daysofweek_id', 'dayname', )
        labels = {'daysofweek_id': 'ID', 'dayname': 'Ngày', }

    def __init__(self, *args, **kwargs):
        super(DaysOfWeekForm, self).__init__(*args, **kwargs)
        self.fields['daysofweek_id'].widget.attrs.update({'autofocus': 'autofocus', })


# Cập nhật DaysOfWeek
class DaysOfWeekUpdateForm(DaysOfWeekForm):
    def __init__(self, *args, **kwargs):
        super(DaysOfWeekForm, self).__init__(*args, **kwargs)
        self.fields['dayname'].widget.attrs.update({'autofocus': 'autofocus', })
        self.fields['daysofweek_id'].widget.attrs.update({'readonly': 'readonly', })


class DaysOfWeekSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class DaysOfWeekFilter(BaseFilter):
    search_fields = {'search_text': ['dayname', ], }


# --------------------------------------------------------------------------
# Nhóm làm việc
# Thêm mới WorkingGroup
class WorkingGroupForm(forms.ModelForm):
    class Meta:
        model = WorkingGroup
        fields = ('name', )
        labels = {'name': 'Tên nhóm', }

    def __init__(self, *args, **kwargs):
        super(WorkingGroupForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus', })


# Cập nhật WorkingGroup
class WorkingGroupUpdateForm(WorkingGroupForm):
    def __init__(self, *args, **kwargs):
        super(WorkingGroupForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus', })


class WorkingGroupSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class WorkingGroupFilter(BaseFilter):
    search_fields = {'search_text': ['name', ], }


# --------------------------------------------------------------------------
# Chi tiết thời gian làm việc
# Thêm mới WorkSchedules
class WorkSchedulesForm(forms.ModelForm):
    # countries = forms.ModelMultipleChoiceField(queryset=DaysOfWeek.objects.all(), to_field_name="dayname")
    # daysofweek = forms.ModelMultipleChoiceField(queryset=DaysOfWeek.objects.all(), to_field_name="dayname")

    class Meta:
        model = WorkSchedules
        # fields = ('workinggroup', 'workingtime', 'daysofweek', )
        fields = '__all__'
        labels = {'workinggroup': 'Nhóm', 'workingtime': 'Ca', 'daysofweek': 'Ngày', }
        widgets = {
            'workingtime': forms.TextInput(),
            'daysofweek': forms.SelectMultiple,
            'workinggroup': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(WorkSchedulesForm, self).__init__(*args, **kwargs)
        self.fields['workinggroup'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Chọn...', })
        self.fields['workingtime'].widget.attrs.update({'placeholder': 'Chọn...', })
        # self.fields['daysofweek'].widget.attrs.update({'placeholder': 'Chọn...', })
        self.fields['daysofweek'].queryset = DaysOfWeek.objects.all()
        self.fields['daysofweek'].to_field_name = 'dayname'
        self.fields['daysofweek'].empty_label = None
    """
    def clean_option_field(self):
        return ','.join(self.cleaned_data['option'])

    def clean_daysofweek_id(self, *args, **kwargs):
        t = self.cleaned_data.get('daysofweek_id')
        if len(t) == 0:
            raise forms.ValidationError('Tỷ lệ không được nhỏ hơn không (0)!')
        return 1

    def form_valid(self, form):
        form.instance.daysofweek = DaysOfWeek.objects.get(self.kwargs['pk'])
        return super(WorkSchedulesForm, self).form_valid(form)
    """


# Cập nhật WorkSchedules
class WorkSchedulesUpdateForm(WorkSchedulesForm):
    # daysofweek = forms.ModelMultipleChoiceField(queryset=DaysOfWeek.objects.all(), to_field_name="dayname")

    def __init__(self, *args, **kwargs):
        super(WorkSchedulesForm, self).__init__(*args, **kwargs)
        self.fields['workinggroup'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Chọn...', })
        self.fields['workingtime'].widget.attrs.update({'placeholder': 'Chọn...', })
        self.fields['daysofweek'].widget.attrs.update({'placeholder': 'Chọn...', })
        # self.fields['daysofweek'].queryset = DaysOfWeek.objects.all()
        self.fields['daysofweek'].to_field_name = 'dayname'
        self.fields['daysofweek'].empty_label = None


class WorkSchedulesSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class WorkSchedulesFilter(BaseFilter):
    # Tìm kiếm many-to-many (m2m)
    search_fields = {'search_text': ['workinggroup__name', 'workingtime__name', ], }


# --------------------------------------------------------------------------
# Hợp đồng lao động
# Thêm mới LaborContract
class LaborContractForm(forms.ModelForm):
    class Meta:
        model = LaborContract
        fields = '__all__'
        labels = {
            'contract_number': 'Số hợp đồng',
            'contract_day': 'Ngày hợp đồng',
            'cif': 'Nhân viên',
            'company': 'Công ty',
            'dept': 'Phòng',
            'subdept': 'Bộ phận',
            'salary_basic': 'Lương cơ bản',
            'insurance': 'Mã tỷ lệ đóng BHXH',
            'union': 'Mã tỷ lệ đóng công đoàn',
            'salary_benefit': 'Phụ cấp thường xuyên',
            'scale': 'Mã hệ số lương',
            'mealmoney': 'Mã phụ cấp tiền ăn trưa',
            'startday': 'Ngày hiệu lực',
            'endday': 'Ngày thay đổi thông tin',
            'maturity_date': 'Ngày hết hạn hợp đồng',
            'term': 'Thời hạn hợp đồng',
            'workinggroup': 'Nhóm làm việc'
        }
        widgets = {
            'cif': forms.TextInput(),
            'company': forms.TextInput(),
            # 'dept': forms.(),
            # 'subdept': forms.TextInput(),
            'salary_basic': forms.TextInput(),
            'insurance': forms.TextInput(),
            'union': forms.TextInput(),
            'scale': forms.TextInput(),
            'mealmoney': forms.TextInput(),
            'workinggroup': forms.TextInput(),
            'contract_day': DateInput,
            'maturity_date': DateInput,
            'startday': DateInput,
            'endday': DateInput,
        }

        localized_fields = ('salary_benefit', 'startday', 'endday',)

    def __init__(self, *args, **kwargs):
        super(LaborContractForm, self).__init__(*args, **kwargs)
        self.fields['contract_number'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': '', })
        self.fields['salary_benefit'].widget.attrs.update({'style': 'text-align: right', })
    """
    def clean_option_field(self):
        return ','.join(self.cleaned_data['option'])

    def clean_daysofweek_id(self, *args, **kwargs):
        t = self.cleaned_data.get('daysofweek_id')
        if len(t) == 0:
            raise forms.ValidationError('Tỷ lệ không được nhỏ hơn không (0)!')
        return 1

    def form_valid(self, form):
        form.instance.daysofweek = DaysOfWeek.objects.get(self.kwargs['pk'])
        return super(WorkSchedulesForm, self).form_valid(form)
    """


# Cập nhật LaborContract
class LaborContractUpdateForm(LaborContractForm):
    # daysofweek = forms.ModelMultipleChoiceField(queryset=DaysOfWeek.objects.all(), to_field_name="dayname")

    def __init__(self, *args, **kwargs):
        super(LaborContractForm, self).__init__(*args, **kwargs)
        self.fields['contract_number'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': '', })


class LaborContractSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm...', 'autofocus': 'autofocus', })
    )


class LaborContractFilter(BaseFilter):
    # Tìm kiếm many-to-many (m2m)
    search_fields = {'search_text': ['contract_number', 'cif', ], }
