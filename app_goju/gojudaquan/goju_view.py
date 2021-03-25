from app_goju.gojudaquan import bp
from flask import render_template
from app_goju.gojudaquan.forms import DouyinForm,BeianForm,Wyy_ssForm,Wyy_shuijForm
from app_goju.gojudaquan.forms import BilibiliForm,AvatarForm,IpymcxForm,IpcxForm,Sfz_cxForm,Sfz_xx_cxForm
import requests


@bp.route('/gojudaquan')
def gojudaquan():

    return render_template('gojudaquan/gojudaquans.html')

# 抖音去水印路由
@bp.route('/douyin',methods=['GET','POST'])
def douyin():
    form = DouyinForm()
    if form.validate_on_submit():
        url = "https://v1.alapi.cn/api/video/dy?url="
        res = requests.get(url+form.username.data)
        r = res.json()
        codes = r['code']
        douyin_title = r['data']['title']
        douyin_video_url = r['data']['video_url']
        douyin_cover_image = r['data']['cover_url']
        return render_template('shipin/douyin.html',codes=codes,
                               douyin_title=douyin_title,douyin_video_url=douyin_video_url,
                               douyin_cover_image=douyin_cover_image,form=form)
    return render_template('shipin/douyin.html',form=form)

# 备案路由
@bp.route('/beian',methods=['GET','POST'])
def beian():
    form = BeianForm()
    if form.validate_on_submit():
        url = "https://api.66mz8.com/api/icp.php?domain="
        res = requests.get(url + form.beian.data)
        r = res.json()
        z_tai = r['code']
        zhu_mc = r['主办单位名称']
        zhu_xz = r['主办单位性质']
        beian_hao = r['备案许可证号']
        beian_name = r['网站备案名称']
        wz_sy = r['网站首页网址']
        beian_sj = r['备案审核时间']
        zuixin_sh = r['备案审核时间']
        return render_template('yuming/beian.html',form=form,
                               z_tai=z_tai,zhu_mc=zhu_mc,zhu_xz=zhu_xz,beian_hao=beian_hao,
                               beian_name=beian_name,wz_sy=wz_sy,beian_sj=beian_sj,zuixin_sh=zuixin_sh)
    return render_template('yuming/beian.html',form=form)

# 网易云音乐数据搜索
@bp.route('/wyy_ss',methods=['GET','POST'])
def wyy_ss():
    form = Wyy_ssForm()
    if form.validate_on_submit():
        url = "https://v1.alapi.cn/api/music/search?keyword="
        res = requests.get(url + form.username.data)
        r = res.json()
        a = r['data']['songs']
        codes = r['code']
        alist = []
        for im in range(len(a)):
            ab = a[im]['artists']
            for pm, b in zip(ab, a):
                alist.append({"歌名": b['name'],'歌名id': b['id'],"歌手名称": pm['name'],'歌手id': pm['id']})
        return render_template('yinyue/wangyiyu_ss.html',form=form,alist=alist,codes=codes)
    return render_template('yinyue/wangyiyu_ss.html',form=form)

# 网易云音乐获取歌单的随机歌曲
@bp.route('/wyy_shuij',methods=['GET','POST'])
def wyy_shuij():
    form = Wyy_shuijForm()
    if form.validate_on_submit():
        url = "https://api.uomg.com/api/rand.music?mid="
        res = requests.get(url + form.ge_ids.data + "&format=json")
        r = res.json()
        codes = r['code']
        return render_template('yinyue/wyy_shuij.html',form=form,r=r,codes=codes)
    return render_template('yinyue/wyy_shuij.html',form=form)

# 随机获取网易云音乐热门歌曲接口
@bp.route('/wyy_sj_hq')
def wyy_si_hq():
    url = "https://api.66mz8.com/api/rand.music.163.php?format=json"
    res = requests.get(url)
    rs = res.json()
    codes = rs['code']
    return render_template('yinyue/wyy_sj_hq.html',rs=rs,codes=codes)

