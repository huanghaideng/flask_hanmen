from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField,SubmitField
# https://www.free-api.com/
class DouyinForm(FlaskForm):
    username = StringField('填写你的抖音短链接',validators=[DataRequired()])
    submit = SubmitField('提交')

class BeianForm(FlaskForm):
    beian = StringField('域名备案查询',validators=[DataRequired()])
    submit = SubmitField('提交')

class Wyy_ssForm(FlaskForm):
    username = StringField('请输入你要搜索的网易云音乐名称',validators=[DataRequired()])
    submit = SubmitField('提交')

class Wyy_shuijForm(FlaskForm):
    ge_ids = StringField('填写歌单id',validators=[DataRequired()])
    submit = SubmitField('提交')

class BilibiliForm(FlaskForm):
    bili = StringField('b站的视频地址',validators=[DataRequired()])
    submit = SubmitField('提交')

class AvatarForm(FlaskForm):
    imgss = StringField('选择输出分类[男，女，动漫男，动漫女]，为空随机输出',validators=[DataRequired()])
    submit = SubmitField('提交')

class IpymcxForm(FlaskForm):
    ip_cx = StringField('输入IP或者域名',validators=[DataRequired()])
    submit = SubmitField('提交')

class IpcxForm(FlaskForm):
    ip_cxs = StringField('请输入你的ip地址',validators=[DataRequired()])
    submit = SubmitField('提交')

class Sfz_cxForm(FlaskForm):
    name = StringField('请输入你要查询的身份证号码',validators=[DataRequired()])
    submit = SubmitField('提交')

class Sfz_xx_cxForm(FlaskForm):
    name = StringField('请输入你要查询的身份证号码',validators=[DataRequired()])
    submit = SubmitField('提交')

class Sjh_cxForm(FlaskForm):
    name = StringField('请输入你要查询的手机号',validators=[DataRequired()])
    submit = SubmitField('提交')

class Zw_fyForm(FlaskForm):
    name = StringField('请输入',validators=[DataRequired()])
    submit = SubmitField('提交')