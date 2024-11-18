import requests
from pyquery import PyQuery

url = "https://www.qidian.com/rank/yuepiao/?source=m_jump/"
heasers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "cookie": "hiijack=0; e1=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A5%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_rank%22%2C%22eid%22%3A%22qd_C45%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A71%22%7D; _csrfToken=TTuRjWZZ0xa2iPOSIzMKeHbrrBtrlDo840YIMhta; newstatisticUUID=1731153532_1967807144; fu=1426234816; e2=; e1=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A71%22%7D; supportwebp=true; supportWebp=true; traffic_utm_referer=https%3A//www.google.com/; w_tsfp=ltvuV0MF2utBvS0Q6qvokkuvEDwidzg4h0wpEaR0f5thQLErU5mG0Id8vsrxNHPd68xnvd7DsZoyJTLYCJI3dwNHRszAeosSiQ6XwIkt1IdAVUQ2FZ3UUAZNIb8g6GUVKXhCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5WrVswmvLVtzA74T10fG1ClLDi1ysEDpd7gPY0+oJcb9SqA="
}
resp = requests.get(url, headers=heasers)
# 初始化pyquery对象
doc = PyQuery(resp.text)
names = [a.text for a in doc('h2 a')]
print(names)
authors = [a.text for a in doc('p.author a.name')]
print(authors)
