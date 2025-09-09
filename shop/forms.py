from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # username field 스타일 수정
        self.fields['username'].widget.attrs.update({
            'style': 'margin-top: 10px'  # 레이블과 입력폼 사이 간격
        })
        
        # password1 field 스타일 수정
        self.fields['password1'].widget.attrs.update({
            'style': 'margin-top: 10px'  # 레이블과 입력폼 사이 간격
        })

        # password2 field 스타일 수정
        self.fields['password2'].widget.attrs.update({
            'style': 'margin-top: 10px'  # 레이블과 입력폼 사이 간격
        })

        # password1 help_text 수정
        self.fields['password1'].help_text = '<ul style="text-align: left; padding-left: 10px; margin-bottom: 40px; font-size: 13px;">' \
            '<li>다른 개인 정보와 비슷한 비밀번호는 사용할 수 없습니다.</li>' \
            '<li>비밀번호는 최소 8자 이상이어야 합니다.</li>' \
            '<li>자주 사용되는 비밀번호는 사용할 수 없습니다.</li>' \
            '<li>숫자로만 이루어진 비밀번호는 사용할 수 없습니다.</li>' \
            '</ul>'
        
        # password2 help_text 수정
        self.fields['password2'].help_text = '<div style="text-align: left; font-size: 13px;">확인을 위해 이전과 동일한 비밀번호를 입력해 주세요.</div>'
        
        # username help_text 수정
        self.fields['username'].help_text = '<div style="text-align: left; margin-bottom: 40px; font-size: 13px;">' \
            '필수 항목입니다. 150자 이하로 입력해 주세요.<br>' \
            '<span style="display: block; margin-top: 8px;">문자, 숫자, @/./+/-/_만 사용 가능합니다.</span>' \
            '</div>'
        
        # 필드 레이블 한글화
        self.fields['password1'].label = '비밀번호'
        self.fields['password2'].label = '비밀번호 확인'
        self.fields['username'].label = '사용자 이름'
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
        
        error_messages = {
            'password_mismatch': _('두 비밀번호가 일치하지 않습니다.'),
        }