# 随机获取网易云音乐热门评论接口
@bp.route('/wyy_rp')
def wyy_rp():
    url = "https://api.66mz8.com/api/music.163.php?format=json"
    res = requests.get(url)
    rs = res.json()
    codes = rs['code']
    return render_template('yinyue/wyy_rp.html',rs=rs,codes=codes)

# 网站背景图
@bp.route('/wz_bjtu')
def wz_bjtu():
    url = "https://api.66mz8.com/api/bg.img.php?format=json"
    res = requests.get(url)
    rs = res.json()
    codes = rs['code']
    return render_template('tupian/wz_bjtu.html',rs=rs,codes=codes)


# bilibili视频封面获取
@bp.route('/bilibili_fm',methods=['GET','POST'])
def bilibili_fm():
    form = BilibiliForm()
    if form.validate_on_submit():
        url = "https://v1.alapi.cn/api/bbcover?c="
        res = requests.get(url + form.bili.data)
        rs = res.json()
        codes = rs['code']
        return render_template('tupian/bilibili_fm.html',form=form,rs=rs,codes=codes)
    return render_template('tupian/bilibili_fm.html',form=form)

# ACG图片
@bp.route('/acg_tp')
def acg_tp():
    url = "https://v1.alapi.cn/api/acg?format=json"
    res = requests.get(url)
    rs = res.json()
    codes = rs['code']
    return render_template('tupian/acg_tups.html',rs=rs,codes=codes)

# Bing 壁纸获取
@bp.route('/bing_bz')
def bing_bz():
    url = "https://api.asilu.com/bg/"
    res = requests.get(url)
    rs = res.json()
    ams = rs['images']

    return render_template('tupian/bing_bzs.html',ams=ams)


# 随机头像输出
@bp.route('/avatar_sj',methods=['GET','POST'])
def avatar_sj():
    form = AvatarForm()
    if form.validate_on_submit():

        url = "https://api.uomg.com/api/rand.avatar?sort="
        a = "&format=json"
        res = requests.get(url+form.imgss.data+a)
        rs = res.json()
        codes = rs['code']
        imgurl = rs['imgurl']
        return render_template('tupian/avatar_sj.html',form=form,codes=codes,imgurl=imgurl)
    return render_template('tupian/avatar_sj.html',form=form)



# IP域名归属地查询
@bp.route('/ip_ym_cx',methods=['GET','POST'])
def ip_ym_cx():
    form = IpymcxForm()
    if form.validate_on_submit():
        url = "https://api.asilu.com/ip/?ip="
        res = requests.get(url+form.ip_cx.data)
        rs = res.json()
        ips = rs['ip']
        return render_template('ip_cl/ip_ym_cxs.html',form=form,rs=rs,ips=ips)
    return render_template('ip_cl/ip_ym_cxs.html',form=form)


# ip查询
@bp.route('/ip_cx',methods=['GET','POST'])
def ip_cx():
    form = IpcxForm()
    if form.validate_on_submit():
        url = "https://v1.alapi.cn/api/ip?ip="
        res = requests.get(url+form.ip_cxs.data)
        rs = res.json()
        d = rs['data']
        a = rs['data']['ad_info']
        ips = rs['data']['ip']
        codes = rs['code']
        return render_template("ip_cl/ip_cxs.html",form=form,
                               d=d,a=a,ips=ips,codes=codes)
    return render_template("ip_cl/ip_cxs.html",form=form)

# 身份证查询
@bp.route('/sfz_cx',methods=['GET','POST'])
def sfz_cx():
    form = Sfz_cxForm()
    if form.validate_on_submit():
        url = "https://api.asilu.com/idcard/?id="
        res = requests.get(url + form.name.data)
        rs = res.json()
        ckeck = rs['ckeck']
        return render_template('sfz_cl/sfz_cx.html',form=form,rs=rs,ckeck=ckeck)
    return render_template('sfz_cl/sfz_cx.html',form=form)

