
import requests
url = "https://mail.qq.com/cgi-bin/getcomposedata?t=signature&fun=compose&sid=zRXo3LCWu_1pNwJd&qzonesign=&r=1602496266347"
hearders ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
cookies_tem= "RK=GNY1eZHhE4; ptcz=b29f96ff7d8b49353300c3f6992b003989a15183caf7c282be5662b0e3d16076; pgv_pvi=8851774464; tvfe_boss_uuid=d45093d6843c0a88; o_cookie=894856408; webp=1; gr_user_id=2267f721-6f87-413f-b7f0-5f858ab467f3; grwng_uid=1615f892-2d6a-4d8a-91e4-26fb72037229; pac_uid=1_894856408; eas_sid=o175k87182m4B4U1W8A0l8T9n0; uin_cookie=o0894856408; ied_qq=o0894856408; XWINDEXGREY=0; _ga=GA1.2.1440307698.1595665979; Qs_lvt_323937=1581244142%2C1585125650%2C1595665979; Qs_pv_323937=902391040994189400%2C2936405773107828000%2C2873338385315902500; p_uin=o0894856408; wimrefreshrun=0&; qm_logintype=qq; qm_flag=0; qqmail_alias=894856408@qq.com; qm_domain=https://mail.qq.com; foxacc=894856408&0; edition=mail.qq.com; qm_loginfrom=894856408&wpt; new_mail_num=894856408&0; ptui_loginuin=894856408@qq.com; uin=o0894856408; skey=@RbrinD6Hq; pt4_token=8Zj6gPvoJpSKJ4P5xNLoa165jlBLiAgspwPZPTa3ODE_; p_skey=8v4xI1EGttqRQi2ekwpBUON9N7ZhepI2pw1khLwV-Nw_; sid=894856408&0744187fca864ad3cc535b71d3d2d239,qOHY0eEkxRUd0dHFSUWkyZWt3cEJVT045TjdaaGVwSTJwdzFraEx3Vi1Od18.; qm_username=894856408; qm_lg=qm_lg; qm_ptsk=894856408&@RbrinD6Hq; ssl_edition=sail.qq.com; username=894856408&894856408; xm_uin=13102661919730904; xm_sid=zdhveYxsTEQuVmVrADVqaQAA; xm_skey=13102661919730904&b6d2282ff684ca86159d375d357225e8; CCSHOW=000000"
data = {
"t": "signature",
"fun": "compose",
"sid": "zRXo3LCWu_1pNwJd",
"qzonesign":"" ,
"r": "1602496266347"
}
#Cookies参数
cookes={}
for i in cookies_tem.split(";"):
    value =  i.split("=")
    cookes[value[0]] = value[1]
#如何使用Cookies
r=  requests.post(url,headers=hearders,data=data,cookies= cookes)
print(r.text)