# 身份证信息查询
@bp.route('/sfz_xx_cx',methods=['GET','POST'])
def sfz_xx_cx():
    form = Sfz_xx_cxForm()
    if form.validate_on_submit():
        url = "http://api.guaqb.cn/music/id/card.php?id="
        res = requests.get(url + form.name.data)
        rs = res.json()
        msg = rs['msg']
        return render_template('sfz_cl/sfz_xx_cx.html', form=form,rs=rs,msg=msg)
    return render_template('sfz_cl/sfz_xx_cx.html',form=form)


from app_goju.gojudaquan.forms import Sjh_cxForm
# 手机归属地查询
@bp.route('/sjh_cx',methods=['GET','POST'])
def sjh_cx():
    form = Sjh_cxForm()
    if form.validate_on_submit():
        url = "https://api.asilu.com/phone/?phone="
        r = requests.get(url+form.name.data)
        rs = r.json()
        return render_template("sj_cl/sjh_cx.html", form=form,rs=rs)
    return render_template("sj_cl/sjh_cx.html",form=form)

# 随机录言
@bp.route('/suijiluyan')
def suijiluyan():
    url = "https://api.66mz8.com/api/quotation.php?format=json"
    r = requests.get(url)
    rs = r.json()
    codes = rs['code']
    return render_template('xw_zx/suijiluyu.html',rs=rs,codes=codes)

# 今日热榜
@bp.route('/jr_rp')
def jr_rp():
    url = "https://v1.alapi.cn/api/tophub/get"
    r = requests.get(url)
    rs = r.json()
    codes = rs['code']
    am = rs['data']['list']
    return render_template("xw_zx/jr_rp.html",codes=codes,am=am)

# 知乎日报
@bp.route('/zhihu_rb')
def zhihu_rb():
    url = "https://v1.alapi.cn/api/zhihu/latest"
    r = requests.get(url)
    rs = r.json()
    codes = rs['code']
    am = rs['data']['stories']
    return render_template('xw_zx/zhihu_rb.html',am=am,codes=codes)

# 历史上的今天
@bp.route('/lzsd_jt')
def lzsd_jt():
    url = "https://v1.alapi.cn/api/eventHitory"
    r = requests.get(url)
    rm = r.json()
    codes = rm['code']
    am = rm['data']
    return render_template("xw_zx/lzsd_jt.html",codes=codes,am=am)

# 微博热搜榜
@bp.route('/wb_rsb')
def wb_rsb():
    url = "https://v1.alapi.cn/api/new/wbtop?num=100"
    r = requests.get(url)
    rm = r.json()
    codes = rm['code']
    am = rm['data']
    return render_template("xw_zx/wb_rsb.html",am=am,codes=codes)

# 汉服新闻
@bp.route('/hf_xw')
def hf_xw():
    url = "https://v1.alapi.cn/api/new/hanfu?num=20"
    r = requests.get(url)
    rm = r.json()
    codes = rm['code']
    am = rm['data']
    return render_template("xw_zx/hf_xw.html",codes=codes,am=am)

# 网易新闻头条
@bp.route('/wy_xw_tt')
def wy_xw_tt():
    url = "https://v1.alapi.cn/api/new/toutiao?start=1&num=50"
    r = requests.get(url)
    rm = r.json()
    codes = rm['code']
    am = rm['data']
    return render_template("xw_zx/wy_xw_tt.html",codes=codes,am=am)

from app_goju.gojudaquan.forms import Zw_fyForm
# 中文翻译
@bp.route('/zw_fy',methods=['GET','POST'])
def zw_fy():
    form = Zw_fyForm()
    if form.validate_on_submit():
        url = "https://api.66mz8.com/api/translation.php?info="
        r = requests.get(url + form.name.data)
        rm = r.json()
        codes = rm['code']
        sr = rm['info']
        cc = rm['fanyi']
        return render_template("jq_fy/zw_fy.html", form=form,codes=codes,sr=sr,cc=cc)
    return render_template("jq_fy/zw_fy.html",form=form)

# 关于我
@bp.route('/guangyuwo')
def guangyuwo():


    return render_template("guangyuwos.html")

# 开源
@bp.route('/kaiyuan')
def kaiyuan():

    return render_template('kaiyuan.html')